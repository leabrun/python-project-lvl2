from gendiff.formatters.ident_format import formater
from gendiff.differ import differ
from gendiff.parsing.io import open_files


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1, dict2 = open_files(file_path1, file_path2)
    diff = differ(dict1, dict2)
    return formater(diff, format)
