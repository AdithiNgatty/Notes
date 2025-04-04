from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (Frontend-Backend Communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Connection
client = MongoClient("mongodb://mongo:27017")
db = client.notes_db
notes_collection = db.notes

# Pydantic Model
class Note(BaseModel):
    text: str

@app.get("/notes")
async def get_notes():
    notes = list(notes_collection.find({}, {"_id": 0}))  # Exclude _id
    return notes

@app.post("/notes")
async def add_note(note: Note):
    notes_collection.insert_one(note.dict())
    return {"message": "Note added"}

@app.delete("/notes")
async def delete_notes():
    notes_collection.delete_many({})  # Deletes all notes
    return {"message": "All notes deleted"}
