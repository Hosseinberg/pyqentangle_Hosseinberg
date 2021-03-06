
import unittest2

import numpy as np
from scipy.integrate import quad

import pyqentangle

class testContinuousEntanglement(unittest2.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEntangledOscillators(self):
        fcn = lambda x1, x2: np.exp(-((0.5 * (x1 + x2)) ** 2)) * np.exp(-(x1 - x2) ** 2) * np.sqrt(2. / np.pi)
        decompositions = pyqentangle.continuous_schmidt_decomposition(fcn, -10., 10., -10., 10., keep=10)
        eigenvalues = list(map(lambda item: item[0], decompositions))
        self.assertAlmostEqual(eigenvalues[0], 0.888888889)
        self.assertAlmostEqual(eigenvalues[1], 0.098765432)

        norm1, err1 = quad(lambda x1: np.real(np.conjugate(decompositions[0][1](np.array([x1])))*decompositions[0][1](np.array([x1]))), -10, 10)
        norm2, err2 = quad(lambda x2: np.real(np.conjugate(decompositions[0][2](np.array([x2])))*decompositions[0][2](np.array([x2]))), -10, 10)
        print(norm1, err1)
        print(norm2, err2)
        # self.assertAlmostEqual(norm1, 1., err1)
        # self.assertAlmostEqual(norm2, 1., err2)

    def testInterpolation(self):
        xarray = np.array([0., 1., 2.])
        yarray = np.array([0., 1., 4.])
        self.assertAlmostEqual(pyqentangle.continuous.numerical_continuous_interpolation(xarray, yarray, 0.5), 0.5)
        self.assertAlmostEqual(pyqentangle.continuous.numerical_continuous_interpolation(xarray, yarray, 1.5), 2.5)

if __name__ == '__main__':
    unittest2.main()