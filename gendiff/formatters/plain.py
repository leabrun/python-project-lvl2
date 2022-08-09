def plain(diff):
    diff.sort(key=lambda x: x['name'])
    result = build_plain(diff)
    return '\n'.join(result)


def build_plain(diff, path=''):
    result = []
    for node in diff:
        if node['status'] == 'nested':
            path_to_change = path + node['name'] + '.'
            difference = build_plain(node['children'], path_to_change)
            result.extend(difference)
        if node['status'] == 'added':
            path_to_change = path + node['name']
            change = to_string(node['data'])
            difference = (
                f"Property '{path_to_change}' was added "
                f"with value: {change}"
            )
            result.append(difference)
        if node['status'] == 'deleted':
            path_to_change = path + node['name']
            change = to_string(node['data'])
            difference = "Property '{}' was removed".format(path_to_change)
            result.append(difference)
        if node['status'] == 'changed':
            path_to_change = path + node['name']
            change_before = to_string(node['data before'])
            change_after = to_string(node['data after'])
            difference = (
                f"Property '{path_to_change}' was updated. "
                f"From {change_before} to {change_after}"
            )
            result.append(difference)
    return result


def to_string(data):
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
