import json
import yaml


def filter_values(all_values, dict):
    values_copy = list(all_values.copy())
    for value in all_values:
        if value in dict:
            values_copy.remove(value)
            values_copy.insert(0, value)
    return values_copy


def open_file(first_path, second_path):
    if first_path.endswith('.json') and second_path.endswith('.json'):
        first_dict = json.load(open(first_path))
        second_dict = json.load(open(second_path))
    elif first_path.endswith('.yaml') and second_path.endswith('.yaml'):
        first_dict = yaml.load(open(first_path), Loader=yaml.Loader)
        second_dict = yaml.load(open(second_path), Loader=yaml.Loader)
    return first_dict, second_dict


def generate_diff(first_path, second_path):
    first_dict, second_dict = open_file(first_path, second_path)
    identical = first_dict.items() & second_dict.items()
    missed = first_dict.items() - second_dict.items()
    extra = second_dict.items() - first_dict.items()
    all_values = identical | missed | extra
    all_values = filter_values(all_values, first_dict)
    sorted_pairs = sorted(
        all_values, key=lambda pair: pair[0].lower()
    )
    diff = []
    for k, v in sorted_pairs:
        if (k, v) in missed:
            diff.append(('- ' + k, v))
        elif (k, v) in extra:
            diff.append(('+ ' + k, v))
        else:
            diff.append((' ' + k, v))

    diff = json.dumps(dict(diff), indent=2)
    return diff
