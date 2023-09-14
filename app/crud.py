from sqlalchemy.orm import Session
from . import models, schemas

def get_person(db: Session, user_id: int):
    return db.query(models.Person).filter(models.Person.id == user_id).first()

def get_person_name(db: Session, name: str):
    return db.query(models.Person).filter(models.Person.name == name).first()

def get_persons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Person).offset(skip).limit(limit).all()

def create_person(db: Session, person: schemas.PersonCreate):
    new_person = models.Person(name= person.name)
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person

def update_person(db: Session, name: str, update_person: schemas.PersonCreate):
    db_person = db.query(models.Person).filter(
        models.Person.name == name).first()
    db_person.name = update_person.name
    db.commit()
    db.refresh(db_person)
    return db_person

def delete_person(db:Session, name: str):
    db.query(models.Person).filter(
        models.Person.name == name).delete()
    db.commit()
    return f"Person with name: {name} has been deleted"