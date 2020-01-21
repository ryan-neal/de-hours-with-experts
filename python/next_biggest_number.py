#!/usr/bin/python3
import sys
from itertools import permutations


def main():
    next_biggest_number(sys.argv[1])



def next_biggest_number(num):
    num = int(num)
    minimum_difference = 100000
    saved_index = -1
    array_num = convert_to_array(num)

    if is_sorted_desc(array_num):
        return -1

    combos = create_combinations(array_num)
    possible_answers = []
    
    for lst in combos:
        possible_answers.append(convert_to_integer(lst))
    
    possible_answers = possible_answers[1:]

    for idx in range(len(possible_answers)):
        if possible_answers[idx] - num < minimum_difference and possible_answers[idx] - num > 0:
            minimum_difference = possible_answers[idx] - num
            saved_index = idx

    return possible_answers[saved_index]

def convert_to_array(num):
    arr = []
    for digit in str(num):
        arr.append(int(digit))
    return arr

def create_combinations(arr):
    first_number = arr[0]
    answer = []
    for i in list(permutations(arr)):
        answer.append(i)
    answer = list(map(list, answer))
    return answer

def convert_to_integer(lst):
    return int("".join(map(str, lst))) 

def is_sorted_desc(lst):
    for idx in range(len(lst)-1):
        if lst[idx+1] > lst[idx]:
            return False
    return True

if __name__ == "__main__":
    main()



