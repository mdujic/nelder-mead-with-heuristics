import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5 import QtCore

from simplex import *
import numpy as np


class App(QMainWindow):



    def __init__(self):
        super().__init__()

        self.initUI()




    def initUI(self):

        # Tell the window that we accept touch events.
        self.setGeometry(400, 200, 900, 600)
        self.setFixedSize(900, 600)

       #Global variables
        self.metod_used="DirEsc"
        self.function_selected = "sphere"
        self.function = ""

        # Set background
        self.setStyleSheet("background-color: white;")

        # Add title

        self.serifFont = QFont("Times", 50, QFont.Bold)
        self.functionFont = QFont("Times", 30, QFont.Bold)
        self.resultFont = QFont("Times", 10, QFont.Bold)

        self.appTitle = QLabel(self)
        self.appTitle.setText("Nelder Mead ")
        self.appTitle.setFont(self.serifFont)
        self.appTitle.setStyleSheet("padding: 5px; color: #242424")
        self.appTitle.adjustSize()

        self.function_used = QLabel(self)
        self.function_used.setFont(self.functionFont)
        self.function_used.setStyleSheet("padding: 5px; color: #242424")
        self.function_used.move(500, 100)

        self.result = QLabel(self)
        self.result.setFont(self.functionFont)
        self.result.setStyleSheet("padding: 5px; color: #242424")
        self.result.move(100, 500)


        # All the BUTTONS and text and pictures

        self.button = QPushButton("Find minimum", self)
        #self.button_delete = QPushButton("Delete", self)

        self.setWindowTitle('Nelder Mead')

        # Create font for parametars
        self.paramaterFont = QFont("Times", 10, QFont.Black)

        # Create textbox for Lambda

        self.text_lambda = QLabel(self)
        self.text_lambda.setText("Lambda:")
        self.text_lambda.setFont(self.paramaterFont)
        self.text_lambda.setStyleSheet("padding: 5px; color: #242424")
        self.text_lambda.adjustSize()
        self.text_lambda.move(0,220)

        self.textbox_lambda = QLineEdit(self)
        self.textbox_lambda.move(120, 220)
        self.textbox_lambda.resize(100, 30)
        self.textbox_lambda.setPlaceholderText("Enter lambda")

        # Create textbox for M

        self.text_M = QLabel(self)
        self.text_M.setText("M:")
        self.text_M.setFont(self.paramaterFont)
        self.text_M.setStyleSheet("padding: 5px; color: #242424")
        self.text_M.adjustSize()
        self.text_M.move(0, 260)

        self.textbox_M = QLineEdit(self)
        self.textbox_M.move(120, 260)
        self.textbox_M.resize(100, 30)
        self.textbox_M.setPlaceholderText("Enter M")

        # Create textbox for Epsilon

        self.text_epsilon = QLabel(self)
        self.text_epsilon.setText("Epsilon:")
        self.text_epsilon.setFont(self.paramaterFont)
        self.text_epsilon.setStyleSheet("padding: 5px; color: #242424")
        self.text_epsilon.adjustSize()
        self.text_epsilon.move(0, 300)

        self.textbox_epsilon = QLineEdit(self)
        self.textbox_epsilon.move(120, 300)
        self.textbox_epsilon.resize(100, 30)
        self.textbox_epsilon.setPlaceholderText("Enter Epsilon")

        # Create textbox for Epsilon apostrophe

        self.text_epsilon_apostrophe = QLabel(self)
        self.text_epsilon_apostrophe.setText("Epsilon':")
        self.text_epsilon_apostrophe.setFont(self.paramaterFont)
        self.text_epsilon_apostrophe.setStyleSheet("padding: 5px; color: #242424")
        self.text_epsilon_apostrophe.adjustSize()
        self.text_epsilon_apostrophe.move(0, 340)

        self.textbox_epsilon_apostrophe = QLineEdit(self)
        self.textbox_epsilon_apostrophe.move(120, 340)
        self.textbox_epsilon_apostrophe.resize(100, 30)
        self.textbox_epsilon_apostrophe.setPlaceholderText("Enter Epsilon\'")

        # Only for simulated annealing

        self.text_n_iterations = QLabel(self)
        self.text_n_iterations.setText("Rest of parametars are only if simulate annealing is selected: ")
        self.text_n_iterations.setFont(self.paramaterFont)
        self.text_n_iterations.setStyleSheet("padding: 5px; color: #242424")
        self.text_n_iterations.adjustSize()
        self.text_n_iterations.move(0, 380)

        # Create textbox for n_iterations

        self.text_n_iterations = QLabel(self)
        self.text_n_iterations.setText("n:")
        self.text_n_iterations.setFont(self.paramaterFont)
        self.text_n_iterations.setStyleSheet("padding: 5px; color: #242424")
        self.text_n_iterations.adjustSize()
        self.text_n_iterations.move(0, 420)

        self.textbox_n_iterations = QLineEdit(self)
        self.textbox_n_iterations.move(120, 420)
        self.textbox_n_iterations.resize(100, 30)
        self.textbox_n_iterations.setPlaceholderText("Enter n")

        # Create textbox for temperature

        self.text_temperature = QLabel(self)
        self.text_temperature.setText("Temperature:")
        self.text_temperature.setFont(self.paramaterFont)
        self.text_temperature.setStyleSheet("padding: 5px; color: #242424")
        self.text_temperature.adjustSize()
        self.text_temperature.move(0, 460)

        self.textbox_temperature = QLineEdit(self)
        self.textbox_temperature.move(120, 460)
        self.textbox_temperature.resize(100, 30)
        self.textbox_temperature.setPlaceholderText("Enter temperature")

        self.function_button_group = QButtonGroup()


        # Radio button for sphere function
        self.radioButton_sphere = QRadioButton("Sphere function", self)
        self.radioButton_sphere.setGeometry(QtCore.QRect(50, 120, 120, 20))

        # adding signal and slot
        self.radioButton_sphere.clicked.connect(self.sphere_selected)

        # Radio button for Rosenbrock function
        self.radioButton_rosenbrock = QRadioButton("Rosenbrock function", self)
        self.radioButton_rosenbrock.setGeometry(QtCore.QRect(50, 150, 120, 20))

        # adding signal and slot
        self.radioButton_rosenbrock.clicked.connect(self.rosenbrock_selected)

        # Radio button for Ackley function
        self.radioButton_ackley = QRadioButton("Ackley function", self)
        self.radioButton_ackley.setGeometry(QtCore.QRect(50, 180, 120, 20))

        # adding signal and slot
        self.radioButton_ackley.clicked.connect(self.ackley_selected)


        self.function_button_group.addButton(self.radioButton_sphere, 0)
        self.function_button_group.addButton(self.radioButton_rosenbrock, 1)
        self.function_button_group.addButton(self.radioButton_ackley, 2)
        # Create a button find min

        self.button.move(540, 210)
        self.button.resize(90, 30)
        self.button.setStyleSheet("border-radius: 10 ; border: 2px solid black; color: black")
        self.button.setEnabled(True)
        self.button.setIcon(QIcon('icons8-speech-to-text-30.png'))
        self.button.setIconSize(QSize(50, 25))
        self.button.setToolTip("Pokrece algoritam i nalazi minimum")
        self.button.setToolTipDuration(3000)
        self.button.setFont(QFont('SansSerif', 10))
        self.button.clicked.connect(self.on_click_find_min)

        # Create a save function button
        #self.button_play_rv = QPushButton("Save function", self)
        #.button_play_rv.move(400, 210)
        #self.button_play_rv.resize(120, 30)
        #self.button_play_rv.setStyleSheet("border-radius: 10 ; border: 2px solid black; color: black")
        #self.button_play_rv.setEnabled(True)
        #self.button_play_rv.clicked.connect(self.save_function)
        #self.button_play_rv.setToolTip("Save function")
        #self.button_play_rv.setToolTipDuration(3000)




        # Create delete button

        #self.button_delete.move(300, 340)
        #self.button_delete.resize(70, 35)
        #self.button_delete.setStyleSheet("border-radius: 10; border: 2px solid black; color: black")
        #self.button_delete.setIcon(QIcon('trash.png'))
        #self.button_delete.setIconSize(QSize(50, 25))
        #self.button_delete.clicked.connect(self.on_click_delete_function)


        # Radio button for directional_escape
        self.radioButton_directional_escape = QRadioButton("Directional escape", self)
        self.radioButton_directional_escape.setGeometry(QtCore.QRect(180, 120, 120, 20))


        # adding signal and slot
        self.radioButton_directional_escape.clicked.connect(self.directional_escape_selected)

        # Radio button for non_tabu_search
        self.radioButton_non_tabu_search = QRadioButton("Non tabu search", self)
        self.radioButton_non_tabu_search.setGeometry(QtCore.QRect(180, 150, 120, 20))

        # adding signal and slot
        self.radioButton_non_tabu_search.clicked.connect(self.non_tabu_search_selected)

        # Radio button for simulated_annealing
        self.radioButton_simulated_annealing = QRadioButton("Simulated annealing", self)
        self.radioButton_simulated_annealing.setGeometry(QtCore.QRect(180, 180, 120, 20))

        # adding signal and slot
        self.radioButton_simulated_annealing.clicked.connect(self.simulated_annealing_selected)

    def f(self, x):
        Sum = 0
        exec(self.function)
        return Sum


    @pyqtSlot()
    def directional_escape_selected(self):
        self.metod_used = "DirEsc"

    @pyqtSlot()
    def non_tabu_search_selected(self):
        self.metod_used = "NonTabu"


    @pyqtSlot()
    def simulated_annealing_selected(self):
        self.metod_used = "SimAnn"

    @pyqtSlot()
    def sphere_selected(self):
        self.function_selected = "sphere"

    @pyqtSlot()
    def rosenbrock_selected(self):
        self.function_selected = "rosenbrock"

    @pyqtSlot()
    def ackley_selected(self):
        self.function_selected = "ackley"



    @pyqtSlot()
    def on_click_find_min(self):
        def f1(x):
            # Sphere
            # x in interval [-30, -30]
            Sum = 0
            for i in range(0, N):
                Sum = Sum + (x[i]) ** 2
            return Sum

        def f2(x):
            # Rosenbrock
            # za epsilon = 10e-30 dao nulu
            # x in interval [-30, -30]
            Sum = 0
            for i in range(0, N - 1):
                Sum = Sum + 100 * ((x[i]) ** 2 - x[i + 1]) ** 2 + (x[i] - 1) ** 2
            return Sum

        def f3(x):
            # Ackley
            # x in interval [-5, -10]
            Sum1, Sum2 = 0, 0
            for i in range(0,N):
                Sum1 = Sum1 + (x[i])**2
                Sum2 = Sum2 + math.cos(2*math.pi*x[i])
            Sum= -20.0*math.exp(-0.2*math.sqrt((1/N)*(Sum1)))-math.exp((1/N) * Sum2) + math.e + 20
            return Sum
        f = f1
        if self.function_selected == "sphere":
            f = f1
        elif self.function_selected == "rosenbrock":
            f = f2
        else:
            f = f3
        if self.metod_used == "DirEsc":
            Lambda = 10
            if self.textbox_lambda.text():
                Lambda = int(self.textbox_lambda.text())
            M = 100000
            if self.textbox_M.text():
                M = int(self.textbox_M.text())
            Epsilon = 0
            if self.textbox_epsilon.text():
                Epsilon = float(self.textbox_epsilon.text())
            # set_trace()
            EpsilonApostrophe = 0
            if self.textbox_epsilon_apostrophe.text():
                EpsilonApostrophe = float(self.textbox_epsilon_apostrophe.text())
            x_best = DirectionalEscape(f, Epsilon, EpsilonApostrophe, Lambda, M)
            self.result.setText(str(f(x_best)))
            self.result.adjustSize()
        elif self.metod_used == "NonTabu":
            Lambda = 10
            if self.textbox_lambda.text():
                Lambda = int(self.textbox_lambda.text())
            M = 100000
            if self.textbox_M.text():
                M = int(self.textbox_M.text())
            Epsilon = 10e-10
            if self.textbox_epsilon.text():
                Epsilon = float(self.textbox_epsilon.text())
            # set_trace()
            EpsilonApostrophe = 10e-20
            if self.textbox_epsilon_apostrophe.text():
                EpsilonApostrophe = float(self.textbox_epsilon_apostrophe.text())
            x_best = NonTabuSearch(f, Epsilon, EpsilonApostrophe, Lambda, M)
            self.result.setText(str(f(x_best)))
            self.result.adjustSize()
            print(x_best)
        else:
            Lambda = 100
            if self.textbox_lambda.text():
                Lambda = int(self.textbox_lambda.text())
            n_iterations = 10
            if self.textbox_n_iterations.text():
                n_iterations = int(self.textbox_n_iterations.text())
            Epsilon = 0
            if self.textbox_epsilon.text():
                Epsilon = float(self.textbox_epsilon.text())
            Temperature = 1000
            if self.textbox_temperature.text():
                Temperature = int(self.textbox_temperature.text())
            # perform the simulated annealing search
            best, score, scores = SimulatedAnnealing(f, n_iterations, Epsilon, Lambda, Temperature)
            print('Done!')
            print('f(%s) = %f' % (best, score))
            self.result.setText(str(score))
            self.result.adjustSize()



    #@pyqtSlot()
    #def save_function(self):
    #    self.function_used.setText("f(x)= " + self.textbox.text())
    #    self.function_used.adjustSize()
    #    self.function = self.textbox.text()#

#        self.textbox.clear()


    @pyqtSlot()
    def on_click_delete_function(self):
        self.function_used.setText("")
        self.function_used.adjustSize()
        self.function=""



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    pal = QPalette()
    pal.setBrush(QPalette.Background, QBrush(QPixmap("./pozadina.png")))
    app.setPalette(pal)
    window.show()
    sys.exit(app.exec_())