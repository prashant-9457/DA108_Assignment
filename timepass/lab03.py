previous_passwords = []

while True:
    password = input("Enter your password: ")
    previous_passwords.append(password)

    # Boolean variables
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Special characters to check
    special_characters = "@#$%&*!?"

    # Loop to check character types
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    # Check password strength
    if len(password) < 6:
        print("Password is WEAK! It must be at least 6 characters.\n")
    elif has_upper and has_lower and has_digit and has_special:
        print("Password is STRONG! Great job 🎉\n")
        break
    elif has_upper and has_lower and has_digit:
        print("Password is MEDIUM. Try adding special characters like @, #, $, etc.\n")
    else:
        print("Password is WEAK! Use a mix of letters, numbers, and special characters.\n")

