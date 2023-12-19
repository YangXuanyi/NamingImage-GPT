'''
该文件主要实现为UI界面的各组件接入槽函数，实现控件功能
'''

from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QImage

class Controller(QMainWindow):
    def __init__(self, window):
        super(Controller, self).__init__()
        self.window = window
        self.window.setupUi(self)   #实例化UI界面中的操作元件
        self.window.pushButton.clicked.connect(self.button1_clicked)        #选取图像按钮
        self.window.pushButton_2.clicked.connect(self.button4_clicked)     #一键提取按钮
        self.window.pushButton_6.clicked.connect(self.button6_clicked)

    def button1_clicked(self):
        print("Button clicked from controller!")
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "", "", "(*.png *.jpg *.bmp)")
        print(image_path)
        #功能1: 展示当前正在处理的图像
        self.show_image_on_graphicsView(image_path)


    def button4_clicked(self):
        # 一键提取按钮对应功能函数
        ## 调用OFA和Chatgpt算法获取提取结果

        # 功能1：打印OFA提取结果
        content_txt = '图像内容1\n由OFA生成'
        self.print_image_content(content_txt)
        # 功能2：打印chatgpt命名结果
        naming_txt = '图像名称1\n由chatgpt生成'
        self.print_image_naming(naming_txt)

    def button6_clicked(self):
        #清空输入按钮，对应清空图像、两个富文本框、两个程序进度条
        #1 清空图像
        scene = QGraphicsScene()
        self.window.graphicsView.setScene(scene)
        scene.clear()
        #2 清空文本数据
        self.window.textBrowser_4.clear()
        self.window.textBrowser_2.clear()
        #3 清空进度条
        #####待完成


    def show_image_on_graphicsView(self, image_path):
        '''
        在QGraphicsScene控件上展示图像
        :param image_path:
        :return:
        '''
        scene = QGraphicsScene()
        view = QGraphicsView(scene)
        #获取当前控件的大小,并将图片缩放使其在控件中完全展示.
        # 注：图片调整大小是一次性的且不会因为拖拉窗口而进行大小自适应调整(因为拖拉产生的缩放并不会更新画布的size)
        # 控件的size只由MainGUI中的MainWindow.resize()决定，在当前设置参数下控件的大小为(640,480)
        current_size = view.size()
        image = QImage(image_path)
        if image.width() > current_size.width():
            scale = current_size.width() / image.width()
            image = image.scaled(int(current_size.width()),int(image.height()*scale))
        if image.height() > current_size.height():
            scale = current_size.height() / image.height()
            image = image.scaled(int(image.width()*scale),current_size.height())
        pixmap = QPixmap.fromImage(image)
        scene.addPixmap(pixmap)
        # 将场景设置给QGraphicsView
        self.window.graphicsView.setScene(scene)

    def print_image_content(self, content_txt):
        '''
        将算法提取出的图像内容打印至富文本框中textBrowser_4中
        :return:
        '''

        self.window.textBrowser_4.append(content_txt)

    def print_image_naming(self, naming_txt):
        '''
        将算法输出的图像名称打印至富文本框textBrowser_2中
        :param naming_txt:
        :return:
        '''
        self.window.textBrowser_2.append(naming_txt)