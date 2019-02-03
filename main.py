"""
This is the most simple solution that I could come up with on my own.
The basic idea of the function is to first make a temporary list equal to the list given. This list will be used to add
the height of the water residing into the wells formed by the water falling down on the array.
"""


def cool_function_name(input_list):
    # First I declare the temporary lists and the variable 'peak'. The forward and backwards 'lists' and the 'peak'
    # variable, which is the highest value of the given list.
    temp_list_forward = input_list[:]
    temp_list_backward = input_list[::-1]
    peak = max(input_list)

    # Below a nested for loop is executed, first to - in a way - go through the list vertically and then the nested for
    # loop is used to go through the array/list element by element to check if the element afterwards is lower.
    # The temporary list 'temp_list' is then incremented when ever the condition evaluates to true.
    for i in range(peak):
        for x in range(len(temp_list_forward) - 1):
            if temp_list_forward[x] > temp_list_forward[x + 1]:
                temp_list_forward[x + 1] += 1
    # Now the list is looped through in reverse order as well.
    for i in range(peak):
        for x in range(len(temp_list_backward) - 1):
            if  temp_list_backward[x] > temp_list_backward[x + 1]:
                temp_list_backward[x + 1] += 1

    # Below the variable 'result_counter' is declared to count the number of cells that is now filled with water
    # compared to the list given. When the two temp lists overlap and exceeds the original list given, the number of
    # cells the two temporary both exceeds the original list is added to the result counter. Lastly the the function
    # returns the result.
    result_counter = 0
    flipped_temp_list_backward = temp_list_backward[::-1]
    for i in range(len(temp_list_forward) - 1):
        if temp_list_forward[i] > input_list[i] and flipped_temp_list_backward[i] > input_list[i]:
            if temp_list_forward[i] > flipped_temp_list_backward[i]:
                result_counter += (flipped_temp_list_backward[i] - input_list[i])
            else:
                result_counter += (temp_list_forward[i] - input_list[i])

    return result_counter
