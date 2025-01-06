
def greet(name):
    return f"Hi there {name}! Hope you are enjoying this lesson."

if __name__ == "__main__":
    user_name = input("Please enter your name: ")

    message = greet(user_name)
    print(message)