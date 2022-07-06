from fastapi.testclient import TestClient
from app.main import app

def test_patente_id_ok():
    client = TestClient(app)

    patente_id = '1'

    response = client.get(
        '/patente/'+patente_id
    )

    assert response.status_code == 200, response.text


def test_patente_ok():
    client = TestClient(app)

    patente = 'AAAA000'

    response = client.get(
        '/patente/'+patente
    )

    assert response.status_code == 200, response.text