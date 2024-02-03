# todo app

# day 9 - v3

# ---------------------- if / else block ---------------------

# print(dir(list))
# print(help(list.remove))

# from functions import get_todos , write_todos
import functions
import os
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('it is ', now)

todos = []

# day 12 - custom functions

FILEPATH = 'todos.txt'

while True:
    user_action = input('type add, show , complete , edit or exit \n')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        # remove /n from the todos
        # new_todos = [item.strip('\n') for item in todos]

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1} - {item}'
            print(row)

    elif user_action.startswith('complete'):

        try:
            number = int(user_action[9:])

            todos = functions.get_todos('todos.txt')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            print(f'{todo_to_remove} is removed')

            functions.write_todos(todos)

        except IndexError:
            print(f'There are only {len(todos)} todo list ,'
                  f' There is no index in the todo list')
            continue

    elif user_action.startswith('edit'):

        try:
            number = int(user_action[5:])
            number = number - 1
            new_todo = input('enter a new todo : ')

            todos = functions.get_todos('todos.txt')

            todos[number] = new_todo

            print('todo is modified')

            functions.write_todos(todos)

        except ValueError:
            print('Enter number after edit to modify todo list')
            continue  # start the program from start

    elif user_action.startswith('exit'):
        break
    else:
        print('command is not valid')

print('bye')

# ---------------------- if / else block ---------------------
