"""
This module contains the Flask application for managing bank accounts.
"""

from flask import Flask, render_template, request, redirect, url_for
from models import Bank

app = Flask(__name__)
bank = Bank()

@app.route('/')
def index():
    """
    Route for the homepage.
    """
    return render_template('index.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    """
    Route to create a new bank account.
    """
    if request.method == 'POST':
        name = request.form['name']
        initial_balance = float(request.form['balance'])
        bank.create_account(name, initial_balance)
        return redirect(url_for('accounts'))
    return render_template('create_account.html')

@app.route('/accounts')
def accounts():
    """
    Route to display all bank accounts.
    """
    all_accounts = bank.get_all_accounts()
    return render_template('accounts.html', accounts=all_accounts)

if __name__ == '__main__':
    app.run(debug=True)

