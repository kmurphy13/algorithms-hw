# Kira Murphy
# Algorithm HW1

def irpr(lst :list) -> int:
    """
    Given a list of integers, return the IRPR index
    :param lst: A list of integers representing news mentions for a fire department incident
    :return: The incident response public relations index
    """
    # Sort the list
    new_list = sorted(lst)
    # Go through the sorted list backwards
    for i in new_list[::-1]:
        occurrences = 0
        # Go through the list forwards and check if there are
        # occurrences greater than equal to i and if so, this is the IRPR
        for j in new_list[::]:
            if j >= i:
                occurrences = occurrences + 1
        if occurrences >= i:
            return i

if __name__ == "__main__":
    print(irpr([1, 4, 1, 4, 2, 1, 3, 5, 6]))
    print(irpr([138, 0, 3, 36, 29, 13, 9, 12, 110, 1, 0, 12, 5, 0, 1, 0, 1, 1, 4, 11, 52, 12, 2, 1, 2, 4, 99, 4]))
