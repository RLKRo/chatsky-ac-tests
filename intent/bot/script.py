from chatsky import RESPONSE, TRANSITIONS, Transition as Tr
import chatsky.conditions as cnd

from .custom import conditions


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
            RESPONSE: "Welcome to our service! What would you like to do?",
            TRANSITIONS: [
                Tr(dst="buy", cnd=conditions.Intent(intent="buy")),
                Tr(dst="sell", cnd=conditions.Intent(intent="sell")),
                Tr(dst="unknown", priority=0.5),
            ]
        },
        "buy": {
            RESPONSE: "It appears you want to buy something."
        },
        "sell": {
            RESPONSE: "It appears you want to sell something."
        },
        "unknown": {
            RESPONSE: "Please state if you'd like to buy or sell something."
        }
    }
}

START_NODE = ("technical_flow", "start_node")
FALLBACK_NODE = ("technical_flow", "fallback")
