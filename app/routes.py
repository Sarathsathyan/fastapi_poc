from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas, database
router = APIRouter()

@router.post("/authors/", response_model=schemas.AuthorBase)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(database.get_db)):
    
    return crud.create_author(db, author)

