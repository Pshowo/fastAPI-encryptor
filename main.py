from vigenere.encryptor import Vigenere
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
import string
from vigenere import *
import vigenere

v = Vigenere(string.printable)

tags_metadata = [
    {
        "name": "cipher",
        "description": "Inculde encrypt and decrypt methods.",
    },
    {
        "name": "encryptor",
        "description": "POST message which you want to encode.",
    },
    {
        "name": "decryptor",
        "description": "POST close message and key to decode it.",
    },
]


class Message(BaseModel):
    msg: str
    key: Optional[str]

app = FastAPI(
    title="fastAPI enctryptor",
    description="API with cipher algorithm to encrypt and decrypt a message using by Vigenere method.",
    version='v1',
    openapi_tags=tags_metadata
)
VER = '/v1' 

fake_msg = {
    0: "fake msg"
}


def append_message(open_msg, close_msg, key):
    global fake_msg
    fake_msg[max(fake_msg,key=int)+1] = {
        "open_msg": open_msg,
        "key": key,
        "close_msg": close_msg }


@app.get("/",  tags=['cipher'])
async def root():
    return {
        "version": "1.0",
        "name": "fastAPI-encryptor",
        "docs": "/docs",
        "cipher_vigenere": "/v1/vigenere"
        }


@app.get(VER + "/vigenere", tags=['cipher'])
async def vigenere():
    return {
        "encryptor": "/encryptor",
        "decryptor": "/decryptor"
    }


@app.post(VER + "/vigenere/encryptor", tags=['encryptor'])
async def vigenere_encryptor(open_msg: Message):
    """Encoding messege.

    **open_msg** - contain only message.
    Returns
    -------
    [json]

    - **open_msg** - open message to encode
    - **key** - key to decode encrypted message
    - **close_msg** - encrypted message
    """
    close_msg, key = v.encrypt(open_msg.msg)
    append_message(open_msg.msg, close_msg, key)
    return fake_msg


@app.post(VER + "/vigenere/decryptor", tags=['decryptor'])
async def vigenere_decryptor(closed_msg: Message):
    """Decoding message:
    
    **closed_msg** - must contain closed message and key
    Returns
    -------
    [str]
        Decoding message
    """
    open_msg = v.decrypt(closed_msg.msg, closed_msg.key)
    return {"decoded_messege": open_msg}

# Run server: uvicorn main:app --reload
# Run docs: http://localhost:8000/docs
