"""
Extremely simple question just return weather the amount of times the robot went left is equal to the amount of times he went right and weather the amount of times he went up is equal to down.
Time complexity is O(n) with n being the length of the string
Space complexity is O(1)
"""


def judgeCircle(moves: str) -> bool:
    return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')
