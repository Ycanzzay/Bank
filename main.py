vowels_count = 0
input_str = input("Введите строку: ")
for char in input_str:
    if char.lower() in "аяуюоеёэиы":
     vowels_count += 1

print("Количество гласных в строке:", vowels_count)