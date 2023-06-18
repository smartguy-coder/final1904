import pytest
from fastapi.testclient import TestClient

import main


@pytest.fixture()
def client():
    with TestClient(app=main.app) as client:
        yield client

