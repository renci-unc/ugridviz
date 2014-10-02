#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A client for the discovery and vizualization of data conforming to UGRID conventions.

Ugrid conventions: https://github.com/ugrid-conventions/ugrid-conventions
"""

import sys
from PyQt4 import QtGui, QtCore


class UgridViz(QtGui.QWidget):
    """
    The main display widget.
    """
    def __init__(self):
        """
        Override parent's special init method.
        """
        super(UgridViz, self).__init__()
        self.initGui()

    def initGui(self):
        """
        Consolidate initialization of the widget.
        """
        self.dimension()
        self.layOut()
        self.decorate()
        self.show()
        return

    def dimension(self):
        """
        Dimension and position the widget.
        """
        ag = QtGui.QDesktopWidget().availableGeometry()
        self.resize(3 * ag.width() / 4, 3 * ag.height() / 4)
        fg = self.frameGeometry()
        fg.moveCenter(ag.center())
        self.move(fg.topLeft())
        return

    def layOut(self):
        """
        Layout the widget container.
        """
        fg = self.frameGeometry()
        viewmap = QtGui.QPixmap(fg.width(), fg.height())
        viewmap.fill()
        viewer = QtGui.QLabel(self)
        viewer.setPixmap(viewmap)
        urlLabel = QtGui.QLabel("URL:")
        urlEdit = QtGui.QLineEdit(self)
        urlButton = QtGui.QPushButton("Load")
        urlBox = QtGui.QHBoxLayout()
        urlBox.addWidget(urlLabel)
        urlBox.addWidget(urlEdit, 1)
        urlBox.addWidget(urlButton)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(viewer, 1, QtCore.Qt.AlignTop)
        vbox.addLayout(urlBox)
        self.setLayout(vbox)
        return

    def decorate(self):
        """
        Decorate the window with the usual graphic elements.
        """
        self.setWindowTitle('UgridViz')
        return

    def closeEvent(self, event):
        """
        Intercept exiting the application
        """
        event.accept()
        return


def main():
    """
    Consolidate running the application.
    """
    QtCore.pyqtRemoveInputHook()
    app = QtGui.QApplication(sys.argv)
    ugridviz = UgridViz()
    print app.exec_()

if __name__ == '__main__':
    main()