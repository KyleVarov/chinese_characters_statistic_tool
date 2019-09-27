import collections
import operator

char_dict = collections.OrderedDict()

f = open("초급+중급한자.txt", encoding="utf-8")
file = f.read()
full_file = file.rstrip('\n')

for letter in full_file:
    if letter not in char_dict and letter != '\n':
        char_dict[letter] = 0
    if letter in char_dict:
        char_dict[letter] += 1

ordered_char_dict = collections.OrderedDict(sorted(char_dict.items(), key=operator.itemgetter(1), reverse=True))

char_total = len(ordered_char_dict)

for char, value in ordered_char_dict.items():
    percentage = value/char_total*100
    print(char, value, percentage)

    #print(char)
    #print(value)
    #print(float(percentage))

print("amount of characters:", char_total)

