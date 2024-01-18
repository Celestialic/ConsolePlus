import consoleplus as c

def com_parse():
    if command == 'help':
        print('CMD+ - дополнение к cmd')

    if command == 'cls':
        print(c.cls())

    if command == 'md':
        name = str(input('Название: '))
        path = str(input('Путь: '))
        c.md(name=name, path=path)

    if command == 'rd':
        c.rd()

while True:
    command = input('CMD+: ')

    com_parse()