numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for i2 in range(2, i):
        if i % i2 == 0:
            is_prime = False
            not_primes.append(i)
            break;
    if is_prime:
        primes.append(i)


print('Primes: ', primes)
print('Not primes: ', not_primes)