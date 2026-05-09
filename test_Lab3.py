import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_too_many():
    result = []
    input_arr = [67, 67, 67, 67, 6, 7, 76, 77, 61, 62, 21]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 1)

def test_no_input():
    result = []
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 0)

def test_not_num():
    result = []
    input_arr = [67, 6.7, 67, 67, 6, 7, 76, 77]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 2)