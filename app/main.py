from os import makedev
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
import time
from psycopg2.extras import RealDictCursor

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


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


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
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    print(posts)
    return {"data": posts}


@app.get("/posts/latest")
async def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}


@app.get("/posts/{id}")
async def get_post(id: int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID: {id} not found!")

    return {"data": post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING *""",
                   (str(id), ))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The post you're trying to delete doesn't exists")

    return {"error": "false", "detail": "Post successfully deleted"}


@app.put("/posts/{id}")
async def update_post(id: int, post: Post):

    cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s RETURNING * """,
                   (post.title, post.content, post.published))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The post you're trying to delete doesn't exists")

    return {"detail": "Post Updated successfully"}
