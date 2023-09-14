from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Welcome to Musa Okai's HNGTask2 API"}

@app.post("/api", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):

    if person.name == "":
        raise HTTPException(status_code=400, detail="Name can't be empty")
    
    db_person = crud.get_person_name(db, name= person.name)
    
    if db_person:
        raise HTTPException(status_code=409, detail= "Name already exists")
    return crud.create_person(db=db, person=person)

@app.get("/api/", response_model= list[schemas.Person])
def read_persons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    persons = crud.get_persons(db, skip=skip, limit=limit)
    return persons

@app.get("/api/user_id", response_model=schemas.Person)
def read_person(name: str , db: Session = Depends(get_db)):
    if not name:
        raise HTTPException(
            status_code=400, detail="Name query parameter is required")
    
    db_person = crud.get_person_name(db = db , name= name)

    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

@app.put("/api/user_id", response_model= schemas.Person)
def update_person(new_person: schemas.PersonCreate, name: str = Query(), db: Session = Depends(get_db)):
    
    db_person = crud.get_person_name(db = db, name= name)
    
    if db_person is None:
        raise HTTPException(status_code=404, detail= "Name not found")
    return crud.update_person(db=db, name= name, update_person=new_person)


@app.delete("/api/user_id")
def delete_user(name: str = Query(..., description="Name of the user"), db: Session = Depends(get_db)):

    db_person = crud.get_person_name(name=name, db=db)

    if db_person is None:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = crud.delete_person(name=name, db=db)
    if deleted_user:
        return {"message": f"User with name {name} has been deleted"}
    raise HTTPException(status_code=500, detail="Failed to delete user")