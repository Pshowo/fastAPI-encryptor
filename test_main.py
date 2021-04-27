from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "version": "1.0",
        "name": "fastAPI-encryptor",
        "cipher_vigenere": "/v1/vigenere"}

def test_root():
    response = client.get("/v1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

def test_vigenere():
    response = client.get("/v1/vigenere")
    assert response.status_code == 200
    assert response.json() == {
        "encryptor": "/encryptor",
        "decryptor": "/decryptor"
    }