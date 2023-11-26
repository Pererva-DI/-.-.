import json


def task() -> float:
    filename = "input.json"
    with open(filename) as f:
        python_list = json.load(f)
    multiply = [dictionary["score"] * dictionary["weight"] for dictionary in python_list]
    total_sum = sum(multiply)
    return round(total_sum, 3)


print(task())
