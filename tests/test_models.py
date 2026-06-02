import pytest
import datetime
from src.app.models import Transcation


def test_create_valid_revenue_transcation():
    """Test creating a valid revenue transcation with default date."""

    trans = Transcation(type='revenue', description='Salary', amount=845.0)
    assert trans.id is None
    assert trans.type == 'revenue'
    assert trans.description == 'Salary'
    assert trans.amount == 845.0
    assert trans.date == datetime.datetime.today().isoformat()


def test_create_valid_expense_transcation():
    """Test creating a valid expense transcation with default date."""

    trans = Transcation(type='expense', description='Food', amount=60.0)
    assert trans.id is None
    assert trans.type == 'expense'
    assert trans.description == 'Food'
    assert trans.amount == 60.0
    assert trans.date == datetime.datetime.today().isoformat()
