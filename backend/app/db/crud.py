import uuid
from sqlalchemy.orm import Session
from app.db.models import Conversation, Message

def get_or_create_conversation(db: Session, session_id: str | None):
    if session_id:
        convo = db.query(Conversation).filter_by(id=session_id).first()
        if convo:
            return convo

    convo = Conversation(id=str(uuid.uuid4()))
    db.add(convo)
    db.commit()
    db.refresh(convo)
    return convo


def save_message(db: Session, conversation_id: str, sender: str, text: str):
    msg = Message(
        conversation_id=conversation_id,
        sender=sender,
        text=text
    )
    db.add(msg)
    db.commit()


def get_conversation_history(db: Session, conversation_id: str, limit: int = 10):
    return (
        db.query(Message)
        .filter_by(conversation_id=conversation_id)
        .order_by(Message.timestamp.asc())
        .limit(limit)
        .all()
    )
