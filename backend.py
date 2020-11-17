import sys
from PyQt5 import QtWidgets,QtGui,QtCore,QtCore
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication,QMainWindow,QMessageBox,QFileDialog,QInputDialog
from PyQt5.QtGui import QImage, QPixmap
from ui import Ui_HeartDiseases

import Heartdisease
"""
Object Names to Access Data:


---To access data widgets---
[
    age
    sex
    chestPain
    restingBP
    serumCholestrol
    fastingBP
    restingECG
    maxHeartRate
    ExcerciseAngina
    STDepression
    PeakExercise
    NoMajorVessels
    Thalassemia
]
---To access buttons---
[
    clearBtn
    submitBtn
]

"""

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui=Ui_HeartDiseases()
        self.ui.setupUi(self)
        self.ui.submitBtn.clicked.connect(lambda: self.test_input())
        self.ui.clearBtn.clicked.connect(lambda: self.clfn())
        #self.showMaximized()  --Enbale to show maximized
    def clfn(self):

            self.ui.age.clear()
            self.ui.sex.clear()
            self.ui.chestPain.clear()
            self.ui.restingBP.clear()
            self.ui.serumCholestrol.clear()
            self.ui.fastingBP.clear()
            self.ui.restingECG.clear()
            self.ui.maxHeartRate.clear()
            self.ui.ExcerciseAngina.clear()
            self.ui.STDepression.clear()
            self.ui.PeakExercise.clear()
            self.ui.NoMajorVessels.clear()
            self.ui.Thalassemia.clear()
            self.ui.label_28.setPixmap(QtGui.QPixmap("H2.jpg"))
            '''super(MainWindow, self).__init__()
            self.ui.setupUi(self)
            self.ui.submitBtn.clicked.connect(lambda: self.test_input())
            self.ui.clearBtn.clicked.connect(lambda: self.clfn())'''

    def test_input(self) -> None:

        
        my_dict= {'age':self.ui.age.text(),'sex':self.ui.sex.text(),'cp':self.ui.chestPain.text(),
                  'trestbps':self.ui.restingBP.text(),
                  'chol':self.ui.serumCholestrol.text(),'fbs':self.ui.fastingBP.text(),
                  'restecg':self.ui.restingECG.text(),'thalach':self.ui.maxHeartRate.text(),
                  'exang':self.ui.ExcerciseAngina.text(),'oldpeak':self.ui.STDepression.text(),
                  'slope':self.ui.PeakExercise.text(),'ca':self.ui.NoMajorVessels.text(),
                  'thal':self.ui.Thalassemia.text()}
        
        output = Heartdisease.check_input(my_dict)

        if output == 0:

            print("Diagnosis suggests that patient does not suffer from heartdisease.")

            self.ui.label_28.setPixmap(QtGui.QPixmap("H3.jpg"))

        else:

            print("Our diagnosis suggests patient suffers from heartdisease.\nPlease get checked soon.")
            self.ui.label_28.setPixmap(QtGui.QPixmap("H1.jpg"))




if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())