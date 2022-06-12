from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import to_json


def formating(diff_list, format):
    if format == 'stylish':
        return stylish(diff_list)
    elif format == 'plain':
        return plain(diff_list)
    elif format == 'json':
        return to_json(diff_list)
