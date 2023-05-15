import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    a=0
    b=0
    i=0
    f=open(file_path)
    k=json.load(f)
    b=max(k.values())
    return b


# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)