test = ['mountain', 'sea', 'sky', 'grass', 'Wind', 'Sun', 'Fire', 'Ground', 'Stars']

# print the list
print(test[0])

# store a message, capitalisation with .title
message = "Look,  " + test[0].title() + "!"
print(message)
print(test)

# replace value from [0]
test[0] = 'hill'
# still holding old value from line
print(message)
message = "Look,  " + test[0].title() + "!"
print(test)
print(message)
# put 'sheep' at the end of the list, append it#
test.append('sheep')
print(test)
# insert the 'house' at the given spot#
test.insert(0, 'house')
print(test)
# deletes the first item in the list indicated by [0]
del test[0]
print(test)
# removes the item on [1] (second item) and stores it in ping
ping = test.pop(1)
print(ping)
print(test)
# removes the item 'sky'
test.remove('sky')
print(test)
# sorts it temporarily
print(sorted(test))
print(test)
test.reverse()
print(test)
test.reverse()
print(test)
test.sort(reverse=True)
print(test)
