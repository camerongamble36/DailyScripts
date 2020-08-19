import random
print('-------------------------------------')
print('---------RANDOM BABY NAMES-----------')
print('-------------------------------------')


def set_word_skeleton(word_skeleton, num):
    for _ in range(num):
        word_skeleton.append(None)
    print(word_skeleton)
    return word_skeleton


def set_word_index(word_index, num):
    for i in range(num):
        word_index[i] = random.randint(0, 25)
    print(word_index)
    return word_index


def word_converter(word_skeleton):
    valid = True
    if (len(word_skeleton) >= 0 and len(word_skeleton) <= 3) and word_skeleton[1] not in ['a', 'e', 'i', 'o', 'u']:
        print('Not a real name, must have at least a vowel in the middle')
        valid = False
    else:
        for index, item in enumerate(word_skeleton):
            if item == 0:
                word_skeleton[index] = 'a'
            if item == 1:
                word_skeleton[index] = 'b'
            if item == 2:
                word_skeleton[index] = 'c'
            if item == 3:
                word_skeleton[index] = 'd'
            if item == 4:
                word_skeleton[index] = 'e'
            if item == 5:
                word_skeleton[index] = 'f'
            if item == 6:
                word_skeleton[index] = 'g'
            if item == 7:
                word_skeleton[index] = 'h'
            if item == 8:
                word_skeleton[index] = 'i'
            if item == 9:
                word_skeleton[index] = 'j'
            if item == 10:
                word_skeleton[index] = 'k'
            if item == 11:
                word_skeleton[index] = 'l'
            if item == 12:
                word_skeleton[index] = 'm'
            if item == 13:
                word_skeleton[index] = 'n'
            if item == 14:
                word_skeleton[index] = 'o'
            if item == 15:
                word_skeleton[index] = 'p'
            if item == 16:
                word_skeleton[index] = 'q'
            if item == 17:
                word_skeleton[index] = 'r'
            if item == 18:
                word_skeleton[index] = 's'
            if item == 19:
                word_skeleton[index] = 't'
            if item == 20:
                word_skeleton[index] = 'u'
            if item == 21:
                word_skeleton[index] = 'v'
            if item == 22:
                word_skeleton[index] = 'w'
            if item == 23:
                word_skeleton[index] = 'x'
            if item == 24:
                word_skeleton[index] = 'y'
            if item == 25:
                word_skeleton[index] = 'z'

        return word_skeleton, valid


def baby_name_str(word_array):

    baby_name = ''
    for i in word_array:
        baby_name += str(i)

    return baby_name


# Main function
if __name__ == "__main__":
    word_skeleton = []
    # Baby name made up of 3 - 9 characters at random
    num = random.randint(2, 9)
    skeleton1 = set_word_skeleton(word_skeleton, num)
    word_index_skeleton = set_word_index(skeleton1, num)
    babyName, validity = word_converter(word_index_skeleton)

    if validity:
        print(baby_name_str(babyName))
    else:
        print('Sorry the baby name was not valid')
