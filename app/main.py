from fastapi import FastAPI
from .database import engine
from . import models
from .routers import user

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API")

app.include_router(user.router)