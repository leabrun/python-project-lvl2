import yaml
import json


def open_file(file_path):
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        return yaml.load(open(file_path), Loader=yaml.Loader)
    elif file_path.endswith('.json'):
        return json.load(open(file_path))


def open_files(first_path, second_path):
    file1 = open_file(first_path)
    file2 = open_file(second_path)

    return file1, file2
