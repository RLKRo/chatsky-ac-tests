from json import load
from pathlib import Path
from uuid import uuid4
from time import perf_counter
import asyncio

import pytest
from chatsky import Message

from .bot.pipeline import pipeline


TEST_DATA_FILE = Path(__file__).parent / "test_data.json"
DIALOG_TURN_TIMEOUT = 0.4

with open(TEST_DATA_FILE, "r") as fd:
    TEST_DATA = load(fd)


@pytest.mark.parametrize(
    "test_case", TEST_DATA
)
def test_happy_paths(test_case: str):
    happy_path = TEST_DATA[test_case]

    ctx_id = uuid4()

    for step_id, (request_raw, reference_response_raw) in enumerate(happy_path):
        request = Message.model_validate(request_raw)
        reference_response = Message.model_validate(reference_response_raw)
        print(f"USER: {request}")

        start_time = perf_counter()
        ctx = asyncio.run(pipeline._run_pipeline(request, ctx_id))
        total_time = perf_counter() - start_time
        actual_response = ctx.last_response
        print(f"BOT : {actual_response}")
        print(f"TIME: {total_time}")

        assert reference_response == actual_response, f"""check_happy_path failed
step id: {step_id}
reference response: {reference_response}
actual response: {actual_response}
"""
        assert total_time < DIALOG_TURN_TIMEOUT
