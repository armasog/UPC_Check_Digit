import unittest

'''
Rules to generate the 12th digit (check digit) of UPC bar codes

Sum the digits at odd-numbered positions (1st, 3rd, 5th, ..., 11th). If you use 0-based indexing, this is the even-numbered positions (0th, 2nd, 4th, ... 10th).

Multiply the result from step 1 by 3.

Take the sum of digits at even-numbered positions (2nd, 4th, 6th, ..., 10th) in the original number, and add this sum to the result from step 2.

Find the result from step 3 modulo 10 (i.e. the remainder, when divided by 10) and call it M.

If M is 0, then the check digit is 0; otherwise the check digit is 10 - M.

'''

class TestSuite(unittest.TestCase):
    def test_check_digit_generator(self):
        assert check_digit_generator('03600029145') == 2
    def test_upc_checker(self):
        assert upc_checker('036000291452') == True and upc_checker('036000291453') == False


def check_digit_generator(first_11_digits):
    # Argument first_11_digits expected as string because Python 3 generates a syntax error when int values are passed
    # with leading zeroes
    odd_positions = sum([int(x) for x in first_11_digits[0::2]])
    even_positions = sum([int(x) for x in first_11_digits[1::2]])
    m = (odd_positions * 3 + even_positions) % 10
    return m if m == 0 else 10 - m

def upc_checker(upc):
    # Argument upc expected as string because Python 3 generates a syntax error when int values are passed with leading
    # zeroes
    check_digit = int(upc[11])
    return check_digit_generator(upc[:11]) == check_digit