def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    d = a
    if d < b:
        d = b
    if d < c:
        d = c
    d = c
    if d > b:
        d = b
    if d > a:
        d = a
    return d

print(main(15, 48, 14))


 