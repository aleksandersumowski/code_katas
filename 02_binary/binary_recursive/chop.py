from math import floor
def chop(number, array):
    if not array or len(array) == 0 or number < array[0] or number > array[len(array) - 1]:
        return -1
    return __chop(number, array, 0, len(array))

def __chop(number, array, lower_index, upper_index):
    index = int(floor((lower_index + upper_index)/2))
    if array[index] == number:
        return index
    if lower_index == upper_index:
        return -1
    if array[index] > number:
        return __chop(number, array, lower_index, index - 1)
    return __chop(number, array, index + 1, upper_index)
