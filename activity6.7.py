# Antonio Alvarez
# 1796498

user_pass = input()
new_pass = ''

for i in user_pass:
    if  i=='i':
        new_pass +="!"
    elif i=='a':
        new_pass += "@"
    elif i == 'm':
        new_pass += "M"
    elif i == 'B':
        new_pass += "8"
    elif i == 'o':
        new_pass += "."
    else:
        new_pass += i


new_pass += "q*s"
print(new_pass)
