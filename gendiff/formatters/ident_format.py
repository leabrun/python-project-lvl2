from gendiff.formatters.to_stylish import stylish
from gendiff.formatters.to_plain import plain
from gendiff.formatters.to_json import to_json


def formater(diff_list, format):
    if format == 'stylish':
        return stylish(diff_list)
    elif format == 'plain':
        return plain(diff_list)
    elif format == 'json':
        return to_json(diff_list)
