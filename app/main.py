from fastapi import FastAPI
from .crud import create_author
from .database import SessionLocal
from .routes import router

app = FastAPI()

app.include_router(router)
# @app.get('/')
# def get_root():
#     return "Welcome to books api"
    

