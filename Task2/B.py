<<<<<<< HEAD
s = input()
if s.isupper():
    print(s.lower())
elif len(s) == 1 and s.islower():
    print(s.upper())
elif s[0].islower() and s[1:].isupper():
    print(s.capitalize())
else:
=======
s = input()
if s.isupper():
    print(s.lower())
elif len(s) == 1 and s.islower():
    print(s.upper())
elif s[0].islower() and s[1:].isupper():
    print(s.capitalize())
else:
>>>>>>> 2336f7ec8a38f51be205a3b2b6e95a88d433f73c
    print(s)