import sys
from UI.CalculatorUI import UiMainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication

from sin import sin
from cos import cos
from arcsin import arcsin
from arctan import arctan


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        self.mode = False  # 标志位，False-角度模式 True-弧度模式
        self.is_compute = False  # 标志位，是否进行了运算
        self.is_error = False  # 标志位，运算是否出错，出错了运算按钮将锁死
        self.ui.number_0_button.clicked.connect(lambda: self.display_number(0))
        self.ui.number_1_button.clicked.connect(lambda: self.display_number(1))
        self.ui.number_2_button.clicked.connect(lambda: self.display_number(2))
        self.ui.number_3_button.clicked.connect(lambda: self.display_number(3))
        self.ui.number_4_button.clicked.connect(lambda: self.display_number(4))
        self.ui.number_5_button.clicked.connect(lambda: self.display_number(5))
        self.ui.number_6_button.clicked.connect(lambda: self.display_number(6))
        self.ui.number_7_button.clicked.connect(lambda: self.display_number(7))
        self.ui.number_8_button.clicked.connect(lambda: self.display_number(8))
        self.ui.number_9_button.clicked.connect(lambda: self.display_number(9))
        self.ui.del_button.clicked.connect(self.display_delete_one_number)
        self.ui.reset_button.clicked.connect(self.display_reset)
        self.ui.dot_button.clicked.connect(self.display_dot)
        self.ui.sign_button.clicked.connect(self.change_sign)
        self.ui.sin_button.clicked.connect(lambda: self.compute(0))
        self.ui.cos_button.clicked.connect(lambda: self.compute(1))
        self.ui.arctan_button.clicked.connect(lambda: self.compute(2))
        self.ui.arcsin_button.clicked.connect(lambda: self.compute(3))
        self.ui.mode_button.clicked.connect(self.change_mode)

    def change_mode(self):
        """
        改变输入模式，角度模式或弧度模式
        :return: None
        """
        self.mode = ~self.mode
        if self.mode:
            self.ui.mode_display_box.setText("Radia")
        else:
            self.ui.mode_display_box.setText("Angle")

    def str_to_number(self):
        """
        将显示框的文本转为对应的数值
        :return: number，字符串对应的值
        """
        number_str = self.ui.display_box.text()
        if "°" in number_str:
            number_str = number_str[:-1]  # 去掉度数单位，截取数字文本
        return eval(number_str)

    def display_to_box(self, content):
        """
        在显示框上显示内容
        :param content: str，要的显示内容；
        :return: None
        """
        self.ui.display_box.setText(content)

    def compute(self, compute_type):
        """
        根据不同的按钮功能，对用户输入进行计算，将计算结果显示到显示框上；
        :param compute_type: int，计算类型的标识；
        :return: None；
        """
        if self.is_error:
            return
        input_value = self.str_to_number()  # 获取用户输入
        if compute_type == 0:
            result = sin(input_value, self.mode)  # 计算sin
        elif compute_type == 1:
            result = cos(input_value, self.mode)  # 计算cos
        elif compute_type == 2:
            result = str(arctan(input_value)) + "°"  # 计算arctan
        else:
            result = arcsin(input_value)  # 计算arcsin
            if isinstance(result, bool):
                # 返回一个bool值说明输入有误，显示提示信息
                result = "无效输入"
                self.is_error = True
            else:
                result = str(result) + "°"
        self.display_to_box(str(result))  # 显示结果
        self.is_compute = True

    def display_number(self, number):
        """
        在显示框上显示按钮对应的值
        :param number: 按钮对应的值
        :return: None
        """
        display_content = self.ui.display_box.text()  # 获取显示框的文本
        if display_content == "0" or self.is_compute:
            display_content = str(number)  # 当前内容为0，直接更新为的按钮数字
        else:
            display_content += str(number)  # 当前内容不为0，追加数字
        self.display_to_box(display_content)  # 回显内容
        self.is_compute = False
        self.is_error = False

    def display_dot(self):
        """
        在显示框上显示一个小数点.
        :return: None
        """
        display_content = self.ui.display_box.text()  # 获取显示框的文本
        if "." in display_content or self.is_compute:
            return
        else:
            display_content += "."  # 追加一个小数点
            self.display_to_box(display_content)  # 回显内容

    def display_delete_one_number(self):
        """
        清除当前显示框上数值最右侧的一位数；
        当显示框上的数值只有一位时，再次按清除按钮显示0；
        :return: None;
        """
        display_content = self.ui.display_box.text()  # 获取显示框文本
        if self.is_compute:
            return
        if len(display_content) == 1:
            display_content = "0"  # 当显示框上的数值只有一位时，再次按清除按钮显示0；
        else:
            display_content = display_content[:-1]  # 清除当前显示框上数值最右侧的一位数
        self.display_to_box(display_content)  # 回显内容

    def display_reset(self):
        """
        重置显示框上的内容为0
        :return:None
        """
        self.is_compute = False
        self.is_error = False
        self.display_to_box("0")

    def change_sign(self):
        """
        改变显示框上文本的正负号
        :return:
        """
        display_content = self.ui.display_box.text()  # 获取显示框的文本
        if display_content == "0":  # 文本内容为0，不作符号处理
            return
        elif "-" in display_content:
            display_content = display_content[1:]
        else:
            display_content = "-" + display_content
        self.display_to_box(display_content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
