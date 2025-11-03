# Helper functions to shorten test code in the notebook.
import numpy as np


def assert_array_equal(result, expected, tol=0):
    '''
    Raises AssertionError if an array "result" is not equal to the array "expected".
    If a tolerance tol is specified, compare approximate values using tol
    as relative tolerance.
    '''
    # Convert to NumPy array in case result is a list
    result_array = np.array(result)
    np.testing.assert_allclose(result_array, expected, atol=0, rtol=tol)


def assert_array_in(result, expected, tol=0):
    '''
    Raises AssertionError if an array "result" is not equal to any of the arrays
    in a list of arrays "expected".
    If a tolerance tol is specified, compare approximate values using tol
    as relative tolerance.
    '''
    # Convert to NumPy array in case result is a list
    result_array = np.array(result)

    # Test against all accepted expected arrays, return as soon as we have a match
    for test_array in expected:
        if np.allclose(result_array, test_array, atol=0, rtol=tol):
            return

    # No match
    raise AssertionError(f'Problem: {result} is not in the expected correct results:\n{np.array(expected)}')
