sum = 0
for i in range(1, 11, 2):
    sum = i + sum
print(sum)


number = [1, 2, 3, 4, 5, 6,"Banana"]
number.remove("Banana")
print(number)

for i in range(len(number) - 1, 0, -1):
    print(i)

for i in number[::-1]:
    print(i)

s = "abcdef"
x = ""
for i in s[::-1]:
    x += i+", "

x = x[:-2]
print(x)
