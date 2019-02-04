guests = ['Anthony', 'Brendan', 'Charlotte', 'Diana', 'Ethan']
message = "You are invited to Dinner, "

print(message + guests[0])
print(message + guests[1])
print(message + guests[2])
print(message + guests[3])
print(message + guests[-1])


print("Sadly, " + guests[2] + " is not able to attend. ")
guests[2] = 'Gregory'
print(guests[2] + " will be joining us though!")