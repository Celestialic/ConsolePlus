import os

def cls():
    x = '\n' * 300
    return x

def md(name, path):
    if name == '' or path =='':
        print('ERROR C201')
    os.mkdir(name=name, path=path)