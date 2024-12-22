import re
from typing import Optional

from pydantic import BaseModel


class Input(BaseModel):
    request: str


class IntentModel(BaseModel):
    result: Optional[str]


intents = {
    "buy": re.compile(r"\b(?:buy|purchase|acquire|get|take|obtain)\b", flags=re.I),
    "sell": re.compile(r"\b(?:sell|sale|unload|trade)\b", flags=re.I)
}


async def get_intent(
    request: Input
) -> IntentModel:
    for intent, pattern in intents.items():
        if pattern.search(request.request) is not None:
            return IntentModel(result=intent)
    return IntentModel(result=None)
