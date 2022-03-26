import numpy as np


def calculate(number_list):
    if len(number_list) < 9:
        raise ValueError("List must contain nine numbers.")
    calculations = {}

    np_matrix = np.reshape(number_list, (3, 3))
    calculations['mean'] = [np.mean(np_matrix, axis=0).tolist(), np.mean(np_matrix, axis=1).tolist(),
                            np.mean(np_matrix).tolist()]
    calculations['variance'] = [np.var(np_matrix, axis=0).tolist(), np.var(np_matrix, axis=1).tolist(),
                                np.var(np_matrix).tolist()]
    calculations['standard deviation'] = [np.std(np_matrix, axis=0).tolist(), np.std(np_matrix, axis=1).tolist(),
                                          np.std(np_matrix).tolist()]
    calculations['max'] = [np.amax(np_matrix, axis=0).tolist(), np.amax(np_matrix, axis=1).tolist(),
                           np.amax(np_matrix).tolist()]
    calculations['min'] = [np.amin(np_matrix, axis=0).tolist(), np.amin(np_matrix, axis=1).tolist(),
                           np.amin(np_matrix).tolist()]
    calculations['sum'] = [np.sum(np_matrix, axis=0).tolist(), np.sum(np_matrix, axis=1).tolist(),
                           np.sum(np_matrix).tolist()]

    return calculations
