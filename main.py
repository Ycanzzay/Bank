variors = int(input('Количество воинов '))
list = list()
x = 0
index = 0
while x < variors:
    x = x + 1
    list.append(x)
k = int(input('Убитый воин '))
while len(list) > 1:
    if index != 0:
        index = len(list) - index
    else:
        index = k - 1
    if index < 0:
        index = index + k - 1
    while index <= (len(list) - 1):
        del list[index]
        if index == len(list):
            index = 0
            break
        else:
            index = index + (k - 1)
print(list)