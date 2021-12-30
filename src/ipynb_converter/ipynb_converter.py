import json
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

    file_path = (r"C:\Users\Vitor\Desktop\Projetos\Python"
                 +r"\Analise_DIEESE\dados_salario_minimo.ipynb")
    ipynb_converter(file_path)
