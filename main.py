from fastapi import FastAPI
from analyzer import sentiment_analyzer
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

@app.get("/")
async def root():
    return { "message": "hello world" }


@app.get("/sentiment/{text}")
async def sentiment(text):
    print(text)

    sentiment = sentiment_analyzer(text)

    return { "sentiment": sentiment }


