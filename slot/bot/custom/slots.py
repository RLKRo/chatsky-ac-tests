import httpx

from chatsky.slots.slots import SlotNotExtracted
from chatsky import Message


async def extract(request: Message, regexp: str):
    async with httpx.AsyncClient() as client:
        r = await client.post("http://models_service:8000/slot", params={"request": request.text, "regexp": regexp})

    result = r.json()["result"]

    if result is None:
        return SlotNotExtracted("Match not found")
    return result


async def extract_email(request: Message):
    regexp = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"

    return await extract(request, regexp)


async def extract_bitcoin_address(request: Message):
    regexp = r"[13][a-km-zA-HJ-NP-Z0-9]{26,33}"

    return await extract(request, regexp)
