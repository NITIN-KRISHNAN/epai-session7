import math
import string
import random
from functools import partial
from functools import reduce

VOWELS = ['a', 'e', 'i', 'o', 'u']
PROFANE_WORDS = [
    "4r5e",
    "5h1t",
    "5hit",
    "a55",
    "anal",
    "anus",
    "ar5e",
    "arrse",
    "arse",
    "ass",
    "ass-fucker",
    "asses",
    "assfucker",
    "assfukka",
    "asshole",
    "assholes",
    "asswhole",
    "a_s_s",
    "b!tch",
    "b00bs",
    "b17ch",
    "b1tch",
    "ballbag",
    "balls",
    "ballsack",
    "bastard",
    "beastial",
    "beastiality",
    "bellend",
    "bestial",
    "bestiality",
    "bi+ch",
    "biatch",
    "bitch",
    "bitcher",
    "bitchers",
    "bitches",
    "bitchin",
    "bitching",
    "bloody",
    "blow job",
    "blowjob",
    "blowjobs",
    "boiolas",
    "bollock",
    "bollok",
    "boner",
    "boob",
    "boobs",
    "booobs",
    "boooobs",
    "booooobs",
    "booooooobs",
    "breasts",
    "buceta",
    "bugger",
    "bum",
    "bunny fucker",
    "butt",
    "butthole",
    "buttmunch",
    "buttplug",
    "c0ck",
    "c0cksucker",
    "carpet muncher",
    "cawk",
    "chink",
    "cipa",
    "cl1t",
    "clit",
    "clitoris",
    "clits",
    "cnut",
    "cock",
    "cock-sucker",
    "cockface",
    "cockhead",
    "cockmunch",
    "cockmuncher",
    "cocks",
    "cocksuck ",
    "cocksucked ",
    "cocksucker",
    "cocksucking",
    "cocksucks ",
    "cocksuka",
    "cocksukka",
    "cok",
    "cokmuncher",
    "coksucka",
    "coon",
    "cox",
    "crap",
    "cum",
    "cummer",
    "cumming",
    "cums",
    "cumshot",
    "cunilingus",
    "cunillingus",
    "cunnilingus",
    "cunt",
    "cuntlick ",
    "cuntlicker ",
    "cuntlicking ",
    "cunts",
    "cyalis",
    "cyberfuc",
    "cyberfuck ",
    "cyberfucked ",
    "cyberfucker",
    "cyberfuckers",
    "cyberfucking ",
    "d1ck",
    "damn",
    "dick",
    "dickhead",
    "dildo",
    "dildos",
    "dink",
    "dinks",
    "dirsa",
    "dlck",
    "dog-fucker",
    "doggin",
    "dogging",
    "donkeyribber",
    "doosh",
    "duche",
    "dyke",
    "ejaculate",
    "ejaculated",
    "ejaculates ",
    "ejaculating ",
    "ejaculatings",
    "ejaculation",
    "ejakulate",
    "f u c k",
    "f u c k e r",
    "f4nny",
    "fag",
    "fagging",
    "faggitt",
    "faggot",
    "faggs",
    "fagot",
    "fagots",
    "fags",
    "fanny",
    "fannyflaps",
    "fannyfucker",
    "fanyy",
    "fatass",
    "fcuk",
    "fcuker",
    "fcuking",
    "feck",
    "fecker",
    "felching",
    "fellate",
    "fellatio",
    "fingerfuck ",
    "fingerfucked ",
    "fingerfucker ",
    "fingerfuckers",
    "fingerfucking ",
    "fingerfucks ",
    "fistfuck",
    "fistfucked ",
    "fistfucker ",
    "fistfuckers ",
    "fistfucking ",
    "fistfuckings ",
    "fistfucks ",
    "flange",
    "fook",
    "fooker",
    "fuck",
    "fucka",
    "fucked",
    "fucker",
    "fuckers",
    "fuckhead",
    "fuckheads",
    "fuckin",
    "fucking",
    "fuckings",
    "fuckingshitmotherfucker",
    "fuckme ",
    "fucks",
    "fuckwhit",
    "fuckwit",
    "fudge packer",
    "fudgepacker",
    "fuk",
    "fuker",
    "fukker",
    "fukkin",
    "fuks",
    "fukwhit",
    "fukwit",
    "fux",
    "fux0r",
    "f_u_c_k",
    "gangbang",
    "gangbanged ",
    "gangbangs ",
    "gaylord",
    "gaysex",
    "goatse",
    "God",
    "god-dam",
    "god-damned",
    "goddamn",
    "goddamned",
    "hardcoresex ",
    "hell",
    "heshe",
    "hoar",
    "hoare",
    "hoer",
    "homo",
    "hore",
    "horniest",
    "horny",
    "hotsex",
    "jack-off ",
    "jackoff",
    "jap",
    "jerk-off ",
    "jism",
    "jiz ",
    "jizm ",
    "jizz",
    "kawk",
    "knob",
    "knobead",
    "knobed",
    "knobend",
    "knobhead",
    "knobjocky",
    "knobjokey",
    "kock",
    "kondum",
    "kondums",
    "kum",
    "kummer",
    "kumming",
    "kums",
    "kunilingus",
    "l3i+ch",
    "l3itch",
    "labia",
    "lmfao",
    "lust",
    "lusting",
    "m0f0",
    "m0fo",
    "m45terbate",
    "ma5terb8",
    "ma5terbate",
    "masochist",
    "master-bate",
    "masterb8",
    "masterbat*",
    "masterbat3",
    "masterbate",
    "masterbation",
    "masterbations",
    "masturbate",
    "mo-fo",
    "mof0",
    "mofo",
    "mothafuck",
    "mothafucka",
    "mothafuckas",
    "mothafuckaz",
    "mothafucked ",
    "mothafucker",
    "mothafuckers",
    "mothafuckin",
    "mothafucking ",
    "mothafuckings",
    "mothafucks",
    "mother fucker",
    "motherfuck",
    "motherfucked",
    "motherfucker",
    "motherfuckers",
    "motherfuckin",
    "motherfucking",
    "motherfuckings",
    "motherfuckka",
    "motherfucks",
    "muff",
    "mutha",
    "muthafecker",
    "muthafuckker",
    "muther",
    "mutherfucker",
    "n1gga",
    "n1gger",
    "nazi",
    "nigg3r",
    "nigg4h",
    "nigga",
    "niggah",
    "niggas",
    "niggaz",
    "nigger",
    "niggers ",
    "nob",
    "nob jokey",
    "nobhead",
    "nobjocky",
    "nobjokey",
    "numbnuts",
    "nutsack",
    "orgasim ",
    "orgasims ",
    "orgasm",
    "orgasms ",
    "p0rn",
    "pawn",
    "pecker",
    "penis",
    "penisfucker",
    "phonesex",
    "phuck",
    "phuk",
    "phuked",
    "phuking",
    "phukked",
    "phukking",
    "phuks",
    "phuq",
    "pigfucker",
    "pimpis",
    "piss",
    "pissed",
    "pisser",
    "pissers",
    "pisses ",
    "pissflaps",
    "pissin ",
    "pissing",
    "pissoff ",
    "poop",
    "porn",
    "porno",
    "pornography",
    "pornos",
    "prick",
    "pricks ",
    "pron",
    "pube",
    "pusse",
    "pussi",
    "pussies",
    "pussy",
    "pussys ",
    "rectum",
    "retard",
    "rimjaw",
    "rimming",
    "s hit",
    "s.o.b.",
    "sadist",
    "schlong",
    "screwing",
    "scroat",
    "scrote",
    "scrotum",
    "semen",
    "sex",
    "sh!+",
    "sh!t",
    "sh1t",
    "shag",
    "shagger",
    "shaggin",
    "shagging",
    "shemale",
    "shi+",
    "shit",
    "shitdick",
    "shite",
    "shited",
    "shitey",
    "shitfuck",
    "shitfull",
    "shithead",
    "shiting",
    "shitings",
    "shits",
    "shitted",
    "shitter",
    "shitters ",
    "shitting",
    "shittings",
    "shitty ",
    "skank",
    "slut",
    "sluts",
    "smegma",
    "smut",
    "snatch",
    "son-of-a-bitch",
    "spac",
    "spunk",
    "s_h_i_t",
    "t1tt1e5",
    "t1tties",
    "teets",
    "teez",
    "testical",
    "testicle",
    "tit",
    "titfuck",
    "tits",
    "titt",
    "tittie5",
    "tittiefucker",
    "titties",
    "tittyfuck",
    "tittywank",
    "titwank",
    "tosser",
    "turd",
    "tw4t",
    "twat",
    "twathead",
    "twatty",
    "twunt",
    "twunter",
    "v14gra",
    "v1gra",
    "vagina",
    "viagra",
    "vulva",
    "w00se",
    "wang",
    "wank",
    "wanker",
    "wanky",
    "whoar",
    "whore",
    "willies",
    "willy",
    "xrated",
    "xxx",
]


