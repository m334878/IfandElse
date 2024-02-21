#a = input()
#b = 200
#if b > a:
#  print("b is greater than a")

# user will enter a number
print('Enter a number')

# convert input str to an int
a = int(input())
print(f"You have enter {a}")
print()
print('Enter another number')

# convert input str to an int
b = int(input())
print()

if b > a:
    print(f"{b} is greater than {a}")
    print()
elif a > b:
    print(f"{a} is greater than {b}")
    print()
else:
    print(f"Both {a} and {b} are equal")
    print()
##
