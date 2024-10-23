#!/bin/bash

time python -c "from bot.pipeline import pipeline; from chatsky import Message; pipeline(Message('/start'))"
