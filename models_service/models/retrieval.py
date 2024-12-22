from typing import Optional

from sentence_transformers import SentenceTransformer
from pydantic import BaseModel
import numpy as np


model = SentenceTransformer("clips/mfaq")


faq_dataset = {
    "What is Chatsky?": "Chatsky is an open-source, Apache 2.0-licensed library that was developed specifically for creating dialog systems.",
    "How to install Chatsky?": "Chatsky can be installed on your system using pip: `pip install chatsky`.",
}


class Input(BaseModel):
    request: str


class AnswerModel(BaseModel):
    result: Optional[str]


THRESHOLD = 5


async def get_answer(
    request: Input
) -> AnswerModel:
    questions = list(map(lambda x: "<Q>" + x, faq_dataset.keys()))
    q_emb, *faq_emb = model.encode(["<Q>" + request.request] + questions)

    scores = list(map(lambda x: np.linalg.norm(x - q_emb), faq_emb))

    argmin = scores.index(min(scores))
    if scores[argmin] < THRESHOLD:
        return AnswerModel(result=faq_dataset[list(faq_dataset.keys())[argmin]])
    return AnswerModel(result=None)
