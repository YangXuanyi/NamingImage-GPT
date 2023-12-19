from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage


def show_image():
    app = QApplication([])

    # 加载图像到QPixmap对象中
    image = QImage("./imgs/lukou.jpg")
    pixmap = QPixmap.fromImage(image)

    # 创建QGraphicsView和QGraphicsScene
    scene = QGraphicsScene()
    scene.addPixmap(pixmap)

    view = QGraphicsView(scene)

    # 设置QGraphicsView的对齐方式为居中
    view.setAlignment(Qt.AlignCenter)

    # 调整视图的垂直滚动值，使图像垂直居中
    view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    view.horizontalScrollBar().setSliderPosition(view.horizontalScrollBar().maximum() // 2)

    # 调整图像的大小以适应视图
    view.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    view.show()
    app.exec_()


show_image()