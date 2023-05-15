import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    a=0
    b=0
    i=0
    f=open(file_path)
    k=json.load(f)
    b=min(k.values())
    return b

# test
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
