#http://learnpythonthehardway.org/book/ex5.html
my_name = 'Kiraly Zalan'
my_age = 27 # not a lie
my_height = 175 # cm
my_weight = 105 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print("My name is %s" % my_name)
print("I'm %d years old" % my_age)
print("I'm %d centimeters tall." % my_height)
print("I'm %d kilograms heavy." % my_weight)
print("Actually that's enough heavy.")
print("I've got %s eyes and %s hair." % (my_eyes, my_hair))
print("My teeth are usually %s depending on the coffee and cigarettes." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))
