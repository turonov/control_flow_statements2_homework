def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a == b:
        d = 0
    if a > b :
        d = a
    if b > a:
        d = b  
    return d

print(main(22, 22))    