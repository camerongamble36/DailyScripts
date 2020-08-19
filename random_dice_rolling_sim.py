import random

print('---------------------------------------')
print('---------RANDOM DICE ROLLING-----------')
print('---------------------------------------')


def roll_dice(decision):

    if decision == 'Y':
        return roll()
    elif decision == 'N':
        pass
    else:
        print('Sorry I didn\'t understand that answer')


def roll():
    # 3 rolls
    for i in range(0, 3):
        result = random.randint(0, 12)
        print("Roll "+str(i+1)+": "+str(result))
    return result


if __name__ == '__main__':
    decision = input('\n\nDo you want to roll the dice? (Y/N) ')
    final_dice_roll = roll_dice(decision)
    print("\nYour final dice roll is: " + str(final_dice_roll))
