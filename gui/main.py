import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5 import QtCore
import math
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

import numpy as np
from numpy import exp
from numpy.random import rand
import copy
import random


class Second(QMainWindow):
    def __init__(self, scores, f):
        super().__init__()
        self.initPlotUI(scores, f)


    def initPlotUI(self, scores, f):
        self.setGeometry(400, 200, 900, 600)
        self.setFixedSize(600, 450)
        self.appTitle = QLabel(self)
        self.appTitle.setText("Plot")
        self.appTitle.setStyleSheet("padding: 5px; color: #242424")
        self.appTitle.adjustSize()

        self.setWindowTitle('Plot')
        self.setStyleSheet("background-color: white;")
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        pg.mkColor('blue')
        #pg.co

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        label_style = {'color': '#000000', 'font-size': '14pt'}
        self.graphWidget.setLabel('bottom', "Improvement Number", **label_style)
        self.graphWidget.setLabel('left', "Evaluation f(x)", **label_style)
        # plot data: x, y values
        print(scores)
        help_array = []
        for i in range(0, len(scores)):
            help_array.append(i)
        self.graphWidget.plot(help_array, scores[:], pen = 'k')


class Solution(QMainWindow):
    def __init__(self, x_best, f, N):
        super().__init__()
        self.initSolutionUI(x_best, f, N)


    def initSolutionUI(self, x_best, f, N):
        self.setGeometry(400, 200, 900, 600)
        self.setFixedSize(800, 450)

        self.functionFont = QFont("Times", 15, QFont.Bold)
        self.setWindowTitle('Solution')
        self.setStyleSheet("background-color: white;")
        self.result_min = QLabel(self)
        self.result_min.setFont(self.functionFont)
        self.result_min.move(50, 50)
        self.result_min.resize(1000, 70)
        self.result_min.setWordWrap(True)
        self.result_func = QLabel(self)
        self.result_func.setFont(self.functionFont)
        self.result_func.move(50, 250)
        self.result_func.adjustSize()
        message = "min = ["
        counter = N
        for i in x_best:
            counter -= 1
            message += f'{i:.2e}'
            if counter != 0:
                message += ", "
        message += "]"
        # print("Doso sam do tu")
        print(message)

        self.result_min.setText(message)
        # self.result_min.adjustSize()
        func_message = "f(min) = "
        func_message += f'{f(x_best):.4e}'
        print(func_message)
        self.result_func.setText(func_message)
        self.result_func.adjustSize()





