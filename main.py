
def cool_function_name(input_list):
    temp_list = input_list[:]

    for i in range(len(input_list)):
        for x in range(len(temp_list) - 1):
            if temp_list[x] > temp_list[x + 1]:
                temp_list[x + 1] += 1

    result_counter = 0
    for i in range(len(temp_list) - 1):
        if temp_list[i] > input_list[i]:
            result_counter += (temp_list[i] - input_list[i])

    return result_counter

print cool_function_name([2, 5, 1, 3, 1, 2, 1, 7, 7, 6])