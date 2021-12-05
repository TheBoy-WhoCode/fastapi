from os import makedev
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    likes: Optional[int] = None


my_posts = [{"title": "AI", "content": "AI is the beast", "id": 1},
            {"title": "Computer Vision", "content": "Computer vision is best", "id": 2}]


def find_post(id):
    for i in my_posts:
        if i['id'] == id:
            return i


def find_index_post(id):
    for i, j in enumerate(my_posts):
        if j["id"] == id:
            return i


@app.get("/")
async def root():
    return {"message": "Hello Jiten"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.get("/posts/latest")
async def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}


@app.get("/posts/{id}")
async def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID: {id} not found!")

    return {"data": post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 10000)
    my_posts.append(post_dict)
    return {"data": my_posts}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The post you're trying to delete doesn't exists")
    else:
        my_posts.pop(index)
    return {"error": "false", "detail": "Post successfully deleted"}


@app.put("/posts/{id}")
async def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The post you're trying to delete doesn't exists")
    else:
        post_dict = post.dict()
        post_dict["id"] = id
        my_posts[index] = post_dict
    return {"detail": post_dict}
