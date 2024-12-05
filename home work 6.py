def check_password(password):
    if len(password) < 6:
        return False
    return True


password = input("Enter your password: ")

if check_password(password):
    print("Password is strong enough.")
else:
    print("Password is too weak. It must be at least 6 characters long and contain both letters and numbers.")


