import pytest
from pathlib import Path
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize(
    "file1,file2,answer,format",
    [
        ('file1.json', 'file2.json', 'answer_stylish.txt', 'stylish'),
        ('file1.yml', 'file2.yml', 'answer_stylish.txt', 'stylish'),
        ('file1.json', 'file2.json', 'answer_plain.txt', 'plain'),
        ('file1.yml', 'file2.yml', 'answer_plain.txt', 'plain'),
        ('file1.json', 'file2.json', 'answer_json.json', 'json'),
        ('file1.yml', 'file2.yml', 'answer_json.json', 'json')
    ]
)
def test_differ(file1, file2, answer, format):
    file1_path = get_path(file1)
    file2_path = get_path(file2)
    answer_path = get_path(answer)
    with open('{}'.format(answer_path)) as f:
        answer = f.read()[:-1]
    assert generate_diff(file1_path, file2_path, format) == answer
    if format == 'stylish':
        assert generate_diff(file1_path, file2_path) == answer


def get_path(file):
    return Path(Path(__file__).parent.absolute() / 'fixtures' / file)
