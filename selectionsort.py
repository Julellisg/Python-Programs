# Selection Sort
# Time Complexity: O(n^2)

import sys

def selection_sort(list):
    # loop through each index in the list
    for i in range(0, len(list)):
        smallest_num = i

        # loop through each item ignoring the the indexes in 'i' that have been selected already
        for j in range(i, len(list)):
            if  list[smallest_num] > list[j]:   # if a new smallest number has been found
                smallest_num = j                # save the index of the smallest found number

        # perform swap
        temp = list[i]
        list[i] = list[smallest_num]
        list[smallest_num] = temp

    return list

def main():
    unsorted = [5, 2, 8, 1, 9, 3]   # output: [1, 2, 3, 5, 8, 9]
    # unsorted = [1, 2, 3, 4, 5, 6]   # output: [1, 2, 3, 4, 5, 6]
    # unsorted = [6, 5, 4, 3, 2, 1]   # output: [1, 2, 3, 4, 5, 6]

    print(f"Input: {unsorted}")

    sorted = selection_sort(unsorted)

    print(f"Output: {sorted}")

main()