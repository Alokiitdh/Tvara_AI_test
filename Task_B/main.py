from fastapi import FastAPI
from pydantic import BaseModel
from .llm import generate_response

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/generate/")
def generate(request: QueryRequest):
    response = generate_response(request.query)
    return {"response": response}
