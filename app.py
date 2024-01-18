import os
from commands_parser import command_parser

command = "None"

while True:
    command = input('CMDplus: ')

    command_parser()