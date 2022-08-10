from gendiff.formatters.formatting import formating
from gendiff.differ import differ
from gendiff.parsing.io import get_dict_from_file


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = get_dict_from_file(file_path1)
    dict2 = get_dict_from_file(file_path2)
    diff = differ(dict1, dict2)
    return formating(diff, format)
