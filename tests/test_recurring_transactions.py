import unittest
from datetime import datetime
from src.models import Transaction
from src.recurring_transactions import identify_recurring_transactions

class TestRecurringTransactions(unittest.TestCase):

    def test_identify_recurring_transactions(self):
        transactions = [
            Transaction("Spotify", -14.99, datetime(2021, 1, 29)),
            Transaction("Spotify", -14.99, datetime(2020, 12, 29)),
            Transaction("Spotify", -14.99, datetime(2020, 11, 29)),
            Transaction("One-off", -50.00, datetime(2021, 2, 15)),
        ]

        recurring_transactions = identify_recurring_transactions(transactions)
        self.assertEqual(len(recurring_transactions), 3)
        for transaction in recurring_transactions:
            self.assertEqual(transaction[0], "Spotify")
            self.assertEqual(transaction[1], -14.99)

    def test_non_recurring_transactions(self):
        transactions = [
            Transaction("Grocery", -50.00, datetime(2021, 1, 15)),
            Transaction("Grocery", -75.00, datetime(2021, 2, 3)),
            Transaction("Grocery", -60.00, datetime(2021, 3, 1)),
        ]

        recurring_transactions = identify_recurring_transactions(transactions)
        self.assertEqual(recurring_transactions, [])

if __name__ == '__main__':
    unittest.main()