import session7
import os
import re
import inspect

MANDATORY_FUNCTIONS = [
    'gen_random_number_plates_partial',
    'gen_random_number_plates',
    'add_third_num',
    'biggest_char',
    'add_even',
    'profane_filter',
    'shift_char',
    'sigmoid',
    'strip_vowels',
    'add_iterables',
    'check_fibonacci',
    ]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 300 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in MANDATORY_FUNCTIONS:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_mandatory_fuctions_availability():
    MANDATORY_FUNCTIONS_AVAILABILITY = True
    f = open("session7.py", "r")
    content = f.read()
    f.close()
    for c in MANDATORY_FUNCTIONS:
        if c not in content:
            MANDATORY_FUNCTIONS_AVAILABILITY = False
            pass
    assert MANDATORY_FUNCTIONS_AVAILABILITY == True, "You have not implemented all the functions"

def test_add_third_num():
    assert session7.add_third_num([1,2,3,4,5,6,7]) == 12

def test_gen_random_number_plates_partial():
    res = session7.gen_random_number_plates_partial('DL')
    test_res = all(x for x in res if 'DL' in x)
    assert test_res == True

def test_gen_random_number_plates():
    res = session7.gen_random_number_plates()
    test_res = all(x for x in res if 'KA' in x) and len(res) == 15
    assert test_res == True

def test_biggest_char():
    assert session7.biggest_char("abcd}123") == "}" and session7.biggest_char("ABCabc") == "c"

def test_add_even():
    assert session7.add_even([1,2,3,4]) == 6

def test_shift_char():
    assert session7.shift_char('tsai') == 'yxfn'

def test_remove_vowels():
    assert session7.strip_vowels("nitin") == "ntn"

def test_relu():
    assert session7.relu([0,1,2,3,-1,-2,-3]) == [0,1,2,3,0,0,0]

def test_sigmoid():
    assert session7.sigmoid([0,100]) == [0.5,1]

def test_iterables_add():
    assert session7.add_iterables([1,2,4,6], [2,3,5,3]) == [5, 9, 9]

def test_check_fibonacci():
    assert session7.check_fibonacci(144) == True and session7.check_fibonacci(145) == False

