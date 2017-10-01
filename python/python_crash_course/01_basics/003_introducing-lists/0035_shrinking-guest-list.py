Guests = ['Roger Water', 'Elenor Rigby', 'Enrico Pazi', 'Peter Highwand']

print("This is a Dinner Invitation for " + Guests[0] + ".")
print("This is a Dinner Invitation for " + Guests[1] + ".")
print("This is a Dinner Invitation for " + Guests[2] + ".")
print("This is a Dinner Invitation for " + Guests[3] + ".")

print("\nWe were able to find a bigger Table, so 3 new Guests will join us.")

Guests.insert(0, 'Henry Winters')
Guests.insert(3, 'Angela Summers')
Guests.append('Michael Burrows')
print("This is a Dinner Invitation for " + Guests[0] + ".")
print("This is a Dinner Invitation for " + Guests[1] + ".")
print("This is a Dinner Invitation for " + Guests[2] + ".")
print("This is a Dinner Invitation for " + Guests[3] + ".")
print("This is a Dinner Invitation for " + Guests[4] + ".")
print("This is a Dinner Invitation for " + Guests[5] + ".")
print("This is a Dinner Invitation for " + Guests[6] + ".")

print("Sadly we can only invite two People")

Uninv_Michael = Guests.pop(6)
print("Sorry " + Uninv_Michael + ", you can't come.")
print(Guests)

Uninv_Peter = Guests.pop(5)
print("Sorry " + Uninv_Peter + ", You can't come.")
print(Guests)

Uninv_Enrico = Guests.pop(4)
print("Sorry " + Uninv_Enrico + ", you can't come.")
print(Guests)

Uninv_Angela = Guests.pop(3)
print("Sorry " + Uninv_Angela + ", you can't come.")
print(Guests)

Uninv_Elenor = Guests.pop(2)
print("Sorry " + Uninv_Elenor + ", you can't come.")

print(Guests[0] + " and " + Guests[1] + ", you are still invited!")
del Guests[1]
del Guests[0]
print(Guests)
