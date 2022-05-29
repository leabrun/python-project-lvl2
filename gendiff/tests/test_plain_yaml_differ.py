from gendiff.differ import generate_diff

correct_answer = """
{
  "- follow": false,
  " host": "hexlet.io",
  "- proxy": "123.234.53.22",
  "- timeout": 50,
  "+ timeout": 20,
  "+ verbose\"": true
}
"""


def test_generate_diff():
    file_path1 = 'gendiff/tests/fixture/plain_yaml/file1.yaml'
    file_path2 = 'gendiff/tests/fixture/plain_yaml/file2.yaml'
    answer = generate_diff(file_path1, file_path2)
    assert answer == correct_answer


print(test_generate_diff())
