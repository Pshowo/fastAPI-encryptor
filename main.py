from fastapi import FastAPI

app = FastAPI()
VER = '/v1' 

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get(VER + "/")
async def root():
    return {
        "FastAPI": "encryptor",
        'version': VER
    }

# Run server: uvicorn main:app --reload
# Run docs: http://localhost:8000/docs