# READ
def read(array, index):
    # O(1)
    return array[index]


# LINEAR SEARCH
def search(array, value):
    # O(n)
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


# INSERT
def insert(array, item, index):
    # O(n)
    array = array[:] + [None]
    # move elements to the right by one to make room for new item
    for i in range(len(array) - 1, index, -1):
        array[i] = array[i - 1]
    array[index] = item
    return array


def pythonic_insert(array, item, index):
    # O(n)
    return array[:index] + [item] + array[index:]


# DELETE
def delete(array, index):
    # O(n)
    array = array[:]  # added for speed checks to prevent mutability errors
    for i in range(index, len(array) - 1):
        array[i] = array[i + 1]
    del array[len(array) - 1]
    return array


def pythonic_delete(array, index):
    # O(n)
    return array[:index] + array[index + 1 :]


if __name__ == "__main__":
    # Tests
    array = ["red", "green", "blue"]
    assert read(array, 1) == "green"
    assert search(array, "blue") == 2
    assert search(array, "does not exist") == -1
    assert insert(array, "orange", 1) == ["red", "orange", "green", "blue"]
    assert pythonic_insert(array, "orange", 1) == ["red", "orange", "green", "blue"]
    assert delete(array, 1) == ["red", "blue"]
    assert pythonic_delete(array, 1) == ["red", "blue"]

    # Speed Comaprisons
    import timeit

    print("insert: ", timeit.timeit(lambda: insert(array, "orange", 1), number=100000))
    print(
        "pythonic_insert: ",
        timeit.timeit(lambda: pythonic_insert(array, "orange", 1), number=100000),
    )
    print("delete: ", timeit.timeit(lambda: delete(array, 1), number=100000))
    print(
        "pythonic_delete: ",
        timeit.timeit(lambda: pythonic_delete(array, 1), number=100000),
    )
