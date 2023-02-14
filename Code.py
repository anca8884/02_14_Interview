from typing import List  

def order_helper(a, b):
    if a < b:
        return (a, b)
    else:
        return (b, a)


def pair_sum_count(numbers: List[int], A: int):
    counter = 0
    for number_one in numbers:
        for number_two in numbers:
            if number_one + number_two == A:
              if order_helper(number_one, number_two) == (number_one, number_two):
                counter += 1
    return counter

pair_sum_count([1,2,3,4,5,6,7], 5)
