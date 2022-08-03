#!/usr/bin/env python3
from fileinput import close
import rospy
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from sympy import maximum

from fcntl import DN_DELETE
from pickle import TRUE
import sys
from threading import Timer
import time
from tokenize import String

from sympy import false, true
import rospy

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from geometry_msgs.msg import Twist
from std_msgs.msg import String


class Ui_ControlWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.timer = QTimer()
        self.timer_2 = QTimer()
        self.timer_3 = QTimer()
        self.timer_4 = QTimer()
        self.timer.timeout.connect(self.on_timeout)
        self.timer_2.timeout.connect(self.on_timeout_2)
        self.timer_3.timeout.connect(self.on_timeout_3)
        self.timer_4.timeout.connect(self.on_timeout_4)

    def setupUi(self, ControlWindow):

        self.ControlWindow = ControlWindow

        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.cmdvel = Twist()

        self.testpub = rospy.Publisher('hmilog', String, queue_size=10)
        self.logmsg = String()

        ControlWindow.setObjectName("ControlWindow")
        ControlWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(ControlWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.myPause = QtWidgets.QPushButton(self.centralwidget)
        self.myPause.setGeometry(QtCore.QRect(490, 240, 261, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.myPause.setFont(font)
        self.myPause.setObjectName("myPause")

        self.myPrev = QtWidgets.QPushButton(self.centralwidget)
        self.myPrev.setGeometry(QtCore.QRect(0, 0, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.myPrev.setFont(font)
        self.myPrev.setObjectName("myPause")

        self.myForward = QtWidgets.QPushButton(self.centralwidget)
        self.myForward.setGeometry(QtCore.QRect(450, 50, 341, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.myForward.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newicon/icons/front.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.myForward.setIcon(icon6)
        self.myForward.setIconSize(QtCore.QSize(125, 125))
        self.myForward.setObjectName("myForward")

        self.myBackward = QtWidgets.QPushButton(self.centralwidget)
        self.myBackward.setGeometry(QtCore.QRect(450, 430, 341, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.myBackward.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newicon/icons/back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.myBackward.setIcon(icon7)
        self.myBackward.setIconSize(QtCore.QSize(125, 125))
        self.myBackward.setObjectName("myBackward")

        self.myRight = QtWidgets.QPushButton(self.centralwidget)
        self.myRight.setGeometry(QtCore.QRect(840, 240, 341, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.myRight.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newicon/icons/right.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.myRight.setIcon(icon8)
        self.myRight.setIconSize(QtCore.QSize(175, 175))
        self.myRight.setObjectName("myRight")

        self.myLeft = QtWidgets.QPushButton(self.centralwidget)
        self.myLeft.setGeometry(QtCore.QRect(60, 240, 341, 161))

        self.myPause.clicked.connect(self.pause)
        self.myPrev.clicked.connect(self.prev)
        self.myForward.pressed.connect(self.forward)
        self.myBackward.pressed.connect(self.backward)
        self.myLeft.pressed.connect(self.left)
        self.myRight.pressed.connect(self.right)

        self.myForward.released.connect(self.pause)
        self.myBackward.released.connect(self.pause)
        self.myLeft.released.connect(self.pause)
        self.myRight.released.connect(self.pause)

        font = QtGui.QFont()
        font.setPointSize(20)
        self.myLeft.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newicon/icons/left.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.myLeft.setIcon(icon5)
        self.myLeft.setIconSize(QtCore.QSize(175, 175))
        self.myLeft.setObjectName("myLeft")
        ControlWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ControlWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        ControlWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ControlWindow)
        self.statusbar.setObjectName("statusbar")
        ControlWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ControlWindow)
        QtCore.QMetaObject.connectSlotsByName(ControlWindow)

    def on_timeout(self):
        self.timer.start(100)
        self.cmdvel.linear.x = -0.15
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)
        self.testpub.publish("yaaay")

    def on_timeout_2(self):
        self.timer_2.start(100)
        self.cmdvel.linear.x = 0.15
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)

    def on_timeout_3(self):
        self.timer_3.start(100)
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = -0.25
        self.pub.publish(self.cmdvel)

    def on_timeout_4(self):
        self.timer_4.start(100)
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0.25
        self.pub.publish(self.cmdvel)

    def prev(self):
        print("close")
        self.ControlWindow.close()

    def forward(self):
        self.timer.start(100)
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)
        self.timer.start(100)

    def backward(self):
        self.timer.start(100)
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)
        self.timer_2.start(100)

    def left(self):
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)
        self.timer_3.start(100)

    def right(self):
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)
        self.timer_4.start(100)

    def pause(self):
        self.timer.stop()
        self.timer_2.stop()
        self.timer_3.stop()
        self.timer_4.stop()
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)

    def retranslateUi(self, ControlWindow):
        _translate = QtCore.QCoreApplication.translate
        ControlWindow.setWindowTitle(_translate("ControlWindow", "MainWindow"))
        self.myPrev.setText(_translate("ControlWindow", "Back"))
        self.myPause.setText(_translate("ControlWindow", "PAUSE"))
        # self.myForward.setText(_translate("ControlWindow", "FORWARD"))
        # self.myBackward.setText(_translate("ControlWindow", "BACKWARD"))
        # self.myRight.setText(_translate("ControlWindow", "RIGHT"))
        # self.myLeft.setText(_translate("ControlWindow", "LEFT"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ControlWindow = QtWidgets.QMainWindow()
    ui = Ui_ControlWindow()
    ui.setupUi(ControlWindow)
    ControlWindow.show()

    sys.exit(app.exec_())
