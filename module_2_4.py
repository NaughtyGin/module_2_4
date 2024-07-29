numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

is_prime = True
for i in numbers:
    if i == int(len(numbers)):  # ввёл условие, т.к. выдавало ошибку IndexError: list index out of range в строке 10
        break
    for j in numbers[:i]:
        is_prime = (int(numbers[i]) % int(numbers[j]) == 0)
        if is_prime == True and j == i:
            primes.append(numbers[i])
        elif is_prime == True and j != i:
            not_primes.append(numbers[i])
            break

print(f'Prime: {primes}')
print(f'Not Prime: {not_primes}')
