def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    number = s[ : : ]
    if int(s) == int(number):
        number = number
    else:
        number = -1

    return number

print(main('12343456565'))