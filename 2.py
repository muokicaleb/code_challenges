# challange 2
'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

'''


def place_product(list1):
    list2 = []

    for i in range(len(list1)):
        temp = list1
        temp = del temp[i]

        result = 1
        for x in temp:
            result = result * x

        list2[i] = result


test = [3, 2, 1]
place_product(test)
