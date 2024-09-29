import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

def generate_report(csv_file_path, goal):
    # Load data
    df = pd.read_csv(csv_file_path)
    
    # Data preprocessing
    df['Date'] = pd.to_datetime(df['Date'])
    df['Amount'] = df['Amount'].astype(float)
    
    # Summarize total expenses and income
    total_expense = df[df['Amount'] < 0]['Amount'].sum()
    total_income = df[df['Amount'] > 0]['Amount'].sum()
    
    # Set savings goal
    savings_goal = goal
    necessary_savings = total_expense - savings_goal
    
    # Split data into categories (e.g., rent, groceries, etc.)
    expense_categories = df[df['Amount'] < 0].groupby('Title')['Amount'].sum()
    
    # Predict future expenses and saving opportunities
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    X = df[['Month', 'Year']]
    y = df['Amount']
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict next month's expenses
    next_month = pd.DataFrame({'Month': [X['Month'].max() + 1], 'Year': [X['Year'].max()]})
    predicted_expense = model.predict(next_month)[0]
    
    # Optimization for savings
    savings_per_category = expense_categories / total_expense * necessary_savings
    
    # Create report dictionary
    report = {
        'total_income': total_income,
        'total_expense': total_expense,
        'predicted_next_month_expense': predicted_expense,
        'necessary_savings': necessary_savings,
        'savings_per_category': savings_per_category.to_dict()
    }
    
    # Generate visualizations
    plt.figure(figsize=(10, 6))
    expense_categories.plot(kind='bar', color='salmon')
    plt.title('Current Expenses by Category')
    expense_plot_path = os.path.join('static', 'expense_plot.png')
    plt.savefig(expense_plot_path)
    plt.close()
    
    plt.figure(figsize=(10, 6))
    savings_per_category.plot(kind='bar', color='green')
    plt.title('Required Savings by Category')
    savings_plot_path = os.path.join('static', 'savings_plot.png')
    plt.savefig(savings_plot_path)
    plt.close()
    
    plots = {
        'expense_plot': expense_plot_path,
        'savings_plot': savings_plot_path
    }
    
    return report, plots
