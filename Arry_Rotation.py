"""
# CyclicRotation

An array A consisting of N integers is given. Rotation of the array means that
each element is shifted right by one index, and the last element of the array
is moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
(elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be
shifted to the right K times.

Write a function:

    class Solution { public int[] solution(int[] A, int K); }

that, given an array A consisting of N integers and an integer K,
returns the array A rotated K times.

For example, given
    A = [3, 8, 9, 7, 6]
    K = 3

the function should return [9, 7, 6, 3, 8]. Three rotations were made:
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
"""


def solution(a, k):
    """Rotate the array A by k steps

    :param a: [[int]] Array of integers.
    :param k: [int] Number of times to shift right.
    :return: The rotated array.

    * Exclude empty lists which might cause a divide-by-zero error.
    * Remove cyclic looping back the start position by applying the modulo of len(A) to K.
    * If no shifts to make, we're done.
    * Slice the array into two fragments, at mod_k, the 'head' and 'tail'.
    * Swap the two fragments, tail to head, and return the recombination.
    """
    if not len(a):  # An empty list has nothing to do.
        return a

    mod_k = (len(a) + k) % len(a)

    if mod_k == 0:  # No shifting is necessary.
        return a

    # Splice at mod_k and swap the tail and head.
    head = a[:-mod_k]
    tail = a[len(a) - mod_k:]
    return tail + head


print(solution([3, 8, 9, 7, 6], 3))
