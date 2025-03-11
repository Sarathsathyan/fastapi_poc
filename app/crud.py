from sqlalchemy.orm import Session
from .models import Author
from .schemas import AuthorCreate

def create_author(db: Session, author: AuthorCreate) -> Author:
    import ipdb; ipdb.set_trace()
    new_author = Author(name=author.name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author