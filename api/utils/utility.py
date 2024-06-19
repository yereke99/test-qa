import string
import random


def generate_random_username():
    # Define the characters that can be used in the username
    alphanumeric_chars = string.ascii_letters + string.digits
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    # Generate a username with the specified requirements
    username = ''.join(random.choice(alphanumeric_chars) for _ in range(7))
    username += random.choice(string.digits)  # Add a digit
    username += random.choice(string.ascii_uppercase)  # Add an uppercase letter
    username += random.choice(string.ascii_lowercase)  # Add a lowercase letter
    username += random.choice(special_chars)  # Add a special character
    
    # Shuffle the characters in the username to make it random
    username = ''.join(random.sample(username, len(username)))
    
    return username


