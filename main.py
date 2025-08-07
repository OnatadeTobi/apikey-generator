from fastapi import FastAPI
import secrets

app = FastAPI()

@app.post('/generate-key')
def generate_key():
    key = 't-key_'  + secrets.token_urlsafe(24)
    return {'apikey': key}
