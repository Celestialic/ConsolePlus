import consoleplus as c

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
        
    else:
        print('ERROR C182')

while True:
    command = input('CMD+: ')
    com_parse(command)
