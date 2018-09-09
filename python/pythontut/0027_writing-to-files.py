# open() opens the specified file, the modifier after it
# lets you either (a)append to it or (r)write a new file.

employee_file = open("employees.txt", "a")
employee_file.write("\nToby - Human Resources")

employee_file.close()
