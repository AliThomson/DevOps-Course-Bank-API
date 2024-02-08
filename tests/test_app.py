"""Integration tests for app.py"""
from typing import Type
from flask.testing import FlaskClient
from flask.wrappers import Response
import pytest

from bank_api.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


def test_account_creation(client: FlaskClient):
    response = client.post('/accounts/Name 1')

    assert b'Name 1' in response.data
    assert response.status_code == 200
  
def test_account_creation_fails_when_account_name_is_blank(client: FlaskClient):
    response = client.post('/accounts/')

    assert response.status_code == 404

def test_account_get(client: FlaskClient):
    response = client.post('/accounts/Name 2')
    response = client.get('/accounts/Name 2')

    assert b'Name 2' in response.data
    
# Use the client to make requests to the Flask app.
    # response = client.get('/example/route')
    # Or use client.post to make a POST request
    # https://flask.palletsprojects.com/en/1.1.x/testing/
    # pass