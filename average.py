import json

def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    a = 0
    b = 0
    f = open(file_path)
    k = json.load(f)
    k = k.values()
    for i in k:
        a += i
        b += 1
    return a/b
    

# test
file_path = "data.json"
average = average_expenses(file_path)
print(average)
