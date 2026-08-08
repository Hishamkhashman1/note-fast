from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine #add more as needed
from sqlalchemy.orm import declarative_base, Session, sessionmaker

from pydantic import BaseModel

#app setup
app = FastAPI(title="get your notes now")

#Db Setup
engine = create_engine("sqlite:///notes.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

#Db models
class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index= True)
    title = Column(String)
    message = Column(String, nullable=False)

Base.metadata.create_all(engine)

#pydantic models (data class models)
class NoteCreate(BaseModel):
    id: int
    title:str
    message:str

class NoteResponse(BaseModel):
    id:int
    title:str
    message:str

    class Config:
        from_attributes = True

#db def for later DI
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

#endpoints go here think CRUD

@app.get("/")
def get_root():
    return {"message":"welcome to the notes API"}

@app.post("/notes/",response_model=NoteResponse)
def create_note(note:NoteCreate,db:Session=Depends(get_db)):
    new_note = Note(**note.model_dump())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

#get all
@app.get("/notes/",response_model=list[NoteResponse])
def get_all_notes(db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return notes



