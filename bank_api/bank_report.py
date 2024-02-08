from bank_api.bank import Bank


class BankReport:
    def __init__(self, bank: Bank):
        self.bank = bank

    def get_balance(self, name: str):
        transactions = self.bank.transactions
        balance = 0
        for transaction in transactions:
            if transactions.name == name:
                balance += transaction.amount

        return balance