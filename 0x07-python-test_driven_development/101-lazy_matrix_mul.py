#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""The program defines a matrix multiplication function using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """The program returns the multiplication of two matrices

    Args:
        m_a (list of lists of ints/floats): The 1st matrix
        m_b (list of lists of ints/floats): The 2nd matrix
    """

    return (np.matmul(m_a, m_b))
