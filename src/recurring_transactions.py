from typing import List, Tuple
from collections import defaultdict
from datetime import timedelta
from models import Transaction

def identify_recurring_transactions(transactions: List[Transaction]) -> List[Tuple[str, float, str]]:
    grouped_transactions = defaultdict(list)
    for transaction in transactions:
        grouped_transactions[transaction.description.lower()].append(transaction)

    recurring_transactions = []

    for description, group in grouped_transactions.items():
        if len(group) < 2:
            continue

        group.sort(key=lambda t: t.date)
        intervals = [(group[i+1].date - group[i].date).days for i in range(len(group)-1)]
        amounts = [t.amount for t in group]

        if is_recurring(intervals, amounts):
            recurring_transactions.extend([(t.description, t.amount, t.date.strftime('%Y-%m-%d')) for t in group])

    return recurring_transactions

def is_recurring(intervals: List[int], amounts: List[float]) -> bool:
    if len(set(intervals)) == 1 and len(set(amounts)) == 1:
        return True

    # Check for monthly recurrence (allowing for some variation)
    if all(25 <= interval <= 35 for interval in intervals) and len(set(amounts)) <= 2:
        return True

    # Check for weekly recurrence
    if all(6 <= interval <= 8 for interval in intervals) and len(set(amounts)) <= 2:
        return True

    return False

if __name__ == "__main__":
    # Example usage
    sample_transactions = [
        Transaction.from_dict({"description": "Spotify", "amount": -14.99, "date": "2021-01-29"}),
        Transaction.from_dict({"description": "Spotify", "amount": -14.99, "date": "2020-12-29"}),
        Transaction.from_dict({"description": "Spotify", "amount": -14.99, "date": "2020-11-29"}),
        Transaction.from_dict({"description": "One-off purchase", "amount": -50.00, "date": "2021-02-15"}),
    ]

    recurring_transactions = identify_recurring_transactions(sample_transactions)
    print(f"Recurring transactions: {recurring_transactions}")