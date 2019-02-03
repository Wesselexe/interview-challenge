from main import cool_function_name

def challenge_input():
    assert cool_function_name([2, 5, 1, 3, 1, 2, 1, 7, 7, 6]) == 17, "Error..."
    return "cool_function_name() passed successfully"

print challenge_input()

def random_test1():
    assert cool_function_name([2, 3, 2, 3, 1, 1, 2, 1, 2]) == 4, "Random test with [2, 3, 2, 3, 1, 1, 2, 1, 2]"
    return "random_test1() passed successfully"

print random_test1()