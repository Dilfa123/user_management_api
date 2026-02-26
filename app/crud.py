from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
from .utils import hash_password

def create_user(db: Session, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)

    db_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(models.User).all()


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    user = get_user(db, user_id)

    if user_update.email:
        existing_email = db.query(models.User).filter(
            models.User.email == user_update.email,
            models.User.id != user_id
        ).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already in use")

    for key, value in user_update.model_dump(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}