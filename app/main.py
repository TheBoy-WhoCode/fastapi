from fastapi import FastAPI

from app.routers.vote import vote
from . import models
from .database import engine
from .routers import users, posts, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

# HOME ROUTE


@app.get("/")
async def root():
    return {"message": "Hello Jiten"}
