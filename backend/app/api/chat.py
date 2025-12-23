from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.db.crud import (
    get_or_create_conversation,
    save_message,
    get_conversation_history
)
from app.utils.validators import validate_message
from app.services.llm_service import generate_reply

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/chat/message")
def chat_message(payload: dict, db: Session = Depends(get_db)):
    try:
        user_message = validate_message(payload.get("message"))
        session_id = payload.get("sessionId")

        conversation = get_or_create_conversation(db, session_id)

        save_message(db, conversation.id, "user", user_message)

        history = get_conversation_history(db, conversation.id)

        reply = generate_reply(history, user_message)

        save_message(db, conversation.id, "ai", reply)

        return {
            "reply": reply,
            "sessionId": conversation.id
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
