from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmar)
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert (Afirmar)


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }
