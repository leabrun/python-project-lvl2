#!/usr/bin/env python3

from gendiff.parser import arg_parser
from gendiff.differ import generate_diff


def main():
    first_file, second_file, format = arg_parser()
    diff = generate_diff(first_file, second_file, format)
    print(diff)


if __name__ == '__main__':
    main()
