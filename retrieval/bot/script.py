from chatsky import RESPONSE, TRANSITIONS, Transition as Tr
import chatsky.conditions as cnd

from .custom.responses import ChatskyQnA


SCRIPT = {
    "technical_flow": {
        "start_node": {
            TRANSITIONS: [
                Tr(
                    dst=("main_flow", "greeting_node"),
                    cnd=cnd.ExactMatch("/start")
                )
            ],
        },
        "fallback": {
            RESPONSE: "Error.",
        },
    },
    "main_flow": {
        "greeting_node": {
            RESPONSE: "Hi! Ask me questions about Chatsky.",
            TRANSITIONS: [
                Tr(dst="qna")
            ]
        },
        "qna": {
            RESPONSE: ChatskyQnA(),
            TRANSITIONS: [
                Tr(dst="qna")
            ]
        }
    }
}

START_NODE = ("technical_flow", "start_node")
FALLBACK_NODE = ("technical_flow", "fallback")
