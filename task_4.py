# Decorator for error handling
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter the argument for the command"
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    # if len(args) != 2:
    #     return "Error: Please provide both name and phone number"
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added"


@input_error
def change_contact(args, contacts):
    # if len(args) != 2:
    #     return "Error: Please provide both name and new phone number"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact '{name}' updated."
    raise KeyError
    # return f"Error: Contact '{name}' not found."


@input_error
def show_phone(args, contacts):
    # if len(args) != 1:
    #     return "Error: Please provide the name of the contact"
    name = args[0]
    if name in contacts:
        return f"Phone for '{name}': {contacts[name]}"
    raise KeyError
    # return f"Error: Contact '{name}' not found"


@input_error
def show_all(contacts):
    if contacts:
        result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return f"All contacts:\n{result}"
    return "No contacts found"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


# Запуск головної функції
if __name__ == "__main__":
    main()
