from gendiff.differ import generate_diff

correct_answer = """
{
  "- follow": false,
  " host": "hexlet.io",
  "- proxy": "123.234.53.22",
  "+ timeout": 50,
  "- timeout": 20,
  "+ verbose": true
}
"""


def test_generate_diff():
    file_path1 = 'gendiff/tests/fixture/plain_json/file1.json'
    file_path2 = 'gendiff/tests/fixture/plain_json/file2.json'
    answer = generate_diff(file_path1, file_path2)
    assert answer == correct_answer
