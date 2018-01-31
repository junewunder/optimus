# CHANGE HERE
string = 'jacob'


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):   # only odd numbers
        if n % i == 0:
            return False

    return True


numbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14,
    'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20,
    'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27,
    's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35
}

string = string[::-1]

highestbase = -1
for l in string:
    if numbers[l] > highestbase:
        highestbase = numbers[l] + 1

for base in range(highestbase, 10000):
    total = 0
    for i, l in enumerate(string):
        total += numbers[l] * base ** i

    if is_prime(total):
        print(string[::-1], 'is prime in base', base, 'equal to', total)
        break
