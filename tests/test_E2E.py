import http

from fastapi.testclient import TestClient


def test_index_positive(client: TestClient) -> None:
    response = client.get('/test_user?first=100&second=50')
    assert response.status_code == http.HTTPStatus.OK
    assert response.json() == {'status': 'ok'}


def test_index_negative(client: TestClient) -> None:
    response = client.get('/test_user')
    assert response.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY
