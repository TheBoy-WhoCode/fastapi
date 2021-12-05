from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    likes: Optional[int] = None




@app.get("/")
async def root():
    return {"message": "Hello Jiten"}

@app.post("/post")
async def create_posts(post: Post):
    print(post.title)
    return {"data":post.dict()}

