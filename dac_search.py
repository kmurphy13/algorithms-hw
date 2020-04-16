# Kira Murphy
# CS362 HW2

def dac_search(lst: list, key) -> bool:
    """
    Function that searches for an item in an unsorted array by splitting the array into halves
    and recursively searching for the item in each half
    :param lst: The unsorted array
    :param key: The item being searched for
    :return: True if the item is in the list, false otherwise
    """
    if len(lst) == 1:
        if lst[0] == key:
            return True
        else:
            return False
    return dac_search(lst[:len(lst)//2], key) or dac_search(lst[len(lst)//2:len(lst)], key)


if __name__ == "__main__":
    lst = [138, 0, 3, 36, 29, 13, 9, 12, 110, 1, 0, 12, 5, 0, 1, 0, 1, 1, 4, 11, 52, 12, 2, 1, 2, 4, 99]
    print(dac_search(lst,99))