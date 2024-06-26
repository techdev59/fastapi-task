from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.dependencies import get_db, get_current_user
from cachetools import TTLCache

router = APIRouter()

cache = TTLCache(maxsize=100, ttl=300)

@router.post("/addpost", response_model=schemas.Post)
def add_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if len(post.text.encode('utf-8')) > 1024 * 1024:
        raise HTTPException(status_code=400, detail="Payload too large")
    return crud.create_post(db=db, post=post, user_id=current_user.id)

@router.get("/getposts", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.id in cache:
        return cache[current_user.id]
    posts = crud.get_posts(db=db, user_id=current_user.id)
    cache[current_user.id] = posts
    return posts

@router.delete("/deletepost/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    success = crud.delete_post(db=db, post_id=post_id, user_id=current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted"}
