x, y, z = 10, "Asif", 11.2
print(y)
print(z)
print(x)

i = 0
while i < 5:
    print("Hola")
    i += 1

a = float(1234)
print(a)
print(type(a))


def oddEven(element):
    if element % 2 == 0:
        print("This number is Even")
    elif element % 2 != 0 and element > 10 or element < 50:
        print("This number is odd")


oddEven(int(input("Enter a number to check odd or even: ")))

s = "roadtosdet"
arr = [1,2,3,4,5]
print(arr[-1])

for i in arr[len(arr):0:-1]:
    print(i)


