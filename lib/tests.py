from random import randint
from time import time


def test_algorithm(algorithm, problem_instances, in_place=False, output=0):
    t0 = time()
    correct = True
    for instance, verify in problem_instances:
        try:
            instance_string = format_data(instance)
            if type(instance) == tuple:
                result = algorithm(*instance)
            else:
                result = algorithm(instance)
            if in_place:
                result = instance
            if not verify(result):
                correct = False
                print(f"{algorithm.__name__} failed "
                    f"for {instance_string}\n"
                    f"output was {format_data(result)}")
        except Exception as e:
            correct = False
            print(f"{algorithm.__name__} crashed "
                f"for {instance_string}\n"
                f"error was {e.args}")
    if correct:
        print(f"{algorithm.__name__} was correct "
            f"for the {len(problem_instances)} given problem instances.")
    print(f"Tests took {round(time() - t0, 8)} seconds.\n")


def format_data(data, max_length=50):
    string = str(data)
    if len(string) > max_length:
        return string[:max_length//2] + " ... " + string[-max_length//2:]
    return string


def get_sort_problem_instances():
    return [(instance, lambda x: x == sorted(x)) for instance in (
        [],
        [0],
        list(range(10)),
        list(range(10, -1, -1)),
        list(randint(-100, 100) for _ in range(100)),
    )]

def get_merge_sort_problem_instances():
    return [((instance, 0, len(instance) - 1), lambda x: x[0] == sorted(x[0])) \
        for instance, correct_result in get_sort_problem_instances()]

def get_maximum_subarray_problem_instances():
    return [
        (([0], 0, 0), lambda x: x == (0, 0, 0)),
        ((list(range(1, 10)), 0, 8), lambda x: x == (0, 8, sum(range(10)))),
        (([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], 0, 15), lambda x: x == (7, 10, 43)),
    ]

def get_bisect_problem_instances():
    return [
        (([0], 0, 0, 0), lambda x: x == 0),
        (([1, 5, 7], 0, 2, 7), lambda x: x == 2),
        (([1, 5, 7, 19, 47], 0, 4, 10), lambda x: x == None),
    ]

def get_counting_sort_problem_instances():
    return [((instance, [None] * len(instance), \
        max(instance) + 1 if instance else 1), lambda x: x[1] == sorted(x[1])) \
        for instance, _ in get_sort_problem_instances()
        if (min(instance) if instance else 0) >= 0]

def get_radix_sort_problem_instances():
    return [
        (([""], 0), lambda x: x == [""]),
        ((["A"], 1), lambda x: x == ["A"]),
        ((["A", "B", "C"], 1), lambda x: x == ["A", "B", "C"]),
        ((["C", "B", "A"], 1), lambda x: x == ["A", "B", "C"]),
        ((["AC", "AB", "AA"], 2), lambda x: x == ["AA", "AB", "AC"]),
        ((["CARL", "PETE", "ADAM"], 4), \
            lambda x: x == ["ADAM", "CARL", "PETE"]),
    ]

def get_bucket_sort_problem_instances():
    return [(instance, lambda x: x == sorted(x)) for instance in (
        [],
        [0],
        list(x/10 for x in range(10)),
        list(x/10 for x in range(9, -1, -1)),
        list(randint(0, 999)/1000 for _ in range(100)),
    )]

def get_randomized_select_problem_instances():
    return [
        (([0], 0, 0, 1), lambda x: x == 0),
        (([0, 1], 0, 1, 1), lambda x: x == 0),
        (([0, 1], 0, 1, 2), lambda x: x == 1),
        (([5, 1, 2, 4, 3], 0, 4, 3), lambda x: x == 3),
    ]

class Heap(list):
    heap_size = 0

def get_heapsort_problem_instances():
    return [(Heap(instance), correct_answer) \
        for instance, correct_answer in get_sort_problem_instances()]

def get_activity_selector_problem_instances():
    # start times, finish times, k (time?), activity count
    return [
        ((
            [0, 0],
            [0, 1],
            0, 1
        ), lambda x: x == {1}),
        ((
            [0, 1, 0, 2],
            [0, 2, 3, 3],
            0, 3
        ), lambda x: x == {1, 3}),
        ((
            [0, 4, 5, 5, 6, 5, 0],
            [0, 5, 5, 6, 7, 7, 9],
            0, 6
        ), lambda x: x == {1, 2, 3, 4}),
        ((
            [0, 1, 3, 0, 5, 3, 5,  6,  8,  8,  2, 12],
            [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16],
            0, 11
        ), lambda x: x == {1, 4, 8, 11} or x == {2, 4, 9, 11}),
    ]