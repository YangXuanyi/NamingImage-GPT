import sys
from PyQt5 import QtWidgets
from GUI.MainGUI_v2 import Ui_MainWindow
from GUI.Controller import Controller


if __name__ == '__main__':
    # 创建一个应用程序对象
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()               #接入软件UI界面
    window = Controller(window)            #将UI界面接入功能函数,完成软件实例化
    window.show()
    # 运行应用程序的主事件循环
    sys.exit(app.exec_())