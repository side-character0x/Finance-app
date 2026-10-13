# Finance App

A finance app made with Flask server which suppports multiple users with individual accounts which can only be accessed with the PIN defined by the user and all the user data will be stored in a SQlite database and user can add income , add expense and view their balance in a interactive UI.

## Features

- Authentication system with PIN
- Add income and expense to balance
- Persistant memory with SQlite
- Multi-user support with individual accounts

## Tech Stack

- Python
- Flask
- Html/CSS

## How to Run

1. Clone the repository:
   git clone https://github.com/side-character0x/Finance-app
   cd Finance-app

2. Install dependencies:
   pip install flask

3. Run the app:
   python app.py

4. Open in your browser:
   http://127.0.0.1:5000

## Project Structure

- `app.py` — Flask routes and session handling
- `db.py` — database connection and queries
- `templates/` — HTML pages (login, signin, home)
- `finance.db` — SQLite database (created on first run)

## Status

Built during Hack Club Terra (prep week 2). Currently supports income
tracking and balance display. Expense tracking and transaction history
are planned next.