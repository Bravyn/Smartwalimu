from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"messaget": "Hello World"}

@app.get("/sentiment")
async def sentiment():
    pass