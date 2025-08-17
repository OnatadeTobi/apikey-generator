from fastapi import FastAPI
from pydantic import BaseModel, Field
import secrets

app = FastAPI()

class KeyRequest(BaseModel):
    prefix: str = 'sk_test'                           #Prefix of the API KEY
    length: int = Field(default=32, ge=8, le=64)      #Length of the API KEY

@app.post('/generate-key')
def generate_key(data: KeyRequest):

    random_part = secrets.token_urlsafe(data.length)[:data.length]
    key = f"{data.prefix}_{random_part}"
    return {'apikey': key}             
