from fastapi.testclient import TestClient
from fastapi import FastAPI, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from requests.auth import HTTPBasicAuth
import json

from main import app, append_message, fake_msg

client = TestClient(app)
security = HTTPBasic(realm="Basic")

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
        "encryptor": "/v1/vigenere/encryptor",
        "decryptor": "/v1/vigenere/decryptor"
    }


def test_vigenere_encryptor(credentials: HTTPBasicCredentials = Security(security)):
    auth = HTTPBasicAuth(username="admin", password="qwerty")
    response = client.post(
        "/v1/vigenere/encryptor",
        json={"msg": "BEDE"},
        auth=auth
    )
    resp = response.json()
    assert response.status_code == 200

    response = client.post(
        "/v1/vigenere/encryptor?q=sampleTextToEncode",
        json={"msg": ""},
        auth=auth
    )
    resp = response.json()
    assert response.status_code == 200


def test_vigenere_decryptor(credentials: HTTPBasicCredentials = Security(security)):
    auth = HTTPBasicAuth(username="admin", password="qwerty")
    response = client.post(
        "/v1/vigenere/decryptor",
        json={"msg": "BFAC", "key": "ABDE"},
        auth=auth
    )
    assert response.status_code == 200


def test_security_no_credentials():
    response = client.post("/v1/vigenere/encryptor")
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401, response.text
    assert response.headers["WWW-Authenticate"] == 'Basic'

def test_security_invalid_credentials(credentials: HTTPBasicCredentials = Security(security)):
    auth = HTTPBasicAuth(username="a", password="q")
    response = client.post(
        "/v1/vigenere/encryptor", headers={"Authorization": "Basic notabase64token"}
    )
    assert response.status_code == 401, response.text
    assert response.headers["WWW-Authenticate"] == 'Basic'
    assert response.json() == {"detail": "Invalid authentication credentials"}
