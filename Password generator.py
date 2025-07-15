import random
import string

def generate_password(length):
    # Define possible characters: lowercase, uppercase, digits, and special symbols
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure password length is valid
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    # Randomly choose characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== PASSWORD GENERATOR ===")
    
    try:
        # Get user input
        length = int(input("Enter desired password length: "))
        
        # Generate password
        password = generate_password(length)
        
        if password:
            print("\nGenerated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
