from fastapi import FastAPI
from pydantic import BaseModel
import secrets

app = FastAPI()

class KeyRequest(BaseModel):
    prefix: str = 'sk_test'

@app.post('/generate-key')
def generate_key(data: KeyRequest):
    key = f"{data.prefix}_{secrets.token_urlsafe(24)}"
    return {'apikey': key}