def check_fibonacci(num):
    """
    Check is the given number is a fibonacci number
    :param num:
    :return: true when the number is a fibonacci number else false
    """
    if num > 10000:
        raise ValueError('Input number less than or equal to 10000')
    fibonacci_series = get_fibonacci_series()
    print("check_fibonacci", num in fibonacci_series)
    return num in fibonacci_series


def get_fibonacci_series():
    """
    Function to calculate fibonacci_series upto 10000
    :return: list that contains fibonacci_series upto 10000
    """
    fibonacci_series = [0, 1]
    list(map(lambda x : fibonacci_series.append(sum(fibonacci_series[-2:])),
                    range(2, 20)))
    return fibonacci_series


def add_iterables(int1, int2):
    """
    Function that adds two iterables when element of first iterable is even and element of second iterable is odd
    :param int1: first iterable
    :param int2: second iterable
    :return: list that contains sum of iterables when first iterable's element is even and second itereable's element is odd
    """
    result = [a + b for a, b in zip(int1, int2) if a % 2 == 0 and b % 2 != 0]
    print("add_iterables", result)
    return result


def strip_vowels(x):
    """
    Function to remove all vowels from a string
    :param x: input string
    :return: string with all vowels removed
    """
    result_list = [a for a in x if a not in VOWELS]
    result_string = ""
    result_string = result_string.join(result_list)
    print("strip_vowels", x, result_string)
    return result_string


