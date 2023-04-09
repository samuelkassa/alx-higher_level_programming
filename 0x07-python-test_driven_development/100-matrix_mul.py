#!/usr/bin/python3
"""Defines the multiplication of two matrices"""



def matrix_mul(m_a, m_b):
    """Multiplies two matrices to produce one matrix
    Args:
        m_a (a list of lists of integers or floats): the first matrix
        m_b (a list of lists of integers or floating points): The second matrix

    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints / floats
        TypeError: If either m_a or m_b is []
        TypeError: If either m_a or m_b has different sized rows
        ValueError: If m_a and m_b can not be multiplied

    Returns:
        A new matrix representing the multiplication of m_a and m_b
    """
    
    if m_a == [] or m_a == [[]]:
        raise TypeError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise TypeError("m_b can't be empty")
    
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
            for ele in [num for row in m_a for num in row]):
        raise ValueError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
            for ele in [num for row in m_b for num in row]):
        raise ValueError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all (len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    invert_b = []
    for row in range(len(m_b[0])):
        new_row = []
        for col in range(len(m_b)):
            new_row.append(m_b[col][row])
        invert_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in invert_b:
            product = 0
            for i in range(len(invert_b[0])):
                product += row[i] * col[i]
            new_row.append(product)
        new_matrix.append(nw_row)
    return new_matrix
