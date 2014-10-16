import argparse

## Louie: This is weird. You're declaring your parser in the global namespace and then letting lex access it.
## Try putting this parsing into a file, returning the parsed arguments, then passing that into your lex function.
def lex_parser():
    parser = argparse.ArgumentParser(description='Lexicographic sort.')
    parser.add_argument("infile", help="A text based input file with .txt extension", type=argparse.FileType('r'))
    parser.add_argument("outfile", help="A text base output file with .txt extension", type=argparse.FileType('w'))
    parser.add_argument("-i", "--insensitive", action="store_true", help="case insensitive lexicographic sort")
    parser.add_argument("-n", "--nline", type=int, help="number of lines to print in output")
    # TODO: How to set the default max for --nline to be based on the length of the input file?

    ## Louie: You can just set default to None, then in your lex function, check if it's None and if it is then set it to length of file.
    ## You cannot do it at the moment of the parse because you don't have the file yet.

    parser.add_argument("-p", "--printout", type=str, help="print result on console", default="no",
                        choices=['yes', 'no'])

    ## Parser looks good besides small fixes mentioned above.

    args = parser.parse_args()
    return args

def lex(args):
    """
    This program performs a simple lexicographic sort
    :param args:
    :return:
    """
    ## Louie: Your code is very dense. Try to break it up into "logical" chunks. Think code paragraphs.
    ## It's easier to read that way.


    # Open file and read the input lines
    to_sort = args.infile
    lines = to_sort.readlines()
    to_sort.close()

    #start checking for flags and options
    if args.insensitive:  # add check to make sure its a string
        lex_sort = sorted(lines, key=lambda y: y.lower())
    else:
        lex_sort = sorted(lines)

    ## Louie: Use a list comprehension for this. Read about it here: https://docs.python.org/3/tutorial/datastructures.html. Section 5.1.3
    #Check for value of --nline. If no value given default it to max length of input/output sort
    if args.nline == None:
        nline = len(lex_sort)
    else:
        nline=args.nline

    #clean resultant output to be printed in the outfile or console
    out_sort = args.outfile
    for i in range(nline):
        output=lex_sort[i]
        out_sort.write(output)
        #check for console printing in the same loop
        if args.printout == 'yes':
            print(lex_sort[i])
    out_sort.close()

if __name__ == "__main__":
    args=lex_parser()
    lex(args)
