""" Python module to validate if a string is palindrome
How to validate types:
mypy <nombre-archivo>.py --check-untyped-defs """


def is_palindorme(string: str) -> bool:
    """ Returns true or false depending if string is or not palindrome """
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    """ Main function """
    print(is_palindorme('Anita lava la tina'))

if __name__ == '__main__':
    run()
