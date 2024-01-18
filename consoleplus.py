import os

def cls():
    x = '\n' * 300
    return x

def md(name, path):
    if name == '' or path == '':
        print('ERROR C201')
    else:
        os.makedirs(os.path.join(path, name))

def rd(name, path):
    if name == '' or path == '':
        print('ERROR C201')
    else:
        os.removedirs(os.path.join(path, name))

def ls():
    files = os.listdir()
    for file in files:
        file_path = os.path.join(os.getcwd(), file)
        size = os.path.getsize(file_path)
        print(f"{file} - {size} байт")