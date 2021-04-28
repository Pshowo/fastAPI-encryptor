from fastapi.testclient import TestClient
import json

from main import app, append_message, fake_msg

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
    response = client.post(
        "/v1/vigenere/encryptor",
        json={"msg": "BEDE"},
    )
    resp = response.json()
    print(resp)
    assert response.status_code == 200
    assert resp['1']["open_msg"] == "BEDE"
    assert fake_msg[1]["open_msg"] == "BEDE"


def test_vigenere_decryptor():
    response = client.post(
        "/v1/vigenere/decryptor",
        json={"msg": "BFAC", "key": "ABDE"},
    )
    assert response.status_code == 200
    assert response.json() == {"decoded_messege": "BEDE"}
    
#{'0': 'fake msg', '1': {'open_msg': 'BEDE', 'key': 'EBFE', 'close_msg': 'FFCC'}}
#{'0': 'fake msg', '1': {'open_msg': 'BEDE', 'key': 'CDAB', 'close_msg': 'DBDF'}}