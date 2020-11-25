# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcu.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 564)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 564))
        Dialog.setMaximumSize(QtCore.QSize(400, 564))
        Dialog.setWindowOpacity(1.0)
        Dialog.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_equal = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_equal.sizePolicy().hasHeightForWidth())
        self.pushButton_equal.setSizePolicy(sizePolicy)
        self.pushButton_equal.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_equal.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.gridLayout.addWidget(self.pushButton_equal, 6, 3, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)
        self.pushButton_0.setMinimumSize(QtCore.QSize(181, 88))
        self.pushButton_0.setMaximumSize(QtCore.QSize(200, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 6, 0, 1, 2)
        self.pushButton_point = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_point.sizePolicy().hasHeightForWidth())
        self.pushButton_point.setSizePolicy(sizePolicy)
        self.pushButton_point.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_point.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_point.setFont(font)
        self.pushButton_point.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_point.setObjectName("pushButton_point")
        self.gridLayout.addWidget(self.pushButton_point, 6, 2, 1, 1)
        self.pushButton_percent = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_percent.sizePolicy().hasHeightForWidth())
        self.pushButton_percent.setSizePolicy(sizePolicy)
        self.pushButton_percent.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_percent.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_percent.setFont(font)
        self.pushButton_percent.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.gridLayout.addWidget(self.pushButton_percent, 2, 2, 1, 1)
        self.pushButton_plusMinus = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_plusMinus.sizePolicy().hasHeightForWidth())
        self.pushButton_plusMinus.setSizePolicy(sizePolicy)
        self.pushButton_plusMinus.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_plusMinus.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_plusMinus.setFont(font)
        self.pushButton_plusMinus.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_plusMinus.setObjectName("pushButton_plusMinus")
        self.gridLayout.addWidget(self.pushButton_plusMinus, 2, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_8.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_9.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 3, 2, 1, 1)
        self.pushButton_multiply = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_multiply.sizePolicy().hasHeightForWidth())
        self.pushButton_multiply.setSizePolicy(sizePolicy)
        self.pushButton_multiply.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_multiply.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_multiply.setFont(font)
        self.pushButton_multiply.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.gridLayout.addWidget(self.pushButton_multiply, 3, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_7.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)
        self.pushButton_divide = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_divide.sizePolicy().hasHeightForWidth())
        self.pushButton_divide.setSizePolicy(sizePolicy)
        self.pushButton_divide.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_divide.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_divide.setFont(font)
        self.pushButton_divide.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_divide.setCheckable(True)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.gridLayout.addWidget(self.pushButton_divide, 2, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_4.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_5.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_6.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 4, 2, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_1.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 5, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_2.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 1, 1, 1)
        self.pushButton_minus = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_minus.sizePolicy().hasHeightForWidth())
        self.pushButton_minus.setSizePolicy(sizePolicy)
        self.pushButton_minus.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_minus.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_minus.setCheckable(True)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.gridLayout.addWidget(self.pushButton_minus, 4, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_3.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 5, 2, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_plus.sizePolicy().hasHeightForWidth())
        self.pushButton_plus.setSizePolicy(sizePolicy)
        self.pushButton_plus.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButton_plus.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_plus.setCheckable(True)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout.addWidget(self.pushButton_plus, 5, 3, 1, 1)
        self.sub_label = QtWidgets.QLabel(Dialog)
        self.sub_label.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sub_label.setFont(font)
        self.sub_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sub_label.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"}\n"
"")
        self.sub_label.setText("")
        self.sub_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sub_label.setIndent(4)
        self.sub_label.setObjectName("sub_label")
        self.gridLayout.addWidget(self.sub_label, 0, 0, 1, 4)
        self.main_label = QtWidgets.QLabel(Dialog)
        self.main_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_label.sizePolicy().hasHeightForWidth())
        self.main_label.setSizePolicy(sizePolicy)
        self.main_label.setMinimumSize(QtCore.QSize(400, 61))
        self.main_label.setMaximumSize(QtCore.QSize(400, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.main_label.setFont(font)
        self.main_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_label.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"}\n"
"")
        self.main_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.main_label.setIndent(15)
        self.main_label.setObjectName("main_label")
        self.gridLayout.addWidget(self.main_label, 1, 0, 1, 4)
        self.pushButtonClear = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClear.sizePolicy().hasHeightForWidth())
        self.pushButtonClear.setSizePolicy(sizePolicy)
        self.pushButtonClear.setMinimumSize(QtCore.QSize(94, 88))
        self.pushButtonClear.setMaximumSize(QtCore.QSize(94, 88))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.gridLayout.addWidget(self.pushButtonClear, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.pushButton_equal.setText(_translate("Dialog", "="))
        self.pushButton_0.setText(_translate("Dialog", "0"))
        self.pushButton_point.setText(_translate("Dialog", "."))
        self.pushButton_percent.setText(_translate("Dialog", "%"))
        self.pushButton_plusMinus.setText(_translate("Dialog", "+/-"))
        self.pushButton_8.setText(_translate("Dialog", "8"))
        self.pushButton_9.setText(_translate("Dialog", "9"))
        self.pushButton_multiply.setText(_translate("Dialog", "*"))
        self.pushButton_7.setText(_translate("Dialog", "7"))
        self.pushButton_divide.setText(_translate("Dialog", "÷"))
        self.pushButton_4.setText(_translate("Dialog", "4"))
        self.pushButton_5.setText(_translate("Dialog", "5"))
        self.pushButton_6.setText(_translate("Dialog", "6"))
        self.pushButton_1.setText(_translate("Dialog", "1"))
        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_minus.setText(_translate("Dialog", "-"))
        self.pushButton_3.setText(_translate("Dialog", "3"))
        self.pushButton_plus.setText(_translate("Dialog", "+"))
        self.main_label.setText(_translate("Dialog", "0"))
        self.pushButtonClear.setText(_translate("Dialog", "C"))
