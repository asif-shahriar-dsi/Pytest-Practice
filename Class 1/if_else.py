# x = int(input("Enter a number: "))
#
# if x > 10:
#     print("Yahoo!")
# elif x == -1:
#     print("20")
# else:
#     print("Boo")



x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

if x>y and x>z:
    print(f'Biggest number is {x}')
elif y>x and y>z:
    print(f'Biggest number is {y}')
else:
    print(f'Biggest number is {z}')

