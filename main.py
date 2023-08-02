#CIS245: Bellevue File Creation Software 1.0

def prompt_user(message):
    return input(message)

def write_to_file(file_name, name, address, phone_number):
    with open(file_name, 'w') as file:
        file.write(f"\n{name},{address},{phone_number}")

def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        return data

def main():
    file_name = prompt_user("Enter the file name: ")
    name = prompt_user("Enter your name: ")
    address = prompt_user("Enter your street address: ")
    phone_number = prompt_user("Enter your phone number: ")

    write_to_file(file_name, name, address, phone_number)
    print("\nThe specified data has been written to the file successfully.")

    print("\nDisplaying file contents:")
    data = read_file(file_name)
    print(data)

if __name__ == "__main__":
    main()
