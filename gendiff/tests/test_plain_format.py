from gendiff.differ import generate_diff

correct_answer = """
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
"""


def test_generate_diff():
    file_path1 = 'gendiff/tests/fixture/recursive_json/file1.json'
    file_path2 = 'gendiff/tests/fixture/recursive_json/file2.json'
    answer = generate_diff(file_path1, file_path2, 'plain')
    assert answer == correct_answer
