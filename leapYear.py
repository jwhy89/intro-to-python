a = 2000

if a % 400 == 0:
    print("true")
elif a % 100 == 0:
    print("false")
elif a % 4 == 0:
    print("true")
else:
    print("false")

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Daisy"
car1.color = "blue"
car1.kind = "sedan"
car1.value = 30000.00

car2 = Vehicle()
car2.name = "Lightning"
car2.color = "red"
car2.kind = "race car"
car2.value = 100000.00

# test code
print(car1.description())
print(car2.description())