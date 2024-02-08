"""Unit tests for bank.py"""

import pytest

from bank_api.bank import Bank


@pytest.fixture
def bank() -> Bank:
    return Bank()

def test_create_account_raises_error_if_name_blank(bank: Bank):
    # This means: assert an exception is raised during the following block
    with pytest.raises(Exception):
        bank.create_account('')

def test_bank_creates_empty(bank: Bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0

def test_can_create_and_get_account(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'

def test_get_account_raises_error_if_no_account_matches(bank: Bank):
    bank.create_account('Name 1')

    # This means: assert an exception is raised during the following block
    with pytest.raises(ValueError):
        bank.get_account('Name 2')

def test_add_funds_adds_to_correct_account(bank: Bank):
    bank.create_account('Name 3')
    bank.add_funds('Name 3', 50)

    testTransaction = bank.transactions[0]

    assert len(bank.transactions) == 1
    assert testTransaction.amount == 50

def test_add_funds_errors_when_account_does_not_exist(bank: Bank):

    with pytest.raises(ValueError):
       bank.add_funds('Name 4', 50)

# def test_add_funds_errors_when_account_does_not_exist(bank: Bank):
#     bank.create_account('Name 5')

#     with pytest.raises(ValueError):
#        bank.add_funds('Name 5', £2)
