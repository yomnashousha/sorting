#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

If cmp(a, b) returns -1, then a < b;
if cmp(a, b) returns  1, then a > b;
if cmp(a, b) returns  0, then a == b.
'''

import copy


def cmp_standard(a, b):
    '''
    used for sorting from lowest to highest

    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    '''
    used for sorting from highest to lowest

    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    '''
    used for sorting based on the last digit only

    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.

    NOTE:
    In python, helper functions are frequently prepended with the _.
    and not part of the "public interface".


    >>> _merged([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    '''
    if not xs:
        return ys
    elif not ys:
        return xs
    else:
        if cmp(xs[0], ys[0]) == 1:
            return [ys[0]] + _merged(xs, ys[1:], cmp)
        else:
            return [xs[0]] + _merged(xs[1:], ys, cmp)


def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    copy_xs = copy.deepcopy(xs)
    if len(xs) <= 1:
        return xs
    else:
        mid = len(xs) // 2
        left = merge_sorted(copy_xs[:mid], cmp)
        right = merge_sorted(copy_xs[mid:], cmp)
        return _merged(left, right, cmp)


def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            put all the values equal to p in a list
            sort the greater/less than lists recursively
            return the concatenation of (less than, equal, greater than)

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    if len(xs) <= 1:
        return xs
    mid = len(xs) // 2
    pivot = xs[mid]
    xs_smaller = quick_sorted([x for x in xs if cmp(x, pivot) == -1], cmp=cmp)
    xs_bigger = quick_sorted([x for x in xs if cmp(x, pivot) == 1], cmp=cmp)
    xs_equal = [x for x in xs if cmp(x, pivot) == 0]
    return xs_smaller + xs_equal + xs_bigger


def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    The main advantage of quick_sort is that it can be implemented "in-place".
    This means that no extra lists are allocated,
    or that the algorithm uses Theta(1) additional memory.

    Follow the pseudocode of the Lomuto partition scheme given on wikipedia
    (https://en.wikipedia.org/wiki/Quicksort#Algorithm)
    to implement quick_sort as an in-place algorithm.
    '''
