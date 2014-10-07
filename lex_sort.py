import argparse

parser = argparse.ArgumentParser(description='Lexicographic sort.')
parser.add_argument("infile", help="A text based input file with .txt extension", type=argparse.FileType('r'))
parser.add_argument("outfile", help="A text base output file with .txt extension",type=argparse.FileType('w'))
parser.add_argument("-i", "--insensitive", action="store_true",help="case insensitive lexicographic sort")
parser.add_argument("-nl", "--nline", type=int, help="number of lines to print in output", default=100)
parser.add_argument("-p", "--printout", type=str, help="print result on console", default="no",
                        choices=['y', 'Y', 'yes', 'YES', 'n', 'no', "N", "NO"])

args = parser.parse_args()
f=args.infile
lines=f.read()
f.close()
if args.insensitive:
    lexsort=sorted(lines,key=lambda y:y.lower())
else:
    lexsort=sorted(lines)
o=args.outfile
o.write(str(lexsort))
o.close()
if args.printout =="yes":
    print(lexsort)
# TODO: fix formatting of output and then work on -nl