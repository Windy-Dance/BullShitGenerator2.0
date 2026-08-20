# coding : utf-8
# Author : Parallel
# Create On
import json


def readJSON(filename=""):
    if not filename:
        return None
    if not filename.lower().endswith(".json"):
        return None
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)