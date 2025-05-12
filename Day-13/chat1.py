from flask import Flask, request, render_template, session, redirect
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_mistralai import ChatMistralAI

app = Flask(__name__)
app.secret_key = 'secret_key' 


model = ChatMistralAI(model="open-mistral-nemo", temperature=0, max_retries=2, api_key='TGQVjoqcEdUcgMuW9rDrhqxLzMmIYY9A')


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("placeholder", "{chat_history}"),
    ("human", "{query}")
])


chain = prompt | model


chat_histories = {}

def get_history() -> ChatMessageHistory:
    """Fetch or create a new message history for the session."""
    session_id = session.get("session_id")
    
    if not session_id:
        session["session_id"] = "default_session"
        session_id = session["session_id"]

    if session_id not in chat_histories:
        chat_histories[session_id] = ChatMessageHistory()
    return chat_histories[session_id]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        history = get_history()

        inputs = {"query": query, "chat_history": history.messages}
        result = chain.invoke(inputs)
        response = result.content

        history.messages.append({"type": "user", "content": query})
        history.messages.append({"type": "ai", "content": response})

        session["last_result"] = response

        return redirect("/")

    history = get_history()
    chat = [(msg["type"], msg["content"]) for msg in history.messages]

    result = session.get("last_result", "")

    return render_template("chat1.html", chat=chat, result=result)

if __name__ == "__main__":
    app.run(debug=True)

