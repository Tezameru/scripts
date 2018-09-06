monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
}

print(monthConversions["Jan"])
print(monthConversions.get("Feb"))
print(monthConversions.get("Luv", "Not a valid entry"))