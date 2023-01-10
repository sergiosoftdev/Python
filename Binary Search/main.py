import random as rand

def main():

    arr = []

    while len(arr) < 100:

        arr.append(rand.randint(1,100))

    arr.sort()
    target = int(input("Choose the target: "))

    l = 0
    r = len(arr) - 1

    if target in arr:
        while l <= r:

            mid = int((l+r) / 2)

            if target == arr[mid]:
                return mid

            if target < arr[mid]:
                r = mid
            if target > arr[mid]:
                l = mid - 1

    else:

        return  "Not in array"

main()
