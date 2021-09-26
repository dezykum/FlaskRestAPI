"""
Coding Challenge #2: Prime Numbers

Challenge:Take a input of a Integer and return a list of Prime Numbers

Example: If 17 was submitted, [2, 3, 5, 7, 11, 13, 17] should be returned.

"""

def prime_number(input_data):
    primes = []
    for num in range(0, input_data + 1):
        if num > 1:
            for i in range(2, num):
               if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

if __name__ == '__main__':
    print("Prime Numbers till 17 are :",prime_number(17))
    print("Prime Numbers till 100 are :",prime_number(100))