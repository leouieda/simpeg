# Copyright (c) 2013 SimPEG Developers.
# Distributed under the terms of the MIT License.
# SPDX-License-Identifier: MIT
# This code is part of the SimPEG project (https://simpeg.xyz)
import subprocess
import unittest
import os

import subprocess
import unittest
import os


class Doc_Test(unittest.TestCase):
    @property
    def path_to_docs(self):
        dirname, filename = os.path.split(os.path.abspath(__file__))
        return dirname.split(os.path.sep)[:-2] + ["docs"]

    def test_html(self):
        wd = os.getcwd()
        os.chdir(os.path.sep.join(self.path_to_docs))

        response = subprocess.run(["make", "html"])
        self.assertTrue(response.returncode == 0)
        # response = subprocess.call(["make", "html"], shell=True)  # Needed for local test on Windows
        # self.assertTrue(response == 0)

        os.chdir(wd)

    def test_linkcheck(self):
        wd = os.getcwd()
        os.chdir(os.path.sep.join(self.path_to_docs))

        response = subprocess.run(["make", "linkcheck"])
        print(response.returncode)
        self.assertTrue(response.returncode == 0)
        # response = subprocess.call(["make", "linkcheck"], shell=True)  # Needed for local test on Windows
        # print(response)
        # self.assertTrue(response == 0)

        os.chdir(wd)


if __name__ == "__main__":
    unittest.main()
