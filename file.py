def add_one(some_list):
    number_str = ""
    for digit in some_list:
        number_str += str(digit)
    number = int(number_str)
    number += 1
    result = []
    for digit in str(number):
        result.append(int(digit))
    return result

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test123'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
