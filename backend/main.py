from fastapi import FastAPI
from pydantic import BaseModel
from backend.agent import TitanicAgent

app = FastAPI(title="Titanic QA API")
agent = TitanicAgent()


class AskRequest(BaseModel):
    question: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/ask")
async def ask(req: AskRequest):
    res = agent.ask(req.question)
    return res


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
