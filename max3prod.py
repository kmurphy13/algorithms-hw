# Kira Murphy
# Algorithm HW1

def max3prod(lst : list) -> float:
    """
    Given a list of floating point numbers, return the maximum product that can be computed
    from any three of the numbers.
    :param lst: The list of floats
    :return: The maximum product of three elements in the list
    """
    # Sort the list
    new_list = sorted(lst)
    # Get the length of the list
    list_length = len(new_list)

    # Once the list is sorted, there are two possibilities. The largest product
    # will either be the product of the highest three numbers or of the lowest
    # two numbers and the highest number (to ensure a positive answer).
    first_possibility = new_list[0]*new_list[1]*new_list[list_length-1]
    second_possibility = new_list[list_length-1]*new_list[list_length-2]*new_list[list_length-3]

    # Return whichever is larger
    if first_possibility > second_possibility:
        return first_possibility
    return second_possibility

if __name__ == "__main__":
    print(max3prod([-10.3, -12.8, 5.1, -6.02]))