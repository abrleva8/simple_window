from PyQt5 import QtCore, QtGui, QtWidgets

import pickle
import pandas as pd
from sklearn import preprocessing

class Ui_MainWindow(object):

    data_sibutramin = []
    data_diet = []
    labels = []
    text_edits = []


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.l_snils = QtWidgets.QLabel(self.centralwidget)
        self.l_snils.setGeometry(QtCore.QRect(50, 10, 71, 31))
        self.l_snils.setFont(font)
        self.l_snils.setAlignment(QtCore.Qt.AlignCenter)
        self.l_snils.setObjectName("l_snils")

        self.te_snils = QtWidgets.QTextEdit(self.centralwidget)
        self.te_snils.setGeometry(QtCore.QRect(140, 10, 104, 31))
        self.te_snils.setObjectName("te_snils")

        self.l_pet = QtWidgets.QLabel(self.centralwidget)
        self.l_pet.setGeometry(QtCore.QRect(50, 50, 71, 31))
        self.l_pet.setFont(font)
        self.l_pet.setAlignment(QtCore.Qt.AlignCenter)
        self.l_pet.setObjectName("l_pet")

        self.cb_pet = QtWidgets.QComboBox(self.centralwidget)
        self.cb_pet.setGeometry(QtCore.QRect(140, 50, 104, 31))
        self.cb_pet.setFont(font)
        self.cb_pet.setObjectName("cb_pet")
        self.cb_pet.addItem("")
        self.cb_pet.addItem("")
        self.text_edits.append(self.cb_pet)

        self.l_mzo = QtWidgets.QLabel(self.centralwidget)
        self.l_mzo.setGeometry(QtCore.QRect(50, 90, 71, 31))
        self.l_mzo.setFont(font)
        self.l_mzo.setAlignment(QtCore.Qt.AlignCenter)
        self.l_mzo.setObjectName("l_mzo")

        self.cb_mzo = QtWidgets.QComboBox(self.centralwidget)
        self.cb_mzo.setGeometry(QtCore.QRect(140, 90, 104, 31))
        self.cb_mzo.setFont(font)
        self.cb_mzo.setObjectName("cb_mzo")
        self.cb_mzo.addItem("")
        self.cb_mzo.addItem("")
        self.text_edits.append(self.cb_mzo)

        self.l_ohs = QtWidgets.QLabel(self.centralwidget)
        self.l_ohs.setGeometry(QtCore.QRect(50, 130, 71, 31))
        self.l_ohs.setFont(font)
        self.l_ohs.setAlignment(QtCore.Qt.AlignCenter)
        self.l_ohs.setObjectName("l_ohs")

        self.te_ohs = QtWidgets.QTextEdit(self.centralwidget)
        self.te_ohs.setGeometry(QtCore.QRect(140, 130, 104, 31))
        self.te_ohs.setObjectName("te_ohs")
        self.text_edits.append(self.te_ohs)

        self.l_lpnp = QtWidgets.QLabel(self.centralwidget)
        self.l_lpnp.setGeometry(QtCore.QRect(50, 210, 71, 31))
        self.l_lpnp.setFont(font)
        self.l_lpnp.setAlignment(QtCore.Qt.AlignCenter)
        self.l_lpnp.setObjectName("l_lpnp")

        self.te_lpnp = QtWidgets.QTextEdit(self.centralwidget)
        self.te_lpnp.setGeometry(QtCore.QRect(140, 210, 104, 31))
        self.te_lpnp.setObjectName("te_lpnp")
        self.text_edits.append(self.te_lpnp)

        self.l_lpvp = QtWidgets.QLabel(self.centralwidget)
        self.l_lpvp.setGeometry(QtCore.QRect(50, 170, 71, 31))
        self.l_lpvp.setFont(font)
        self.l_lpvp.setAlignment(QtCore.Qt.AlignCenter)
        self.l_lpvp.setObjectName("l_lpvp")

        self.te_lpvp = QtWidgets.QTextEdit(self.centralwidget)
        self.te_lpvp.setGeometry(QtCore.QRect(140, 170, 104, 31))
        self.te_lpvp.setObjectName("te_lpvp")
        self.text_edits.append(self.te_lpvp)

        self.l_tg = QtWidgets.QLabel(self.centralwidget)
        self.l_tg.setGeometry(QtCore.QRect(30, 250, 111, 31))
        self.l_tg.setFont(font)
        self.l_tg.setAlignment(QtCore.Qt.AlignCenter)
        self.l_tg.setObjectName("l_tg")

        self.te_tg = QtWidgets.QTextEdit(self.centralwidget)
        self.te_tg.setGeometry(QtCore.QRect(140, 250, 104, 31))
        self.te_tg.setObjectName("te_tg")
        self.text_edits.append(self.te_tg)

        self.l_height = QtWidgets.QLabel(self.centralwidget)
        self.l_height.setGeometry(QtCore.QRect(50, 290, 71, 31))
        self.l_height.setFont(font)
        self.l_height.setAlignment(QtCore.Qt.AlignCenter)
        self.l_height.setObjectName("l_height")

        self.te_height = QtWidgets.QTextEdit(self.centralwidget)
        self.te_height.setGeometry(QtCore.QRect(140, 290, 104, 31))
        self.te_height.setObjectName("te_height")
        self.text_edits.append(self.te_height)

        self.l_hips_girph = QtWidgets.QLabel(self.centralwidget)
        self.l_hips_girph.setGeometry(QtCore.QRect(20, 330, 101, 31))
        self.l_hips_girph.setFont(font)
        self.l_hips_girph.setAlignment(QtCore.Qt.AlignCenter)
        self.l_hips_girph.setObjectName("l_hips_girph")

        self.te_hips_girph = QtWidgets.QTextEdit(self.centralwidget)
        self.te_hips_girph.setGeometry(QtCore.QRect(140, 330, 104, 31))
        self.te_hips_girph.setObjectName("te_hips_girph")
        self.text_edits.append(self.te_hips_girph)

        self.l_noms_index_ir = QtWidgets.QLabel(self.centralwidget)
        self.l_noms_index_ir.setGeometry(QtCore.QRect(0, 410, 141, 31))
        self.l_noms_index_ir.setFont(font)
        self.l_noms_index_ir.setAlignment(QtCore.Qt.AlignCenter)
        self.l_noms_index_ir.setObjectName("l_noms_index_ir")

        self.te_noms_index_ir = QtWidgets.QTextEdit(self.centralwidget)
        self.te_noms_index_ir.setGeometry(QtCore.QRect(140, 410, 104, 31))
        self.te_noms_index_ir.setObjectName("te_noms_index_ir")
        self.text_edits.append(self.te_noms_index_ir)

        self.l_glucose = QtWidgets.QLabel(self.centralwidget)
        self.l_glucose.setGeometry(QtCore.QRect(50, 370, 71, 31))
        self.l_glucose.setFont(font)
        self.l_glucose.setAlignment(QtCore.Qt.AlignCenter)
        self.l_glucose.setObjectName("l_glucose")

        self.te_glucose = QtWidgets.QTextEdit(self.centralwidget)
        self.te_glucose.setGeometry(QtCore.QRect(140, 370, 104, 31))
        self.te_glucose.setObjectName("te_glucose")
        self.text_edits.append(self.te_glucose)


        self.btn_prediction = QtWidgets.QPushButton(self.centralwidget)
        self.btn_prediction.setGeometry(QtCore.QRect(300, 300, 121, 51))
        self.btn_prediction.setObjectName("btn_prediction")
        self.btn_prediction.clicked.connect(self.get_data_from_label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l_snils.setText(_translate("MainWindow", "СНИЛС"))
        self.l_tg.setText(_translate("MainWindow", "ТГ"))
        self.l_ohs.setText(_translate("MainWindow", "ОХС"))
        self.l_lpvp.setText(_translate("MainWindow", "ЛПВП"))
        self.l_mzo.setText(_translate("MainWindow", "МЗО/МНО"))
        self.cb_mzo.setItemText(0, _translate("MainWindow", "МЗО"))
        self.cb_mzo.setItemText(1, _translate("MainWindow", "МНО"))
        self.cb_pet.setItemText(0, _translate("MainWindow", "да"))
        self.cb_pet.setItemText(1, _translate("MainWindow", "нет"))
        self.l_pet.setText(_translate("MainWindow", "ПЭТ"))
        self.btn_prediction.setText(_translate("MainWindow", "Предсказать"))
        self.l_lpnp.setText(_translate("MainWindow", "ЛПНП"))
        self.l_noms_index_ir.setText(_translate("MainWindow", "Индекс Нома - IR"))
        self.l_hips_girph.setText(_translate("MainWindow", "Обхват бедер"))
        self.l_height.setText(_translate("MainWindow", "Рост"))
        self.l_glucose.setText(_translate("MainWindow", "Глюкоза"))


    def get_data_from_label(self):
        self.data_sibutramin = []
        self.data_diet = []
        for text_edit in self.text_edits:
            if text_edit in [self.te_height, self.te_glucose, self.te_hips_girph, self.te_noms_index_ir]:
                data_to_add_diet = text_edit.toPlainText()
                self.data_diet.append(float(data_to_add_diet))
                continue
            elif text_edit == self.cb_pet:
                data_to_add_sibutramin = 1 if text_edit.currentText() == 'да' else 0
            elif text_edit == self.cb_mzo:
                data_to_add_sibutramin = 1 if text_edit.currentText() == 'МЗО' else 0
            else:
                data_to_add_sibutramin = text_edit.toPlainText()
            self.data_sibutramin.append(float(data_to_add_sibutramin))
        print(*self.data_sibutramin)
        print(*self.data_diet)
        sib_filename = "sibutramin17_05.pkl"
        diet_filename = "diet_21_05.pkl"
        with open(sib_filename, 'rb') as file:
            sib_clf_sib = pickle.load(file)
            file.close()
        with open(diet_filename, 'rb') as diet_file:
            sib_clf_diet = pickle.load(diet_file)
        # print(sib_clf)
        pd_array = pd.DataFrame(self.data_sibutramin)
        pd_array = preprocessing.scale(pd_array)
        pd_array = pd_array.transpose()
        result = sib_clf_sib.predict(pd_array)
        pd_array_diet = pd.DataFrame(self.data_diet)
        pd_array_diet = preprocessing.scale(pd_array_diet)
        pd_array_diet = pd_array_diet.transpose()
        result_diet = sib_clf_diet.predict(pd_array_diet)
        print("Принимая сибутрамин вы похудеете на " + str(*result) + "% в течение 3 месяцев")
        print("Соблюдая диету вы похудеете на " + str(*result_diet) + "% в течение 3 месяцев")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
