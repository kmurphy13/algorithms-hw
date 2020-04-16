def lchp(lst :list) -> int:
    """
    Given a list of integers, returns the largest contiguous household population using
    divide and conquer
    :param lst: A list of household numbers
    :return: The largest contiguous household population
    """
    if len(lst)==1:
        return lst[0]

    # Calculate the midpoint of the list
    midpoint = len(lst)//2

    # Split the list into two lists
    l1 = lst[:midpoint]
    l2 = lst[midpoint:]

    # Find the largest sum on the left but going 'backwards'
    left_sum = 0
    left_current = 0
    for i in range(midpoint,-1,-1):
        left_current += lst[i]
        if left_current > left_sum:
            left_sum = left_current

    # Find the largest sum on the right
    right_current = 0
    right_sum =  0
    for i in range(midpoint+1, len(lst)):
        right_current += lst[i]
        if right_current > right_sum:
            right_sum = right_current

    # Add the largest sum on the left to the largest sum on the right
    total_sum = left_sum + right_sum

    # Return the maximum of the crossing point sum, the lchp for the left side of the list, and the lcp for the
    # right side of the list
    return max(lchp(l1),lchp(l2),total_sum)

if __name__ == "__main__":
    print(lchp([2, 3, -1]))
    print(lchp([1, -2, 7, 5, 6, -5, 5, 8, 1, -6]))
    print(lchp([-1, -2, -7, -5, -6, -5, -5, -8, -1, -6]))
    print(lchp([-2, 4, -1, 2, 1]))
    print(lchp([-1, 12, 3, -2, 5, 1, 1, -90]))
