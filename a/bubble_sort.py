def bubble_sort(array: list):
    unsorted_until_index = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
        unsorted_until_index -= 1
    return array


if __name__ == "__main__":
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([1]) == [1]
    assert bubble_sort([]) == []
    arr = [9999, 576, 3, 788, 103, 56, 12]
    assert bubble_sort(arr) == [3, 12, 56, 103, 576, 788, 9999]
