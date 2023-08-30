import json


def print_pretty_json(data: dict):
    pretty_json = json.dumps(data, indent=2)
    print(pretty_json)
