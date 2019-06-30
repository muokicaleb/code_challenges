'''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''


k = 17

list_ = [10, 15, 3, 7]

sorted_list = sorted(list_)
len_list = len(sorted_list)


def checker(sorted_list):
    counter = 0
    start = 0
    stop = len_list - 1
    
    sum_ = sorted_list[start] + sorted_list[stop]
    while sum_ != k and counter <= len_list:
        sum_ = sorted_list[start] + sorted_list[stop]
        if sum_ > k:
            stop = stop - 1
        elif sum_ < k:
            start = start + 1
            counter = counter + 1

    if (sum_ == k) and (start != stop):
        print("true \n  " + str(sorted_list[start]) + 
                " and " + str(sorted_list[stop]) + " make up " + str(k))
    else:
        print("false")

checker(sorted_list)
