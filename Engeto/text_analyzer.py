def separator():
    print("-"*35)
    pass


def user_login():
    users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

    user_name = input("Fill in a user name: ")
    password = input("Fill in a password: ")

    if user_name in users and password == users[user_name]:
        print("Welcome to the app", user_name)
    else:
        print("Login failed")
        exit()

def get_text():
    TEXTS = [
             '''Situated about 10 miles west of Kemmerer,
             Fossil Butte is a ruggedly impressive
             topographic feature that rises sharply
             some 1000 feet above Twin Creek Valley
             to an elevation of more than 7500 feet
             above sea level. The butte is located just
             north of US 30N and the Union Pacific Railroad,
             which traverse the valley. ''',
             '''At the base of Fossil Butte are the bright
             red, purple, yellow and gray beds of the Wasatch
             Formation. Eroded portions of these horizontal
             beds slope gradually upward from the valley floor
             and steepen abruptly. Overlying them and extending
             to the top of the butte are the much steeper
             buff-to-white beds of the Green River Formation,
             which are about 300 feet thick.''',
             '''The monument contains 8198 acres and protects
             a portion of the largest deposit of freshwater fish
             fossils in the world. The richest fossil fish deposits
             are found in multiple limestone layers, which lie some
             100 feet below the top of the butte. The fossils
             represent several varieties of perch, as well as
             other freshwater genera and herring similar to those
             in modern oceans. Other fish such as paddlefish,
             garpike and stingray are also present.'''
             ]

    text_number = int(input(f"Choose a text for analysis 1-{len(TEXTS)}:"))

    if text_number not in range(1, len(TEXTS) + 1):
        print("invalid input")
        exit()

    return TEXTS[text_number - 1]


def get_words(text):
    delimiters = " ,.\n"
    tmp = ""
    words = []
    for c in text:
        if c in delimiters:
            if tmp != "":
                words.append(tmp)
            tmp = ""
        else:
            tmp += c
    if tmp != "":
        words.append(tmp)
    return words


def count_words_with_first_capital(words):
    count_title = 0
    for word in words:
        if word.istitle():
            count_title += 1
    print("There are ", count_title, "words with first letter capital")

def count_words_with_all_capital(words):
    count_upper=0
    for word in words:
        if word.isupper():
            count_upper += 1
    print("There are ", count_upper, "words with all letters capital")

def count_words_with_all_lower(words):
    count_lower=0
    for word in words:
        if word.islower():
            count_lower += 1
    print("There are ", count_lower, "words with all letters lower")

def count_numbers(words):
    count_numbers=0
    for word in words:
        if word.isnumeric():
            count_numbers += 1
    print("There are ", count_numbers, "numbers")

def sum_numbers(words):
    sum_numbers=0
    for word in words:
        if word.isnumeric():
            sum_numbers += int(word)
    print("The sum of the numerical strings is ", sum_numbers)

    pass

def headline(lenghts):
    m = max(lenghts.values())
    print("LEN", "|", f"{'OCURRENCE':<{m}}", "|", "NR.")

def histogram(words):
    lenghts = {}

    for word in words:
       if len(word) in lenghts:
           lenghts[len(word)] += 1
       else:
           lenghts.update({len(word): 1})

    headline(lenghts)
    m = max(lenghts.values())
    for key in sorted(lenghts.keys()):

       print(f"{key : <3}","|",f"{'*'* lenghts[key]:<{m}}","|",lenghts[key])


# START OF THE PROGRAM
user_login()

separator()

selected_text = get_text()

separator()

words = get_words(selected_text)


count_words_with_first_capital(words)

count_words_with_all_capital(words)

count_words_with_all_lower(words)

count_numbers(words)

sum_numbers(words)

separator()


histogram(words)