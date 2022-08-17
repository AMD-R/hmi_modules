#!/usr/bin/env python3
from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
import numpy


class QRDetector(QtWidgets.QWidget):
    """QRCode Detector widget.
    Parameters
    ----------
    Parent: QWidget = None
        Parent widget of the widget
    """
    detected: QtCore.pyqtBoundSignal = QtCore.pyqtSignal(str)
    started: QtCore.pyqtBoundSignal = QtCore.pyqtSignal(int)
    stopped: QtCore.pyqtBoundSignal = QtCore.pyqtSignal()

    def __init__(self, parent: QtWidgets.QWidget = None, start: bool = True):
        super().__init__(parent)
        # OpenCV variables
        self.camera: cv2.VideoCapture = cv2.VideoCapture()
        self.qr_reader: cv2.QRCodeDetector = cv2.QRCodeDetector()

        # Display
        layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self)
        self.image: QtWidgets.QLabel = QtWidgets.QLabel("No Feed", self)
        self.image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image)

        # Starting Capture
        if start:
            self.start()

    def timerEvent(self, event: QtCore.QTimerEvent) -> None:
        """Capture image and displaying it."""
        # Getting captured image
        _, img = self.camera.read()
        # Detect and decoding QR Code
        ret_qr, _, _ = self.qr_reader.detectAndDecode(img)
        # Setting Label
        img: numpy.ndarray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pixmap: QtGui.QImage = QtGui.QImage(img, img.shape[1], img.shape[0],
                                            QtGui.QImage.Format_RGB888)
        self.image.setPixmap(QtGui.QPixmap.fromImage(pixmap))

        # Emmiting dectected signal
        if ret_qr is not None:
            self.detected.emit(ret_qr)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """Resizing Capture Resolution when widget resizes."""
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.width())
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height())

    @QtCore.pyqtSlot()
    def start(self, index: int = 0, rate: int = 10) -> None:
        """Starts the QRCode Detection.
        Parameters
        ----------
        index: int
            id of the video capturing device to open.
        rate: int
            Refresh rate of camera capture in ms.
        """
        self.camera.open(index)
        self.timer: int = self.startTimer(rate)
        self.started.emit(index)

    @QtCore.pyqtSlot()
    def stop(self) -> None:
        """Stops the QRCode Detection."""
        self.camera.release()
        self.killTimer(self.timer)
        self.image.setText("No Feed")
        self.stopped.emit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QMainWindow()
    detector = QRDetector(window)
    window.setCentralWidget(detector)
    window.show()

    QtCore.QTimer.singleShot(5000, detector.stop)

    sys.exit(app.exec_())
