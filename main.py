from fastapi import FastAPI

import library

app = FastAPI()


@app.get("/{user}", description='some desc')
def index(user: str, first: int | float, second: int | float) -> dict:
    result = library.add_two_numbers(first, second)
    library.write_csv(user, first, second, result)
    return {'status': 'ok'}


@app.get("/admin/{admin}")
def get_data(admin: str) -> dict:
    if admin == '999':
        data = library.read_csv()
        return {'status': 'ok', 'data': data, 'count': len(data)}
    return {'status': 'not allowed'}
