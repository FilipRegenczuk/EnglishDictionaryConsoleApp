import json
from difflib import get_close_matches       # method used to check similarities between words

data = json.load(open("data.json"))         # file data.json contains English words and its meanings


# Function responsible for searching a translation of the word.
def translate(word):
    word = word.lower()

    if word in data:
       return data[word]
    elif word.title() in data:          # if user enter "poland" this will check for "Poland"
        return data[word.title()]
    elif word.upper() in data:          # if user enter "nato" this will check for "NATO"
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff = 0.75)) != 0:
        check = input("Did You mean '{}'? Enter: 'Y' if yes / 'N' if no.\n>> ".format(get_close_matches(word, data.keys())[0]))
        if check == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif check == 'N':
            return "The word does not exist."
        else:
            return "Wrong command."
    else:
        return "The word does not exist."


while True:
    word = input("Enter a word: ")

    if word == "\exit":
        break
    else:
        output = translate(word)

        if type(output) == list:
            for item in output:
                print("-", item)
        else:
            print(output)
