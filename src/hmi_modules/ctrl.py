#!/usr/bin/env python3
import rospy
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from std_msgs.msg import String

from geometry_msgs.msg import Twist


class Ui_ControlWindow(QtWidgets.QWidget):
    quitted = QtCore.pyqtSignal()

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.__setup_timer()

        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.cmdvel = Twist()

        self.testpub = rospy.Publisher('hmilog', String, queue_size=10)
        self.logmsg = String()

        # Pause Button
        self.myPause = QtWidgets.QPushButton(self)
        self.myPause.setGeometry(QtCore.QRect(490, 240, 261, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.myPause.setFont(font)
        self.myPause.setObjectName("myPause")

        # Button to quit widget
        self.myQuit = QtWidgets.QPushButton(self)
        self.myQuit.setGeometry(QtCore.QRect(0, 0, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        quit_icon = QtGui.QIcon()
        quit_icon.addPixmap(QtGui.QPixmap(":/newicon/icons/exit.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.myQuit.setIcon(quit_icon)
        self.myQuit.setIconSize(QtCore.QSize(125, 125))
        self.myQuit.setObjectName("myQuit")

        # Button to move AMD-R forward
        self.myForward = QtWidgets.QPushButton(self)
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

        # Button to move AMD-R backward
        self.myBackward = QtWidgets.QPushButton(self)
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

        # Button to move AMD-R right
        self.myRight = QtWidgets.QPushButton(self)
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

        # Button to move AMD-R right
        self.myLeft = QtWidgets.QPushButton(self)
        self.myLeft.setGeometry(QtCore.QRect(60, 240, 341, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.myLeft.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newicon/icons/left.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.myLeft.setIcon(icon5)
        self.myLeft.setIconSize(QtCore.QSize(175, 175))
        self.myLeft.setObjectName("myLeft")

        # Signal connection when buttons are clicked
        self.myPause.clicked.connect(self.pause)
        self.myQuit.clicked.connect(self.quit)
        self.myForward.pressed.connect(self.forward)
        self.myBackward.pressed.connect(self.backward)
        self.myLeft.pressed.connect(self.left)
        self.myRight.pressed.connect(self.right)

        # Signal connection when buttons are released
        self.myForward.released.connect(self.pause)
        self.myBackward.released.connect(self.pause)
        self.myLeft.released.connect(self.pause)
        self.myRight.released.connect(self.pause)

    def forward_timeout(self):
        """Timer timeout to countinously move AMD-R forward when button is held down."""
        self.cmdvel.linear.x = -0.15
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)
        self.testpub.publish("yaaay")

    def backward_timeout(self):
        """Timer timeout to countinously move AMD-R backward when button is held down."""
        self.cmdvel.linear.x = 0.15
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)

    def left_timeout(self):
        """Timer timeout to countinously move AMD-R left when button is held down."""
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = -0.25
        self.pub.publish(self.cmdvel)

    def right_timeout(self):
        """Timer timeout to countinously move AMD-R right when button is held down."""
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0.25
        self.pub.publish(self.cmdvel)

    @QtCore.pyqtSlot()
    def quit(self):
        self.quitted.emit()

    @QtCore.pyqtSlot()
    def forward(self):
        """Starts timer to move AMD-R forward."""
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)
        self.forward_timer.start(100)

    @QtCore.pyqtSlot()
    def backward(self):
        """Starts timer to move AMD-R backward."""
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)
        self.backward_timer.start(100)

    @QtCore.pyqtSlot()
    def left(self):
        """Starts timer to move AMD-R left."""
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)
        self.left_timer.start(100)

    @QtCore.pyqtSlot()
    def right(self):
        """Starts timer to move AMD-R right."""
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)
        self.right_timer.start(100)

    @QtCore.pyqtSlot()
    def pause(self):
        """Function to stop all the timers/movement when button are released."""
        self.forward_timer.stop()
        self.backward_timer.stop()
        self.left_timer.stop()
        self.right_timer.stop()
        self.cmdvel.linear.x = 0
        self.cmdvel.linear.y = 0
        self.cmdvel.linear.z = 0
        self.cmdvel.angular.x = 0
        self.cmdvel.angular.y = 0
        self.cmdvel.angular.z = 0
        self.pub.publish(self.cmdvel)

    def __setup_timer(self):
        self.forward_timer = QtCore.QTimer()
        self.backward_timer = QtCore.QTimer()
        self.left_timer = QtCore.QTimer()
        self.right_timer = QtCore.QTimer()

        self.forward_timer.timeout.connect(self.forward_timeout)
        self.backward_timer.timeout.connect(self.backward_timeout)
        self.left_timer.timeout.connect(self.left_timeout)
        self.right_timer.timeout.connect(self.right_timeout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ControlWindow = QtWidgets.QMainWindow()
    ui = Ui_ControlWindow()
    ui.setupUi(ControlWindow)
    ControlWindow.show()

    sys.exit(app.exec_())
