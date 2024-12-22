from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from chatsky.messengers.common import MessengerInterface
from chatsky import Message


class HTTPMessengerInterface(MessengerInterface):
    async def connect(self, pipeline_runner):
        app = FastAPI()

        class Input(BaseModel):
            ctx_id: str
            request: str

        class Output(BaseModel):
            response: Optional[str]

        @app.post("/chat")
        async def respond(request: Input) -> Output:
            context = await pipeline_runner(Message(text=request.request), request.ctx_id)
            return Output(response=context.last_response.text)

        class HealthCheck(BaseModel):
            status: str = "OK"

        @app.get("/health")
        def get_health() -> HealthCheck:
            return HealthCheck(status="OK")

        uvicorn.run(
            app,
            host="0.0.0.0",
            port=5000,
        )
