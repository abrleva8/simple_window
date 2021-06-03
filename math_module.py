import pickle
import pandas as pd
import drug
from sklearn import preprocessing


def predict(clf, data):
    pd_array = pd.DataFrame(data)
    pd_array = preprocessing.scale(pd_array)
    pd_array = pd_array.transpose()
    result = clf.predict(pd_array)
    return round(result[0], 2)


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
        return sib_predict, "сибутрамин", drug.Sibutramin()
    elif diet_predict == max_:
        return diet_predict, "диетy", drug.Diet()
    else:
        return ligur_predict, "лираглутид", drug.Liraglutid()
