# Insertion Sort
# Time Complexity: O(n^2)

def insertion_sort(list):
    
    # loop through each element except the very first one
    for i in range(1, len(list)):
        j = i;
        
        while j > 0 and list[j-1] > list[j]:    # catches if left element > right element
            # perform swap
            temp = list[j-1]
            list[j-1] = list[j]
            list[j] = temp
            
            j -= 1

    return list


def main():
    unsorted = [5, 2, 8, 1, 9, 3]   # output: [1, 2, 3, 5, 8, 9]
    # unsorted = [1, 2, 3, 4, 5, 6]   # output: [1, 2, 3, 4, 5, 6]
    # unsorted = [6, 5, 4, 3, 2, 1]   # output: [1, 2, 3, 4, 5, 6]

    print(f"Input: {unsorted}")

    sorted = insertion_sort(unsorted)

    print(f"Output: {sorted}")


main()
