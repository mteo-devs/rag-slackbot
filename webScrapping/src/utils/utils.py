import json


def writeJSON(filename: str, jsonObj: dict):
    with open(filename, "w") as jsonFile:
        json.dump(jsonObj, jsonFile, indent=4)


def readJSON(filename: str) -> dict:
    with open(filename) as f:
        return json.load(f)

