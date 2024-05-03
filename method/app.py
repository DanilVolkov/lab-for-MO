from PyQt5 import QtWidgets, QtGui
from main_design import Ui_MainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from func_parser import function_parsing
from nelder_mead import calculate_neldermead
import sys
        

class mywindow(QtWidgets.QMainWindow):
    
    function = lambda self, x: eval("x[0]**2 + x[1]**2")
    
    left_x1 = -10
    left_x2 = -10
    right_x1 = 10
    right_x2 = 10
    
    dimensions = 0
    
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
        
        self.ui.lineEdit.textEdited.connect(self.function_changed)
        
        self.ui.leftx1.textEdited.connect(self.interval_changed)
        self.ui.leftx2.textEdited.connect(self.interval_changed)
        self.ui.rightx1.textEdited.connect(self.interval_changed)
        self.ui.rightx2.textEdited.connect(self.interval_changed)
        
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
        points = calculate_neldermead(self.function, self.dimensions)
        output = ""
        count = 1
        for point in points:
            output += "x" + str(count) + " = " + str(np.round(point, 2)) + "\n"
            count += 1
        output += "Q(X) = " + str(np.round(self.function(points), 4))
        self.ui.label.setText(output)
        
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
        
    def refresh_plot(self):
        for ax in self.ui.widget.fig.axes:
            ax.clear()
        
        X = []
        grid_size = (min(self.right_x1, self.right_x2) - min(self.left_x1, self.left_x2)) / 20
        X.append(np.arange(self.left_x1, self.right_x1, grid_size))
        X.append(np.arange(self.left_x2, self.right_x2, grid_size))
        X[0], X[1] = np.meshgrid(X[0], X[1])
        Z = self.function(X)

        self.ui.widget.axes.plot_surface(X[0], X[1], Z)
        self.ui.widget.canvas.draw()
        self.ui.widget.show()
        
        
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())