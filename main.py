from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel, Field
import secrets

from models import ApiKey
from db import create_db_and_tables, get_session
from sqlmodel import Session

app = FastAPI()

@app.on_event('startup')
def on_startup():
    create_db_and_tables

# class KeyRequest(BaseModel):
#     prefix: str = 'sk_test'                           #Prefix of the API KEY
#     length: int = Field(default=32, ge=8, le=64)      #Length of the API KEY

@app.post('/generate-key')
def generate_key(
    prefix: str = Query('sk_test'),
    length: int = Query(default=32, ge=8, le=64),
    session: Session =  Depends(get_session)
):
    token = secrets.token_urlsafe(length)
    full_key = f" {prefix}_{length}"
    key_obj = ApiKey(key=full_key, prefix=prefix)
    session.add(key_obj)
    session.commit()
    session.refresh(key_obj)
    return {'API KEY': key_obj.key}

    # random_part = secrets.token_urlsafe(data.length)[:data.length]
    # key = f"{data.prefix}_{random_part}"
    # return {'apikey': key}]

@app.get('/keys')
def list_keys(session: Session = Depends(get_session)):
    keys = session.query(ApiKey).all()
    return keys  



