import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password length should be at least 4"

    # character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # ensure at least one from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # fill remaining length
    all_chars = lowercase + uppercase + digits + symbols
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # shuffle to avoid predictable pattern
    random.shuffle(password)

    return "".join(password)


# example usage
print("Generated password:", generate_password(16))