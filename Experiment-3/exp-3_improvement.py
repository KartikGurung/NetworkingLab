from fastapi import FastAPI
from random import randint
from hashlib import sha256

app = FastAPI()


@app.get("/")
def home():
    return "This is the home directory"


@app.post("/user", status_code=201)
def challange():
    nonce = randint(0, 50000)
    secret = randint(0, 30005)

    hash_response = sha256(f"{nonce}{secret}".encode()).hexdigest()

    return {"nonce": nonce, "secret": secret, "hash_response": hash_response}