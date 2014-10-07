*Program Name*: lex_sort.py


The program takes 2 required __positional arguments__ 

* ```infile``` - a text based file with a ```.txt``` extension
* ```outfile``` - a text based file with a ```.txt``` extension

The program should return an informative error to the user if a ```.txt``` extension is not provided.
The program reads the contents of the text in ```infile``` and performs a _lexicographic sort_ on the contents
of that file and returns the sorted output to an ```outfile```.

Three optional arguments are provided with default values

* ```-i or --insensitive``` a flag that defaults to ```TRUE``` - a case insensitive  _lexicographic sort_
* ```-nl or --nline``` a numeric option that defaults to ```all content``` - prints only ```nline``` lines to the output
* ```-p or --printout``` a string option that defaults to ```no or n``` - prints output to console in addition to ```outfile```

Note: ```-p``` can be used as a flag by defaulting the action to ```FALSE``` in ```parse_args()```. This is just
to demonstrate the usage of a string optional argument.

Below are example executions of all the different arguments. Examples for combination usage have not been 
shown in these examples below, but checks to ensure proper usage will be placed in the program.

**Example Execution of Simple case.**

```$python lex_sort.py input.txt output.txt```

**Side Effects**

_Before Execution_

```input.txt:```

efg

A

Bcd

aa

abc


out.txt does NOT exist

_After Execution_

```input.txt:```

efg

A

Bcd

aa

abc


```out.txt:```

A

Bcd

aa

abc

efg


**Execution with case insensitive _flag_**

```$python lex_sort.py -i input.txt output.txt```

OR

```$python lex_sort.py --insensitive input.txt output.txt```


```input.txt:```

efg

A

Bcd

aa

bbc


out.txt does NOT exist

_After Execution_

```input.txt:```

efg

A

Bcd

aa

bbc


```output.txt:```

A

aa

Bcd

bbc

efg


**An _optional numeric argument_ that will print out only n lines of output - ```nline```**

```$python lex_sort.py -nl 2 input.txt output.txt```

OR

```$python lex_sort.py --nline 2 input.txt output.txt```


_Before Execution_

```input.txt:```

efg

A

Bcd

aa

abc


out.txt does NOT exist

_After Execution_

```input.txt:```

efg

A

Bcd

aa

abc


```out.txt:```

A

Bcd



**An _optional string argument_ that will print the output on the console in addition to generating an out.txt file
 - ```printout```**
 
 
```$python lex_sort.py -p input.txt output.txt```

OR

```$python lex_sort.py --printout input.txt output.txt```


_Before Execution_

```input.txt:```

efg

A

Bcd

aa

abc


out.txt does NOT exist

_After Execution_

```input.txt:```

efg

A

Bcd

aa

abc


```out.txt:```

A

aa

Bcd

bbc

efg


```console output:```

A

aa

Bcd

bbc

efg