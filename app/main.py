from fastapi import FastAPI, Request
from app.imap_sync import start_sync
from app.elastic import search_emails, store_email
from app.ai_categorizer import categorize_email
from app.notifier import notify_interested
from pydantic import BaseModel

app = FastAPI()

class EmailData(BaseModel):
    subject: str
    sender: str
    body: str
    folder: str
    account: str

@app.on_event("startup")
async def startup_event():
    start_sync()

@app.post("/email")
def store_and_categorize_email(email: EmailData):
    label = categorize_email(email.body)
    store_email(email.dict(), label)
    if label == "Interested":
        notify_interested(email.dict())
    return {"status": "stored", "label": label}

@app.get("/emails/search")
def search(q: str):
    return search_emails(q)
