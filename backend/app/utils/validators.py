MAX_MESSAGE_LENGTH = 1000

def validate_message(message: str):
    if not message or not message.strip():
        raise ValueError("Message cannot be empty")

    if len(message) > MAX_MESSAGE_LENGTH:
        return message[:MAX_MESSAGE_LENGTH]

    return message.strip()
