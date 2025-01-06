
def greet(name):
    return f"Hello {name}! Welcome to our Git Collaboration demo!"

if __name__ == "__main__":
    user_name = input("Please enter your name: ")

    message = greet(user_name)
    print(message)