def test_profanity():
    assert session7.profane_filter(
        '''Python is meant to be an easily readable language. Its formatting is visually uncluttered, and it often uses English keywords where other languages use punctuation. Unlike many other languages, it does not use curly brackets to delimit blocks, and semicolons after statements are optional. It has fewer syntactic exceptions and special cases than C or Pascal.[65]
        Indentation
        Main article: Python syntax and semantics § Indentation
        Python uses whitespace indentation, rather than curly brackets or keywords, to delimit blocks. An increase in indentation comes after certain statements; a decrease in indentation signifies the end of the current block.[66] Thus, the program's visual structure accurately represents the program's semantic structure.[1] This feature is sometimes termed the off-side rule, which some other languages share, but in most languages indentation doesn't have any semantic meaning.
        
        Statements and control flow
        Python's statements include (among others):
        
        The assignment statement (token '=', the equals sign). This operates differently than in traditional imperative programming languages, and this fundamental mechanism (including the nature of Python's version of variables) illuminates many other features of the language. Assignment in C, e.g., x = 2, translates to "typed variable name x receives a copy of numeric value 2". The (right-hand) value is copied into an allocated storage location for which the (left-hand) variable name is the symbolic address. The memory allocated to the variable is large enough (potentially quite large) for the declared type. In the simplest case of Python assignment, using the same example, x = 2, translates to "(generic) name x receives a reference to a separate, dynamically allocated object of numeric (int) type of value 2." This is termed binding the name to the object. Since the name's storage location doesn't contain the indicated value, it is improper to call it a variable. Names may be subsequently rebound at any time to objects of greatly varying types, including strings, procedures, complex objects with data and methods, etc. Successive assignments of a common value to multiple names, e.g., x = 2; y = 2; z = 2 result in allocating storage to (at most) three names and one numeric object, to which all three names are bound. Since a name is a generic reference holder it is unreasonable to associate a fixed data type with it. However at a given time a name will be bound to some object, which will have a type; thus there is dynamic typing.
        The if statement, which conditionally executes a block of code, along with else and elif (a contraction of else-if).
        The for statement, which iterates over an iterable object, capturing each element to a local variable for use by the attached block.
        The while statement, which executes a block of code as long as its condition is true.
        The try statement, which allows exceptions raised in its attached code block to be caught and handled by except clauses; it also ensures that clean-up code in a finally block will always be run regardless of how the block exits.
        The raise statement, used to raise a specified exception or re-raise a caught exception.
        The class statement, which executes a block of code and attaches its local namespace to a class, for use in object-oriented programming.
        The def statement, which defines a function or method.
        The with statement, from Python 2.5 released in September 2006,[67] which encloses a code block within a context manager (for example, acquiring a lock before the block of code is run and releasing the lock afterwards, or opening a file and then closing it), allowing Resource Acquisition Is Initialization (RAII)-like behavior and replaces a common try/finally idiom.[68]
        The break statement, exits from the loop.
        The continue statement, skips this iteration and continues with the next item.
        The pass statement, which serves as a NOP. It is syntactically needed to create an empty code block.
        The assert statement, used during debugging to check for conditions that ought to apply.
        The yield statement, which returns a value from a generator function. From Python 2.5, yield is also an operator. This form is used to implement coroutines.
        The import statement, which is used to import modules whose functions or variables can be used in the current program. There are three ways of using import: import <module name> [as <alias>] or from <module name> import * or from <module name> import <definition 1> [as <alias 1>], <definition 2> [as <alias 2>], ....
        The print statement was changed to the print() function in Python 3.
        Python does not support tail call optimization or first-class continuations, and, according to Guido van Rossum, it never will.[69][70] However, better support for coroutine-like functionality is provided in 2.5, by extending Python's generators.[71] Before 2.5, generators were lazy iterators; information was passed unidirectionally out of the generator. From Python 2.5, it is possible to pass information back into a generator function, and from Python 3.3, the information can be passed through multiple stack levels.[72]
    ''') == False and session7.profane_filter(''' 5h1t
        Python is meant to be an easily readable language. Its formatting is visually uncluttered, and it often uses English keywords where other languages use punctuation. Unlike many other languages, it does not use curly brackets to delimit blocks, and semicolons after statements are optional. It has fewer syntactic exceptions and special cases than C or Pascal.[65]

        Indentation
        Main article: Python syntax and semantics § Indentation
        Python uses whitespace indentation, rather than curly brackets or keywords, to delimit blocks. An increase in indentation comes after certain statements; a decrease in indentation signifies the end of the current block.[66] Thus, the program's visual structure accurately represents the program's semantic structure.[1] This feature is sometimes termed the off-side rule, which some other languages share, but in most languages indentation doesn't have any semantic meaning.

        Statements and control flow
        Python's statements include (among others):

        The assignment statement (token '=', the equals sign). This operates differently than in traditional imperative programming languages, and this fundamental mechanism (including the nature of Python's version of variables) illuminates many other features of the language. Assignment in C, e.g., x = 2, translates to "typed variable name x receives a copy of numeric value 2". The (right-hand) value is copied into an allocated storage location for which the (left-hand) variable name is the symbolic address. The memory allocated to the variable is large enough (potentially quite large) for the declared type. In the simplest case of Python assignment, using the same example, x = 2, translates to "(generic) name x receives a reference to a separate, dynamically allocated object of numeric (int) type of value 2." This is termed binding the name to the object. Since the name's storage location doesn't contain the indicated value, it is improper to call it a variable. Names may be subsequently rebound at any time to objects of greatly varying types, including strings, procedures, complex objects with data and methods, etc. Successive assignments of a common value to multiple names, e.g., x = 2; y = 2; z = 2 result in allocating storage to (at most) three names and one numeric object, to which all three names are bound. Since a name is a generic reference holder it is unreasonable to associate a fixed data type with it. However at a given time a name will be bound to some object, which will have a type; thus there is dynamic typing.
        The if statement, which conditionally executes a block of code, along with else and elif (a contraction of else-if).
        The for statement, which iterates over an iterable object, capturing each element to a local variable for use by the attached block.
        The while statement, which executes a block of code as long as its condition is true.
        The try statement, which allows exceptions raised in its attached code block to be caught and handled by except clauses; it also ensures that clean-up code in a finally block will always be run regardless of how the block exits.
        The raise statement, used to raise a specified exception or re-raise a caught exception.
        The class statement, which executes a block of code and attaches its local namespace to a class, for use in object-oriented programming.
        The def statement, which defines a function or method.
        The with statement, from Python 2.5 released in September 2006,[67] which encloses a code block within a context manager (for example, acquiring a lock before the block of code is run and releasing the lock afterwards, or opening a file and then closing it), allowing Resource Acquisition Is Initialization (RAII)-like behavior and replaces a common try/finally idiom.[68]
        The break statement, exits from the loop.
        The continue statement, skips this iteration and continues with the next item.
        The pass statement, which serves as a NOP. It is syntactically needed to create an empty code block.
        The assert statement, used during debugging to check for conditions that ought to apply.
        The yield statement, which returns a value from a generator function. From Python 2.5, yield is also an operator. This form is used to implement coroutines.
        The import statement, which is used to import modules whose functions or variables can be used in the current program. There are three ways of using import: import <module name> [as <alias>] or from <module name> import * or from <module name> import <definition 1> [as <alias 1>], <definition 2> [as <alias 2>], ....
        The print statement was changed to the print() function in Python 3.
        Python does not support tail call optimization or first-class continuations, and, according to Guido van Rossum, it never will.[69][70] However, better support for coroutine-like functionality is provided in 2.5, by extending Python's generators.[71] Before 2.5, generators were lazy iterators; information was passed unidirectionally out of the generator. From Python 2.5, it is possible to pass information back into a generator function, and from Python 3.3, the information can be passed through multiple stack levels.[72]
    ''')