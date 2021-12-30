import json
import sys
from typing import Union

def ipynb_converter(filepath: str, save_name: Union[None, str] = None) -> None:
    '''Converts a Jupyter Notebook into Python file.'''
    
    if not save_name:
        save_name = filepath.split('\\')[-1].split('.')[0]
        save_name += ".py"

    with open(filepath, 'rb') as f:
        ipynb = json.loads(f.read())

    with open(save_name, 'w+') as f:
        for cell in ipynb["cells"]:
            if cell["cell_type"] == "code":
                for code in cell["source"]:
                    f.write(''.join([code,'\n']))
    
    return None

if __name__ == "__main__":

    try:
        file_path = sys.argv[1]
    except IndexError:
        print("Missing file name.")
        exit()

    try:
        save_name = sys.argv[2]
    except IndexError:
        save_name = None

    try:
        ipynb_converter(file_path, save_name)
    except json.decoder.JSONDecodeError:
        if not (f := open(file_path, 'rb')):
            print("File is empty or is not in JSON format.")
    except FileNotFoundError:
        print("File was not found. Please, try reviewing the url.")
