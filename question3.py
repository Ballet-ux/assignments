def sum_odd_even (numbers):
    even_sum = sum(i for i in numbers if i % 2 ==0)
    odd_sum = sum(i for i in numbers if i % 2 !=0)
    return even_sum,odd_sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_odd_even(numbers)
print(result)