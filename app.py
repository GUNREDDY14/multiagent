# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents import CoderAgent

app = FastAPI(title="LangChain Code Generator API")

# Initialize agent
coder_agent = CoderAgent()

# Request schema
class CodeRequest(BaseModel):
    prompt: str

# Response schema
class CodeResponse(BaseModel):
    generated_code: str

@app.post("/generate_code", response_model=CodeResponse)
def generate_code(request: CodeRequest):
    output = coder_agent.generate_code(request.prompt)
    if not output:
        raise HTTPException(status_code=500, detail="Code generation failed.")
    return CodeResponse(generated_code=output)
