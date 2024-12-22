import httpx

from chatsky import BaseCondition, Context


class Intent(BaseCondition):
    intent: str

    async def call(self, ctx: Context) -> bool:
        async with httpx.AsyncClient() as client:
            r = await client.post("http://models_service:8000/intent", json={"request": ctx.last_request.text})

        result = r.json()["result"]

        return result == self.intent
