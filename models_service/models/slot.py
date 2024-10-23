import re
from typing import Optional

from pydantic import BaseModel


class SlotModel(BaseModel):
    result: Optional[str]


async def extract_slot(
    request: str,
    regexp: str,
    group: int = 0,
) -> SlotModel:
    search = re.search(regexp, request)
    if search is None:
        return SlotModel(result=None)
    return SlotModel(
        result=search.group(group)
    )
