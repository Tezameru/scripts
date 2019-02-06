# Seeing the World: Think of at least five places in the world you’d like to
# visit. Store the locations in a list. Make sure the list is not in alphabetical order.

countries = ['Paraguay', 'France', 'Greece', 'Italy', 'Sweden']
# Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
print("1. Original Order")
print(countries)
# Use sorted() to print your list in alphabetical order without modifying the
# actual list.
print("2. sorted() to print in alphabetical order")
print(sorted(countries))
# Show that your list is still in its original order by printing it.
print("3. list still in original order")
print(countries)
# Use sorted() to print your list in reverse alphabetical order without changing
# the order of the original list.
print("4. sorted to print list in reverse alphabetical without changing original list")
print(sorted(countries, reverse=True))
# Show that your list is still in its original order by printing it again.
print("5. List still in original order")
print(countries)
# Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
print("6. reverse() to change list oder, then print to show changed order")
countries.reverse()
print(countries)
# Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
print("7. reverse() to change order again, print list to show original order")
countries.reverse()
print(countries)
# Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
print("8. use sort() to change order of list to alphabetical again, print to show changes")
countries.sort()
print(countries)
# Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.
print("9. sort() to change list in reverse alphabetical, then print to show order changed")
countries.sort(reverse=True)
print(countries)
