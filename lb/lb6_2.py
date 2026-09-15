def solution(arr):

    copy_arr = list(arr)
    for i in range(len(copy_arr)):
        if copy_arr[i] < 10:
            copy_arr[i] = 0
        elif copy_arr[i] > 20:
            copy_arr[i] = 1
    print(arr, copy_arr)

print("Тест")
test = [1,20,3,4,50,6,700,80,11, 1000,1211,12,93,44,1]
solution(test)

print("Программа")
status = True
while status:
    user_input = input("Введите элементы списка в строчку: ")
    user_array = list(map(int, user_input.split()))
    if len(user_array) == 15:
        solution(user_array)
        status = False
    else:
        print(f"Вы ввели: {len(user_array)} элементов. Введите ровно 15 элементов!")