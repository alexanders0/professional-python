""" Module to validate if number is prime
How to validate types:
mypy <nombre-archivo>.py --check-untyped-defs """


def is_prime(number: int) -> bool:
    """ Returns true if number is prime, otherwise returns false """
    counter = 0

    for i in range(1, number + 1):
        if i in (1, number):
            continue
        if number % i == 0:
            counter += 1

    return not bool(counter)

def run():
    """ Main function """
    print(is_prime(11))

if __name__ == "__main__":
    run()
