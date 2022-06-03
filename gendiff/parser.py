import argparse


def arg_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format to output')

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
