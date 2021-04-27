from fastapi.testclient import TestClient
import json

from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "version": "1.0",
        "name": "fastAPI-encryptor",
        "docs": "/docs",
        "cipher_vigenere": "/v1/vigenere"
        }

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

def test_vigenere_encryptor():
    response = client.get("/v1/vigenere/encryptor")
    assert response.status_code == 200
    assert response.json() == {'0': "fake msg"}


def test_vigenere_decryptor():
    response = client.get("/v1/vigenere/decryptor")
    assert response.status_code == 200
    assert response.json() == {'0': "fake msg"}