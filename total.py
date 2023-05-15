import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    f=open(file_path)
    f=json.load(f)
    k=f.values()
    return k


# test
file_path = "data.json"
total = total_expenses(file_path)
print(total)
