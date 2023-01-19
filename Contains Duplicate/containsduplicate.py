import random as rand

def main():

    #We declare the array

    givenarray = []

    # We introduce random numbers in the range of (1,10) to our array, before the array's length reaches 5

    while len(givenarray) < 5:
        givenarray.append(rand.randint(1,10))

    # We convert the array to a hashset, this is going to just keep the numbers without duplicates.
    # And if the length of the hashset of array is different from the original array, we have duplicates on our original array.
    # Explanation:
    
    # Let's imagine we have this array = [5,6,6,7,8]
    # The function set is going to convert our original array into this one: [5,6,7,8]

    # That's why we compare lengths, so, as we can see, they are going to be always different if
    # the original array has a duplicate number in it.

    if len(set(givenarray)) != len(givenarray): 
        
        return True

    else:

        return False

if __name__ == "__main__":
    main()