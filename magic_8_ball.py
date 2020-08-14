import random
print("-----------------------------------------------------")
print("------------------- Magic 8 Ball --------------------")
print('-----------------------------------------------------\n')

magicAnswer = 0
rerolls = 3


def shake():
    magicAnswer = random.randint(0, 12)
    rerolls - 1
    print(magicAnswer)


print("RULES:\n1. Only 3 rerolls\n2. Concentrate\n3. Take what you get\n\n")
decision = input('Do you want to roll today? ')

if decision == 'Y':
    print('Here we go')
    print(magicAnswer)
elif decision == 'N':
    magicAnswer = None
    print('Ok, maybe tomorrow')
else:
    print('Sorry I did not understand that option')


if magicAnswer == 0:
    print('You\'re not too lucky today')
elif magicAnswer == 1:
    print('Yes')
elif magicAnswer == 2:
    print('Feeling Lucky, I\'d say do it ;)')
elif magicAnswer == 3:
    print('Don\'t do it!!!')
elif magicAnswer == 4:
    print('Maybe reroll')
elif magicAnswer == 5:
    print('Try it out tomorrow')
elif magicAnswer == 6:
    print('Today is the day')
elif magicAnswer == 7:
    print('My Sources say no')
elif magicAnswer == 8:
    print('Outlook looking hazy, maybe reroll')
elif magicAnswer == 9:
    print('concentrate then ask again')
elif magicAnswer == 12:
    print('No')
else:
    print('Sorry something went wrong')
