def repetition_element(arr):
    duplicate = False
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                print("Найден поторяющийся элемент: ", arr[i])
                duplicate = True
    if not duplicate:
        print("Повторяющиея элементы не найдены")

def duplicate_element_d(arr):
    duplicate = dict()
    for i in range(len(arr)):
        if arr[i] not in duplicate:
            duplicate[arr[i]] = 1
        else:
            duplicate[arr[i]] += 1
    print("Найдены повторяющиеся элементы: ", [i for i in range(len(arr)) if duplicate[arr[i]] == 1])


print("Тест")
test1 = [1,5,4,3,1,5,-8,9, -8]
repetition_element(test1)
# duplicate_element_d(test1)

print("Программа")
user_input = input("Введите элементы списка в строчку: ")
user_array = list(map(int, user_input.split()))
repetition_element(user_array)