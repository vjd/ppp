import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Lexicographic sort.')
    parser.add_argument("infile", help="A text based input file with .txt extension")
    parser.add_argument("outfile", help="A text base output file with .txt extension")
    parser.add_argument("-i", "--insensitive", action="store_true", help="case insensitive lexicographic sort")

    return parser.parse_args()

def other_function(args):
    print("infile: {}".format(args.infile))
    print("infile: {}".format(args.outfile))
    print("infile: {}".format(args.insensitive))


if __name__ == '__main__':
    args = parse_args()
    other_function(args)
