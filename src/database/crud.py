from sqlalchemy.orm import Session

from src.database.models import models, schemas

""" 
Create utility functions to: 
1. Read a single user by ID and by email 
2. Read multiple users 
3. Read multiple items 
"""


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)   # Note: User item.model_dump() in pydantic v2
    db.add(db_item)  # Adds instance to database session
    db.commit()  # Commits the changes to the database
    db.refresh(db_item)  # Refreshes instance so it contains any new data from the database like the generated ID
    return db_item
