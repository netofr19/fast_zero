from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, world!'}


@app.get('/html', status_code=HTTPStatus.OK)
def read_html():
    return """
    <head>
        <title>Olá, Mundo</title>
    </head>
    <body>
        <h1>Hello, world!</h1>
    </body>
    </html>
    """
