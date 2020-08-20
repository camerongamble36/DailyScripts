import random


def set_array():

    array = [None] * 100
    for index, item in enumerate(array):
        if item == None:
            array[index] = random.randint(0, 100)

    return array


def binary_search_for_ice_cream(array, left, right, x):

    # Check base case
    if right >= left:

        mid = left + (right - left) // 2

        # If element is present at the middle itself
        if array[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif array[mid] > x:
            return binary_search_for_ice_cream(array, left, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binary_search_for_ice_cream(array, mid + 1, right, x)

    else:
        # Element is not present in the array
        return -1


if __name__ == "__main__":
    random_number_line = set_array()
    # Random number line is sorted for binary search
    random_number_line.sort()
    # Amount of licks is randomly set
    ice_cream_sweet_spot = random.randint(0, 100)
    guess = int(input('What\'s your guess? (0 - 100 Licks) '))

    print("Guess: " + str(guess))
    print('Sweet Spot: ' + str(ice_cream_sweet_spot))
    print("Random Number Array: " + str(random_number_line))
    result = binary_search_for_ice_cream(
        random_number_line, 0, len(random_number_line) - 1, ice_cream_sweet_spot)
    if result != -1:
        print("The Ice Cream is present at index "+str(result))
    else:
        print("The Ice Cream is not present in array")
# Use Binary search for guessing methods
