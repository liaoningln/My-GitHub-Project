def calculate_special_sum(n):
    sum = 0
    for i in range(1, n):
        # calculate
        sum = sum + i ** 2 * (i + 1)
    return sum
# assert  calculate_special_sum(3) == 14
n=3
print("Sum: ",calculate_special_sum(n))
