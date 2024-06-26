"""
Count minimal number of jumps from position X to Y.

A small frog wants to get to the other side of the road.
The frog is currently located at position X and wants to get to a position
 greater than or equal to Y.
The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its
 target.

Write a function:

    def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from
position X to a position equal to or greater than Y.

For example, given:
  X = 10
  Y = 85
  D = 30

the function should return 3, because the frog will be positioned as follows:

        after the first jump, at position 10 + 30 = 40
        after the second jump, at position 10 + 30 + 30 = 70
        after the third jump, at position 10 + 30 + 30 + 30 = 100

Write an efficient algorithm for the following assumptions:

        X, Y and D are integers within the range [1..1,000,000,000];
        X ≤ Y.
"""


def solution(x, y , d):
    """Calculate the miminum number of jumps from X to Y.

    :param X: [int] Start position.
    :param Y: [int] End position.
    :param D: [int] Size of the jump.
    :return: Minium number of jumps in O(1) time and space complexity.

    * Integer divide the difference between the start and end position by the jump size.
    * If there is a remainder, froggy needs one more hop to get past the end.
    * Otherwise froggy landed right on it!  Yay for frog.
    """
    quot, rem = divmod(y - x, d)
    return quot + 1 if rem != 0 else quot


print(solution(10, 85, 30))
