import sys

from PyQt5.QtGui import QPixmap, QPalette, QBrush

from Euclidean_distance_similarity import EuclideanDistance
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
# 导入designer工具生成的login模块
from tj import Ui_MainWindow
class MyMainForm(Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.ed = EuclideanDistance()
        self.setupUi(self)
        self.lineEdit.editingFinished.connect(self.editingFinished_func)
        self.pushButton.clicked.connect(lambda: self.onButtonClicked())
    #按钮响应信号槽
    def onButtonClicked(self):
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        list1 = self.ed.top10_simliar(self.lineEdit.text())
        list2 = self.ed.recommend(self.lineEdit.text())
        ts = ''.join('(%s,%f)\t\n' %(a,b) for (a,b) in list1)
        rs = ''.join('%s,%s)\t\n' %(a,b) for (a,b) in list2)
        self.textBrowser_2.append(ts)
        self.textBrowser.append(rs)
    def editingFinished_func(self):
        pass

if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # palette = QPalette()
    # pix = QPixmap("D:\\movie_data\\20230425220636.jpg")
    #
    # palette.setBrush(QPalette.Background, QBrush(pix))
    # myWin.setPalette(palette)
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
