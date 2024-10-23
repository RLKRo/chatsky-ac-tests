from chatsky import RESPONSE, TRANSITIONS, LOCAL, Transition as Tr, PRE_TRANSITION, Message
import chatsky.processing as proc
import chatsky.conditions as cnd
import chatsky.responses as rsp
from chatsky.slots import FunctionSlot

from .custom import slots


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
        LOCAL: {
            PRE_TRANSITION: {
                "extract_slots": proc.Extract(
                    "email",
                    "bitcoin_address"
                )
            },
            TRANSITIONS: [
                Tr(dst="partially_extracted"),
                Tr(dst="fully_extracted", cnd=cnd.SlotsExtracted("email", "bitcoin_address"), priority=2),
            ]
        },
        "greeting_node": {
            RESPONSE: "Hi! To finish your order, "
                      "please provide your email and return bitcoin address in case the order fails.",
        },
        "partially_extracted": {
            RESPONSE: rsp.FilledTemplate(
                "You did not provide some of the data:\nemail: {email}\nbitcoin address: {bitcoin_address}"
            )
        },
        "fully_extracted": {
            RESPONSE: rsp.FilledTemplate(
                "Thank you. Your data:\nemail: {email}\nbitcoin address: {bitcoin_address}"
            )
        },
    }
}

START_NODE = ("technical_flow", "start_node")
FALLBACK_NODE = ("technical_flow", "fallback")

SLOTS = {
    "email": FunctionSlot(func=slots.extract_email),
    "bitcoin_address": FunctionSlot(func=slots.extract_bitcoin_address)
}
