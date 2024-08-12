# 💰 Paisa Tracker Application
#### Website:  <https://paisatracker.onrender.com>

**PaisaTracker** is your all-in-one money management solution.

- 📈 Effortlessly track income and expenses.
- 📊 Create detailed budgets to reach your savings goals.
- 💡 Gain valuable insights into your spending habits.
- 💸 Make informed financial decisions.
- 🏦 Take control of your financial future with PaisaTracker.

## 🌟 Overview

The **Paisa Tracker Application** is a comprehensive web-based tool designed to help users manage their personal finances effectively. Built using the Flask framework, this application allows users to track their expenses, categorize them, and generate detailed financial reports based on various time periods. The application also includes robust user authentication and password recovery features to ensure secure access to personal financial data.

## ✨ Features

### 🔒 User Authentication

- **Registration**: New users can create an account by providing their username, email, and password. Passwords are securely hashed using the `pbkdf2:sha256` method to protect user information.
- **Login**: Registered users can log in to their accounts using their email and password. Session management is handled through Flask-Session, ensuring a seamless user experience.
- **Logout**: Users can log out of their accounts, which clears the session and ensures that their data remains secure.

### 💵 Expense Management

- **Add Expense**: Users can add new expenses by providing details such as category (e.g., food, transport), amount, description, and date. This functionality allows users to keep a detailed record of their expenditures.
- **View Expenses**: Users can view their recent expenses categorized by type. The application displays the most recent 100 entries for both income and expenses, providing a clear overview of financial activity.

### 📊 Reporting

- **Generate Reports**: Users can generate reports based on different time periods:
  - **Last 7 Days**: View expenses and income over the past week.
  - **This Month**: Analyze expenses and income for the current month.
  - **Last Month**: Review financial activity from the previous month.

  The reports include detailed information about the total amount of income and expenses, providing users with insights into their financial habits.

### 🔐 Password Recovery

- **OTP-Based Recovery**: Users who forget their passwords can request a One-Time Password (OTP) to reset their credentials. The OTP is sent via email using SMTP, and users can change their password once they successfully verify the OTP.

## 🛠️ Technologies Used

- **Flask**: A lightweight web framework used to build the web application. It handles routing, rendering templates, and managing sessions.
- **Flask-Session**: A Flask extension for managing user sessions using server-side storage, such as the filesystem.
- **SQLAlchemy**: A library for SQL database management, facilitating interactions with the SQLite database.
- **Werkzeug**: A library that provides password hashing utilities, ensuring secure storage of user passwords.
- **SQLite**: A relational database management system used to store user and expense data.
- **SMTP**: Simple Mail Transfer Protocol used for sending OTP emails.

# 📝 Installation

To get started with the Expense Tracker Application, follow these steps:

1. **Clone the Repository** 🔄

   Clone the project repository from GitHub to your local machine:

   ```bash
   https://github.com/code50/159784713/tree/1142ffe68b89a70860d993c3e9dc973a5ec6b413/project

2. **Set Up a Virtual Environment** 🌐

    Create and activate a virtual environment to manage project dependencies:

      ```bash
      python -m venv venv

- **Acitivate virtual environmwnt**

   Windows:
   ```bash
   venv\Scripts\activate

3. **Install Dependencies** 📦

    Install the required packages listed in requirements.txt:

      ```bash
      pip install -r requirements.txt

- **Troubleshooting:**

  - **Ensure** `requirements.txt` is Correct: Verify it lists valid package names and versions.
  - **Update pip:** Run `pip install --upgrade pip` to make sure you have the latest version.
  - **Check for Installation Errors**: Review error messages for specific issues with package installations.

4. **Configure the Databse** 🗄️

      Ensure that the `expenses.db` SQLite database file is in place. If it's missing, follow the application's instructions to initialize it.

- **Troubleshooting**:
  - **Confirm File Presence**: Make sure `expenses.db` exists in the project directory.
  - **Initialize Database:** If the file is missing, you might need to run a database setup script or create it manually. Refer to the application's documentation for details.

5. **Run the Application** 🚀

     Start the Flask development server:

      ```bash
      flask run


  The application will be available at http://127.0.0.1:5000/ in your web browser.

- **Troubleshooting**:
    - **Check Flask Installation:**:Ensure Flask is installed

        ```bash
        pip show flask

    - **Set Environment Variables:**

      Flask needs environment variables set. For example

        ```bash
        set FLASK_APP=app.py
        set FLASK_ENV=development

   - **Review Error Messages:**

        Look for clues in the error messages if the server doesn't start. Common issues include missing modules or syntax errors in `app.py`.


5. **Configure Email Settings for OTP** 📧

      Update the email credentials in `helpers.py`:

         ```bash
          sender_email = "your-email@example.com"
          sender_password = "your-email-password"

- **Troubleshooting:**

    - **Check Credentials:** Ensure the email address and password are correct.
    - **Email Provider Settings:** Some providers require special settings or application-specific passwords. Check your provider’s documentation.

## Application Structure 📂

    The project structure is as follows:

  - **`app.py`**: Main application file that defines routes and handles business logic.
  - **`helpers.py`**: Contains utility functions for generating OTPs and sending emails.
  - **`db.py`**: This file contains database-related tasks such as creating tables, connecting to the database, and handling database migrations. It serves as the bridge between the application and the database, ensuring data is stored and retrieved efficiently.
  - **`create_db.sql`**: A SQL script used to initialize the database. It typically contains commands to create necessary tables, indexes, and any initial data that the application requires. This file is essential for setting up the database schema during initial deployment or for resetting the database during development.
  - **`all_sql_queries.sql`**:For all sql queroes used in project
  - **`templates/`**: Directory containing HTML templates for rendering views.
  - **`static/`**: Directory for static files such as CSS and JavaScript.
  - **`requirements.txt`**: File listing the project dependencies.
  - **`README.md`**: Documentation file providing an overview and setup instructions.

## Routes 🌐

  - **`/`**: The home page of the application, which provides an introduction and navigation options.
  - **`/login`**: Page for user login. Requires email and password. Users are redirected to the home page upon successful login.
  - **`/register`**: Page for user registration. Users must provide a username, email, and password to create an account.
  - **`/home`**: Dashboard for managing expenses. Allows users to add new expenses and view recent entries.
  - **`/expense`**: Page for viewing expense records. Displays the most recent 100 expenses categorized under 'expense.'
  - **`/income`**: Page for viewing income records. Displays the most recent 100 entries categorized under 'income.'
  - **`/report`**: Generates and displays financial reports based on the selected time period (last 7 days, this month, last month).
  - **`/forgot_password`**: Page for password recovery. Users can request an OTP to reset their password.
  - **`/logout`**: Logs out the user and clears the session.


## LICENSE ![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)

  This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing 🤝

   Contributions are welcome! Fork the repository, make your changes, and submit a pull request. Ensure your changes follow the project's coding standards and include tests.


## Acknowledgments 🙏

  - **Flask**: Lightweight web framework.
  - **Flask-Session**: Session management.
  - **SQLAlchemy**: Database interactions.
  - **Werkzeug:** Secure password hashing.
  - **SMTP**: Email handling.
