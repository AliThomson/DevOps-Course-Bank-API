import pytest

from bank_api.bank import Bank
from bank_api.bank_report import BankReport


@pytest.fixture
def bank() -> Bank:
    return Bank()

def test_bank_report_reports_correct_transactions(bank: Bank):
    # This means: assert an exception is raised during the following block
    bank = Bank()
    bank_report = BankReport(bank)
    bank.create_account('Name 1')
    bank.add_funds('Name 1', 50)

    result = bank_report.get_balance('Name 1') == 50

    assert result == 50