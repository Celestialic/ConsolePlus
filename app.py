import consoleplus as c

def com_parse(command):
    if command == 'help':
        print('CMD+ - Дополнение к cmd')

    if command == 'cls':
        print(c.cls())

    if command == 'md':
        name = input('Название: ')
        path = input('Путь: ')
        c.md(name=name, path=path)

    if command == 'rd':
        name = input('Название: ')
        path = input('Путь: ')
        c.rd(name=name, path=path)

while True:
    command = input('CMD+: ')
    com_parse(command)
