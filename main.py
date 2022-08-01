from fastapi import FastAPI, Query, HTTPException, status
from pydantic import BaseModel
from typing import Optional
import requests


app = FastAPI()


url = "https://jsonplaceholder.typicode.com/posts"
headers = {"user-agent": "app/0.0.1"}
res = requests.get(url, headers=headers)


database = res.json()


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class UpdatePost(BaseModel):
    userId: Optional[int] = None
    id: Optional[int] = None
    title: Optional[str] = None
    body: Optional[str] = None


@app.get("/get-posts/")
def get_posts():
    return database


@app.get("/get-post/{post_id}")
def get_post(post_id: int = Query(None, description="The ID of the post you want to view")):
    for post in database:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Post title not found.")


@app.get("/get-post-by-user/{userId}")
def get_post(user_id: int = Query(None, description="The ID of the user you want to view posts of")):
    posts = []
    for post in database:
        if post["userId"] == user_id:
            posts.append(post)
    if len(posts) != 0:
        return posts
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="User ID not found.")


@app.get("/get-by-title/{title}")
def get_post(title: str = Query(None, description="Title of the post you want to view")):
    posts = [post for post in database if title.lower() in post["title"].lower()]
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post title not found.")
    return posts if len(posts) > 1 else posts[0]


@app.post("/create-post/{post_id}")
def create_post(post_id: int, post: Post):
    if post_id in database:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Post ID already exists.")
    database[post_id] = post
    return database[post_id]


@app.put("/update-post/{post_id}")
def update_post(post_id: int, post: UpdatePost):
    if post_id not in database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post ID does not exist.")
    if post.title is not None:
        database[post_id].title = post.title
    if post.body is not None:
        database[post_id].body = post.title
    return database[post_id]


@app.delete("/delete-post")
def delete_post(post_id: int = Query(None, description="The ID of the post you want to delete")):
    for post in database:
        if post["id"] == post_id:
            database.remove(post)
            return database
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Post ID does not exist.")
