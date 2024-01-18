import consoleplus as c
import os

def com_parse(command):
    if command == 'help':
        print('CMD+ - Дополнение к cmd')

    elif command == 'cls':
        print(c.cls())

    elif command == 'md':
        name = input('Название: ')
        path = input('Путь: ')
        c.md(name=name, path=path)

    elif command == 'rd':
        name = input('Название: ')
        path = input('Путь: ')
        c.rd(name=name, path=path)

    elif command == 'ls':
        c.ls()

    elif command.startswith('cd '):
        new_path = command[3:]
        try:
            os.chdir(new_path)
            print(f"Дериктория заменена на: {os.getcwd()}")
        except FileNotFoundError:
            print(f"ERROR С141")
        
    else:
        print('ERROR C182')

while True:
    command = input('CMD+: ')
    com_parse(command)
