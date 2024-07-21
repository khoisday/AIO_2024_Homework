import numpy as np


def compute_vector_length(vector):
    return np.linalg.norm(vector)


def compute_dot_vector(vector1, vector2):
    return np.dot(vector1, vector2)


def matrix_multi_vector(matrix, vector):
    return np.dot(matrix, vector)


def matrix_multi_matrix(matrix1, matrix2):
    return np.dot(matrix1, matrix2)


def inverse_matrix(matrix):
    return np.linalg.inv(matrix)
