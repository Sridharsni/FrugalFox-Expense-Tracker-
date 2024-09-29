from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    salary = float(request.form['salary'])
    rent = float(request.form['rent'])
    utilities = float(request.form['utilities'])
    misc = float(request.form['miscellaneous'])
    goal = float(request.form['goal'])

    # Calculate total expenses and necessary savings
    total_expense = rent + utilities + misc
    necessary_savings = salary - total_expense

    # Pie Chart for Expense Breakdown
    expenses = [rent, utilities, misc]
    labels = ['Rent', 'Utilities', 'Miscellaneous']
    
    fig1, ax1 = plt.subplots()
    ax1.pie(expenses, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    
    # Save Pie chart to buffer
    pie_chart = io.BytesIO()
    plt.savefig(pie_chart, format='png')
    pie_chart.seek(0)
    pie_chart_base64 = base64.b64encode(pie_chart.getvalue()).decode('utf-8')

    # Bar Chart for Expense Comparison
    df = pd.DataFrame({
        'Category': ['Rent', 'Utilities', 'Miscellaneous'],
        'Amount': [rent, utilities, misc]
    })

    fig2, ax2 = plt.subplots()
    df.plot(kind='bar', x='Category', y='Amount', ax=ax2)
    
    # Save Bar chart to buffer
    bar_chart = io.BytesIO()
    plt.savefig(bar_chart, format='png')
    bar_chart.seek(0)
    bar_chart_base64 = base64.b64encode(bar_chart.getvalue()).decode('utf-8')

    # Gauge Chart for Progress Towards Goal
    current_savings = salary - total_expense
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=current_savings,
        title={'text': "Current Savings"},
        gauge={'axis': {'range': [None, goal]},
               'bar': {'color': "green"}}
    ))

    gauge_html = gauge.to_html(full_html=False)

    # Pass all the calculated data and charts to the summary template
    report = {
        'total_income': salary,
        'total_expense': total_expense,
        'necessary_savings': necessary_savings
    }

    return render_template('summary.html',
                           report=report,
                           pie_chart=pie_chart_base64,
                           bar_chart=bar_chart_base64,
                           gauge_chart=gauge_html)

if __name__ == '__main__':
    app.run(debug=True)
