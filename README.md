# Bank App

This is a simple Flask application to manage bank accounts. 
The application allows users to create a new bank account and display all existing accounts.

## Project Structure


- **app.py**: The main Flask application file.
- **models.py**: The file containing the Bank and BankAccount classes.
- **templates/**: The directory containing all HTML template files.
  - **base.html**: The base template.
  - **index.html**: The homepage template.
  - **create_account.html**: The template for creating a new account.
  - **accounts.html**: The template for displaying all bank accounts.
- **static/**: The directory for static files like CSS.
  - **style.css**: The CSS file for styling the application.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/bank_app.git
    cd bank_app
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install Flask
    ```

## Usage

1. Run the Flask application:
    ```bash
    flask run
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Running pylint

To check the code quality using pylint, run:
```bash
pylint app.py models.py


