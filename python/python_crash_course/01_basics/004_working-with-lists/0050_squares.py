squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

del squares[0]
print(squares)
del squares[1]
print(squares)
del squares[2]
print(squares)
del squares[3]
print(squares)
del squares[4]
print(squares)
del squares[0]
print(squares)
del squares[0]
print(squares)
del squares[0]
print(squares)
del squares[0]
print(squares)


for value in range(1, 11):
    square = value**2
    squares.insert(0, square)
print(squares)
