#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A client for the discovery and vizualization of data conforming to UGRID conventions.

Ugrid conventions: https://github.com/ugrid-conventions/ugrid-conventions
"""

import sys
from PyQt4 import QtGui, QtCore


class UgridViz(QtGui.QWidget):

    def __init__(self):
        super(UgridViz, self).__init__()
        self.initGui()

    def initGui(self):
        self.dimension()
        self.decorate()
        self.show()
        return

    def dimension(self):
        ag = QtGui.QDesktopWidget().availableGeometry()
        self.resize(3 * ag.width() / 4, 3 * ag.height() / 4)
        fg = self.frameGeometry()
        fg.moveCenter(ag.center())
        self.move(fg.topLeft())
        return

    def decorate(self):
        self.setWindowTitle('UgridViz')
        return

    def closeEvent(self, event):
        event.accept()
        return


def main():
    QtCore.pyqtRemoveInputHook()
    app = QtGui.QApplication(sys.argv)
    ugridviz = UgridViz()
    print app.exec_()

if __name__ == '__main__':
    main()