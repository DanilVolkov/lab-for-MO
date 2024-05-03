from PyQt5 import QtWidgets, QtCore
from main_design import Ui_MainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from func_parser import function_parsing
from nelder_mead import calculate_neldermead
import nelder_mead as nm
import sys
        

class mywindow(QtWidgets.QMainWindow):
    
    max_iterations = 1000
    delay = 2000
    
    function = lambda self, x: eval("x[0]**2 + x[1]**2")
    
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
        self.ui.widget.axes = self.ui.widget.fig.add_subplot(111, projection='3d')

        layout = QtWidgets.QVBoxLayout(self.ui.widget)
        layout.addWidget(self.ui.widget.canvas)
        
        self.refresh_plot()
        
        self.timer.timeout.connect(self.make_step)
        
        self.ui.lineEdit.textEdited.connect(self.function_changed)
        self.ui.lineEdit.setText("x1**2 + x2**2")
        
        self.ui.leftx1.textEdited.connect(self.interval_changed)
        self.ui.leftx2.textEdited.connect(self.interval_changed)
        self.ui.rightx1.textEdited.connect(self.interval_changed)
        self.ui.rightx2.textEdited.connect(self.interval_changed)
        self.ui.leftx1.setText(str(self.left_x1))
        self.ui.leftx2.setText(str(self.left_x2))
        self.ui.rightx1.setText(str(self.right_x1))
        self.ui.rightx2.setText(str(self.right_x2))
        
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton.setEnabled(False)
        
    def function_changed(self, text):
        try:
            self.dimensions, function_str  = function_parsing(text)
            self.function = lambda x: eval(function_str)
            
            if self.dimensions == 2:
                self.refresh_plot()
            
            self.ui.pushButton.setEnabled(True)
        except Exception:
            self.ui.pushButton.setEnabled(False)
            
    
    def btnClicked(self):
        points = np.zeros(1)
        if self.dimensions == 2:
            self.simplex = np.eye(self.dimensions + 1, self.dimensions)
            self.iteration = 0
            self.draw_simplex()
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
        self.simplex = nm.make_step(self.function, self.simplex)
        self.draw_simplex()
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
                self.ui.widget.axes.plot([self.simplex[i, 0],self.simplex[j, 0]], 
                                        [self.simplex[i, 1],self.simplex[j, 1]], 
                                        [z[i], z[j]],
                                        color="r")
        self.ui.widget.canvas.draw()
        self.ui.widget.show()
        
        
    def interval_changed(self):
        if self.ui.leftx1.text().isdigit():
             self.left_x1 = int(self.ui.leftx1.text())

        if self.ui.leftx2.text().isdigit():
             self.left_x2 = int(self.ui.leftx2.text())
             
        if self.ui.rightx1.text().isdigit():
             self.right_x1 = int(self.ui.rightx1.text())
             
        if self.ui.rightx2.text().isdigit():
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
        
        
    def refresh_plot(self):
        for ax in self.ui.widget.fig.axes:
            ax.clear()
        
        X = []
        grid_size = (min(self.right_x1, self.right_x2) - min(self.left_x1, self.left_x2)) / 20
        X.append(np.arange(self.left_x1, self.right_x1, grid_size))
        X.append(np.arange(self.left_x2, self.right_x2, grid_size))
        X[0], X[1] = np.meshgrid(X[0], X[1])
        Z = self.function(X)

        self.ui.widget.axes.plot_wireframe(X[0], X[1], Z)
        self.ui.widget.canvas.draw()
        self.ui.widget.show()
        
        
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())