class App(QMainWindow):



    def __init__(self):
        super().__init__()

        self.initUI()




    def initUI(self):

        # Tell the window that we accept touch events.
        self.setGeometry(400, 200, 900, 600)
        self.setFixedSize(1200, 900)

       #Global variables
        self.method_used= "DirEsc"
        self.function_selected = "sphere"
        self.function = ""

        # Set background
        self.setStyleSheet("background-color: white;")

        # Add title

        self.serifFont = QFont("Times", 40, QFont.Bold)
        self.functionFont = QFont("Times", 20, QFont.Bold)
        self.resultFont = QFont("Times", 10, QFont.Bold)
        self.paramaterFont = QFont("Times", 10, QFont.Black)
        self.explain_labels_font = QFont("Times", 11)
        self.only_labels = QFont("Times", 10)
        self.only_labels.setItalic(True)
        self.explain_labels_font.setUnderline(True)


        self.setWindowTitle('Nelder Mead algorithm with heuristics')

        self.appTitle = QLabel(self)
        self.appTitle.setText("Nelder Mead algorithm with heuristics")
        self.appTitle.setFont(self.serifFont)
        self.appTitle.setStyleSheet("padding: 5px; color: #242424")
        self.appTitle.adjustSize()

        self.result_min = QLabel(self)
        self.result_min.setFont(self.functionFont)
        self.result_min.move(50, 750)
        self.result_min.resize(1000, 70)
        self.result_min.setWordWrap(True)

        self.result_func = QLabel(self)
        self.result_func.setFont(self.functionFont)
        self.result_func.move(50, 840)
        self.result_func.adjustSize()

        start = 280
        start_left_column = 20


        self.explain_func = QLabel(self)
        self.explain_func.setText("Choose parameters:")
        self.explain_func.setFont(self.explain_labels_font)
        self.explain_func.adjustSize()
        self.explain_func.move(30, 370)

        # Create textbox for Lambda

        for_the_lable = 150
        self.text_lambda = QLabel(self)
        self.text_lambda.setText("Lambda:")
        self.text_lambda.setFont(self.paramaterFont)
        self.text_lambda.setStyleSheet("padding: 5px; color: #242424")
        self.text_lambda.adjustSize()
        self.text_lambda.move(start_left_column,280 + for_the_lable)

        self.textbox_lambda = QLineEdit(self)
        self.textbox_lambda.move(start_left_column+140, 280 + for_the_lable)
        self.textbox_lambda.resize(100, 30)
        self.textbox_lambda.setPlaceholderText("Enter lambda")

        # Create textbox for M

        self.text_M = QLabel(self)
        self.text_M.setText("M:")
        self.text_M.setFont(self.paramaterFont)
        self.text_M.setStyleSheet("padding: 5px; color: #242424")
        self.text_M.adjustSize()
        self.text_M.move(start, 260 + for_the_lable)

        self.textbox_M = QLineEdit(self)
        self.textbox_M.move(start+140, 260 + for_the_lable)
        self.textbox_M.resize(100, 30)
        self.textbox_M.setPlaceholderText("Enter M")

        # Create textbox for Epsilon

        self.text_epsilon = QLabel(self)
        self.text_epsilon.setText("Epsilon:")
        self.text_epsilon.setFont(self.paramaterFont)
        self.text_epsilon.setStyleSheet("padding: 5px; color: #242424")
        self.text_epsilon.adjustSize()
        self.text_epsilon.move(start, 300 + for_the_lable)

        self.textbox_epsilon = QLineEdit(self)
        self.textbox_epsilon.move(start+140, 300 + for_the_lable)
        self.textbox_epsilon.resize(100, 30)
        self.textbox_epsilon.setPlaceholderText("Enter Epsilon")

        # Create textbox for Epsilon apostrophe

        self.text_epsilon_apostrophe = QLabel(self)
        self.text_epsilon_apostrophe.setText("Epsilon':")
        self.text_epsilon_apostrophe.setFont(self.paramaterFont)
        self.text_epsilon_apostrophe.setStyleSheet("padding: 5px; color: #242424")
        self.text_epsilon_apostrophe.adjustSize()
        self.text_epsilon_apostrophe.move(start, 340 + for_the_lable)

        self.textbox_epsilon_apostrophe = QLineEdit(self)
        self.textbox_epsilon_apostrophe.move(start+140, 340 + for_the_lable)
        self.textbox_epsilon_apostrophe.resize(100, 30)
        self.textbox_epsilon_apostrophe.setPlaceholderText("Enter Epsilon\'")

        # Create textbox for n_iterations

        self.text_n_iterations = QLabel(self)
        self.text_n_iterations.setText("Num iter in nelder:")
        self.text_n_iterations.setFont(self.paramaterFont)
        self.text_n_iterations.setStyleSheet("padding: 5px; color: #242424")
        self.text_n_iterations.adjustSize()
        self.text_n_iterations.move(start_left_column, 320 + for_the_lable)

        self.textbox_n_iterations = QLineEdit(self)
        self.textbox_n_iterations.move(start_left_column + 140, 320 + for_the_lable)
        self.textbox_n_iterations.resize(100, 30)
        self.textbox_n_iterations.setPlaceholderText("Enter n")

        # Only for simulated annealing

        self.text_n_iterations = QLabel(self)
        self.text_n_iterations.setText("Only for simulate annealing:")
        self.text_n_iterations.setFont(self.only_labels)
        self.text_n_iterations.setStyleSheet("padding: 5px; color: #242424")
        self.text_n_iterations.adjustSize()
        self.text_n_iterations.move(start, 380 + for_the_lable)


        # Create textbox for temperature

        self.text_temperature = QLabel(self)
        self.text_temperature.setText("Temperature:")
        self.text_temperature.setFont(self.paramaterFont)
        self.text_temperature.setStyleSheet("padding: 5px; color: #242424")
        self.text_temperature.adjustSize()
        self.text_temperature.move(start, 420 + for_the_lable)

        self.textbox_temperature = QLineEdit(self)
        self.textbox_temperature.move(start+140, 420 + for_the_lable)
        self.textbox_temperature.resize(100, 30)
        self.textbox_temperature.setPlaceholderText("Enter temperature")



        # Only for non tabu

        self.text_non_tabu = QLabel(self)
        self.text_non_tabu.setText("Only for non tabu:")
        self.text_non_tabu.setFont(self.only_labels)
        self.text_non_tabu.setStyleSheet("padding: 5px; color: #242424")
        self.text_non_tabu.adjustSize()
        self.text_non_tabu.move(start_left_column, 380 + for_the_lable)

        # Create textbox for temperature

        self.text_r = QLabel(self)
        self.text_r.setText("R:")
        self.text_r.setFont(self.paramaterFont)
        self.text_r.setStyleSheet("padding: 5px; color: #242424")
        self.text_r.adjustSize()
        self.text_r.move(start_left_column, 420 + for_the_lable)

        self.textbox_r = QLineEdit(self)
        self.textbox_r.move(start_left_column + 70, 420 + for_the_lable)
        self.textbox_r.resize(100, 30)
        self.textbox_r.setPlaceholderText("Enter R")

        self.text_sigma = QLabel(self)
        self.text_sigma.setText("Sigma:")
        self.text_sigma.setFont(self.paramaterFont)
        self.text_sigma.setStyleSheet("padding: 5px; color: #242424")
        self.text_sigma.adjustSize()
        self.text_sigma.move(start_left_column, 460 + for_the_lable)

        self.textbox_sigma = QLineEdit(self)
        self.textbox_sigma.move(start_left_column + 70, 460 + for_the_lable)
        self.textbox_sigma.resize(100, 30)
        self.textbox_sigma.setPlaceholderText("Enter Sigma")

        self.function_button_group = QButtonGroup()

        self.text_n_iterations = QLabel(self)
        self.text_n_iterations.setText("------------------------------------------------------------------------------")
        self.text_n_iterations.setFont(self.paramaterFont)
        self.text_n_iterations.setStyleSheet("padding: 5px; color: #242424")
        self.text_n_iterations.adjustSize()
        self.text_n_iterations.move(0, 500 + for_the_lable)

        # Create dimension button

        self.text_dimension = QLabel(self)
        self.text_dimension.setText("Dimension:")
        self.text_dimension.setFont(self.paramaterFont)
        self.text_dimension.setStyleSheet("padding: 5px; color: #242424")
        self.text_dimension.adjustSize()
        self.text_dimension.move(10, 540 + for_the_lable)

        self.textbox_dimension = QLineEdit(self)
        self.textbox_dimension.move(10 + 120, 540 + for_the_lable)
        self.textbox_dimension.resize(100, 30)
        self.textbox_dimension.setPlaceholderText("Enter dimension")


        self.explain_func = QLabel(self)
        self.explain_func.setText("Choose a function:")
        self.explain_func.setFont(self.explain_labels_font)
        self.explain_func.adjustSize()
        self.explain_func.move(30, 100)

        for_the_lable_extra = 20
        start_func_location = 120 + for_the_lable_extra
        # Radio button for sphere function
        self.radioButton_sphere = QRadioButton("Sphere function", self)
        self.radioButton_sphere.setGeometry(QtCore.QRect(50, start_func_location, 120, 20))
        self.radioButton_sphere.setChecked(True)
        # adding signal and slot
        self.radioButton_sphere.clicked.connect(self.sphere_selected)


        # Radio button for Rosenbrock function
        self.radioButton_rosenbrock = QRadioButton("Rosenbrock function", self)
        self.radioButton_rosenbrock.setGeometry(QtCore.QRect(50, start_func_location+30, 120, 20))

        # adding signal and slot
        self.radioButton_rosenbrock.clicked.connect(self.rosenbrock_selected)


        # Radio button for Ackley function
        self.radioButton_ackley = QRadioButton("Ackley function", self)
        self.radioButton_ackley.setGeometry(QtCore.QRect(50, start_func_location+60, 120, 20))

        # adding signal and slot
        self.radioButton_ackley.clicked.connect(self.ackley_selected)



        # Radio button for Griewank function
        self.radioButton_griewank = QRadioButton("Griewank function", self)
        self.radioButton_griewank.setGeometry(QtCore.QRect(50, start_func_location+90, 120, 20))

        # adding signal and slot
        self.radioButton_griewank.clicked.connect(self.griewank_selected)


        # Radio button for Michalewicz function
        self.radioButton_michalewicz = QRadioButton("Michalewicz function", self)
        self.radioButton_michalewicz.setGeometry(QtCore.QRect(50, start_func_location+120, 120, 20))

        # adding signal and slot
        self.radioButton_michalewicz.clicked.connect(self.michalewicz_selected)

        # Radio button for Shekel function
        self.radioButton_shekel = QRadioButton("Shekel function", self)
        self.radioButton_shekel.setGeometry(QtCore.QRect(50, start_func_location + 150, 120, 20))

        # adding signal and slot
        self.radioButton_shekel.clicked.connect(self.shekel_selected)

        # Radio button for Langermann function
        self.radioButton_langermann = QRadioButton("Langermann function", self)
        self.radioButton_langermann.setGeometry(QtCore.QRect(50, start_func_location + 180, 120, 20))

        # adding signal and slot
        self.radioButton_langermann.clicked.connect(self.langermann_selected)


        self.function_button_group.addButton(self.radioButton_sphere, 0)
        self.function_button_group.addButton(self.radioButton_rosenbrock, 1)
        self.function_button_group.addButton(self.radioButton_ackley, 2)
        self.function_button_group.addButton(self.radioButton_griewank, 3)
        self.function_button_group.addButton(self.radioButton_michalewicz, 4)
        self.function_button_group.addButton(self.radioButton_shekel, 5)
        self.function_button_group.addButton(self.radioButton_langermann, 6)
        # Create a button find min

        self.button = QPushButton("Find minimum", self)
        self.button.move(700, 600)
        self.button.resize(120, 50)
        self.button.setStyleSheet("border-radius: 10 ; border: 2px solid black; color: black")
        self.button.setEnabled(True)
        self.button.setFont(QFont('SansSerif', 10))
        self.button.clicked.connect(self.on_click_find_min)





        # Create delete button

        self.button_reset = QPushButton("Reset", self)
        self.button_reset.move(900, 600)
        self.button_reset.resize(120, 50)
        self.button_reset.setStyleSheet("border-radius: 10; border: 2px solid black; color: black")
        self.button.setFont(QFont('SansSerif', 10))
        self.button_reset.clicked.connect(self.on_click_delete_function)


        self.explain_method = QLabel(self)
        self.explain_method.setText("Choose a method:")
        self.explain_method.setFont(self.explain_labels_font)
        self.explain_method.adjustSize()
        self.explain_method.move(start-2, 100)

        # Radio button for directional_escape
        self.radioButton_directional_escape = QRadioButton("Directional escape", self)
        self.radioButton_directional_escape.setGeometry(QtCore.QRect(start, 120 + for_the_lable_extra, 120, 20))
        self.radioButton_directional_escape.setChecked(True)


        # adding signal and slot
        self.radioButton_directional_escape.clicked.connect(self.directional_escape_selected)

        # Radio button for non_tabu_search
        self.radioButton_non_tabu_search = QRadioButton("Non tabu search", self)
        self.radioButton_non_tabu_search.setGeometry(QtCore.QRect(start, 150 + for_the_lable_extra, 120, 20))

        # adding signal and slot
        self.radioButton_non_tabu_search.clicked.connect(self.non_tabu_search_selected)

        # Radio button for simulated_annealing
        self.radioButton_simulated_annealing = QRadioButton("Simulated annealing", self)
        self.radioButton_simulated_annealing.setGeometry(QtCore.QRect(start, 180 + for_the_lable_extra, 120, 20))

        # adding signal and slot
        self.radioButton_simulated_annealing.clicked.connect(self.simulated_annealing_selected)

        # Radio button for Nelder-Mead
        self.radioButton_simulated_annealing = QRadioButton("Nelder mead", self)
        self.radioButton_simulated_annealing.setGeometry(QtCore.QRect(start, 210 + for_the_lable_extra, 120, 20))

        # adding signal and slot
        self.radioButton_simulated_annealing.clicked.connect(self.nelder_mead_selected)

        # Radio button for Iterated method
        self.radioButton_simulated_annealing = QRadioButton("Iterated method", self)
        self.radioButton_simulated_annealing.setGeometry(QtCore.QRect(start, 240 + for_the_lable_extra, 120, 20))

        # adding signal and slot
        self.radioButton_simulated_annealing.clicked.connect(self.iterated_method_selected)

        self.explain_method = QLabel(self)
        self.explain_method.setText("Graph of function in 3D:")
        self.explain_method.setFont(self.explain_labels_font)
        self.explain_method.adjustSize()
        self.explain_method.move(600, 100)

        self.photo = QLabel(self)
        self.photo.move(600, 130)
        self.photo.resize(500, 400)
        self.photo.setPixmap(QPixmap("Sphere.png").scaled(500, 400, QtCore.Qt.KeepAspectRatio))

        self.pbar = QProgressBar(self)
        self.pbar.move(350, 540 + for_the_lable)
        self.pbar.resize(500, 30)

    def f(self, x):
        Sum = 0
        exec(self.function)
        return Sum


    @pyqtSlot()
    def directional_escape_selected(self):
        self.method_used = "DirEsc"

    @pyqtSlot()
    def non_tabu_search_selected(self):
        self.method_used = "NonTabu"

    @pyqtSlot()
    def simulated_annealing_selected(self):
        self.method_used = "SimAnn"

    @pyqtSlot()
    def nelder_mead_selected(self):
        self.method_used = "nelder"

    @pyqtSlot()
    def iterated_method_selected(self):
        self.method_used = "iterated"

    @pyqtSlot()
    def sphere_selected(self):
        self.function_selected = "sphere"
        self.photo.setPixmap(QPixmap("Sphere.png").scaled(500, 400, QtCore.Qt.KeepAspectRatio))
        self.textbox_dimension.setEnabled(True)

    @pyqtSlot()
    def rosenbrock_selected(self):
        self.function_selected = "rosenbrock"
        self.photo.setPixmap(QPixmap("Rosenbrock.png").scaled(500, 400, QtCore.Qt.KeepAspectRatio))
        self.textbox_dimension.setEnabled(True)

    @pyqtSlot()
    def ackley_selected(self):
        self.function_selected = "ackley"
        self.photo.setPixmap(QPixmap("Ackley.png").scaled(500, 400, QtCore.Qt.KeepAspectRatio))
        self.textbox_dimension.setEnabled(True)

    @pyqtSlot()
    def griewank_selected(self):
        self.function_selected = "griewank"
        self.photo.setPixmap(QPixmap("Griewank.png").scaled(500, 400, QtCore.Qt.KeepAspectRatio))
        self.textbox_dimension.setEnabled(True)

    @pyqtSlot()
    def shekel_selected(self):
        self.function_selected = "shekel"
        self.photo.setPixmap(QPixmap("Shekel.jpg").scaled(500, 400, QtCore.Qt.KeepAspectRatio))
        self.textbox_dimension.setEnabled(False)
        self.textbox_dimension.setText("")

    @pyqtSlot()
    def langermann_selected(self):
        self.function_selected = "langermann"
        self.photo.setPixmap(QPixmap("langerman.png").scaled(500, 400, QtCore.Qt.KeepAspectRatio))
        self.textbox_dimension.setEnabled(False)
        self.textbox_dimension.setText("")

    @pyqtSlot()
    def michalewicz_selected(self):
        self.function_selected = "michalewicz"
        self.photo.setPixmap(QPixmap("Michalewicz.png").scaled(500, 400, QtCore.Qt.KeepAspectRatio))
        self.textbox_dimension.setEnabled(True)

    @pyqtSlot()
    def _e(self, index, size):
        arr = np.zeros(size)
        arr[index] = 1.0
        return arr

    @pyqtSlot()
    def Delta(self, x, u, l, N):
        Sum = 0
        # no general, only box constraints
        for i in range(0, N):
            Sum = Sum + max(x[i] - u[i], 0) + max(l[i] - x[i], 0)
        return Sum

    @pyqtSlot()
    def better(self, f, x, y, u, l, N):
        Dx = self.Delta(x, u, l, N)
        Dy = self.Delta(y, u, l, N)
        if (Dx < Dy):
            return True
        elif (Dx == Dy and f(x) < f(y)):
            return True
        else:
            return False

    @pyqtSlot()
    def findExtremes(self, f, s, u, l, N):
        Ds = np.empty([N + 1])
        fs = np.empty([N + 1])
        for i in range(0, N + 1):
            Ds[i] = self.Delta(s[i], u, l, N)
            fs[i] = f(s[i])
        arg_b = np.argmin(Ds)
        for i in range(0, N + 1):
            if Ds[i] == Ds[arg_b] and i != arg_b:
                if (fs[i] < fs[arg_b]):
                    arg_b = i;

        arg_w = np.argmax(Ds)
        for i in range(0, N + 1):
            if Ds[i] == Ds[arg_w] and i != arg_w:
                if (fs[i] > fs[arg_w]):
                    arg_w = i;

        # mask the worst to find the second worst
        Ds[arg_w] = 0

        arg_sw = np.argmax(Ds)
        for i in range(0, N + 1):
            if Ds[i] == Ds[arg_sw] and i != arg_w:
                if (fs[i] > fs[arg_sw]):
                    arg_sw = i;

        return arg_b, arg_w, arg_sw

    @pyqtSlot()
    def centroid(self, s, argWorst):
        return np.mean(np.delete(s, argWorst), axis=0)

    @pyqtSlot()
    def SimplexLocalSearchNormal(self, f, u, l, x, Epsilon, Lambda, M, Alpha=1, Gamma=2, Beta=-0.5):
        N = len(x)
        s = np.empty([N + 1, N])
        s[0] = x
        for j in range(1, N + 1):
            s[j] = x + Lambda * (u[j - 1] - l[j - 1]) * self._e(j - 1, N);
        k = 0
        it = 0

        argBest, argWorst, argSecondWorst = self.findExtremes(f, s, u, l, N)
        sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
        scores = []
        while abs(f(sBest) - f(sWorst)) > Epsilon and k < M:
            if k // 1000 > it:
                it = k // 1000
                print("iteration:", it * 1000, "| best found value: ", f(sBest))
                scores.append(f(sBest))
                self.pbar.setValue(k)

            r = (1 + Alpha) * self.centroid(s, argWorst) - Alpha * sWorst
            if self.better(f, sBest, r, u, l, N) and self.better(f, r, sSecondWorst, u, l, N):
                s[argWorst] = r
            elif self.better(f, r, sBest, u, l, N):
                e = (1 + Gamma) * self.centroid(s, argWorst) - Gamma * sWorst
                if self.better(f, e, r, u, l, N):
                    s[argWorst] = e
                else:
                    s[argWorst] = r
            else:
                c = (1 + Beta) * self.centroid(s, argWorst) - Beta * sWorst
                if self.better(f, c, sWorst, u, l, N):
                    s[argWorst] = c
                else:
                    for j in range(0, N + 1):
                        s[j] = (s[j] + sBest) / 2

            argBest, argWorst, argSecondWorst = self.findExtremes(f, s, u, l, N)
            sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
            k = k + 1

        return sBest, scores

    @pyqtSlot()
    def SimplexLocalSearchForIterated(self, f, u, l, x, Epsilon, Lambda, M, Alpha=1, Gamma=2, Beta=-0.5):
        N = len(x)
        s = np.empty([N + 1, N])
        s[0] = x
        for j in range(1, N + 1):
            s[j] = x + Lambda * (u[j - 1] - l[j - 1]) * self._e(j - 1, N)
        k = 0
        it = 0

        argBest, argWorst, argSecondWorst = self.findExtremes(f, s, u, l, N)
        sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]

        while abs(f(sBest) - f(sWorst)) > Epsilon and k < M:

            r = (1 + Alpha) * self.centroid(s, argWorst) - Alpha * sWorst
            if self.better(f, sBest, r, u, l, N) and self.better(f, r, sSecondWorst, u, l, N):
                s[argWorst] = r
            elif self.better(f, r, sBest, u, l, N):
                e = (1 + Gamma) * self.centroid(s, argWorst) - Gamma * sWorst
                if self.better(f, e, r, u, l, N):
                    s[argWorst] = e
                else:
                    s[argWorst] = r
            else:
                c = (1 + Beta) * self.centroid(s, argWorst) - Beta * sWorst
                if self.better(f, c, sWorst, u, l, N):
                    s[argWorst] = c
                else:
                    for j in range(0, N + 1):
                        s[j] = (s[j] + sBest) / 2

            argBest, argWorst, argSecondWorst = self.findExtremes(f, s, u, l, N)
            sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
            k = k + 1

        return sBest, k


    @pyqtSlot()
    def IteratedSimplex(self, f, lowerBound, upperBound, u, l, dim, Epsilon, EpsilonApostrophe, Lambda, M):
        k = 0
        it = 0
        scores = []
        while (k < M):
            x = np.random.uniform(low=lowerBound, high=upperBound, size=(dim,))

            x, _k = self.SimplexLocalSearchForIterated(f, u, l, x, Epsilon, Lambda, M - k)
            k = k + _k

            try:
                xBest
            except NameError:
                xBest = None

            if (xBest is None or f(x) < f(xBest)):
                xBest, _k = self.SimplexLocalSearchForIterated(f, u, l, x, EpsilonApostrophe, Lambda, M - k)
                k = k + _k

            if k // 1000 > it:
                it = k // 1000
                print("iteration:", it * 1000, "| best found value: ", f(xBest))
                scores.append(f(xBest))
                self.pbar.setValue(k)

        return xBest, scores


    @pyqtSlot()
    def SimplexLocalSearchForDirectional(self, f, u, l, option, x, Epsilon, Lambda, M, Alpha=1, Gamma=2, Beta=-0.5):
        N = len(x)
        s = np.empty([N + 1, N])
        s[0] = x
        for j in range(1, N + 1):
            s[j] = x + Lambda * (u[j - 1] - l[j - 1]) * self._e(j - 1, N);
        k = 0

        argBest, argWorst, argSecondWorst = self.findExtremes(f, s, u, l, N)
        sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
        # set_trace()
        while abs(f(sBest) - f(sWorst)) > Epsilon and k < M and k < 1000:
            # set_trace()
            # if(k%1000 == 0):print(f(sBest),'\n')
            r = (1 + Alpha) * self.centroid(s, argWorst) - Alpha * sWorst
            if (self.better(f, sBest, r, u, l, N) and self.better(f, r, sSecondWorst, u, l, N)):
                s[argWorst] = r
            elif (self.better(f, r, sBest, u, l, N)):
                e = (1 + Gamma) * self.centroid(s, argWorst) - Gamma * sWorst
                if (self.better(f, e, r, u, l, N)):
                    s[argWorst] = e
                else:
                    s[argWorst] = r
            else:
                c = (1 + Beta) * self.centroid(s, argWorst) - Beta * sWorst
                if (self.better(f, c, sWorst, u, l, N)):
                    s[argWorst] = c
                else:
                    if (option == 1):
                        #print(f(sBest))
                        return sBest, k, s, argBest, argWorst, argSecondWorst
                    for j in range(0, N + 1):
                        s[j] = (s[j] + sBest) / 2

            # set_trace()
            argBest, argWorst, argSecondWorst = self.findExtremes(f, s, u, l, N)
            sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
            k = k + 1
        # print(f(sBest))
        return sBest, k, s, argBest, argWorst, argSecondWorst

    @pyqtSlot()
    def DirectionalEscape(self, f, lowerBound, upperBound, u, l, dim, Epsilon, EpsilonApostrophe, Lambda, M, Gamma=1.25,
                          Beta=-0.5):
        k = 0
        it = 0
        #print(lowerBound, upperBound)
        x = np.random.uniform(low=lowerBound, high=upperBound, size=(dim,))
        N = len(x)
        scores = []
        while (k < M):
            # print("Da vidim koliko puta ides")
            # set_trace()
            temp, _k, s, argBest, argWorst, argSecondWorst = self.SimplexLocalSearchForDirectional(f, u, l, 1, x,
                                                                                              Epsilon, Lambda,
                                                                                              M - k)
            x = copy.copy(temp)

            k = k + _k
            try:
                xBest
            except NameError:
                xBest = None

            if xBest is None or f(x) < f(xBest):
                temp, _k, s, argBest, argWorst, argSecondWorst = self.SimplexLocalSearchForDirectional(f, u, l, 2, x,
                                                                                                  EpsilonApostrophe,
                                                                                                  Lambda,
                                                                                                  M - k)
                xBest = np.zeros(N)
                xBest = xBest + temp
                k = k + _k
                scores.append(f(xBest))
                print("***NEW BEST VALUE*** iteration: ", k, "| best found value: ", f(xBest))

            if xBest is not None and k // 1000 > it:
                it = k // 1000
                print("iteration:", it * 1000, "| best found value: ", f(xBest))
                scores.append(f(xBest))
                self.pbar.setValue(k)
                # if f(xBest) < 1:
                #    for i in range(0,N):
                #        s[i][i] = s[i][i] + 10e-2*f(xBest)
                # else:
                # for i in range(0,N):
                #    s[i][i] = s[i][i] + 10e-15

            argBest, argWorst, argSecondWorst = self.findExtremes(f, s, u, l, N)

            xWorst = None

            while xWorst is None or self.better(f, x, xWorst, u, l, N):
                xWorst = copy.copy(x)
                x = Gamma * s[argBest] + (1 - Gamma) * self.centroid(s, argBest)
                s[argBest] = copy.copy(x)
                argBest, argWorst, argSecondWorst = self.findExtremes(f, s, u, l, N)

        return xBest, scores

    @pyqtSlot()
    def SimplexLocalSearchForNonTabu(self, f, u, l, x, Epsilon, Lambda, M, Alpha=1, Gamma=2, Beta=-0.5):
        N = len(x)
        s = np.empty([N + 1, N])
        s[0] = x
        for j in range(1, N + 1):
            s[j] = x + Lambda * (u[j - 1] - l[j - 1]) * self._e(j - 1, N);
        k = 0
        argBest, argWorst, argSecondWorst = self.findExtremes(f, s, u, l, N)
        sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
        # set_trace()
        while abs(f(sBest) - f(sWorst)) > Epsilon and k < M and k < 1000:
            # set_trace()
            # if(k%1000 == 0):print(f(sBest),'\n')
            r = (1 + Alpha) * self.centroid(s, argWorst) - Alpha * sWorst
            if (self.better(f, sBest, r, u, l, N) and self.better(f, r, sSecondWorst, u, l, N)):
                s[argWorst] = r
            elif (self.better(f, r, sBest, u, l, N)):
                e = (1 + Gamma) * self.centroid(s, argWorst) - Gamma * sWorst
                if (self.better(f, e, r, u, l, N)):
                    s[argWorst] = e
                else:
                    s[argWorst] = r
            else:
                c = (1 + Beta) * self.centroid(s, argWorst) - Beta * sWorst
                if (self.better(f, c, sWorst, u, l, N)):
                    s[argWorst] = c
                else:
                    for j in range(0, N + 1):
                        s[j] = (s[j] + sBest) / 2

            # set_trace()
            argBest, argWorst, argSecondWorst = self.findExtremes(f, s, u, l, N)
            sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
            k = k + 1
        # print(f(sBest))
        return sBest, k

    @pyqtSlot()
    def NonTabuSearch(self, f, lowerBound, upperBound, u, l, dim, Epsilon, EpsilonApostrophe, Lambda, M, R, Sigma, Gamma=2,
                      Beta=-0.5):
        # settings.init()
        k = 0
        it = 0
        x = np.random.uniform(low=lowerBound, high=upperBound, size=(dim,))
        N = len(x)
        x, _k = self.SimplexLocalSearchForNonTabu(f, u, l, x, Epsilon, Lambda, M - k)
        k = k + _k
        xBest = np.zeros(dim)
        xBest = xBest + x
        y = np.zeros(dim)
        y = y + x
        running_first_time = True
        scores = []
        while (k < M):

            # set_trace()
            for i in range(1, R):
                x[i] = y[i] + Sigma * (u[i] - l[i])
                x, _k = self.SimplexLocalSearchForNonTabu(f, u, l, x, Epsilon, Lambda, M - k)
                k = k + _k
                if f(x) < f(xBest):
                    print("***NEW BEST VALUE*** iteration: ", k, "| best found value: ", f(x))
                    scores.append(f(x))
                    xBest, _k = self.SimplexLocalSearchForNonTabu(f, u, l, x, EpsilonApostrophe, Lambda, M - k)
                    k = k + _k
                if running_first_time or f(x) < f(xWorst):
                    running_first_time = False
                    xWorst = np.zeros(dim)
                    xWorst = xWorst + x
            y = np.zeros(dim)
            y = y + xWorst
            if (k // 1000 > it):
                it = k // 1000
                print("iteration:", it * 1000, "| best found value: ", f(xBest))
                scores.append(f(xBest))
                self.pbar.setValue(k)
                # num_of_iterations = it*1000

        return xBest, scores

    @pyqtSlot()
    def SimplexLocalSearchForSimulatedAnnealing(self, f, u, l, n_iterations, x, Epsilon, Lambda, Alpha=1, Gamma=2, Beta=-0.5):
        N = len(x)
        s = np.empty([N + 1, N])
        s[0] = x
        for j in range(1, N + 1):
            s[j] = x + Lambda * (u[j - 1] - l[j - 1]) * self._e(j - 1, N);
        k = 0
        argBest, argWorst, argSecondWorst = self.findExtremes(f, s, u, l, N)
        sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
        # set_trace()
        while abs(f(sBest) - f(sWorst)) > Epsilon and k < n_iterations:
            # set_trace()
            # if(k%1000 == 0):print(f(sBest),'\n')
            r = (1 + Alpha) * self.centroid(s, argWorst) - Alpha * sWorst
            if self.better(f, sBest, r, u, l, N) and self.better(f, r, sSecondWorst, u, l, N):
                s[argWorst] = r
            elif self.better(f, r, sBest, u, l, N):
                e = (1 + Gamma) * self.centroid(s, argWorst) - Gamma * sWorst
                if self.better(f, e, r, u, l, N):
                    s[argWorst] = e
                else:
                    s[argWorst] = r
            else:
                c = (1 + Beta) * self.centroid(s, argWorst) - Beta * sWorst
                if self.better(f, c, sWorst, u, l, N):
                    s[argWorst] = c
                else:
                    for j in range(0, N + 1):
                        s[j] = (s[j] + sBest) / 2

            # set_trace()
            argBest, argWorst, argSecondWorst = self.findExtremes(f, s, u, l, N)
            sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
            k = k + 1
        # print(f(sBest))
        return sBest

    @pyqtSlot()
    def SimulatedAnnealing(self, f, lowerBound, upperBound, u, l, n_iterations, dim, Epsilon, Lambda, T_max, T_min=0, beta=1, mu=3, nu=1, tau=1.5,
                           alpha=0.5):
        # generate an initial point

        x_0 = np.random.uniform(low=lowerBound, high=upperBound, size=(dim,))

        scores = list()

        x = copy.copy(x_0)
        scores.append(x_0)
        T = T_max

        # radius
        z_max = (upperBound - lowerBound) / 2
        z_min = (upperBound - lowerBound) / 50
        z_0 = (z_max + z_min) / 2
        z = z_0

        # maximum number of iterations for nelder-mead
        N_max = 500 * dim
        counter = T_min
        while (T > T_min):
            self.pbar.setValue(counter)
            counter += 1
            k = 0
            print(T, f(scores[-1]))
            while (k <= mu):
                # generate neighborhood trail solutions
                h_list = list()
                for i in range(0, dim):
                    start = random.randint(0, dim / nu - 1)
                    y = copy.copy(x)
                    for j in range(0, nu):
                        y[start * nu + j] = np.random.uniform(low=y[start * nu + j] - z,
                                                              high=y[start * nu + j] + z,
                                                              size=(1,))
                    h_list.append(y)

                # find best y
                x_apostrophe = copy.copy(h_list[0])
                for i in range(1, dim):
                    if (f(h_list[i]) < f(x_apostrophe)):
                        x_apostrophe = copy.copy(h_list[i])

                delta_E = f(x_apostrophe) - f(scores[-1])
                if delta_E < 0:  # better solution is always selected
                    x = copy.copy(self.SimplexLocalSearchForSimulatedAnnealing(f, u, l, n_iterations, x_apostrophe, Epsilon, Lambda))
                    scores.append(x)
                    z = tau * z
                    # if(z_max < z):
                    #    z_max = z
                else:
                    z = alpha * z
                    # if(z_min > z):
                    #    z_min = z
                    if rand() < exp(-delta_E / T):  # worse solution likely selected
                        # with higher temperature
                        # x_apostrophe = copy.copy(SimplexLocalSearch(100,x,Epsilon,Lambda))
                        # print(np.linalg.norm(x_apostrophe-scores[-1]))
                        # print(z)
                        scores.append(x_apostrophe)
                        x = copy.copy(x_apostrophe)
                k = k + 1
            T = T - beta

        # apply nelder-mead at best solution
        minimum = copy.copy(x)
        for i in range(0, len(scores)):
            if (f(scores[i]) < f(minimum)):
                minimum = copy.copy(scores[i])

        x = self.SimplexLocalSearchForSimulatedAnnealing(f, u, l, N_max, minimum, Epsilon, Lambda)
        scores.append(x)

        evaluations = list()
        for i in range(0, len(scores)):
            evaluations.append(f(scores[i]))
            if f(scores[i]) < f(minimum):
                minimum = copy.copy(scores[i])

        return [minimum, f(minimum), evaluations]

    @pyqtSlot()
    def display_min_func(self, min_array, func, dim):
        message = "min = ["
        counter = dim
        for i in min_array:
            counter -= 1
            message += f'{i:.2e}'
            if counter != 0:
                message += ", "
        message += "]"
        #print("Doso sam do tu")
        print(message)

        self.result_min.setText(message)
        #self.result_min.adjustSize()
        func_message = "f(min) = "
        func_message += f'{func:.4e}'
        print(func_message)
        self.result_func.setText(func_message)
        self.result_func.adjustSize()

    @pyqtSlot()
    def on_click_find_min(self):


        lowerBound, upperBound = -30, 30


        N = 10
        if self.textbox_dimension.text():
            N = int(self.textbox_dimension.text())
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
            # x in interval [-5, 10]
            Sum1, Sum2 = 0, 0
            for i in range(0, N):
                Sum1 = Sum1 + (x[i])**2
                Sum2 = Sum2 + math.cos(2*math.pi*x[i])
            Sum= -20.0*math.exp(-0.2*math.sqrt((1/N)*(Sum1)))-math.exp((1/N) * Sum2) + math.e + 20
            return Sum

        def f4(x):
            #Griewank
            # x_i in [-600,600]
            d = 4000
            Sum = 0
            for i in range(0, N):
                Sum = Sum + (x[i]-100)**2
            Sum = Sum/d
            Prod = 1
            for i in range(0, N):
                Prod = Prod * math.cos((x[i]-100)/math.sqrt(i+1))
            Sum = Sum - Prod + 1
            return Sum


        def f5(x):
            # Michalewicz
            # x_i in [0,math.pi]
            Sum = 0
            m = 10
            for i in range(0, N):
                Sum = Sum - math.sin(x[i])*(math.sin(((i+1)*(x[i])**2)/math.pi))**(2*m)
            return Sum

        def f6(x):
            # Shekel
            # dimension is 4, x_i in [0,10]
            # m can be changed to 5, 7, and 10
            m = 10
            C = [[4.0, 1.0, 8.0, 6.0, 3.0, 2.0, 5.0, 8.0, 6.0, 7.0],
                 [4.0, 1.0, 8.0, 6.0, 7.0, 9.0, 3.0, 1.0, 2.0, 3.6],
                 [4.0, 1.0, 8.0, 6.0, 3.0, 2.0, 5.0, 8.0, 6.0, 7.0],
                 [4.0, 1.0, 8.0, 6.0, 7.0, 9.0, 3.0, 1.0, 2.0, 3.6]]

            beta = (1 / 10) * np.array([[1], [2], [2], [4], [4], [6], [3], [7], [5], [5]])
            Sum = 0
            for i in range(0, m):
                Sum1 = 0
                for j in range(0, 4):
                    Sum1 += (x[j] - C[j][i]) ** 2
                Sum1 += beta[i]
                Sum += -1 / Sum1
            return Sum[0]

        def f7(x):
            # Langermann
            # dimension is 2, x_i in [0,10]
            d = 2
            m = 5

            A = [[3, 5],
                 [5, 2],
                 [2, 1],
                 [1, 4],
                 [7, 9]]

            c = [1, 2, 5, 2, 3]
            Sum = 0
            for i in range(0, m):
                Sum1 = 0
                for j in range(0, d):
                    Sum1 += (x[j] - A[i][j]) ** 2
                Sum += c[i] * math.exp((-1 / math.pi) * Sum1) * math.cos(math.pi * Sum1)
            return Sum


        f = f1
        if self.function_selected == "sphere":
            f = f1
            lowerBound, upperBound = -30, 30
        elif self.function_selected == "rosenbrock":
            f = f2
            lowerBound, upperBound = -30, 30
        elif self.function_selected == "ackley":
            f = f3
            lowerBound, upperBound = -5, 10
        elif self.function_selected == "griewank":
            f = f4
            lowerBound, upperBound = -600, 600
        elif self.function_selected == "michalewicz":
            f = f5
            lowerBound, upperBound = 0, math.pi
        elif self.function_selected == "shekel":
            N = 4
            f = f6
            lowerBound, upperBound = 0, 10
        elif self.function_selected == "langermann":
            N = 2
            f = f7
            lowerBound, upperBound = 0, 10

        l = [lowerBound for i in range(10)]
        u = [upperBound for i in range(10)]

        if self.method_used == "nelder":
            Lambda = 10
            if self.textbox_lambda.text():
                Lambda = int(self.textbox_lambda.text())
            M = 100000
            if self.textbox_M.text():
                M = int(self.textbox_M.text())
            Epsilon = 0
            if self.textbox_epsilon.text():
                Epsilon = float(self.textbox_epsilon.text())
            self.pbar.setMaximum(M)
            x = np.random.uniform(low=lowerBound, high=upperBound, size=(N,))
            x_best, scores = self.SimplexLocalSearchNormal(f, u, l, x, Epsilon,
                                                    Lambda, M)
            self.display_min_func(x_best, f(x_best), N)
            self.dialog = Second(scores, f)
            self.dialog.show()
            self.dialog_solution = Solution(x_best, f, N)
            self.dialog_solution.show()
        elif self.method_used == "iterated":
            Lambda = 10
            if self.textbox_lambda.text():
                Lambda = int(self.textbox_lambda.text())
            M = 100000
            n_iterations = 10
            if self.textbox_n_iterations.text():
                n_iterations = int(self.textbox_n_iterations.text())
            if self.textbox_M.text():
                M = int(self.textbox_M.text())
            Epsilon = 10e-3
            if self.textbox_epsilon.text():
                Epsilon = float(self.textbox_epsilon.text())
            # set_trace()
            EpsilonApostrophe = 0
            if self.textbox_epsilon_apostrophe.text():
                EpsilonApostrophe = float(self.textbox_epsilon_apostrophe.text())
            self.pbar.setMaximum(M)
            x_best, scores = self.IteratedSimplex(f, lowerBound, upperBound, u, l, N, Epsilon, EpsilonApostrophe,
                                                    Lambda, M)
            self.display_min_func(x_best, f(x_best), N)
            self.dialog_solution = Solution(x_best, f, N)
            self.dialog_solution.show()
            self.dialog = Second(scores, f)
            self.dialog.show()
        elif self.method_used == "DirEsc":
            Lambda = 10
            if self.textbox_lambda.text():
                Lambda = int(self.textbox_lambda.text())
            M = 100000
            n_iterations = 10
            if self.textbox_n_iterations.text():
                n_iterations = int(self.textbox_n_iterations.text())
            if self.textbox_M.text():
                M = int(self.textbox_M.text())
            Epsilon = 0
            if self.textbox_epsilon.text():
                Epsilon = float(self.textbox_epsilon.text())
            # set_trace()
            EpsilonApostrophe = 0
            if self.textbox_epsilon_apostrophe.text():
                EpsilonApostrophe = float(self.textbox_epsilon_apostrophe.text())
            self.pbar.setMaximum(M)
            x_best, scores = self.DirectionalEscape(f, lowerBound, upperBound, u, l, N, Epsilon, EpsilonApostrophe, Lambda, M)
            self.display_min_func(x_best, f(x_best), N)
            self.dialog = Second(scores, f)
            self.dialog.show()
            self.dialog_solution = Solution(x_best, f, N)
            self.dialog_solution.show()
            #self.result.setText(str(f(x_best)))
            #self.result.adjustSize()
        elif self.method_used == "NonTabu":
            Lambda = 10
            if self.textbox_lambda.text():
                Lambda = int(self.textbox_lambda.text())
            M = 100000
            n_iterations = 1000
            if self.textbox_n_iterations.text():
                n_iterations = int(self.textbox_n_iterations.text())
            if self.textbox_M.text():
                M = int(self.textbox_M.text())
            Epsilon = 10e-10
            if self.textbox_epsilon.text():
                Epsilon = float(self.textbox_epsilon.text())
            R = 2
            if self.textbox_r.text():
                R = float(self.textbox_r.text())
            sigma = 1
            if self.textbox_sigma.text():
                sigma = float(self.textbox_sigma.text())
            EpsilonApostrophe = 10e-20
            if self.textbox_epsilon_apostrophe.text():
                EpsilonApostrophe = float(self.textbox_epsilon_apostrophe.text())
            #settings.init()
            #rint(settings.num_of_iterations)
            self.pbar.setMaximum(M)
            x_best, scores = self.NonTabuSearch(f, lowerBound, upperBound, u, l, N, Epsilon, EpsilonApostrophe, Lambda, M, R, sigma)
            #print(settings.num_of_iterations)
            self.display_min_func(x_best, f(x_best), N)
            self.dialog_solution = Solution(x_best, f, N)
            self.dialog_solution.show()
            self.dialog = Second(scores, f)
            self.dialog.show()
            #print(x_best)
        else:
            Lambda = 100
            if self.textbox_lambda.text():
                Lambda = int(self.textbox_lambda.text())
            n_iterations = 5000
            if self.textbox_n_iterations.text():
                n_iterations = int(self.textbox_n_iterations.text())
            Epsilon = 0
            if self.textbox_epsilon.text():
                Epsilon = float(self.textbox_epsilon.text())
            T_max = 10
            if self.textbox_temperature.text():
                T_max = int(self.textbox_temperature.text())
            # perform the simulated annealing search
            self.pbar.setMaximum(T_max-1)
            best, score, scores = self.SimulatedAnnealing(f, lowerBound, upperBound, u, l, n_iterations, N, Epsilon, Lambda, T_max)
            print('Done!')
            print('f(%s) = %f' % (best, score))
            self.display_min_func(best, score, N)
            self.dialog = Second(scores, f)
            self.dialog_solution = Solution(best, f, N)
            self.dialog_solution.show()
            self.dialog.show()




    @pyqtSlot()
    def on_click_delete_function(self):
        self.result_min.setText("")
        self.result_func.setText("")
        self.pbar.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    pal = QPalette()
    pal.setBrush(QPalette.Background, QBrush(QPixmap("./pozadina.png")))
    app.setPalette(pal)
    window.show()
    sys.exit(app.exec_())