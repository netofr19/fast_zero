from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_retorna_ok_e_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, world!'}


def test_read_html_retorna_ola_mundo_html():
    client = TestClient(app)

    response = client.get('/html')

    assert response.text == '''
    <head>
        <title>Olá, Mundo</title>
    </head>
    <body>
        <h1>Hello, world!</h1>
    </body>
    </html>'''
