# Kira Murphy
# CS362 HW

from typing import List, Tuple
from math import inf

def change_rec_naive(amt: int, denom:List[int]) -> int:

    def change(i: int, amt:int) -> int:
        if i >= len(denom):
            return inf

        if amt == 0:
            return 0
        elif denom[i] == amt:
            return 1
        elif denom[i] > amt:
            return change(i+1, amt)
        else:
            return min(
                1 + change(i, amt - denom[i]),
                change(i+1, amt)
            )
    return change(0, amt)

def change_dp(amt: int, denom: List[int]) -> int:
    n = len(denom)

    # make the initial table
    c = [[0]*(amt + 1) for i in range(n)]

    # fill in the last row of the table
    for i in range(amt+1):
        c[n-1][i] = i

    for i in range(n-2, -1, -1):
        for j in range(amt+1):
            if denom[i] > j:
                c[i][j] = c[i+1][j]
            else:
                c[i][j] = min(
                    c[i+1][j],
                    c[i][j - denom[i]] + 1
                )

    return c[0][amt]

def change_dp_with_used(amt: int, denom: List[int]) -> Tuple:
    n = len(denom)

    # make the initial table
    c = [[0]*(amt + 1) for i in range(n)]

    # make a table of used denominations
    used = [[False]*(amt + 1) for i in range(n)]

    # fill in the last row of the table
    for i in range(amt+1):
        c[n-1][i] = i
        used[n-1][i] = True

    for i in range(n-2, -1, -1):
        for j in range(amt+1):
            if denom[i] > j:
                c[i][j] = c[i+1][j]
                used[i][j] = False
            else:
                c[i][j] = min(
                    c[i+1][j],
                    c[i][j - denom[i]] + 1
                )
                if c[i+1][j] < c[i][j - denom[i]] + 1:
                    c[i][j] = c[i+1][j]
                    used[i][j] = False
                else:
                    c[i][j] = c[i][j - denom[i]] + 1
                    used[i][j] = True

    return c[0][amt], used


def print_change(amt: int, used: List[List[bool]], denom: List[int]) -> None:
    """
    Print the denominations used to make change for the given amount
    :param amt: Amount we want change for
    :param used: Table of used denominations
    :param denom: Talbe of denominations
    :return:
    """
    i = 0
    change = ""
    while amt > 0:
        # If the amount is used, add it to the change and subtract from the total amount
        if used[i][amt] == True:
            change += "{} ".format(denom[i])
            amt -= denom[i]
        # If the amount is not used, go to the next denomination
        else:
            i += 1
    print(change)

if __name__ == "__main__":
    denom = [10, 6, 1]
    used_table = change_dp_with_used(19, denom)[1]
    print_change(19, used_table, denom)



