# testing print with hello world
print("Hello, World!")

# type python in terminal to enter interactive mode
# control + z to quit interactive mode

#testing math with python
one = 1
two = 2
three = one + two
print(three)

# testing if and elif
a = 200
b = 33
c = 250

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b")

print("A") if a > b else print("B")

print("A") if a > b else print("=") if a == b else print("B")

if a > b and c > a:
  print("Both conditions are True")

