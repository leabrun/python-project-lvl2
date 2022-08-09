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
            data = to_string(node['data'], indent)
            result += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'added':
            data = to_string(node['data'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
        if node['status'] == 'deleted':
            data = to_string(node['data'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
        if node['status'] == 'changed':
            data = to_string(node['data before'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
            data = to_string(node['data after'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
    result += indent[:-2] + '}'

    return result


def to_string(data, indent):
    if type(data) is dict:
        indent += '    '
        result = '{\n'
        for key in data.keys():
            value = to_string(data[key], indent)
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
