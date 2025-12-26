let sessionId = null;

async function sendMessage(text = null) {
  const input = document.getElementById("message-input");
  const message = text || input.value.trim();
  if (!message) return;

  document.getElementById("welcome").style.display = "none";
  document.getElementById("chat-card").style.display = "block";

  appendMessage("user", message);
  input.value = "";

  try {
    const response = await fetch("/chat/message", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, sessionId })
    });

    const data = await response.json();
    sessionId = data.sessionId;
    appendMessage("ai", data.reply);
  } catch {
    appendMessage("ai", "Sorry, something went wrong.");
  }
}

function appendMessage(sender, text) {
  const chatBox = document.getElementById("chat-box");
  const div = document.createElement("div");
  div.className = `message ${sender}`;
  div.innerText = text;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function handleEnter(e) {
  if (e.key === "Enter") sendMessage();
}

function quickSend(btn) {
  sendMessage(btn.innerText);
}

function resetChat() {
  sessionId = null;
  document.getElementById("chat-box").innerHTML = "";
  document.getElementById("chat-card").style.display = "none";
  document.getElementById("welcome").style.display = "block";
}
