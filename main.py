from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import FastAPI, Depends, HTTPException, status
from vigenere.encryptor import Vigenere
from pydantic import BaseModel
from typing import Optional
from config import *
import secrets
import string

v = Vigenere(string.printable+PL_ext)


class Message(BaseModel):
    msg: str
    key: Optional[str]


security = HTTPBasic()
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

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, USER)
    correct_password = secrets.compare_digest(credentials.password, PASS)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


def append_message(open_msg, close_msg, key):
    global fake_msg
    fake_msg[max(fake_msg,key=int)+1] = {
        "open_msg": open_msg,
        "key": key,
        "close_msg": close_msg}


@app.get("/",  tags=['cipher'])
async def root():
    return {
        "version": "1.0",
        "name": "fastAPI-encryptor",
        "docs": "/docs",
        "cipher_vigenere": "/v1/vigenere",
        "avaiable_chars": v.raw_alphabet
        }


@app.get(VER + "/vigenere", tags=['cipher'])
async def vigenere():
    """
    Shows available methods.
    """
    return {
        "encryptor": "/v1/vigenere/encryptor",
        "decryptor": "/v1/vigenere/decryptor"
    }

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     # tax: Optional[float] = None

@app.post(VER + "/vigenere/encryptor", tags=['encryptor'])
async def vigenere_encryptor(open_msg: Message, q: Optional[str] = None, username: str = Depends(get_current_username)):
    """Encoding messege.

    **open_msg** - contain only message.
    Returns
    -------
    [json]

    - **open_msg** - open message to encode
    - **key** - key to decode encrypted message
    - **close_msg** - encrypted message
    """
    if q:
        close_msg, key = v.encrypt(q)
        append_message(q, close_msg, key)
        return fake_msg
    else:
        close_msg, key = v.encrypt(open_msg.msg)
        append_message(open_msg.msg, close_msg, key)
        return fake_msg


@app.post(VER + "/vigenere/decryptor", tags=['decryptor'])
async def vigenere_decryptor(closed_msg: Message, username: str = Depends(get_current_username)):
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
