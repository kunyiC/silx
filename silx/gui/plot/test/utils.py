# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016 European Synchrotron Radiation Facility
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
# ###########################################################################*/
"""Basic tests for PlotWidget"""

__authors__ = ["T. Vincent"]
__license__ = "MIT"
__date__ = "01/09/2017"


import logging
import contextlib

from silx.gui.test.utils import TestCaseQt

from silx.gui import qt
from silx.gui.plot import PlotWidget
from silx.gui.plot.backends.BackendMatplotlib import BackendMatplotlibQt


logger = logging.getLogger(__name__)


class PlotWidgetTestCase(TestCaseQt):
    """Base class for tests of PlotWidget, not a TestCase in itself.

    plot attribute is the PlotWidget created for the test.
    """

    def __init__(self, methodName='runTest'):
        TestCaseQt.__init__(self, methodName=methodName)

    def _createPlot(self):
        return PlotWidget()

    def setUp(self):
        super(PlotWidgetTestCase, self).setUp()
        self.plot = self._createPlot()
        self.plot.show()
        self.plotAlive = True
        self.qWaitForWindowExposed(self.plot)
        TestCaseQt.mouseClick(self, self.plot, button=qt.Qt.LeftButton, pos=(0, 0))

    def __onPlotDestroyed(self):
        self.plotAlive = False

    def _waitForPlotClosed(self):
        self.plot.setAttribute(qt.Qt.WA_DeleteOnClose)
        self.plot.destroyed.connect(self.__onPlotDestroyed)
        self.plot.close()
        del self.plot
        for _ in range(100):
            if not self.plotAlive:
                break
            self.qWait(10)
        else:
            logger.error("Plot is still alive")

    def tearDown(self):
        self.qapp.processEvents()
        self._waitForPlotClosed()
        super(PlotWidgetTestCase, self).tearDown()

