def main() -> None:
    """
    The main function of the script, which prompts the user and creates the module, adds a function, or adds a class.
    """
    print("1. Create a module")
    print("2. Add a function to a module")
    print("3. Add a class to a module")
    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        module_name, description = prompt_user()
        create_module(module_name, description)
    elif choice == 2:
        add_function_to_module()
    elif choice == 3:
        add_class_to_module()
    else:
        print("Invalid choice.")