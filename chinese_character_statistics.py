
class Character:                    # Character class for making letters into an object
    def __init__(self,char):
        self.char = char
        self.freq = 0

    def get_char(self):
        return self.char

    def get_freq(self):
        return self.freq

    def increase_freq(self):
        self.freq += 1

def selection_sort(list):      # function to sort the character beggining from their highest frequency
  for border in range(0, len(list)-1):
    biggest = border
    for pointer in range(border+1, len(list)):
      if list[pointer].get_freq() > list[biggest].get_freq():
        biggest = pointer

    temp = list[border]
    list[border] = list[biggest]
    list[biggest] = temp

  return list

def calculate_total_amount(list):               #calculating total amount of characters (for percentage)
    character_total_amount = 0
    for char in list:
        character_total_amount += char.get_freq()

    return character_total_amount

############################################################################################

f = open("초급한자chinese_수정본.txt", encoding='utf8')
file = f.read()
full_file = file.rstrip("\n")

all_characters = []
all_character_objects = []



for letter in full_file:            #creating a list of all characters and character objects seperately
    if letter not in all_characters and letter != "\n" and letter is not " " and letter is not"-":
        all_characters.append(letter)
        all_character_objects.append(Character(letter))
    if letter in all_characters:
        for object in all_character_objects:
            if object.get_char() == letter:
                object.increase_freq()


sorted_list = selection_sort(all_character_objects)

total = calculate_total_amount(sorted_list)


for char in sorted_list:                                       
    percentage = char.get_freq() / len(all_characters) * 100    
    print(char.get_char() , char.get_freq() ,percentage, "%")   

    #print(char.get_char())
    #print(char.get_freq())
    #print(percentage, "%")

print(len(all_characters))

print(total)
