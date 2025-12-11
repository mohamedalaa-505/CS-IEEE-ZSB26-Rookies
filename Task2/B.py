s = input()
if s.isupper():
    print(s.lower())
elif len(s) == 1 and s.islower():
    print(s.upper())
elif s[0].islower() and s[1:].isupper():
    print(s.capitalize())
else:
    print(s)