import sys


# def process(num):
#     return num * 2
#
#
# list_of_numbers = [1, 2, 3, 4]
# results = [process(number) for number in list_of_numbers]


# def input_handler():
#     return [int(arg) for arg in sys.argv[1:]]
#
#
# def sum_of_list(nums):
#     total = 0
#     sum_of_nums = [total := total + numbers for numbers in nums]
#     return sum_of_nums[len(sum_of_nums) - 1]
#
#
# list_of_nums = input_handler()
# print(sum_of_list(list_of_nums))


def is_vowel(character):
    vowels = "AEIOUaeiou"
    return character in vowels

