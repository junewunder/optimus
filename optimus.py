# CHANGE HERE
string = '1337'


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):   # only odd numbers
        if n % i == 0:
            return False

    return True

numbers = {
    '0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7,
    '8' : 8, '9' : 9, 'a' : 10, 'b' : 11, 'c' : 12, 'd' : 13, 'e' : 14,
    'f' : 15,'g' : 16,'h' : 17,'i' : 18,'j' : 19,'k' : 20,
    'l' : 21, 'm' : 22, 'o' : 23, 'p' : 24, 'q' : 25, 'r' : 26, 's' : 27,
    't' : 28, 'u' : 29, 'v' : 30, 'w' : 31, 's' : 32, 'y' : 33, 'z' : 34
}


string = string[::-1]

# TODO: is the bee movie script prime????

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
