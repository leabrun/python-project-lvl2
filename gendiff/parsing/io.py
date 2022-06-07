import yaml
import json
from pathlib import Path


def open_file(file_path, file_extencion):
    if file_extencion.lower() == '.json':
        with open(file_path) as f:
            return json.load(f)
    elif file_extencion.lower() == '.yaml' or file_extencion.lower() == '.yml':
        with open(file_path) as f:
            return yaml.safe_load(f)


def open_files(first_path, second_path):
    first_extencion = Path(first_path).suffix
    file1 = open_file(first_path, first_extencion)

    second_extencion = Path(second_path).suffix
    file2 = open_file(second_path, second_extencion)

    return file1, file2
