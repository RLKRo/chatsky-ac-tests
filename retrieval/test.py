from json import load
from pathlib import Path
from uuid import uuid4
from time import perf_counter
import asyncio

import httpx
import pytest


TEST_DATA_FILE = Path(__file__).parent / "test_data.json"
DIALOG_TURN_TIMEOUT = 0.4

with open(TEST_DATA_FILE, "r") as fd:
    TEST_DATA = load(fd)


async def get_response(request: str, ctx_id: str):
    async with httpx.AsyncClient() as client:
        r = await client.get("http://retriaval:5000/chat", params={"request": request, "ctx_id": ctx_id})
    return r.json()["response"]


@pytest.mark.parametrize(
    "test_case", TEST_DATA
)
def test_happy_paths(test_case: str):
    happy_path = TEST_DATA[test_case]

    ctx_id = str(uuid4())

    for step_id, (request, reference_response) in enumerate(happy_path):
        print(f"USER: {request}")

        start_time = perf_counter()

        response = asyncio.run(get_response(request, ctx_id))

        total_time = perf_counter() - start_time

        print(f"BOT : {response}")
        print(f"TIME: {total_time}")

        assert reference_response == response, f"""check_happy_path failed
step id: {step_id}
reference response: {reference_response}
actual response: {response}
"""
        assert total_time < DIALOG_TURN_TIMEOUT
