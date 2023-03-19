# Merge Sort
# Time Complexity: O(n log n)
# * Feel print to uncomment the commented print statements to help understand the execution process

def merge(left, right):
    # print(f"merge with [L]: {left}\t[R]: {right}")    # debugging print
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if (left[i] <= right[j]):  # if left-list element is lesser than right-list element
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # at this point, there might still be elements that haven't been merged yet
    # these will insert the rest into the result
    result += left[i:]
    result += right[j:]

    return result


def merge_sort(list):
    if len(list) <= 1:
        # print(f"{list} done splitting")   # debugging print
        return list

    # can use this to ensure the splitting of the arrays is done correctly
    # print(list) # debugging print
    mid = len(list) // 2
    left = merge_sort(list[0:mid])
    right = merge_sort(list[mid:len(list)])
    return merge(left, right)


def main():
    # output: [3, 9, 10, 27, 38, 43, 82]    input taken from GeeksForGeeks: https://www.geeksforgeeks.org/merge-sort/
    unsorted = [38, 27, 43, 3, 9, 82, 10]
    # unsorted = [5, 2, 8, 1, 9, 3]   # output: [1, 2, 3, 5, 8, 9]
    # unsorted = [1, 2, 3, 4, 5, 6]   # output: [1, 2, 3, 4, 5, 6]
    # unsorted = [6, 5, 4, 3, 2, 1]   # output: [1, 2, 3, 4, 5, 6]

    print(f"Input: {unsorted}")

    sorted = merge_sort(unsorted)

    print(f"Output: {sorted}")


main()
