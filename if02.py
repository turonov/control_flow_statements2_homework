def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a > b:
        if a > c:
            return b
        else: return c
    if b > a:
        if b > c:
            return a
        else: return c   
    return

print(main(54, 14, 25))    