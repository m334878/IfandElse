print('Type a num')
z = input()
if (len(z) == 0):
    print("You did not entered anything")
else:
    try:
      z = int(z)
    except ValueError:
        print('You typed in letter(s) instead')
print(z)