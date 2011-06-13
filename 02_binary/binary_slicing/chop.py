from math import floor

def chop(num, array):
    return __chop(num, array, 0)

def __chop(num, array, base_index):
    if not array or len(array) == 0:
        return -1
    index = len(array) // 2
    testedNum = array[index]
    if testedNum == num:
        return base_index + index
    if num > testedNum:
        return __chop(num, array[index + 1 : len(array)], base_index + index + 1)
    if num < testedNum:
        return __chop(num, array[0: index], base_index)
