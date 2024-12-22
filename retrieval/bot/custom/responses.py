import httpx

from chatsky import BaseResponse, Context, MessageInitTypes


class ChatskyQnA(BaseResponse):
    async def call(self, ctx: Context) -> MessageInitTypes:
        async with httpx.AsyncClient() as client:
            r = await client.post("http://models_service:8000/retrieve", json={"request": ctx.last_request.text})

        result = r.json()["result"]

        if result is None:
            return "I don't have an answer to that."
        return result
