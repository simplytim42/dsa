def insertion_sort(array: list):
    for i in range(len(array)):
        lowest_index = i

        for j in range(i, len(array)):
            if array[j] < array[lowest_index]:
                lowest_index = j

        if lowest_index != i:
            array[i], array[lowest_index] = array[lowest_index], array[i]
    return array


if __name__ == "__main__":
    assert insertion_sort([3, 2, 1]) == [1, 2, 3]
    assert insertion_sort([1]) == [1]
    assert insertion_sort([]) == []
    arr = [9999, 576, 3, 788, 103, 56, 12]
    assert insertion_sort(arr) == [3, 12, 56, 103, 576, 788, 9999]
