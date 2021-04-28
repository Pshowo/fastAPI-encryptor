from vigenere.encryptor import Vigenere
from pydantic import BaseModel
from fastapi import FastAPI
from vigenere import *
import vigenere

v = None

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
    msg:str

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

@app.on_event("startup")
async def startup_event():
    global v
    v = Vigenere()

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
    close_msg, key = v.encrypt(open_msg.msg)
    append_message(open_msg.msg, close_msg, key)
    return fake_msg

@app.get(VER + "/vigenere/decryptor", tags=['decryptor'])
async def vigenere_encryptor():
    return fake_msg

# Run server: uvicorn main:app --reload
# Run docs: http://localhost:8000/docs