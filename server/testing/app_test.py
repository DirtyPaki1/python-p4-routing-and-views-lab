# server/testing/app_test.py

import pytest
from server.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert b"Python Operations with Flask Routing and Views" in response.data

def test_print_string(client):
    response = client.get('/print/Hello')
    assert b"Hello" in response.data

def test_count(client):
    response = client.get('/count/5')
    assert b"0" in response.data
    assert b"1" in response.data
    assert b"4" in response.data

def test_math_add(client):
    response = client.get('/math/5+3')
    assert b"8" in response.data

def test_math_subtract(client):
    response = client.get('/math/10-4')
    assert b"6" in response.data

def test_math_multiply(client):
    response = client.get('/math/2*3')
    assert b"6" in response.data

def test_math_divide(client):
    response = client.get('/math/8div2')
    assert b"4.0" in response.data

def test_math_modulo(client):
    response = client.get('/math/10%3')
    assert b"1" in response.data
