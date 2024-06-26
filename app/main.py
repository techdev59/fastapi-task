import os
from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.routers import auth, posts
from app import models

# Load environment variables
env_file = ".env.prod" if os.getenv("ENV") == "production" else ".env"
load_dotenv(env_file)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

app.include_router(auth.router)
app.include_router(posts.router)

@app.on_event("startup")
async def startup():
    # Initialize database connection and create tables
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    # Close database connection
    pass
