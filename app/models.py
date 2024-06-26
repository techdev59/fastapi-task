from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    class Config:
        from_attributes = True

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="posts")
    class Config:
        from_attributes = True

User.posts = relationship("Post", back_populates="owner")
