from PyQt5 import QtWidgets, QtCore
from des import Ui_MainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from func_parser import function_parsing
from nelder_mead import calculate_neldermead
import nelder_mead as nm
import sys


class mywindow(QtWidgets.QMainWindow):
    max_iterations = 100
    delay = 1000
    function = lambda self, x: eval()
    left_x1 = -10
    left_x2 = -10
    right_x1 = 10
    right_x2 = 10
    dimensions = 0
    timer = QtCore.QTimer()
    simplex = np.eye(dimensions + 1, dimensions)
    iteration = 0

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.widget.fig = Figure()
        self.ui.widget.canvas = FigureCanvas(self.ui.widget.fig)
        self.ui.widget.axes = self.ui.widget.fig.add_subplot(111,
                                                             projection='3d')
        self.ui.widget.axes.mouse_init(pan_btn=None)
        layout = QtWidgets.QVBoxLayout(self.ui.widget)
        layout.addWidget(self.ui.widget.canvas)
        self.dimensions, function_str = function_parsing("-1/(1+x1**2)-1/(1+x2**2)")
        self.function = lambda x: eval(function_str)
        self.refresh_plot()
        self.ui.widget_2.fig = Figure()
        self.ui.widget_2.canvas = FigureCanvas(self.ui.widget_2.fig)
        self.ui.widget_2.axes = self.ui.widget_2.fig.add_subplot(111,
                                                                 projection='3d')
        layout2 = QtWidgets.QVBoxLayout(self.ui.widget_2)
        layout2.addWidget(self.ui.widget_2.canvas)
        self.timer.timeout.connect(self.make_step)
        self.ui.lineEdit.textEdited.connect(self.function_changed)
        self.ui.lineEdit.setText("-1/(1+x1**2)-1/(1+x2**2)")
        self.ui.leftx1.textEdited.connect(self.interval_changed)
        self.ui.leftx2.textEdited.connect(self.interval_changed)
        self.ui.rightx1.textEdited.connect(self.interval_changed)
        self.ui.rightx2.textEdited.connect(self.interval_changed)
        self.ui.leftx1.setText(str(self.left_x1))
        self.ui.leftx2.setText(str(self.left_x2))
        self.ui.rightx1.setText(str(self.right_x1))
        self.ui.rightx2.setText(str(self.right_x2))
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.breakBtnClicked)
        self.ui.pushButton_2.setEnabled(False)

    def function_changed(self, text):
        try:
            self.dimensions, function_str = function_parsing(text)
            self.function = lambda x: eval(function_str)
            if self.dimensions == 2:
                self.refresh_plot()
            self.ui.pushButton.setEnabled(True)
        except Exception:
            self.ui.pushButton.setEnabled(False)

    def breakBtnClicked(self):
        self.timer.stop()
        points = np.round(sum(self.simplex) / (self.dimensions + 1), 5)
        self.show_results(points)

    def btnClicked(self):
        self.ui.lineEdit.setEnabled(False)
        points = np.zeros(1)
        if self.dimensions == 2:
            self.simplex = np.eye(self.dimensions + 1, self.dimensions)
            self.iteration = 0
            self.ui.label.setText("Ищем минимум:)")
            self.ui.pushButton_2.setEnabled(True)
            self.draw_simplex()
            self.draw_minisimplex()
            self.make_step()
        else:
            points = calculate_neldermead(self.function, self.dimensions)
            self.show_results(points)

    def make_step(self):
        if (self.iteration > self.max_iterations or
                np.allclose(self.simplex, self.simplex[0])):
            self.timer.stop()
            points = np.round(sum(self.simplex) / (self.dimensions + 1), 5)
            self.show_results(points)
            return
        self.simplex = nm.make_step(self.function, self.simplex)
        self.draw_simplex()
        self.draw_minisimplex()
        self.timer.start(self.delay)

    def draw_simplex(self):
        self.refresh_plot()
        z = np.zeros((self.dimensions + 1))
        i = 0
        for point in self.simplex:
            z[i] = self.function(point)
            i += 1
        self.ui.widget.axes.scatter(self.simplex[:, 0],
                                    self.simplex[:, 1],
                                    z, edgecolors="red",
                                    linewidth=4)
        for i in range(self.dimensions + 1):
            for j in range(i, self.dimensions + 1):
                self.ui.widget.axes.plot([self.simplex[i, 0],
                                          self.simplex[j, 0]],
                                         [self.simplex[i, 1],
                                          self.simplex[j, 1]],
                                         [z[i], z[j]],
                                         color="r")
        self.ui.widget.canvas.draw()
        self.ui.widget.show()

    def draw_minisimplex(self):
        self.refresh_miniplot()
        z = np.zeros((self.dimensions + 1))
        i = 0
        for point in self.simplex:
            z[i] = self.function(point)
            i += 1
        self.ui.widget_2.axes.scatter(self.simplex[:, 0],
                                      self.simplex[:, 1],
                                      z, edgecolors="red",
                                      linewidth=4)
        for i in range(self.dimensions + 1):
            for j in range(i, self.dimensions + 1):
                self.ui.widget_2.axes.plot([self.simplex[i, 0],
                                           self.simplex[j, 0]],
                                           [self.simplex[i, 1],
                                           self.simplex[j, 1]],
                                           [z[i], z[j]],
                                           color="r")
        self.ui.widget_2.canvas.draw()
        self.ui.widget_2.show()

    def interval_changed(self):
        if self.ui.leftx1.text().lstrip('-+').isdigit():
            self.left_x1 = int(self.ui.leftx1.text())

        if self.ui.leftx2.text().lstrip('-+').isdigit():
            self.left_x2 = int(self.ui.leftx2.text())

        if self.ui.rightx1.text().lstrip('-+').isdigit():
            self.right_x1 = int(self.ui.rightx1.text())

        if self.ui.rightx2.text().lstrip('-+').isdigit():
            self.right_x2 = int(self.ui.rightx2.text())

        self.refresh_plot()

    def show_results(self, points):
        output = ""
        count = 1
        for point in points:
            output += "x" + str(count) + " = " + str(np.round(point, 2)) + "\n"
            count += 1
        output += "Q(X) = " + str(np.round(self.function(points), 4))
        self.ui.label.setText(output)
        self.ui.lineEdit.setEnabled(True)
        self.ui.pushButton_2.setEnabled(False)
        self.interval_changed()

    def get_max_simplex_side(self):
        max = 0
        for i in range(len(self.simplex)):
            for j in range(i, len(self.simplex)):
                if np.linalg.norm(self.simplex[i] - self.simplex[j]) > max:
                    max = np.linalg.norm(self.simplex[i] - self.simplex[j])
        return max

    def refresh_plot(self):
        for ax in self.ui.widget.fig.axes:
            ax.clear()
        if not self.ui.lineEdit.isEnabled():
            if self.left_x1 > min(self.simplex[:, 0]):
                d = self.get_max_simplex_side()
                self.left_x1 -= d

            elif self.right_x1 < max(self.simplex[:, 0]):
                d = self.get_max_simplex_side()
                self.right_x1 += d

            if self.left_x2 > min(self.simplex[:, 1]):
                d = self.get_max_simplex_side()
                self.left_x2 -= d

            elif self.right_x2 < max(self.simplex[:, 1]):
                d = self.get_max_simplex_side()
                self.right_x2 += d
        X = []
        grid_size = (max(self.right_x1, self.right_x2) -
                     max(self.left_x1, self.left_x2)) / 20
        X.append(np.arange(self.left_x1, self.right_x1, grid_size))
        X.append(np.arange(self.left_x2, self.right_x2, grid_size))
        X[0], X[1] = np.meshgrid(X[0], X[1])
        Z = self.function(X)
        self.ui.widget.axes.plot_wireframe(X[0], X[1], Z)
        self.ui.widget.canvas.draw()
        self.ui.widget.show()

    def refresh_miniplot(self):
        for ax in self.ui.widget_2.fig.axes:
            ax.clear()
        X = []
        left1 = min(self.simplex[:, 0])
        right1 = max(self.simplex[:, 0])
        left2 = min(self.simplex[:, 1])
        right2 = max(self.simplex[:, 1])
        grid_size = (min(right1, right2) - min(left1, left2)) / 10
        X.append(np.arange(left1 - 3 * grid_size, right1 + 3 * grid_size,
                           grid_size))
        X.append(np.arange(left2 - 3 * grid_size, right2 + 3 * grid_size,
                           grid_size))
        X[0], X[1] = np.meshgrid(X[0], X[1])
        Z = self.function(X)
        self.ui.widget_2.axes.plot_wireframe(X[0], X[1], Z)
        self.ui.widget_2.canvas.draw()
        self.ui.widget_2.show()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
