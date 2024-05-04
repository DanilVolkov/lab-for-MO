# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maindSdIvV.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 575)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(810, 575))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(550, 550))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(120, 30))
        self.lineEdit.setMaximumSize(QSize(500, 16777215))

        self.verticalLayout.addWidget(self.lineEdit, 0, Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leftx1 = QLineEdit(self.centralwidget)
        self.leftx1.setObjectName(u"leftx1")
        self.leftx1.setMinimumSize(QSize(30, 0))
        self.leftx1.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.leftx1, 0, Qt.AlignmentFlag.AlignRight)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 30))
        self.label_2.setMaximumSize(QSize(120, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.rightx1 = QLineEdit(self.centralwidget)
        self.rightx1.setObjectName(u"rightx1")
        self.rightx1.setMinimumSize(QSize(30, 0))
        self.rightx1.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.rightx1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.leftx2 = QLineEdit(self.centralwidget)
        self.leftx2.setObjectName(u"leftx2")
        self.leftx2.setMinimumSize(QSize(30, 0))
        self.leftx2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.leftx2, 0, Qt.AlignmentFlag.AlignRight)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 30))
        self.label_3.setMaximumSize(QSize(120, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.rightx2 = QLineEdit(self.centralwidget)
        self.rightx2.setObjectName(u"rightx2")
        self.rightx2.setMinimumSize(QSize(30, 0))
        self.rightx2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.rightx2, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setMaximumSize(QSize(500, 16777215))

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(170, 170))
        self.label.setMaximumSize(QSize(500, 500))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(250, 250))
        self.widget_2.setMaximumSize(QSize(250, 250))
        self.widget_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.setStretch(5, 5)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 5)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u041d\u0435\u043b\u0434\u0435\u0440\u0430-\u041c\u0438\u0434\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"< x1 <", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"< x2 <", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0442 \u0431\u0443\u0434\u0443\u0442 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0440\u0430\u0441\u0447\u0435\u0442\u0430", None))
    # retranslateUi

