from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .agent import TitanicAgent
import os

app = FastAPI(title="Titanic QA API")
agent = TitanicAgent()

# Configure CORS so a deployed Streamlit frontend (or any other web UI)
# can call this API from a browser. In production you should restrict
# `allow_origins` to the real frontend host(s).
allowed = os.getenv("ALLOWED_ORIGINS")
if allowed:
    origins = [o.strip() for o in allowed.split(",") if o.strip()]
else:
    origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
