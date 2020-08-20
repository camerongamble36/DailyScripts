# Input data and produces the same story, like a mad lib story
# from StoryCharacters import character
# Use Object oriented Programming
import datetime


class Character:

    def __init__(self, name, birthday, favoriteSubject, favoriteFoodDish, favoriteTVShow, shoe_color):
        self.name = name
        self.birthday = birthday
        self.favoriteSubject = favoriteSubject
        self.favoriteFoodDish = favoriteFoodDish
        self.favoriteTVShow = favoriteTVShow
        self.shoe_color = shoe_color

    # def currentAge(self):
    #     self.birthday


def generate_story(character_list):
    print('Generating Story...')
    pass


def set_character(index):
    print("For character " + str(index))
    name = input('What\'s your name? ')
    bday = input('When\'s your birthday? (mm/dd/yyyy) ')
    favoriteSubject = input('Favorite subject? ')
    favoriteFoodDish = input('Favorite Food Dish? ')
    favoriteTVShow = input('Favorite TV Show? ')
    currentShoeColor = input("Current Shoe Color? ")

    return Character(name, bday, favoriteSubject, favoriteFoodDish, favoriteTVShow, currentShoeColor)


if __name__ == "__main__":

    num_characters = int(input('How many characters? (1-4)'))
    print("You picked " + str(num_characters) + " characters\n\n")
    character_list = []

    for i in range(1, num_characters):
        character_list.append(set_character(i))

    generate_story(character_list)
