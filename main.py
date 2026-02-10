from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to CodeRefine!"}

# Define a request body model
class CodeInput(BaseModel):
    code: str

# Review endpoint
@app.post("/review")
def review_code(input: CodeInput):
    if "print" in input.code:
        return {"review": "Your code uses print statements. Consider using logging for better practice."}
    else:
        return {"review": "No obvious issues found in this simple check."}

# Optimize endpoint
@app.post("/optimize")
def optimize_code(input: CodeInput):
    suggestions = []
    if "for i in range(len(" in input.code:
        suggestions.append("Use 'for item in list' instead of indexing for better readability and performance.")
    if "==" in input.code and "True" in input.code:
        suggestions.append("Avoid comparing directly to True/False. Use conditions naturally.")
    if not suggestions:
        suggestions.append("No performance optimizations detected in this simple check.")
    return {"optimization": suggestions}

# Rewrite endpoint
@app.post("/rewrite")
def rewrite_code(input: CodeInput):
    # Very simple rewrite example
    if "print" in input.code:
        rewritten = input.code.replace("print", "logging.info")
        return {"rewritten_code": f"import logging\nlogging.basicConfig(level=logging.INFO)\n{rewritten}"}
    else:
        return {"rewritten_code": input.code}