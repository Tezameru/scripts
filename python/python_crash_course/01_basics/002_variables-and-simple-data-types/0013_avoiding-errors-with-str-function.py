#age = 23
#message = "Happy " + age + "rd Birthday!"
#
#print(message)
#
#       This does not work, python needs to know that the variable age is to be interpreted as a string
#
#  line 2, in <module>
#     message = "Happy " + age + "rd Birthday!"
# TypeError: must be str, not int

age = 23
message = "Happy " + str(age) + "rd Birthday"
print(message)