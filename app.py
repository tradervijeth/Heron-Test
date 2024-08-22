from flask import Flask, request, jsonify
from src.models import Transaction
from src.recurring_transactions import identify_recurring_transactions
from datetime import datetime

app = Flask(__name__)

@app.route('/identify-recurring', methods=['POST'])
def identify_recurring():
    data = request.json
    if not data or 'transactions' not in data:
        return jsonify({"error": "No transactions provided"}), 400

    transactions = []
    for t in data['transactions']:
        try:
            transaction = Transaction(
                description=t['description'],
                amount=float(t['amount']),
                date=datetime.strptime(t['date'], '%Y-%m-%d')
            )
            transactions.append(transaction)
        except (KeyError, ValueError) as e:
            return jsonify({"error": f"Invalid transaction data: {str(e)}"}), 400

    recurring = identify_recurring_transactions(transactions)
    
    # Convert datetime objects to strings for JSON serialisation
    recurring_json = [
        {"description": r[0], "amount": r[1], "date": r[2]}
        for r in recurring
    ]

    return jsonify({"recurring_transactions": recurring_json})

if __name__ == '__main__':
    app.run(debug=True)