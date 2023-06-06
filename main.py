from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "hello world" }

@app.get("/sentiment/{text}")
async def sentiment(text):

    return {"sentiment": analyze_sentiment(text) }

def analyze_sentiment(text):
    return 1