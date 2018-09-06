lucky_numbers = [4, 81, 15, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed")
print(friends)
print(" append Creed")
friends.insert(1, "Kelly")
print(friends)
print(" insert Kelly")

friends.remove("Jim")
print(" remove Jim")
print(friends)

friends.pop()
print(" pop removes last element in list")
print(friends)

print(friends.index("Kevin"))
print("index gives back which list number the value is set")

friends.sort()
print(" sort sorts alphabetical or by value")

friends2 = friends.copy()

friends.extend(lucky_numbers)
print(" extend Lucky Numbers")
print("This is the list with the lucky numbers")
print(friends)

print("this is the copied list from before")
print(friends2)

print("count gives out the value of how often 'Toby' is in the list")
print(friends.count("Toby"))


print(".reverse reverses a list completely, here for the lucky_numbers")
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

print(".clear completely empties a list")
print(friends)
friends.clear()
print(friends)
