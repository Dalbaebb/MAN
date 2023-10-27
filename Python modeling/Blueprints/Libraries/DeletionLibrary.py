import os

def delete(fileName):
    str = os.path.join(os.getcwd(),fileName)
    print(str)
    if os.path.isfile(str):
        os.remove(str)

