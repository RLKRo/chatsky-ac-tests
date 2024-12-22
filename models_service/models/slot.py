import re
from typing import Optional

from pydantic import BaseModel


class Input(BaseModel):
    request: str
    regexp: str
    group: int = 0


class SlotModel(BaseModel):
    result: Optional[str]


async def extract_slot(
    request: Input
) -> SlotModel:
    search = re.search(request.regexp, request.request)
    if search is None:
        return SlotModel(result=None)
    return SlotModel(
        result=search.group(request.group)
    )
