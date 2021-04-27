from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Run server: uvicorn main:app --reload
# Run docs: http://localhost:8000/docs