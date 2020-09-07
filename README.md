# epai-session7
##Help on module session7:

###NAME - session7

###FUNCTIONS
        
    add_even(input_list)
        Function to add all the even elements of a list using reduce
        :param input_list: input list
        :return: sum of all the even elements of a list

    add_iterables(int1, int2)
        Function that adds two iterables when element of first iterable is even and element of second iterable is odd
        :param int1: first iterable
        :param int2: second iterable
        :return: list that contains sum of iterables when first iterable's element is even and second itereable's element is odd
    
    add_third_num(input_list)
        Adds elements present in every third index of a list
        :param input_list: list of numbers
        :return: sum of every third number
    
    biggest_char(input_string)
        Function to get the character with largest ASCII value using reduce function
        :param input_string: input string
        :return: character with largest ASCII value
    
    check_fibonacci(num)
        Check is the given number is a fibonacci number
        :param num:
        :return: true when the number is a fibonacci number else false
    
    gen_random_number_plates()
        Generates list of random number plates for the "KA" and number range [1000, 9999]
        :param state: state code
        :param num_range: range of numbers to be used in number plate
        :return: list of random number plates
    
    gen_random_number_plates_new(state, num_range)
        Generates list of random number plates for the given state and number range
        :param state: state code
        :param num_range: range of numbers to be used in number plate
        :return: list of random number plates
    
    gen_random_number_plates_partial(state)
        This function generates ranfom number plates by using functools.partial as passing only the state name
        as param and hardcoding the number range
        :param state: state code (string)
        :return: list of random number plates
    
    get_fibonacci_series()
        Function to calculate fibonacci_series upto 10000
        :return: list that contains fibonacci_series upto 10000
    
    profane_filter(input_string)
            Check if a given paragraph contains any Profane word using list comprehension
        :param input_string:
        :return: true if input contains profane
    
    reduce(...)
        reduce(function, sequence[, initial]) -> value
        
        Apply a function of two arguments cumulatively to the items of a sequence,
        from left to right, so as to reduce the sequence to a single value.
        For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
        ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
        of the sequence in the calculation, and serves as a default when the
        sequence is empty.
    
    relu(input_list)
        Function to apply relu on the input list
        x if x > 0 else 0
        :param input_list:
        :return: returns 1D array relu function applied on input
    
    shift_char(input_string)
        shifts all characters by 5 (handle boundary conditions)
        :param input_string: input
        :return: shifted string
    
    sigmoid(input_list)
        sigmoid function for a 1D array (list)
        formula for sigmoud 1 / (1 + math.exp(-x)
        :param input_list:
        :return: returns 1D array sigmoid function applied on input
    
    strip_vowels(x)
        Function to remove all vowels from a string
        :param x: input string
        :return: string with all vowels removed

DATA
    PROFANE_WORDS = ['4r5e', '5h1t', '5hit', 'a55', 'anal', 'anus', 'ar5e'...
    VOWELS = ['a', 'e', 'i', 'o', 'u']

## Test cases

(base) 192:epai-session7 Krish$ pytest -v
================================================================================ test session starts ================================================================================
platform darwin -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/Krish/opt/anaconda3/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/Users/Krish/Downloads/epai/epai-session7/.hypothesis/examples')
rootdir: /Users/Krish/Downloads/epai/epai-session7
plugins: hypothesis-5.5.4, arraydiff-0.3, remotedata-0.3.2, openfiles-0.4.0, doctestplus-0.5.0, astropy-header-0.1.2
collected 19 items                                                                                                                                                                  

test_session7.py::test_readme_exists PASSED                                                                                                                                   [  5%]
test_session7.py::test_readme_contents PASSED                                                                                                                                 [ 10%]
test_session7.py::test_readme_proper_description PASSED                                                                                                                       [ 15%]
test_session7.py::test_readme_file_for_formatting PASSED                                                                                                                      [ 21%]
test_session7.py::test_indentations PASSED                                                                                                                                    [ 26%]
test_session7.py::test_function_name_had_cap_letter PASSED                                                                                                                    [ 31%]
test_session7.py::test_mandatory_fuctions_availability PASSED                                                                                                                 [ 36%]
test_session7.py::test_add_third_num PASSED                                                                                                                                   [ 42%]
test_session7.py::test_gen_random_number_plates_partial PASSED                                                                                                                [ 47%]
test_session7.py::test_gen_random_number_plates PASSED                                                                                                                        [ 52%]
test_session7.py::test_biggest_char PASSED                                                                                                                                    [ 57%]
test_session7.py::test_add_even PASSED                                                                                                                                        [ 63%]
test_session7.py::test_shift_char PASSED                                                                                                                                      [ 68%]
test_session7.py::test_remove_vowels PASSED                                                                                                                                   [ 73%]
test_session7.py::test_relu PASSED                                                                                                                                            [ 78%]
test_session7.py::test_sigmoid PASSED                                                                                                                                         [ 84%]
test_session7.py::test_iterables_add PASSED                                                                                                                                   [ 89%]
test_session7.py::test_check_fibonacci PASSED                                                                                                                                 [ 94%]
test_session7.py::test_profanity PASSED                                                                                                                                       [100%]

================================================================================ 19 passed in 0.10s =================================================================================
