# Assertions are the condition or boolean expression which are always supposed to be true in the code.
# assert statement takes an expression and optional message.
# assert statement is used to check types, values of argument and the output of the function.
# assert statement is used as debugging tool as it halts the program at the point where an error occurs

# Using the assert condition to check if some conditions have been met
# function to sum up numbers in a list
# check if values are non-string
# check if list is not empty

def main():
    # testing the function
    my_nums = [2, 4, 4, 6, 6, 8, 7, 3, 1, 3, 4]
    my_nums_string = [3, 5, 5, 2, 'otieno', 23, 2]
    empty_nums = []
    print(sumUpNumbers(my_nums))
    # print(sumUpNumbers(empty_nums))
    print(sumUpNumbers(my_nums_string))

def sumUpNumbers(list_of_numbers):
    # scope variables
    number = 0
    total = 0

    assert len(list_of_numbers) > 0, "You have entered an empty list, summation not possible"
    assert all(isinstance(n, str) for n in list_of_numbers), "You have a list with strings, summation not possible"

    for number in list_of_numbers:
        total += number
    return total

if __name__=='__main__':
    main()