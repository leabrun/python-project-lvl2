import yaml
import json
from pathlib import Path


def get_dict_from_file(file_path):
    format = get_extension(file_path)
    data = parse(read_file(file_path), format)
    return data


def get_extension(file_path):
    file_extencion = Path(file_path).suffix

    if file_extencion.lower() == '.json':
        return 'json'
    elif file_extencion.lower() == '.yaml' or file_extencion.lower() == '.yml':
        return 'yaml'


def read_file(filename):
    return open(filename)


def parse(filename, format):
    if format == 'json':
        return json.load(filename)
    elif format == 'yaml':
        return yaml.safe_load(filename)
