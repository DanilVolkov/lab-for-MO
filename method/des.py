from PyQt5.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout, QLabel,
                             QLayout, QLineEdit, QPushButton,
                             QSizePolicy, QStatusBar, QVBoxLayout, QWidget)


class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 575)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred,
                                 QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().
                                     hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(810, 575))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum,
                                  QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.
                                      sizePolicy().hasHeightForWidth())
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
        sizePolicy.setHeightForWidth(self.widget.
                                     sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(550, 550))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.
                                              SetDefaultConstraint)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(120, 30))
        self.lineEdit.setMaximumSize(QSize(500, 16777215))

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leftx1 = QLineEdit(self.centralwidget)
        self.leftx1.setObjectName(u"leftx1")
        self.leftx1.setMinimumSize(QSize(30, 0))
        self.leftx1.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.leftx1, 0, Qt.AlignmentFlag.
                                          AlignRight)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 30))
        self.label_2.setMaximumSize(QSize(120, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2, 0, Qt.AlignmentFlag.
                                          AlignHCenter)

        self.rightx1 = QLineEdit(self.centralwidget)
        self.rightx1.setObjectName(u"rightx1")
        self.rightx1.setMinimumSize(QSize(30, 0))
        self.rightx1.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.rightx1, 0, Qt.AlignmentFlag.
                                          AlignLeft)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.leftx2 = QLineEdit(self.centralwidget)
        self.leftx2.setObjectName(u"leftx2")
        self.leftx2.setMinimumSize(QSize(30, 0))
        self.leftx2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.leftx2, 0, Qt.AlignmentFlag.
                                          AlignRight)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 30))
        self.label_3.setMaximumSize(QSize(120, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3, 0, Qt.AlignmentFlag.
                                          AlignHCenter)

        self.rightx2 = QLineEdit(self.centralwidget)
        self.rightx2.setObjectName(u"rightx2")
        self.rightx2.setMinimumSize(QSize(30, 0))
        self.rightx2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.rightx2, 0, Qt.AlignmentFlag.
                                          AlignLeft)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_2, 0,
                                          Qt.AlignmentFlag.AlignLeft)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 30))
        self.pushButton.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 150))
        self.label.setMaximumSize(QSize(500, 500))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(170, 30))

        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().
                                      hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setMinimumSize(QSize(30, 30))
        self.lineEdit_2.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.lineEdit_2, 0,
                                        Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(250, 250))
        self.widget_2.setMaximumSize(QSize(250, 250))
        self.widget_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.widget_2)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u041c\u0435"
                                                             "\u0442\u043e"
                                                             "\u0434 \u041d"
                                                             "\u0435\u043b"
                                                             "\u0434\u0435"
                                                             "\u0440\u0430-"
                                                             "\u041c\u0438"
                                                             "\u0434\u0430",
                                                             None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"< x1 <", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"< x2 <", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u041f\u0440"
                                                             "\u0435\u043a"
                                                             "\u0440\u0430"
                                                             "\u0442\u0438"
                                                             "\u0442\u044c",
                                                             None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u0420\u0430"
                                                           "\u0441\u0441"
                                                           "\u0447\u0438"
                                                           "\u0442\u0430"
                                                           "\u0442\u044c",
                                                           None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u0422\u0443\u0442 "
                                                      "\u0431\u0443\u0434"
                                                      "\u0443\u0442 \u0440"
                                                      "\u0435\u0437\u0443"
                                                      "\u043b\u044c\u0442"
                                                      "\u0430\u0442\u044b "
                                                      "\u0440\u0430\u0441"
                                                      "\u0447\u0435\u0442"
                                                      "\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0421\u043a\u043e"
                                                        "\u0440\u0441\u0442"
                                                        "\u044c \u0441\u0438"
                                                        "\u043c\u0443\u043b"
                                                        "\u044f\u0446\u0438"
                                                        "\u0438 (\u0448\u0430"
                                                        "\u0433/\u0441)",
                                                        None))
    # retranslateUi
