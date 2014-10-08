import argparse

parser = argparse.ArgumentParser(description='Lexicographic sort.')
parser.add_argument("infile", help="A text based input file with .txt extension", type=argparse.FileType('r'))
parser.add_argument("outfile", help="A text base output file with .txt extension", type=argparse.FileType('w'))
parser.add_argument("-i", "--insensitive", action="store_true", help="case insensitive lexicographic sort")
parser.add_argument("-n", "--nline", type=int, help="number of lines to print in output", default=100)
# TODO: How to set the default max for --nline to be based on the length of the input file?
parser.add_argument("-p", "--printout", type=str, help="print result on console", default="no",
                    choices=['yes', 'no'])

args = parser.parse_args()

def lex(infile, outfile):
    '''
    This program performs a simple lexicographic sort
    :param infile: input text based file
    :param outfile: output file with sorted text
    :return: outfile and option print on the console
    '''
    clean_lex_sort = []
    to_sort = infile
    lines = to_sort.readlines()
    to_sort.close()
    if args.insensitive:  # add check to make sure its a string
        lex_sort = sorted(lines, key=lambda y: y.lower())
    else:
        lex_sort = sorted(lines)
    for i in range(len(lex_sort)):
        clean_lex_sort.append(lex_sort[i].strip('\n'))
    #clean_lex_sort = '/n'.join(clean_lex_sort)
    out_sort = args.outfile
    out_sort.write(str(clean_lex_sort))
    out_sort.close()
    print(lines)
    #nlines_to_print = args.nline

    if args.printout == 'yes':
        for i in clean_lex_sort:
            print(i)

# TODO: Learn how to format the list in outfile to print on a newline
# TODO: To print number of lines requested by user using --nline
# TODO: Type check for options with informative error messages in case of user entry error

if __name__ == "__main__":
    lex(infile=args.infile, outfile=args.outfile)