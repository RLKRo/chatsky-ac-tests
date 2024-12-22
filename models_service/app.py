import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from models.slot import extract_slot
from models.intent import get_intent
from models.retrieval import get_answer


app = FastAPI()


app.post("/slot")(extract_slot)
app.post("/intent")(get_intent)
app.post("/retrieve")(get_answer)


class HealthCheck(BaseModel):
    status: str = "OK"


@app.get("/health")
def get_health() -> HealthCheck:
    return HealthCheck(status="OK")


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )
