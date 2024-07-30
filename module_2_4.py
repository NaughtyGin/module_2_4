numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers[:-1]:
    # is_prime = True - определение этой переменной (флага) есть внутри цикла перебора делителей
    for j in numbers[:i]:
        is_prime = int(numbers[i]) % int(numbers[j]) == 0
        # print(i, j, (numbers[i]), numbers[j], is_prime) # использовал при отладке
        if is_prime == True and j == i:
            primes.append(numbers[i])
        elif is_prime == True and j != i:
            not_primes.append(numbers[i])
            break

print(f'Prime: {primes}')
print(f'Not Prime: {not_primes}')