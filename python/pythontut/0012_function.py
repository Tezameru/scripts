# def tells python that I'm about to make a function
def greeter():
    print("Hello User!")


print("top")
greeter()
print("bottom")

# parameters are pieces of info that we give to functions


def say_hi(name, age):
    print("Hello " + name + ", you are " + age)


say_hi("Mike", "34")
say_hi("Steve", "76")
