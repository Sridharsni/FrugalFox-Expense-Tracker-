# Frugal Fox (Finance Tracker)

A simple and intuitive web application designed to help users track their finances, manage expenses, and save towards financial goals. The Finance Tracker allows users to visualize their spending habits, make informed budgeting decisions, and optimize savings through insightful analytics.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Expense Tracking**: Users can input their income and expenses to get a clear picture of their financial health.
- **Visualizations**: Generate pie and bar charts for expense breakdowns, as well as gauge charts for savings progress.
- **Data Analysis**: Utilizes machine learning techniques to predict future expenses and suggest optimal savings strategies.
- **User-Friendly Interface**: Easy-to-navigate web interface for seamless interaction with the application.

## Technologies Used

- **Frontend**:
  - HTML
  - CSS
- **Backend**:
  - Python
  - Flask (Web Framework)
- **Data Visualization**:
  - Matplotlib
  - Plotly
- **Data Handling**:
  - Pandas
- **Machine Learning**:
  - Scikit-learn
- **Deployment**:
  - Can be deployed on platforms like Heroku, AWS, or any server supporting Python and Flask.

## Installation

To get started with the Finance Tracker application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mohan12karthik/Finance_Tracker.git
   cd Finance_Tracker

2. **Set up a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt

4. **Run the application**:
   ```bash
   python app.py

5. **Access the application**:
   - Open your web browser and navigate to http://127.0.0.1:5000/ to access the Finance Tracker app.

## Usage

1. **Input Data**: On the homepage, enter your salary, monthly rent, utilities, miscellaneous expenses, and savings goal in the provided form fields.

2. **Submit the Form**: Click the "Submit" button to process your input.

3. **View Reports**: After submission, you'll be redirected to a summary page that displays:
   - A pie chart showing the breakdown of your expenses.
   - A bar chart comparing different categories of expenses.
   - A gauge chart indicating your current savings status towards your savings goal.

4. **Analyze Your Finances**: Use the visualizations to understand your spending habits and identify areas where you can save more effectively.


## Contributing

- **Team**: Sridharsni Sivakumar, Krupaasree Kalyansundar, Chethan Karunakara, Mohan Karthik V

We welcome contributions to improve the Finance Tracker app! Here’s how you can contribute:

1. **Fork the Repository**: Click on the "Fork" button at the top-right corner of this page.

2. **Create a New Branch**: In your local clone of the repository, create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/AmazingFeature
3. **Make Changes**: Implement your changes or enhancements.

4. **Commit Your Changes**: Once you're satisfied with your changes, commit them with a descriptive message:
   ```bash
   git commit -m 'Add some AmazingFeature'

5. **Push to Your Branch**: Push your changes to your GitHub fork:
   ```bash
   git push origin feature/AmazingFeature

6. **Create a Pull Request**: Go to the original repository and click on the "Pull Requests" tab. Click on "New Pull Request" and select your branch. Provide a description of your changes and submit the pull request.

7. ## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments
- Developed as part of the **SunHack** hackathon.
- Featured on **Devpost**: [Frugal Fox](https://devpost.com/software/frugalfox)

