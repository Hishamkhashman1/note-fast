from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Table, Integer, String, create_engine #add more as needed
from sqlalchemy.orm import declarative_base, Session, sessionmaker

from pydantic import BaseModel

#app setup
app = FastAPI(title="get your notes now")

#Db Setup
engine = create_engine("sqlite:///notes.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

#Db models
class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index= True)
    title = Column(String)
    message = Column(String, nullable=False)

    Base.metadata.create.all(engine)
