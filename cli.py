from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add or show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{str(index + 1)}.) {todo}")

    elif user_action.startswith("edit"):
        try:
            todos = get_todos()

            old_todo_index = int(user_action[5:]) - 1
            new_todo = input("Enter a new todo: ") + "\n"
            todos[old_todo_index] = new_todo

            write_todos(todos)
        except ValueError:
            print("Your command is not valid. ")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = get_todos()

            completed_todo_index = int(user_action[9:]) - 1
            todo_to_remove = todos[completed_todo_index].strip('\n')
            print(f"{todo_to_remove} was removed from the list")
            todos.pop(completed_todo_index)

            write_todos(todos)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Bye!")



