# Recurring Transactions Identifier

This project identifies recurring transactions from a set of bank transactions.
How to Run

# Install dependencies:
pip install -r requirements.txt

# Run the Flask API:
python app.py

Send a POST request to http://127.0.0.1:5000/identify-recurring with JSON payload:
json:

{
  "transactions": [
    {"description": "Spotify", "amount": -14.99, "date": "2021-01-29"},
    {"description": "Spotify", "amount": -14.99, "date": "2020-12-29"},
    {"description": "One-off", "amount": -50.00, "date": "2021-02-15"}
  ]
}


# Logic of recurring_transactions.py
The script identifies recurring transactions by:

1. Grouping transactions by description
2. Analyzing time intervals between transactions in each group
3. Checking for regular patterns (e.g., monthly, weekly) or if all the intervals and transaction amount for those intervals is the same.
4. Considering consistency in transaction amounts

Transactions are classified as recurring if they have consistent intervals and amounts.

# Future Improvements:

1. Enhanced error handling and logging
2. Implementation of authentication
3. Use of HTTPS for secure communication
4. Containerisation using Docker for easier deployment and scaling
5. Comprehensive API status code handling for better error reporting
6. Optimisation of the recurring transaction detection algorithm for large datasets
7. Implementation of machine learning techniques for more accurate pattern recognition
8. Addition of more sophisticated financial analysis features
