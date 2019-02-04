guests = ['Anthony', 'Brendan', 'Charlotte', 'Diana', 'Ethan']
message = "You are invited to Dinner, "

print("Sadly, " + guests[2] + " is not able to attend. ")
guests[2] = 'Gregory'
print(guests[2] + " will be joining us though!")

print("We also found a bigger Table!")

guests.append("Stephan")
guests.insert(0, "Guiseppe")
guests.insert(3, "Timothy")

print(guests)

print(message + guests[0])
print(message + guests[1])
print(message + guests[2])
print(message + guests[3])
print(message + guests[4])
print(message + guests[5])
print(message + guests[6])
print(message + guests[-1])

print("Sorry, I can only invite two People.")
removed = guests.pop()
print("Sorry, I'll have to remove you, " + removed)
removed = guests.pop()
print("Sorry, I'll have to remove you, " + removed)
removed = guests.pop()
print("Sorry, I'll have to remove you, " + removed)
removed = guests.pop()
print("Sorry, I'll have to remove you, " + removed)
removed = guests.pop()
print("Sorry, I'll have to remove you, " + removed)
removed = guests.pop()
print("Sorry, I'll have to remove you, " + removed)

print(guests)

print("You're still invited " + guests[1] + " and " + guests[0])
del guests[1]
del guests[0]
print(guests)
