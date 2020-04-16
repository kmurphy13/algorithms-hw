# Kira Murphy
# CS362 HW

from typing import List, Tuple


def pebble(n) -> Tuple[int, List]:
    """
    Returns the number of ways that the pebble can move all the way to the end of a
    board of length n given step stizes of 1 and 2
    :param n: board length
    :return: number of ways the pebble can move and a list of these moves
    """

    # Helper function to get the list of ways
    def pebble_helper(n)-> List:
        # First base case, the only way to move on 1 tile is in one move
        if n == 1:
            return ['1']
        # Second base case, the two ways to move on 2 tiles
        elif n == 2:
            return ['11','2']
        else:
            # Create a new list of ways
            ways = []
            # We can reach n through every path in n-1 plus one step
            for way in pebble_helper(n-1):
                ways.append(way + "1")
            # We can also reach n through every path in n-2 plus two steps
            for way in pebble_helper(n-2):
                ways.append(way + "2")

            return ways

    paths = pebble_helper(n)
    # Return the number of paths and a list of the paths
    return len(paths), paths

# The runtime of this function is O(2^n) because each time, we are making two recursive calls.

def pebble_dp(n):
    """

    :param n: board length
    :return: number of ways the pebble can move
    """
    # Make a list of length n and initialize it all to 0
    num_ways = [0 for i in range(n + 1)]
    # Define our first two cases
    num_ways[1] = 1
    num_ways[2] = 2

    # From 3 to n, fill out our list by summing the previous two numbers
    for i in range(3,n + 1):
        num_ways[i] = num_ways[i - 1] + num_ways[i - 2]

    # The final element in the list is our answer
    return num_ways[n]

if __name__ == "__main__":
    print(pebble(5))
    print(pebble_dp(5))