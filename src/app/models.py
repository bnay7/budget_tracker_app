import datetime


class Transcation:
    """Represents a sing financial transcation"""

    def __init__(self, type, description, amount, date=None, id=None):
        # Validate the type
        if type not in ['revenue', 'expense']:
            raise ValueError(
                "Transcation type must be 'revenue' or 'expenses'")

        # Validae the amount
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be non negative")

        self.id = id
        self.type = type
        self.description = description
        self.amount = amount
        self.date = datetime.datetime.today().isoformat()

    def __repr__(self):
        """Provides a developer-friendly string representation"""
        return (f"""Transcation(id={self.id}), type ={self.type},\n
               description ='{self.description}, amount={self.amount:.2f},"
               date ='{self.date},)""")

    def display(self):
        """Prodives a user friendly string representation"""
        symbol = "+" if self.type == 'revenue' else "-"
        return f"[{self.date} {symbol}{self.amount:.2f}:{self.description}]"
