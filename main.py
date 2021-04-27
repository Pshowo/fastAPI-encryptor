from fastapi import FastAPI

app = FastAPI()
VER = '/v1' 

fake_msg = {
    0: "fake msg"
}

@app.get("/")
async def root():
    return {
        "version": "1.0",
        "name": "fastAPI-encryptor",
        "docs": "/docs",
        "cipher_vigenere": "/v1/vigenere"
        }

@app.get(VER + "/vigenere")
async def vigenere():
    return {
        "encryptor": "/encryptor",
        "decryptor": "/decryptor"
    }

@app.get(VER + "/vigenere/encryptor")
async def vigenere_encryptor():
    return fake_msg

@app.get(VER + "/vigenere/decryptor")
async def vigenere_encryptor():
    return fake_msg

# Run server: uvicorn main:app --reload
# Run docs: http://localhost:8000/docs