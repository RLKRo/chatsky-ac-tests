from chatsky import Pipeline

from . import script
from . import interface


pipeline = Pipeline(
    script=script.SCRIPT,
    start_label=script.START_NODE,
    fallback_label=script.FALLBACK_NODE,
    messenger_interface=interface.HTTPMessengerInterface(),
    slots=script.SLOTS
)
