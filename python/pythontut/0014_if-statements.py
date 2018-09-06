is_male = True  # True and False need to be written like that
is_tall = False

if is_male:
    print("You are a male!")
else:
    print("You aren't male!")

if is_male or is_tall:
    print("You are a male or tall or both!")
else:
    print("You are neither male nor tall!")

if is_male and is_tall:
    print("You are a male and tall!!")
elif is_male and not is_tall:
    print("You are a short male!")
elif not is_male and is_tall:
    print("You're not a male, but you're tall!")
else:
    print("You are either not male or tall!")
