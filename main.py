from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

app = FastAPI()
OPENAI_API = "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"

openai.api_key = OPENAI_API
class UserInput(BaseModel):
    user_input: str
class BotReply(BaseModel):
    bot_reply: str

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/chat", response_model=BotReply)
def chat(user_input: UserInput):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=user_input.user_input,
            max_tokens=50
        )
        bot_reply = response.choices[0].text.strip()
        return {"bot_reply": bot_reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ChatGPT API error: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
