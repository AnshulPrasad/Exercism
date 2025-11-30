def equilateral(sides):
    return sides[0] == sides[1] == sides[2] != 0


def isosceles(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:  # non-zero sides
        return False
    if a + b >= c and b + c >= a and a + c >= b:  # valid triangles
        return a == b or b == c or c == a  # is isosceles
    else:
        return False


def scalene(sides):
    a, b, c = sides

    if a == 0 or b == 0 or c == 0:  # non-zero sides
        return False

    if a + b >= c and b + c >= a and a + c >= b:  # valid triangle
        return a != b and b != c and c != a  # is scalen
    else:
        return False

    return a != b and a != c and b != c
