# http://learnpythonthehardway.org/book/ex19.html
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print the number of cheeses
    print("You have %d cheeeses!" % cheese_count)
    # print the number of boxes of crackers
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    # print a string
    print("Man that's enough for a party!")
    # print a string with a line break
    print("Get a blanket.\n")

# print a string
print("We can just give the function numbers directly:")

cheese_and_crackers(20, 30)

# print a string
print("OR, we can use variables from our script:")
# set a var to 10
amount_of_cheese = 10
# set a var to 50
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print a string
print("We can even to math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# print a string
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)