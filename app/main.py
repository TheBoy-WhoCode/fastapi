from fastapi import FastAPI
from typing import List
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine
from .routers import users, posts, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host="localhost", database="fastapi", user="postgres", password="Elliot", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Databse Connected successfully...")
        break
    except Exception as error:
        print(error)
        time.sleep(2)


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

# HOME ROUTE


@app.get("/")
async def root():
    return {"message": "Hello Jiten"}
