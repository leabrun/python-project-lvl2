import json
import yaml


def open_file(file_path):
    if file_path.endswith('.yaml'):
        return yaml.load(open(file_path), Loader=yaml.Loader)
    elif file_path.endswith('.json'):
        return json.load(open(file_path))


def open_files(first_path, second_path):
    file1 = open_file(first_path)
    file2 = open_file(second_path)

    return file1, file2


def formater(diff_list, format):
    if format == 'stylish':
        return stylish(diff_list)
    elif format == 'plain':
        return plain(diff_list)
    elif format == 'json':
        return to_json(diff_list)


def to_json(diff_list):
    return json.dumps(diff_list, indent=4)


def plain(diff_list):
    diff_list.sort(key=lambda x: x['name'])
    result = get_diff_plain_list(diff_list)
    return '\n'.join(result)


def get_diff_plain_list(diff_list, path=''):
    result = []
    for node in diff_list:
        if node['status'] == 'nested':
            path_to_change = path + node['name'] + '.'
            difference = get_diff_plain_list(node['children'], path_to_change)
            result.extend(difference)
        if node['status'] == 'added':
            path_to_change = path + node['name']
            change = create_change(node['data'])
            difference = (
                f"Property '{path_to_change}' was added "
                f"with value: {change}"
            )
            result.append(difference)
        if node['status'] == 'deleted':
            path_to_change = path + node['name']
            change = create_change(node['data'])
            difference = "Property '{}' was removed".format(path_to_change)
            result.append(difference)
        if node['status'] == 'changed':
            path_to_change = path + node['name']
            change_before = create_change(node['data before'])
            change_after = create_change(node['data after'])
            difference = (
                f"Property '{path_to_change}' was updated. "
                f"From {change_before} to {change_after}"
            )
            result.append(difference)
    return result


def create_change(data):
    if type(data) is dict or type(data) is list:
        result = '[complex value]'
    elif data is False:
        result = 'false'
    elif data is True:
        result = 'true'
    elif data is None:
        result = 'null'
    elif type(data) is str:
        result = "'{}'".format(data)
    else:
        result = '{}'.format(data)
    return result


def stylish(diff_list, level=0):
    result = '{\n'
    indent = '  '

    for i in range(level):
        indent += '    '

    diff_list.sort(key=lambda x: x['name'])

    for node in diff_list:
        if node['status'] == 'nested':
            data = stylish(node['children'], level + 1)
            result += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'not changed':
            data = format_data(node['data'], indent)
            result += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'added':
            data = format_data(node['data'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
        if node['status'] == 'deleted':
            data = format_data(node['data'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
        if node['status'] == 'changed':
            data = format_data(node['data before'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
            data = format_data(node['data after'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
    result += indent[:-2] + '}'

    return result


def format_data(data, indent):
    if type(data) is dict:
        indent += '    '
        result = '{\n'
        for key in data.keys():
            value = format_data(data[key], indent)
            result += indent + '  ' + key + ': ' + value + '\n'
        result += indent[:-2] + '}'
    elif data is False:
        result = 'false'
    elif data is True:
        result = 'true'
    elif data is None:
        result = 'null'
    else:
        result = str(data)

    return result


def differ(dict1, dict2):
    result = []
    keys = sorted(dict1.keys() | dict2.keys())

    for key in keys:
        node = {'name': key}
        if key not in dict1:
            node['status'] = 'added'
            node['data'] = dict2[key]
        elif key not in dict2:
            node['status'] = 'deleted'
            node['data'] = dict1[key]
        elif type(dict1[key]) is dict and type(dict2[key]) is dict:
            node['status'] = 'nested'
            node['children'] = differ(dict1[key], dict2[key])
        elif dict1[key] == dict2[key]:
            node['status'] = 'not changed'
            node['data'] = dict1[key]
        else:
            node['status'] = 'changed'
            node['data before'] = dict1[key]
            node['data after'] = dict2[key]
        result.append(node)

    return result


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1, dict2 = open_files(file_path1, file_path2)
    diff = differ(dict1, dict2)
    return formater(diff, format)
