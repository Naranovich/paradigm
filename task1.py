def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(n-i-1):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    numbers.reverse()
    print(numbers)

numbers = [4,5,8,2,34,645,7,8,9,23]
print(sort_list_imperative(numbers))