'''
该文件主要实现为UI界面的各组件接入槽函数，实现控件功能
'''

from GPT.GPT_API import gpt_for_txt_SingleProcess, gpt_for_txt_BatchProcess
from OFA_Chinese.OFA_API import OFA_generate_SingleProcess, OFA_generate_BatchProcess
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
import os
import csv

class Controller(QMainWindow):
    def __init__(self, window, hyperparameters):
        super(Controller, self).__init__()
        self.para_dict = hyperparameters
        self.window = window
        self.window.setupUi(self)   #实例化UI界面中的操作元件
        ############################################################################################
        # 单张图像界面UI与功能函数交互
        ############################################################################################
        self.window.pushButton.clicked.connect(self.button1_clicked)        #选取图像按钮
        self.window.pushButton_2.clicked.connect(self.button2_clicked)     #一键提取按钮
        self.window.pushButton_6.clicked.connect(self.button6_clicked)     #清空输入按钮
        self.currentImagePath = ''
        ############################################################################################
        # 批量处理界面UI与功能函数交互
        ############################################################################################
        self.window.pushButton_7.clicked.connect(self.button7_clicked)    #清空输入按钮
        self.window.pushButton_3.clicked.connect(self.button3_clicked)    #选取文件按钮
        self.window.pushButton_4.clicked.connect(self.button4_clicked)  # 一键提取按钮
        self.window.pushButton_5.clicked.connect(self.button5_clicked)  # 导出数据按钮
        self.currentImagePathList = []
        self.Content_list = []       #OFA提取处的批量文本内容
        self.Naming_list = []        #Chatgpt赋予的图像名字

    def button1_clicked(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "", "", "(*.png *.jpg *.bmp)")
        self.currentImagePath = image_path
        #功能1: 展示当前正在处理的图像
        self.show_image_on_graphicsView(image_path)

    def button3_clicked(self):
        # 批量处理界面中的选取文件按钮
        image_paths = []  #文件夹中的所有图像的路径
        folder_path = QFileDialog.getExistingDirectory()
        if folder_path:
            for file_name in os.listdir(folder_path):
                # 判断文件是否为图片文件
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    # 构建图片的完整路径
                    image_path = os.path.join(folder_path, file_name)
                    image_paths.append(image_path)

        self.currentImagePathList = image_paths
        if len(image_paths) == 0:
            self.window.textBrowser_3.clear()
            self.window.textBrowser_3.append("Error! 软件检测到当前目录下没有图像，请重新选择(软件目前"
                                             "只支持.png. jpg .jepg形式的图像)")
            return None
        #在内容提取和命名文本框做标记，通知用户已完成图像选择
        message = '已读入路径: \n' + folder_path + '\n中的图像，请点击“一键提取”按钮进行内容提取和图像命名'
        self.window.textBrowser_3.append(message)
        return image_paths

    def button4_clicked(self):
        #批量处理界面中的一键提取功能
        #使用OFA提取所有图像的内容
        if len(self.currentImagePathList) == 0:
            self.window.textBrowser_3.clear()
            self.window.textBrowser_3.append("Error! 软件没有读到任何图像, "
                                             "当前只支持.png,.jpg和.jepg三种图像格式，请确保所选择的文件目录下有图像！")
            return None
        self.window.textBrowser_3.clear()
        self.window.textBrowser_6.clear()
        if self.currentImagePathList != '':
            self.window.progressBar_6.setValue(5)
            prompt = '图片描述了什么?'
            content_list = OFA_generate_BatchProcess(model_path=self.para_dict['OFA_model_path'],
                                                    image_path_list=self.currentImagePathList,
                                                    prompt=prompt,
                                                    textBrowser=self.window.textBrowser_3,
                                                    progressBar=self.window.progressBar_6)
        else:
            content_list = '未检测到所选目录下的图像,请重新选择'
        print(content_list)
        self.Content_list = content_list
        self.window.progressBar_6.setValue(100)
        QApplication.processEvents()

        #使用chatgpt给所有图像内容起名并时刻显示进度
        self.window.progressBar_4.setValue(0)
        naming_list = gpt_for_txt_BatchProcess(model=self.para_dict['gpt_model_name'],
                                              api_key=self.para_dict['gpt_api_key'],
                                              message_input_list=content_list,
                                              textBrowser=self.window.textBrowser_6,
                                              progressBar=self.window.progressBar_4)
        self.window.progressBar_4.setValue(100)
        print(naming_list)
        self.Naming_list = naming_list
        QApplication.processEvents()

    def button5_clicked(self):
        # 批量处理数据后导出数据到.csv文件
        # 指定CSV文件的路径
        csv_file = self.para_dict['output_file_path']

        if len(self.currentImagePathList) == 0:
            self.window.textBrowser_3.clear()
            self.window.textBrowser_3.append("Error! 系统没有正确读入图像所在文件夹路径，"
                                             "请在点击“选择文件”按钮后再启用此功能")
            QApplication.processEvents()
            return None
        if len(self.Content_list) == 0:
            self.window.textBrowser_3.clear()
            self.window.textBrowser_3.append("Error! 系统没有正确获取到内容提取结果，请重新"
                                            "“选择文件”后进行一键提取")
            print("sucess input")
            QApplication.processEvents()
            return None
        if len(self.Naming_list) == 0:
            self.window.textBrowser_3.clear()
            self.window.textBrowser_3.append("Error! 系统没有正确获取到图像命名结果，请确保断开"
                                             "外网连接以保证gpt顺利运行，同时重新选取文件并提取")
            QApplication.processEvents()
            return None

        # 将列表按列排列
        rows = zip(self.currentImagePathList, self.Content_list, self.Naming_list)
        # 写入CSV文件
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['image_path', 'image_contnet_by_OFA', 'imagee_name_by_gpt'])  # 写入表头
            writer.writerows(rows)  # 写入数据行

        self.window.textBrowser_3.clear()
        self.window.textBrowser_6.clear()
        self.window.textBrowser_3.append('数据已成功保存至软件根目录下的out.csv文件中，请注意查收！')

    def button2_clicked(self):
        # 一键提取按钮对应功能函数
        ## 调用OFA和Chatgpt算法获取提取结果
        if self.currentImagePath == '':
            self.window.textBrowser_4.clear()
            self.window.textBrowser_4.append("Error! 软件没有读入图像文件，请确保正确选取图像后再进行提取！")
            return None

        # 功能1：打印OFA提取结果并时刻显示进度
        self.window.progressBar_5.setValue(10)
        if self.currentImagePath != '':
            prompt = '图片描述了什么?'
            content_txt = OFA_generate_SingleProcess(model_path=self.para_dict['OFA_model_path'],
                                       image_path=self.currentImagePath, prompt=prompt,
                                       progressBar=self.window.progressBar_5)
        else:
            content_txt = '未检测到图像'
        self.window.progressBar_5.setValue(100)
        self.print_image_content(content_txt)
        QApplication.processEvents()

        # 功能2：调用chatgpt提取命名结果并时刻显示进度
        message_input = "将下面的句子缩写至5个token :" + content_txt
        self.window.progressBar_2.setValue(0)
        naming_txt = gpt_for_txt_SingleProcess(model=self.para_dict['gpt_model_name'],
                                               api_key=self.para_dict['gpt_api_key'],
                                               message_input=message_input,
                                               progressBar=self.window.progressBar_2)
        self.window.progressBar_2.setValue(95)
        self.print_image_naming('图：'+naming_txt)
        self.window.progressBar_2.setValue(100)
        QApplication.processEvents()

    def button6_clicked(self):
        #清空输入按钮，对应清空图像、两个富文本框、两个程序进度条和对应的全局变量
        #1 清空图像
        scene = QGraphicsScene()
        self.window.graphicsView.setScene(scene)
        scene.clear()
        #2 清空文本数据
        self.window.textBrowser_4.clear()
        self.window.textBrowser_2.clear()
        #3 清空进度条
        self.window.progressBar_5.setValue(0)
        self.window.progressBar_2.setValue(0)
        #4 全局变量
        self.currentImagePath = ''

    def button7_clicked(self):
        #批量处理界面中的清空输出按钮
        self.window.progressBar_6.setValue(0)
        self.window.progressBar_4.setValue(0)
        self.window.textBrowser_3.clear()
        self.window.textBrowser_6.clear()
        #清空相关的全局存储变量
        self.currentImagePathList = []
        self.Content_list = []
        self.Naming_list = []


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