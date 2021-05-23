import pickle
import pandas as pd
from sklearn import preprocessing


def predict(clf, data_sibutramin):
    pd_array = pd.DataFrame(data_sibutramin)
    pd_array = preprocessing.scale(pd_array)
    pd_array = pd_array.transpose()
    result = clf.predict(pd_array)
    return result[0]


def some_work(filename, data_sibutramin):
    sib_filename = filename
    with open(sib_filename, 'rb') as file:
        clf = pickle.load(file)
        file.close()
    result = predict(clf, data_sibutramin)
    print(f"Принимая {filename} вы похудеете на {result}% в течение 3 месяцев")
