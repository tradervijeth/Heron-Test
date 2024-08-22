from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction:
    description: str
    amount: float
    date: datetime

    @classmethod
    def from_dict(cls, data: dict) -> 'Transaction':
        return cls(
            description=data['description'],
            amount=float(data['amount']),
            date=datetime.strptime(data['date'], '%Y-%m-%d')
        )