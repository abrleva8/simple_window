from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox

import math_module
import person


class UiMainWindow(object):
    text_edits = []
    data_sibutramin = []
    data_diet = []
    data_liragrutid = []
    data = []
    person2 = None

    def __init__(self, main_window_):
        self.statusbar = QtWidgets.QStatusBar(main_window_)
        self.menubar = QtWidgets.QMenuBar(main_window_)
        self.centralwidget = QtWidgets.QWidget(main_window_)
        self.te_snils = QtWidgets.QTextEdit(self.centralwidget)
        self.l_snils = QtWidgets.QLabel(self.centralwidget)
        self.btn_prediction = QtWidgets.QPushButton(self.centralwidget)
        self.te_insulin = QtWidgets.QTextEdit(self.centralwidget)
        self.l_insulin = QtWidgets.QLabel(self.centralwidget)
        self.te_pulse = QtWidgets.QTextEdit(self.centralwidget)
        self.l_pulse = QtWidgets.QLabel(self.centralwidget)
        self.te_waist = QtWidgets.QTextEdit(self.centralwidget)
        self.l_waist = QtWidgets.QLabel(self.centralwidget)
        self.te_weight = QtWidgets.QTextEdit(self.centralwidget)
        self.l_weight = QtWidgets.QLabel(self.centralwidget)
        self.te_noms_index_ir = QtWidgets.QTextEdit(self.centralwidget)
        self.l_noms_index_ir = QtWidgets.QLabel(self.centralwidget)
        self.te_glucose = QtWidgets.QTextEdit(self.centralwidget)
        self.l_glucose = QtWidgets.QLabel(self.centralwidget)
        self.te_hips_girph = QtWidgets.QTextEdit(self.centralwidget)
        self.l_hips_girph = QtWidgets.QLabel(self.centralwidget)
        self.te_height = QtWidgets.QTextEdit(self.centralwidget)
        self.l_height = QtWidgets.QLabel(self.centralwidget)
        self.te_tg = QtWidgets.QTextEdit(self.centralwidget)
        self.l_tg = QtWidgets.QLabel(self.centralwidget)
        self.te_lpnp = QtWidgets.QTextEdit(self.centralwidget)
        self.l_lpnp = QtWidgets.QLabel(self.centralwidget)
        self.te_lpvp = QtWidgets.QTextEdit(self.centralwidget)
        self.l_lpvp = QtWidgets.QLabel(self.centralwidget)
        self.te_ohs = QtWidgets.QTextEdit(self.centralwidget)
        self.l_ohs = QtWidgets.QLabel(self.centralwidget)
        self.cb_mzo = QtWidgets.QComboBox(self.centralwidget)
        self.l_mzo = QtWidgets.QLabel(self.centralwidget)
        self.cb_pet = QtWidgets.QComboBox(self.centralwidget)
        self.l_pet = QtWidgets.QLabel(self.centralwidget)

    def setup_ui(self, main_window_):
        main_window_.setObjectName("MainWindow")
        main_window_.resize(763, 346)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window_.sizePolicy().hasHeightForWidth())
        font = QtGui.QFont()
        font.setPointSize(11)
        main_window_.setSizePolicy(size_policy)

        self.centralwidget.setObjectName("centralwidget")

        self.l_snils.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.l_snils.setFont(font)
        self.l_snils.setAlignment(QtCore.Qt.AlignCenter)
        self.l_snils.setObjectName("l_snils")
        self.l_snils.setToolTip("СНИЛС")

        self.te_snils.setGeometry(QtCore.QRect(100, 10, 104, 31))
        self.te_snils.setObjectName("te_snils")
        self.te_snils.setToolTip("Введите положительное число")
        self.text_edits.append(self.te_snils)

        self.l_pet.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.l_pet.setFont(font)
        self.l_pet.setAlignment(QtCore.Qt.AlignCenter)
        self.l_pet.setToolTip("Проходил ли пацинет позитронно-эмиссионную томографию?")
        self.l_pet.setObjectName("l_pet")

        self.cb_pet.setGeometry(QtCore.QRect(100, 50, 104, 31))
        self.cb_pet.setFont(font)
        self.cb_pet.setObjectName("cb_pet")
        self.cb_pet.addItem("")
        self.cb_pet.addItem("")
        self.text_edits.append(self.cb_pet)

        self.l_mzo.setGeometry(QtCore.QRect(10, 90, 71, 31))
        self.l_mzo.setFont(font)
        self.l_mzo.setAlignment(QtCore.Qt.AlignCenter)
        self.l_mzo.setToolTip("МЗО - метаболически нездоровое ожирение\nМНО - международное нормализованное отношение")
        self.l_mzo.setObjectName("l_mzo")

        self.cb_mzo.setGeometry(QtCore.QRect(100, 90, 104, 31))
        self.cb_mzo.setFont(font)
        self.cb_mzo.setObjectName("cb_mzo")
        self.cb_mzo.addItem("")
        self.cb_mzo.addItem("")
        self.text_edits.append(self.cb_mzo)

        self.l_ohs.setGeometry(QtCore.QRect(10, 130, 71, 31))
        self.l_ohs.setFont(font)
        self.l_ohs.setAlignment(QtCore.Qt.AlignCenter)
        self.l_ohs.setObjectName("l_ohs")
        self.l_ohs.setToolTip("Общий холестирин ммоль/л")

        self.te_ohs.setGeometry(QtCore.QRect(100, 130, 104, 31))
        self.te_ohs.setObjectName("te_ohs")
        self.te_ohs.setToolTip("Введите число от 2 до 9")
        self.text_edits.append(self.te_ohs)

        self.l_lpvp.setGeometry(QtCore.QRect(10, 170, 71, 31))
        self.l_lpvp.setFont(font)
        self.l_lpvp.setAlignment(QtCore.Qt.AlignCenter)
        self.l_lpvp.setObjectName("l_lpvp")
        self.l_lpvp.setToolTip("Липопротеины высокой плотности ммоль/л")

        self.te_lpvp.setGeometry(QtCore.QRect(100, 170, 104, 31))
        self.te_lpvp.setObjectName("te_lpvp")
        self.te_lpvp.setToolTip("Введите число от 0 до 3")
        self.text_edits.append(self.te_lpvp)

        self.l_lpnp.setGeometry(QtCore.QRect(240, 10, 71, 31))
        self.l_lpnp.setFont(font)
        self.l_lpnp.setAlignment(QtCore.Qt.AlignCenter)
        self.l_lpnp.setObjectName("l_lpnp")
        self.l_lpnp.setToolTip("Липопротеины низкой плотности ммоль/л")

        self.te_lpnp.setGeometry(QtCore.QRect(330, 10, 104, 31))
        self.te_lpnp.setObjectName("te_lpnp")
        self.te_lpnp.setToolTip("Введите число от 1.5 до 5")
        self.text_edits.append(self.te_lpnp)

        self.l_tg.setGeometry(QtCore.QRect(220, 50, 111, 31))
        self.l_tg.setFont(font)
        self.l_tg.setAlignment(QtCore.Qt.AlignCenter)
        self.l_tg.setObjectName("l_tg")
        self.l_tg.setToolTip("Тиреоглобулин нг/мл")

        self.te_tg.setGeometry(QtCore.QRect(330, 50, 104, 31))
        self.te_tg.setObjectName("te_tg")
        self.te_tg.setToolTip("Введите число от 0.7 до 5")
        self.text_edits.append(self.te_tg)

        self.l_height.setGeometry(QtCore.QRect(240, 90, 71, 31))
        self.l_height.setFont(font)
        self.l_height.setAlignment(QtCore.Qt.AlignCenter)
        self.l_height.setObjectName("l_height")
        self.l_height.setToolTip("Рост см")

        self.te_height.setGeometry(QtCore.QRect(330, 90, 104, 31))
        self.te_height.setObjectName("te_height")
        self.te_height.setToolTip("Введите число от 150 до 200")
        self.text_edits.append(self.te_height)

        self.l_hips_girph.setGeometry(QtCore.QRect(210, 130, 101, 31))
        self.l_hips_girph.setFont(font)
        self.l_hips_girph.setAlignment(QtCore.Qt.AlignCenter)
        self.l_hips_girph.setObjectName("l_hips_girph")
        self.l_hips_girph.setToolTip("Обхват бедер см")

        self.te_hips_girph.setGeometry(QtCore.QRect(330, 130, 104, 31))
        self.te_hips_girph.setObjectName("te_hips_girph")
        self.te_hips_girph.setToolTip("Введите число от 80 до 120")
        self.text_edits.append(self.te_hips_girph)

        self.l_glucose.setGeometry(QtCore.QRect(240, 170, 71, 31))
        self.l_glucose.setFont(font)
        self.l_glucose.setAlignment(QtCore.Qt.AlignCenter)
        self.l_glucose.setObjectName("l_glucose")
        self.l_glucose.setToolTip("Уровень глюкозы натощак ммоль/л")

        self.te_glucose.setGeometry(QtCore.QRect(330, 170, 104, 31))
        self.te_glucose.setObjectName("te_glucose")
        self.te_glucose.setToolTip("Введите число от 4 до 7")
        self.text_edits.append(self.te_glucose)

        self.l_noms_index_ir.setGeometry(QtCore.QRect(470, 10, 141, 31))
        self.l_noms_index_ir.setFont(font)
        self.l_noms_index_ir.setAlignment(QtCore.Qt.AlignCenter)
        self.l_noms_index_ir.setObjectName("l_noms_index_ir")
        self.l_noms_index_ir.setToolTip("Индекс инсулинорезистентности")

        self.te_noms_index_ir.setGeometry(QtCore.QRect(610, 10, 104, 31))
        self.te_noms_index_ir.setObjectName("te_noms_index_ir")
        self.te_noms_index_ir.setToolTip("Введите число от 2 до 23")
        self.text_edits.append(self.te_noms_index_ir)

        self.l_weight.setGeometry(QtCore.QRect(480, 50, 141, 31))
        self.l_weight.setFont(font)
        self.l_weight.setAlignment(QtCore.Qt.AlignCenter)
        self.l_weight.setObjectName("l_weight")
        self.l_weight.setToolTip("Вес кг")

        self.te_weight.setGeometry(QtCore.QRect(610, 50, 104, 31))
        self.te_weight.setObjectName("te_weight")
        self.te_weight.setToolTip("Введите число от 70 до 160")
        self.text_edits.append(self.te_weight)

        self.l_waist.setGeometry(QtCore.QRect(480, 90, 141, 31))
        self.l_waist.setFont(font)
        self.l_waist.setAlignment(QtCore.Qt.AlignCenter)
        self.l_waist.setObjectName("l_waist")
        self.l_waist.setToolTip("Обхват талии см")

        self.te_waist.setGeometry(QtCore.QRect(610, 90, 104, 31))
        self.te_waist.setObjectName("te_waist")
        self.te_waist.setToolTip("Введите число от 85 до 150")
        self.text_edits.append(self.te_waist)

        self.l_pulse.setGeometry(QtCore.QRect(480, 130, 141, 31))
        self.l_pulse.setFont(font)
        self.l_pulse.setAlignment(QtCore.Qt.AlignCenter)
        self.l_pulse.setObjectName("l_pulse")
        self.l_pulse.setToolTip("Пульс ударов/мин")

        self.te_pulse.setGeometry(QtCore.QRect(610, 130, 104, 31))
        self.te_pulse.setObjectName("te_pulse")
        self.te_pulse.setToolTip("Введите число от 50 до 100")
        self.text_edits.append(self.te_pulse)

        self.l_insulin.setGeometry(QtCore.QRect(480, 170, 141, 31))
        self.l_insulin.setFont(font)
        self.l_insulin.setAlignment(QtCore.Qt.AlignCenter)
        self.l_insulin.setObjectName("l_insulin")
        self.l_insulin.setToolTip("Инсулин мкЕд/мл")

        self.te_insulin.setGeometry(QtCore.QRect(610, 170, 104, 31))
        self.te_insulin.setObjectName("te_insulin")
        self.te_insulin.setToolTip("Введите число от 72 до 335")
        self.text_edits.append(self.te_insulin)

        self.btn_prediction.setGeometry(QtCore.QRect(320, 230, 121, 51))
        self.btn_prediction.setObjectName("btn_prediction")
        self.btn_prediction.clicked.connect(self.get_data_from_label)

        main_window_.setCentralWidget(self.centralwidget)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        main_window_.setMenuBar(self.menubar)

        self.statusbar.setObjectName("statusbar")
        main_window_.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window_)
        QtCore.QMetaObject.connectSlotsByName(main_window_)

    def retranslate_ui(self, main_window_):
        _translate = QtCore.QCoreApplication.translate
        main_window_.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.l_weight.setText(_translate("MainWindow", "Вес"))
        self.l_waist.setText(_translate("MainWindow", "Обхват талии"))
        self.l_pulse.setText(_translate("MainWindow", "Пульс"))
        self.l_insulin.setText(_translate("MainWindow", "Инсулин"))

    def get_data_from_label(self):
        self.data_sibutramin = []
        self.data_diet = []
        self.data_liragrutid = []
        self.data = []
        for text_edit in self.text_edits:
            if text_edit in [self.te_snils, self.cb_pet, self.cb_mzo, self.te_ohs, self.te_lpvp, self.te_lpnp,
                             self.te_tg, self.te_height, self.te_hips_girph, self.te_glucose, self.te_noms_index_ir,
                             self.te_weight, self.te_waist, self.te_pulse, self.te_insulin]:
                if text_edit in [self.cb_pet, self.cb_mzo]:
                    self.data.append(text_edit.currentText())
                    continue
                self.data.append(text_edit.toPlainText())
        self.person2 = person.Person(self.data)
        if not self.person2.is_good_data():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Введены некорректные данные!")
            msg.setInformativeText("Внимательно проверьте и введите ещё раз!")
            msg.setWindowTitle("Ошибка!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return False
        for text_edit in self.text_edits:
            if text_edit in [self.te_snils]:
                continue
            if text_edit in [self.te_height, self.te_glucose, self.te_hips_girph, self.te_noms_index_ir]:
                data_to_add_diet = text_edit.toPlainText()
                self.data_diet.append(float(data_to_add_diet))
                continue
            elif text_edit in [self.te_weight, self.te_waist, self.te_pulse, self.te_insulin]:
                data_to_add_diet = text_edit.toPlainText()
                self.data_liragrutid.append(float(data_to_add_diet))
                continue
            elif text_edit == self.cb_pet:
                data_to_add_sibutramin = 1 if text_edit.currentText() == 'да' else 0
            elif text_edit == self.cb_mzo:
                data_to_add_sibutramin = 1 if text_edit.currentText() == 'МЗО' else 0
            else:
                data_to_add_sibutramin = text_edit.toPlainText()
            self.data_sibutramin.append(float(data_to_add_sibutramin))

        # print(self.data_sibutramin)
        # print(self.data_diet)
        # print(self.data_liragrutid)

        math_module.some_work("sibutramin17_05.pkl", self.data_sibutramin)
        math_module.some_work("diet_21_05.pkl", self.data_diet)
        math_module.some_work("liragrutid_23_05.pkl", self.data_liragrutid)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow(main_window)
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
