from chatsky import Pipeline

from . import script


pipeline = Pipeline(
    script=script.SCRIPT,
    start_label=script.START_NODE,
    fallback_label=script.FALLBACK_NODE
)
