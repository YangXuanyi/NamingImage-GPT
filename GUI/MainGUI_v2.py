# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainGUI_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_7.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_7.addWidget(self.line, 0, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_4.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout_6.addWidget(self.textBrowser_4, 1, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_6.addWidget(self.textBrowser_2, 3, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar_2.setFont(font)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_2.addWidget(self.progressBar_2, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 4, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 2)
        self.progressBar_5 = QtWidgets.QProgressBar(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar_5.setFont(font)
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setObjectName("progressBar_5")
        self.gridLayout.addWidget(self.progressBar_5, 1, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_14 = QtWidgets.QLabel(self.splitter_3)
        self.label_14.setObjectName("label_14")
        self.progressBar_6 = QtWidgets.QProgressBar(self.splitter_3)
        self.progressBar_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.progressBar_6.setProperty("value", 0)
        self.progressBar_6.setObjectName("progressBar_6")
        self.label_15 = QtWidgets.QLabel(self.splitter_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.splitter_3, 1, 0, 1, 1)
        self.splitter_4 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label_11 = QtWidgets.QLabel(self.splitter_4)
        self.label_11.setObjectName("label_11")
        self.progressBar_4 = QtWidgets.QProgressBar(self.splitter_4)
        self.progressBar_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.label_13 = QtWidgets.QLabel(self.splitter_4)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.splitter_4, 1, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 1, 2, 2, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setMinimumSize(QtCore.QSize(0, 300))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_4.addWidget(self.textBrowser_3, 2, 0, 1, 1)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_6.setMinimumSize(QtCore.QSize(0, 300))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.gridLayout_4.addWidget(self.textBrowser_6, 2, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.tab_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButton_7 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_7.setMinimumSize(QtCore.QSize(80, 60))
        self.pushButton_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_3.setMinimumSize(QtCore.QSize(80, 60))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_4.setMinimumSize(QtCore.QSize(80, 60))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_5.setMinimumSize(QtCore.QSize(80, 60))
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.splitter, 2, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_5.setMinimumSize(QtCore.QSize(700, 240))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout_5.addWidget(self.textBrowser_5, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_5)
        self.tabWidget.addTab(self.widget, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NamingImage-GPT"))
        self.label_6.setText(_translate("MainWindow", "图像命名结果："))
        self.label_7.setText(_translate("MainWindow", "运行进度："))
        self.pushButton.setText(_translate("MainWindow", "选取图像"))
        self.pushButton_6.setText(_translate("MainWindow", "清空输入"))
        self.pushButton_2.setText(_translate("MainWindow", "一键提取"))
        self.label_9.setText(_translate("MainWindow", "运行进度："))
        self.label_8.setText(_translate("MainWindow", "图像内容提取："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "单张图像"))
        self.label_14.setText(_translate("MainWindow", "内容提取处理进度："))
        self.label_15.setText(_translate("MainWindow", "结果预览："))
        self.label_11.setText(_translate("MainWindow", "图像命名处理进度："))
        self.label_13.setText(_translate("MainWindow", "结果预览："))
        self.pushButton_7.setText(_translate("MainWindow", "清空输入"))
        self.pushButton_3.setText(_translate("MainWindow", "选取文件"))
        self.pushButton_4.setText(_translate("MainWindow", "一键提取"))
        self.pushButton_5.setText(_translate("MainWindow", "导出数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "批量处理"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">软件说明</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">NamingImageGPT是一款基于ImageCaption和chatgpt的图像命名软件。该软件集成了OFA中文和ChatGPT，并通过PyQt5进行接口封装。它帮助用户以名称或句子的形式总结图像的主要内容。NamingImage GPT可以广泛用于为ImageCaption项目注释文本数据，并为文档工作者提供图像的快速命名方法。总之，它结合了image caption和chatgpt，在多模式GPT模型尚未开源的情况下，提供了一种新的开源多模式理解解决方案。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">具体使用教程见：https://github.com/YangXuanyi/NamingImage-GPT</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">声明：本软件只作为学习和交流使用！</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "关于我们"))
