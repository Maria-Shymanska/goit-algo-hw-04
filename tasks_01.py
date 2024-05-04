import timeit
import random

# сортування злиттям

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
   
#    сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Генеруємо тестові дані для різних розмірів масиву
data_sizes = [10, 100, 1000, 10000]

for size in data_sizes:
    data = [random.randint(0, 1000) for _ in range(size)]
    
    # Вимірюємо час для алгоритму сортування злиттям
    merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
    
    # Вимірюємо час для алгоритму сортування вставками
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
    
    # Вимірюємо час для вбудованого алгоритму Timsort
    sorted_time = timeit.timeit(lambda: sorted(data.copy()), number=1)
    
    print(f"Розмір даних: {size}")
    print(f"Час сортування злиттям: {merge_sort_time} секунд")
    print(f"Час сортування вставками: {insertion_sort_time} секунд")
    print(f"Час вбудованого сортування (Timsort): {sorted_time} секунд")
    print()


