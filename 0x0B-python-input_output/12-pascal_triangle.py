#!/usr/bin/python3


def pascal_triangle(n):
    """ Function that returns the pascal triangle

    Args:
        n: number of lines

    Returns:
         Empty list: if n <= 0 otherwise pascal triangle

    """
    if n <= 0:
        return ([])

    pascal_t = [[1]]
    for i in range(1, n):
        row = [1]
        prev = pascal_t[i - 1]
        for j in range(len(prev)):
                new = prev[j] + prev[j + 1] if j != len(prev) - 1 else 1
                row.append(new)

        pascal_t.append(row)

    return pascal_t
