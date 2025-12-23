import requests
from app.core.prompt import SYSTEM_PROMPT
from app.core.config import settings

GROQ_URL = settings.GROQ_API_URL
MODEL = settings.LLM_MODEL


def generate_reply(history, user_message):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    for msg in history:
        role = "assistant" if msg.sender == "ai" else "user"
        messages.append({"role": role, "content": msg.text})

    messages.append({"role": "user", "content": user_message})

    try:
        response = requests.post(
            GROQ_URL,
            headers={
                "Authorization": f"Bearer {settings.GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL,
                "messages": messages,
                "max_tokens": 200
            },
            timeout=15
        )

        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]

    except Exception:
        return (
            "Sorry, the support agent is temporarily unavailable. "
            "Please try again in a moment."
        )
