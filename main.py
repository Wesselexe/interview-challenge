"""
This is the most simple solution that I could come up with on my own.
The basic idea of the function is to first make a temporary list equal to the list given. This list will be used to add
the height of the water residing into the wells formed by the water falling down on the array.
"""


def cool_function_name(input_list):

    temp_list = input_list[:]
# Below a nested for loop is executed, first to - in a way - go through the list vertically and then the nested for loop
# is used to go through the array/list element by element to check if the element afterwards is lower.
# The temporary list 'temp_list' is then incremented when ever the condition evaluates to true.
    for i in range(len(input_list)):
        for x in range(len(temp_list) - 1):
            if temp_list[x] > temp_list[x + 1]:
                temp_list[x + 1] += 1

# Below the variable 'result_counter' is declared to count the number of cells that is now filled with water compared to
# the list given. Lastly the the function returns the result.
    result_counter = 0
    for i in range(len(temp_list) - 1):
        if temp_list[i] > input_list[i]:
            result_counter += (temp_list[i] - input_list[i])

    return result_counter


print cool_function_name([2, 5, 1, 3, 1, 2, 1, 7, 7, 6])