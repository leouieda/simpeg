# Copyright (c) 2013 SimPEG Developers.
# Distributed under the terms of the MIT License.
# SPDX-License-Identifier: MIT
# This code is part of the SimPEG project (https://simpeg.xyz)
import unittest

from SimPEG import Solver, SolverDiag, SolverCG, SolverLU
from discretize import TensorMesh
from SimPEG.utils import sdiag
import numpy as np
import scipy.sparse as sparse

TOLD = 1e-10
TOLI = 1e-3
numRHS = 5

np.random.seed(77)


def dotest(MYSOLVER, multi=False, A=None, **solverOpts):
    if A is None:
        h1 = np.ones(10) * 100.0
        h2 = np.ones(10) * 100.0
        h3 = np.ones(10) * 100.0

        h = [h1, h2, h3]

        M = TensorMesh(h)

        D = M.faceDiv
        G = -M.faceDiv.T
        Msig = M.getFaceInnerProduct()
        A = D * Msig * G
        A[-1, -1] *= 1 / M.vol[-1]  # remove the constant null space from the matrix
    else:
        M = TensorMesh([A.shape[0]])

    Ainv = MYSOLVER(A, **solverOpts)
    if multi:
        e = np.ones(M.nC)
    else:
        e = np.ones((M.nC, numRHS))
    rhs = A * e
    x = Ainv * rhs
    Ainv.clean()
    return np.linalg.norm(e - x, np.inf)


class TestSolver(unittest.TestCase):
    def test_direct_spsolve_1(self):
        self.assertLess(dotest(Solver, False), TOLD)

    def test_direct_spsolve_M(self):
        self.assertLess(dotest(Solver, True), TOLD)

    def test_direct_splu_1(self):
        self.assertLess(dotest(SolverLU, False), TOLD)

    def test_direct_splu_M(self):
        self.assertLess(dotest(SolverLU, True), TOLD)

    def test_iterative_diag_1(self):
        self.assertLess(
            dotest(SolverDiag, False, A=sdiag(np.random.rand(10) + 1.0)), TOLI
        )

    def test_iterative_diag_M(self):
        self.assertLess(
            dotest(SolverDiag, True, A=sdiag(np.random.rand(10) + 1.0)), TOLI
        )

    def test_iterative_cg_1(self):
        self.assertLess(dotest(SolverCG, False), TOLI)

    def test_iterative_cg_M(self):
        self.assertLess(dotest(SolverCG, True), TOLI)


if __name__ == "__main__":
    unittest.main()
