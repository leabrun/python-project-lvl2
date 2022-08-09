import json


def to_json(diff_list):
    return format(diff_list)


def format(diff_list):
    return json.dumps(diff_list, indent=4)
