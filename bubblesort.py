# Bubble Sort
# Time Complexity: O(n^2)

def bubble_sort(list):

    swapped = True

    while swapped:  # keep looping until there is no swap performed
        swapped = False

        # if we need to compare 2 indexes, we loop through each element starting at index 1 so we can do (i-1) and (i)
        for i in range(1, len(list)):
            if list[i-1] > list[i]:  # check if they are adjacent
                # perform the swap
                temp = list[i-1]
                list[i-1] = list[i]
                list[i] = temp
                swapped = True
    return list


def main():
    unsorted = [5, 2, 8, 1, 9, 3]   # output: [1, 2, 3, 5, 8, 9]
    # unsorted = [1, 2, 3, 4, 5, 6]   # output: [1, 2, 3, 4, 5, 6]
    # unsorted = [6, 5, 4, 3, 2, 1]   # output: [1, 2, 3, 4, 5, 6]

    print(f"Input: {unsorted}")

    sorted = bubble_sort(unsorted)

    print(f"Output: {sorted}")


main()
