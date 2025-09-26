def check_password_strength(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    return has_upper and has_lower and has_digit and has_special

# Take user input
user_password = input("Enter your password: ")

if check_password_strength(user_password):
    print("Your password is strong!")
else:
    print("Weak password! Please make sure it is at least 8 characters, "
          "contains uppercase and lowercase letters, a number, and a special character (!,@,#,$,%).")
