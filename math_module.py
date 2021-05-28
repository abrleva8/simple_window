import pickle
import pandas as pd
from sklearn import preprocessing


def predict(clf, data):
    pd_array = pd.DataFrame(data)
    pd_array = preprocessing.scale(pd_array)
    pd_array = pd_array.transpose()
    result = clf.predict(pd_array)
    return result[0]


def predict_from_file(filename, data):
    with open(filename, 'rb') as file:
        clf = pickle.load(file)
        file.close()
    result = predict(clf, data)
    return result


def max_predict(data_sib, data_diet, data_ligur):
    sib_predict = predict_from_file("sibutramin17_05.pkl", data_sib)
    diet_predict = predict_from_file("diet_21_05.pkl", data_diet)
    ligur_predict = predict_from_file("liragrutid_23_05.pkl", data_ligur)
    max_ = max(sib_predict, diet_predict, ligur_predict)
    if sib_predict == max_:
        return sib_predict, "сибутрамин"
    elif diet_predict == max_:
        return diet_predict, "диета"
    else:
        return ligur_predict, "лирагрутид"
