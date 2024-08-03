#password strength checker

def password_checker(password):
    
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower()for char in password):
        return False
    if not any(char.isupper()for char in password):
        return False
    if not any(char in"@#$%^&*()_"for char in password):
        return False
    return True

print(password_checker("weakPassword"))
print(password_checker("StrongP@ssword0"))


