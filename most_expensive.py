import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str:    fimost expensive item
    """
    f=open(file_path)
    f=json.load(f)
    a=0
   
    for i in f.values():
        if a<i:
            a=i
    return a



# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)