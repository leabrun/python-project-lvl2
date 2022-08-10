import yaml
import json
from pathlib import Path


def get_dict_from_file(file_path):
    file_extension = Path(file_path).suffix
    return open_file(file_path, file_extension)


def open_file(file_path, file_extencion):
    if file_extencion.lower() == '.json':
        with open(file_path) as f:
            return json.load(f)
    elif file_extencion.lower() == '.yaml' or file_extencion.lower() == '.yml':
        with open(file_path) as f:
            return yaml.safe_load(f)
