# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ############################################################################*/
"""Tests that the different implementation of opencl (cpp, opencl) are
    accessible
"""

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "05/05/2017"

import unittest
from silx.image import medianfilter
import numpy
try:
    import scipy
    import scipy.misc
    import scipy.ndimage
except:
    scipy = None

from silx.opencl.common import ocl


@unittest.skipUnless(scipy, "scipy not available")
class TestMedianFilterEngines(unittest.TestCase):
    """Make sure we have access to all the different implementation of
    median filter from image medfilt"""

    if hasattr(scipy.misc, 'ascent'):
        IMG = scipy.misc.ascent()
    else:
        IMG = scipy.misc.lena()

    KERNEL = (1, 1)

    def testCppMedFilt2d(self):
        """test cpp engine for medfilt2d"""
        res = medianfilter.medfilt2d(
            image=TestMedianFilterEngines.IMG,
            kernel_size=TestMedianFilterEngines.KERNEL,
            conditional=False,
            engine='cpp')
        self.assertTrue(numpy.array_equal(res, TestMedianFilterEngines.IMG))

    @unittest.skipUnless(ocl, "PyOpenCl is missing")
    def testOpenCLMedFilt2d(self):
        """test cpp engine for medfilt2d"""
        res = medianfilter.medfilt2d(
            image=TestMedianFilterEngines.IMG,
            kernel_size=TestMedianFilterEngines.KERNEL,
            conditional=False,
            engine='opencl')
        self.assertTrue(numpy.array_equal(res, TestMedianFilterEngines.IMG))


def suite():
    test_suite = unittest.TestSuite()
    for testClass in (TestMedianFilterEngines, ):
        test_suite.addTest(
            unittest.defaultTestLoader.loadTestsFromTestCase(testClass))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
