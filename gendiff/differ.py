import json
import yaml


def filter_values(all_values, dict):
    values_copy = list(all_values.copy())

    for value in all_values:
        if value in dict:
            values_copy.remove(value)
            values_copy.insert(0, value)

    return values_copy


def open_file(file_path):
    if file_path.endswith('.yaml'):
        return yaml.load(open(file_path), Loader=yaml.Loader)
    elif file_path.endswith('.json'):
        return json.load(open(file_path))


def open_files(first_path, second_path):
    file1 = open_file(first_path)
    file2 = open_file(second_path)

    return file1, file2


def generate_diff(first_path, second_path):
    first_dict, second_dict = open_files(first_path, second_path)

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
            diff.append(('  ' + k, v))

    diff = json.dumps(dict(diff), indent=2, separators=('', ': '))

    return diff.replace('\"', '')
