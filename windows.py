import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from typing import Final

import math_module
import person

count_of_var: Final = 15


def about_information():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Внимание!")
    msg.setInformativeText("Программа предназначена только для врачей с соответствующей специализацией!\n"
                           "Использование лекарств не по назначению может привести к нежелательным исходам!")
    msg.setWindowTitle("Предсказание метода лечения")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def error_windows(text, inf_text, title_text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(text)
    msg.setInformativeText(inf_text)
    msg.setWindowTitle(title_text)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


class UiMainWindow(object):
    text_edits = []
    data_sibutramin = []
    data_diet = []
    data_liragrutid = []
    data = []
    person2 = person.Person([""] * count_of_var)
    drugs = None

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
        self.cb_sex = QtWidgets.QComboBox(self.centralwidget)
        self.l_sex = QtWidgets.QLabel(self.centralwidget)
        self.te_result = QtWidgets.QTextEdit(self.centralwidget)
        self.l_result = QtWidgets.QLabel(self.centralwidget)
        self.has_result = False

    def setup_ui(self, main_window_):
        main_window_.setObjectName("MainWindow")
        main_window_.resize(850, 346)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window_.sizePolicy().hasHeightForWidth())
        font = QtGui.QFont()
        font.setPointSize(11)
        main_window_.setSizePolicy(size_policy)

        self.centralwidget.setObjectName("centralwidget")

        self.l_snils.setGeometry(QtCore.QRect(10, 10, 130, 31))
        self.l_snils.setFont(font)
        self.l_snils.setAlignment(QtCore.Qt.AlignCenter)
        self.l_snils.setObjectName("l_snils")
        self.l_snils.setToolTip("СНИЛС")

        self.te_snils.setGeometry(QtCore.QRect(150, 10, 104, 31))
        self.te_snils.setObjectName("te_snils")
        self.te_snils.setToolTip("Введите СНИЛС в форме XXX-XXX-XX YY")
        # self.te_snils.setText("")
        self.te_snils.textChanged.connect(self.some_work)
        self.text_edits.append(self.te_snils)

        self.l_pet.setGeometry(QtCore.QRect(10, 50, 130, 31))
        self.l_pet.setFont(font)
        self.l_pet.setAlignment(QtCore.Qt.AlignCenter)
        self.l_pet.setToolTip("Проходил ли пацинет позитронно-эмиссионную томографию?")
        self.l_pet.setObjectName("l_pet")

        self.cb_pet.setGeometry(QtCore.QRect(150, 50, 104, 31))
        self.cb_pet.setFont(font)
        self.cb_pet.setObjectName("cb_pet")
        self.cb_pet.addItem("")
        self.cb_pet.addItem("")
        self.text_edits.append(self.cb_pet)

        self.l_mzo.setGeometry(QtCore.QRect(10, 90, 130, 31))
        self.l_mzo.setFont(font)
        self.l_mzo.setAlignment(QtCore.Qt.AlignCenter)
        self.l_mzo.setToolTip("МЗО - метаболически здоровое ожирение\nМНО - метаболически нездоровое ожирение")
        self.l_mzo.setObjectName("l_mzo")

        self.cb_mzo.setGeometry(QtCore.QRect(150, 90, 104, 31))
        self.cb_mzo.setFont(font)
        self.cb_mzo.setObjectName("cb_mzo")
        self.cb_mzo.addItem("")
        self.cb_mzo.addItem("")
        self.text_edits.append(self.cb_mzo)

        self.l_ohs.setGeometry(QtCore.QRect(10, 130, 130, 31))
        self.l_ohs.setFont(font)
        self.l_ohs.setAlignment(QtCore.Qt.AlignCenter)
        self.l_ohs.setObjectName("l_ohs")
        self.l_ohs.setToolTip("Общий холестирин, ммоль/л")

        self.te_ohs.setGeometry(QtCore.QRect(150, 130, 104, 31))
        self.te_ohs.setObjectName("te_ohs")
        self.te_ohs.setToolTip("Введите число от 2 до 9")
        self.te_ohs.textChanged.connect(self.some_work)
        self.text_edits.append(self.te_ohs)

        self.l_lpvp.setGeometry(QtCore.QRect(10, 170, 130, 31))
        self.l_lpvp.setFont(font)
        self.l_lpvp.setAlignment(QtCore.Qt.AlignCenter)
        self.l_lpvp.setObjectName("l_lpvp")
        self.l_lpvp.setToolTip("Липопротеины высокой плотности, ммоль/л")

        self.te_lpvp.setGeometry(QtCore.QRect(150, 170, 104, 31))
        self.te_lpvp.setObjectName("te_lpvp")
        self.te_lpvp.setToolTip("Введите число от 0 до 3")
        self.te_lpvp.textChanged.connect(self.some_work)
        self.text_edits.append(self.te_lpvp)

        self.l_lpnp.setGeometry(QtCore.QRect(270, 10, 180, 31))
        self.l_lpnp.setFont(font)
        self.l_lpnp.setAlignment(QtCore.Qt.AlignCenter)
        self.l_lpnp.setObjectName("l_lpnp")
        self.l_lpnp.setToolTip("Липопротеины низкой плотности, ммоль/л")

        self.te_lpnp.setGeometry(QtCore.QRect(430, 10, 104, 31))
        self.te_lpnp.setObjectName("te_lpnp")
        self.te_lpnp.setToolTip("Введите число от 1.5 до 5")
        self.te_lpnp.textChanged.connect(self.some_work)
        self.text_edits.append(self.te_lpnp)

        self.l_tg.setGeometry(QtCore.QRect(270, 50, 180, 31))
        self.l_tg.setFont(font)
        self.l_tg.setAlignment(QtCore.Qt.AlignCenter)
        self.l_tg.setObjectName("l_tg")
        self.l_tg.setToolTip("Тиреоглобулин, нг/мл")

        self.te_tg.setGeometry(QtCore.QRect(430, 50, 104, 31))
        self.te_tg.setObjectName("te_tg")
        self.te_tg.setToolTip("Введите число от 0.7 до 5")
        self.te_tg.textChanged.connect(self.some_work)
        self.text_edits.append(self.te_tg)

        self.l_height.setGeometry(QtCore.QRect(270, 90, 180, 31))
        self.l_height.setFont(font)
        self.l_height.setAlignment(QtCore.Qt.AlignCenter)
        self.l_height.setObjectName("l_height")
        self.l_height.setToolTip("Рост, см")

        self.te_height.setGeometry(QtCore.QRect(430, 90, 104, 31))
        self.te_height.setObjectName("te_height")
        self.te_height.setToolTip("Введите число от 150 до 200")
        self.te_height.textChanged.connect(self.some_work)
        self.text_edits.append(self.te_height)

        self.l_hips_girph.setGeometry(QtCore.QRect(270, 130, 180, 31))
        self.l_hips_girph.setFont(font)
        self.l_hips_girph.setAlignment(QtCore.Qt.AlignCenter)
        self.l_hips_girph.setObjectName("l_hips_girph")
        self.l_hips_girph.setToolTip("Обхват бедер, см")

        self.te_hips_girph.setGeometry(QtCore.QRect(430, 130, 104, 31))
        self.te_hips_girph.setObjectName("te_hips_girph")
        self.te_hips_girph.setToolTip("Введите число от 80 до 120")
        self.te_hips_girph.textChanged.connect(self.some_work)
        self.text_edits.append(self.te_hips_girph)

        self.l_glucose.setGeometry(QtCore.QRect(270, 170, 180, 31))
        self.l_glucose.setFont(font)
        self.l_glucose.setAlignment(QtCore.Qt.AlignCenter)
        self.l_glucose.setObjectName("l_glucose")
        self.l_glucose.setToolTip("Уровень глюкозы натощак, ммоль/л")

        self.te_glucose.setGeometry(QtCore.QRect(430, 170, 104, 31))
        self.te_glucose.setObjectName("te_glucose")
        self.te_glucose.setToolTip("Введите число от 4 до 7")
        self.te_glucose.textChanged.connect(self.some_work)
        self.text_edits.append(self.te_glucose)

        self.cb_sex.setGeometry(QtCore.QRect(710, 10, 104, 31))
        self.cb_sex.setFont(font)
        self.cb_sex.setObjectName("cb_sex")
        self.cb_sex.addItem("")
        self.cb_sex.addItem("")
        self.text_edits.append(self.cb_sex)

        self.l_sex.setGeometry(QtCore.QRect(550, 10, 180, 31))
        self.l_sex.setFont(font)
        self.l_sex.setAlignment(QtCore.Qt.AlignCenter)
        self.l_sex.setToolTip("Пол пациента")
        self.l_sex.setObjectName("l_sex")

        self.l_weight.setGeometry(QtCore.QRect(550, 50, 180, 31))
        self.l_weight.setFont(font)
        self.l_weight.setAlignment(QtCore.Qt.AlignCenter)
        self.l_weight.setObjectName("l_weight")
        self.l_weight.setToolTip("Вес кг")

        self.te_weight.setGeometry(QtCore.QRect(710, 50, 104, 31))
        self.te_weight.setObjectName("te_weight")
        self.te_weight.setToolTip("Введите число от 70 до 160")
        self.te_weight.textChanged.connect(self.some_work)
        self.text_edits.append(self.te_weight)

        self.l_waist.setGeometry(QtCore.QRect(550, 90, 180, 31))
        self.l_waist.setFont(font)
        self.l_waist.setAlignment(QtCore.Qt.AlignCenter)
        self.l_waist.setObjectName("l_waist")
        self.l_waist.setToolTip("Обхват талии, см")

        self.te_waist.setGeometry(QtCore.QRect(710, 90, 104, 31))
        self.te_waist.setObjectName("te_waist")
        self.te_waist.setToolTip("Введите число от 85 до 150")
        self.te_waist.textChanged.connect(self.some_work)
        self.text_edits.append(self.te_waist)

        self.l_pulse.setGeometry(QtCore.QRect(550, 130, 180, 31))
        self.l_pulse.setFont(font)
        self.l_pulse.setAlignment(QtCore.Qt.AlignCenter)
        self.l_pulse.setObjectName("l_pulse")
        self.l_pulse.setToolTip("Пульс, ударов/мин")

        self.te_pulse.setGeometry(QtCore.QRect(710, 130, 104, 31))
        self.te_pulse.setObjectName("te_pulse")
        self.te_pulse.setToolTip("Введите число от 50 до 100")
        self.te_pulse.textChanged.connect(self.some_work)
        self.text_edits.append(self.te_pulse)

        self.l_insulin.setGeometry(QtCore.QRect(550, 170, 180, 31))
        self.l_insulin.setFont(font)
        self.l_insulin.setAlignment(QtCore.Qt.AlignCenter)
        self.l_insulin.setObjectName("l_insulin")
        self.l_insulin.setToolTip("Инсулин, мкЕд/мл")

        self.te_insulin.setGeometry(QtCore.QRect(710, 170, 104, 31))
        self.te_insulin.setObjectName("te_insulin")
        self.te_insulin.setToolTip("Введите число от 72 до 335")
        self.te_insulin.textChanged.connect(self.some_work)
        self.text_edits.append(self.te_insulin)

        self.l_result.setGeometry(QtCore.QRect(420, 230, 141, 31))
        self.l_result.setFont(font)
        self.l_result.setAlignment(QtCore.Qt.AlignCenter)
        self.l_result.setObjectName("l_result")

        self.te_result.setGeometry(QtCore.QRect(535, 220, 250, 61))
        self.te_result.setObjectName("te_result")
        self.te_result.setReadOnly(True)

        self.btn_prediction.setGeometry(QtCore.QRect(90, 230, 116, 51))
        self.btn_prediction.setObjectName("btn_prediction")
        self.btn_prediction.clicked.connect(self.get_data_from_label)
        # self.btn_prediction.

        main_window_.setCentralWidget(self.centralwidget)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")

        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")

        main_window_.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.statusbar.setObjectName("statusbar")
        main_window_.setStatusBar(self.statusbar)

        self.action_save = QtWidgets.QAction(main_window_)
        self.action_save.setObjectName("actionSave")
        self.action_save.triggered.connect(self.file_save)
        # self.action_save.triggered.connect(partial(self.file_save, self.drugs))
        self.menu_file.addAction(self.action_save)

        self.action_about = QtWidgets.QAction(main_window_)
        self.action_about.setObjectName("action_about")
        self.action_about.triggered.connect(about_information)
        self.menu_help.addAction(self.action_about)

        self.retranslate_ui(main_window_)
        QtCore.QMetaObject.connectSlotsByName(main_window_)

    def retranslate_ui(self, main_window_):
        _translate = QtCore.QCoreApplication.translate
        main_window_.setWindowTitle(_translate("MainWindow", "Предсказание метода лечения"))
        self.menu_file.setTitle(_translate("MainWindow", "Файл"))
        self.menu_help.setTitle(_translate("MainWindow", "Помощь"))
        self.l_snils.setText(_translate("MainWindow", "СНИЛС"))
        self.l_tg.setText(_translate("MainWindow", "ТГ, нг/мл"))
        self.l_ohs.setText(_translate("MainWindow", "ОХС, ммоль/л"))
        self.l_lpvp.setText(_translate("MainWindow", "ЛПВП, ммоль/л"))
        self.l_mzo.setText(_translate("MainWindow", "МЗО/МНО"))
        self.cb_mzo.setItemText(0, _translate("MainWindow", "МЗО"))
        self.cb_mzo.setItemText(1, _translate("MainWindow", "МНО"))
        self.cb_pet.setItemText(0, _translate("MainWindow", "да"))
        self.cb_pet.setItemText(1, _translate("MainWindow", "нет"))
        self.cb_sex.setItemText(0, _translate("MainWindow", "муж"))
        self.cb_sex.setItemText(1, _translate("MainWindow", "жен"))
        self.l_pet.setText(_translate("MainWindow", "ПЭТ"))
        self.l_sex.setText(_translate("MainWindow", "Пол"))
        self.btn_prediction.setText(_translate("MainWindow", "Предсказать"))
        self.l_lpnp.setText(_translate("MainWindow", "ЛПНП, ммоль/л"))
        self.l_hips_girph.setText(_translate("MainWindow", "Обхват бедер, см"))
        self.l_height.setText(_translate("MainWindow", "Рост, см"))
        self.l_glucose.setText(_translate("MainWindow", "Глюкоза, ммоль/л"))
        self.l_weight.setText(_translate("MainWindow", "Вес, кг"))
        self.l_waist.setText(_translate("MainWindow", "Обхват талии, см"))
        self.l_pulse.setText(_translate("MainWindow", "Пульс, уд/мин"))
        self.l_insulin.setText(_translate("MainWindow", "Инсулин, мкЕд/мл"))
        self.l_result.setText(_translate("MainWindow", "Результат"))
        self.action_save.setText(_translate("MainWindow", "Сохранить"))
        self.action_about.setText(_translate("MainWindow", "О программе"))

    def some_work(self):
        self.data = []
        for text_edit in self.text_edits:
            if text_edit in [self.cb_pet, self.cb_mzo, self.cb_sex]:
                self.data.append(text_edit.currentText())
                continue
            self.data.append(text_edit.toPlainText())
        self.person2 = person.Person(self.data)
        flag = self.person2.is_good_data()
        self.btn_prediction.setDisabled(not flag)
        flag = flag and self.has_result
        print(self.has_result)
        self.action_save.setDisabled(not flag)

    def get_data_from_label(self):
        self.data_sibutramin = []
        self.data_diet = []
        self.data_liragrutid = []
        if not self.person2.is_good_data():
            error_windows("Введены некорректные данные!", "Внимательно проверьте и введите ещё раз!", "Ошибка!")
            return False
        for text_edit in self.text_edits:
            if text_edit in [self.te_snils]:
                continue
            if text_edit in [self.te_height, self.te_glucose, self.te_hips_girph]:
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
            elif text_edit in [self.cb_sex, self.te_result]:
                continue
            else:
                data_to_add_sibutramin = text_edit.toPlainText()
            self.data_sibutramin.append(float(data_to_add_sibutramin))
        self.data_diet.append(self.person2.index_noma)

        print(self.data_sibutramin)
        print(self.data_diet)
        print(self.data_liragrutid)

        res_number, res_drug, self.drugs = math_module.max_predict(self.data_sibutramin, self.data_diet,
                                                                   self.data_liragrutid)
        self.action_save.setDisabled(False)
        verb = "Соблюдая" if res_drug == "диетy" else "Принимая"
        self.te_result.setPlainText(f"{verb} {res_drug} пациент похудеет на {res_number}% в течение 3 месяцев")

    def file_save(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(None, "QFileDialog.getSaveFileName()", "", "All Files (*);;Python "
                                                                                              "Files (*.py)",
                                                   options=options)
        try:
            file = open(file_name, 'w')
            file.close()
        except FileNotFoundError:
            print('Файл не существует!')
        if os.path.isfile(file_name) and self.person2.is_good_data():
            file = open(file_name, 'w')
            text = self.person2.data_to_save()
            text = text + self.drugs.using()
            file.write(text)
            file.close()
        else:
            error_windows("Файл не был создан!", "Внимательно проверьте и введите ещё раз!", "Ошибка!")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow(main_window)
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
