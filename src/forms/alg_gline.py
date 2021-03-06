# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *

from forms.inline_code_dialog import InlineCodeDialog
from forms.ui_alg_gline import Ui_AlgoGLineStmt
from util.code import try_parse
from util.widgets import center_widget

translate = QCoreApplication.translate


class AlgoGLineStmt(QDialog):
    def __init__(self, parent, origcode=("", "", "", "", '"red"')):
        super().__init__(parent)
        self.ui = Ui_AlgoGLineStmt()
        self.ui.setupUi(self)
        self.setFixedWidth(self.width())
        self.adjustSize()
        self.setFixedSize(self.size())
        self.ui.txtStartX.setText(origcode[0])
        self.ui.txtStartY.setText(origcode[1])
        self.ui.txtEndX.setText(origcode[2])
        self.ui.txtEndY.setText(origcode[3])
        self.ui.txtColor.setText(origcode[4])

        self.ui.btnCodeStartX.clicked.connect(lambda: self.click(self.ui.txtStartX))
        self.ui.btnCodeStartY.clicked.connect(lambda: self.click(self.ui.txtStartY))
        self.ui.btnCodeEndX.clicked.connect(lambda: self.click(self.ui.txtEndX))
        self.ui.btnCodeEndY.clicked.connect(lambda: self.click(self.ui.txtEndY))
        self.ui.btnCodeColor.clicked.connect(self.change_color)

        center_widget(self, parent)

    def done(self, res):
        if res == QDialog.Accepted:
            p = try_parse(self.ui.txtStartX.text(), self)

            if p is None:
                return

            self.f_start_x = p

            p = try_parse(self.ui.txtStartY.text(), self)

            if p is None:
                return

            self.f_start_y = p

            p = try_parse(self.ui.txtEndX.text(), self)

            if p is None:
                return

            self.f_end_x = p

            p = try_parse(self.ui.txtEndY.text(), self)

            if p is None:
                return

            self.f_end_y = p

            p = try_parse(self.ui.txtColor.text(), self)

            if p is None:
                return

            self.f_color = p

            self.ok = True

        super(AlgoGLineStmt, self).done(res)

    def click(self, wgt):
        dlg = InlineCodeDialog(self, wgt.text())
        if dlg.run():
            wgt.setText(dlg.value())

    def change_color(self, _):
        dlg = QColorDialog(self)
        current = self.ui.txtColor.text()
        if current[0] == current[-1] == '"':
            current = current[1:-1]
        dlg.setCurrentColor(QColor(current))
        if dlg.exec_():
            self.ui.txtColor.setText('"%s"' % dlg.currentColor().name())

    def run(self):
        return self.exec_() == QDialog.Accepted and self.ok
