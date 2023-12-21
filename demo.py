import sys
from PyQt5 import QtWidgets
from GUI.MainGUI_v2 import Ui_MainWindow
from GUI.Controller import Controller
import json

if __name__ == '__main__':
    #读取需要自行配置的软件参数
    json_file = "./hyperparameters.json"
    with open(json_file, 'r') as file:
        data = json.load(file)
    hyperparameters = data["hyperparameters"]

    # 创建一个应用程序对象
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()               #接入软件UI界面
    window = Controller(window, hyperparameters)            #将UI界面接入功能函数,完成软件实例化
    window.show()
    # 运行应用程序的主事件循环
    sys.exit(app.exec_())