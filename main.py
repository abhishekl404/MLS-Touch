from PyQt4 import QtGui
import sys # to pass argv to QApplication

import layout # Holds MainWindow and all layout related details

class TouchApp(QtGui.QMainWindow, layout.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)


def main():
	app = QtGui.QApplication(sys.argv)
	screen = TouchApp()
	screen.show()
	app.exec()

if __name__ == '__main__':
	main()