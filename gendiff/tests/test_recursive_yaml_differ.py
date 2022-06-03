from gendiff.differ import generate_diff

correct_answer = """
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
"""


def test_generate_diff():
    file_path1 = 'gendiff/tests/fixture/recursive_yaml/file1.yaml'
    file_path2 = 'gendiff/tests/fixture/recursive_yaml/file2.yaml'
    answer = generate_diff(file_path1, file_path2)
    assert answer == correct_answer
