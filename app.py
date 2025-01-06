
def greet(name):
    return f"Hello there, {name}! Welcome to our git collaboration demo! Hope you are enjoying it."


if __name__ == "__main__":
    user_name = input("Please enter your name: ")

    message = greet(user_name)
    print(message)