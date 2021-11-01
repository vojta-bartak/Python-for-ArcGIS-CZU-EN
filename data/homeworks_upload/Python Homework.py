def sort(numbers):
    for i in range(4):
        min_num = i
        for a in range(i,5):
            if numbers[a] < numbers[min_num]:
               min_num = a
        z = numbers[i]
        numbers[i] = numbers[min_num]
        numbers[min_num] = z
numbers = [15, 1, 19, 9, 8]
sort(numbers)
print(numbers)
