def get_todos(filepath):
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def set_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action.strip()

    if user_action.startswith("add"):
        # todo = input("Enter a To-do: ") + "\n"
        todo = user_action[4:] + "\n"
        todos = get_todos("todos.txt")

        todos.append(todo)

        set_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}--{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter the TODO: ")
            todos[number] = new_todo + "\n"

            set_todos("todos.txt", todos)

        except ValueError:
            print("Not Valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos("todos.txt")

            todos.pop(number - 1)

            set_todos("todos.txt", todos)

        except IndexError:
            print("Invalid Index")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid Command")

print("BYE!")