def relu(input_list):
    """
    Function to apply relu on the input list
    x if x > 0 else 0
    :param input_list:
    :return: returns 1D array relu function applied on input
    """
    output_list = [x if x > 0 else 0 for x in input_list]
    print("relu", input_list, output_list)
    return output_list


def sigmoid(input_list):
    """
    sigmoid function for a 1D array (list)
    formula for sigmoud 1 / (1 + math.exp(-x)
    :param input_list:
    :return: returns 1D array sigmoid function applied on input
    """
    output_list = [1 / (1 + math.exp(-x)) for x in input_list]
    print("sigmoid", input_list, output_list)
    return output_list


def shift_char(input_string):
    """
    shifts all characters by 5 (handle boundary conditions)
    :param input_string: input
    :return: shifted string
    """
    output_string = ""
    op_list = [chr((ord(x) - 26 + 5)) if (ord(x) + 5) > 122 else chr(ord(x) + 5) for x in input_string]
    output_string = output_string.join(op_list)
    print("shift_char", input_string, output_string)
    return output_string


def profane_filter(input_string):
    """
    Check if a given paragraph contains any Profane word using list comprehension
    :param input_string:
    :return: true if input contains profane
    """
    result = bool([x for x in input_string.split() if x in PROFANE_WORDS])
    print("profane_filter", input_string, result)
    return result


def add_even(input_list):
    """
    Function to add all the even elements of a list using reduce
    :param input_list: input list
    :return: sum of all the even elements of a list
    """
    result = reduce(lambda a, b: a+b, [x for x in input_list if x % 2 == 0])
    print("add_even", input_list, result)
    return result


def biggest_char(input_string):
    """
    Function to get the character with largest ASCII value using reduce function
    :param input_string: input string
    :return: character with largest ASCII value
    """
    result = reduce(lambda a, b: a if ord(a) > ord(b) else b, input_string)
    print("biggest_char", input_string, result)
    return result


def add_third_num(input_list):
    """
    Adds elements present in every third index of a list
    :param input_list: list of numbers
    :return: sum of every third number
    """
    result = reduce(lambda a, b: a + b, input_list[::3])
    print("add_third_num", input_list, result)
    return result


def gen_random_number_plates():
    """
    Generates list of random number plates for the "KA" and number range [1000, 9999]
    :param state: state code
    :param num_range: range of numbers to be used in number plate
    :return: list of random number plates
    """
    n = 15
    num_plates = ["KA" + str(random.randint(10, 99)) + random.choice(list(string.ascii_uppercase)) +
                random.choice(list(string.ascii_uppercase)) + str(random.randint(1000, 9999)) for _ in range(n)]
    print("gen_random_number_plates", num_plates)
    return num_plates


def gen_random_number_plates_new(state, num_range):
    """
    Generates list of random number plates for the given state and number range
    :param state: state code
    :param num_range: range of numbers to be used in number plate
    :return: list of random number plates
    """
    n = 15
    num_plates = [state + str(random.randint(10, 99)) + random.choice(list(string.ascii_uppercase)) +
                random.choice(list(string.ascii_uppercase)) + str(random.randint(num_range.start, num_range.stop))
                for _ in range(n)]
    print("gen_random_number_plates_new", num_plates)
    return num_plates


def gen_random_number_plates_partial(state):
    """
    This function generates ranfom number plates by using functools.partial as passing only the state name
    as param and hardcoding the number range
    :param state: state code (string)
    :return: list of random number plates
    """
    gen_random_number_plates_partial_fn = partial(gen_random_number_plates_new, num_range = range(1000, 9999))
    num_plates = gen_random_number_plates_partial_fn(state)
    return num_plates
