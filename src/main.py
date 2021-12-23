import numpy
from numpy.core.fromnumeric import repeat
import pandas as pd

from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer

import pickle
import joblib

dct_read = pickle.load(open("../params/title_movie.p", "rb"))
tf_idf_matrix = pickle.load(open("../model/tf_idf_matrix.p", "rb"))
movies_indices = pickle.load(open("../model/movies_indices.p", "rb"))
                    
similarity = linear_kernel(tf_idf_matrix, tf_idf_matrix)
titles = movies_indices['original_title']
indices = pd.Series(movies_indices.index, index=movies_indices['original_title'])

predic_model = joblib.load("../model/prediction_model.joblib")

tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=10000)
tfidf_vectorizer.fit_transform(movies_indices['overview'])

multilabel_binarizer = MultiLabelBinarizer()
multilabel_binarizer.fit(movies_indices['genres'])

def get_recommendations(title):
    index = indices[title]
    score = list(enumerate(similarity[index]))
    score = sorted(score, key=lambda x: x[1], reverse=True)
    movies_indices = [i[0] for i in score]
    return titles.iloc[movies_indices[1:11]]

def infer_tags(q):
    q_vec = tfidf_vectorizer.transform([q])
    q_pred = predic_model.predict(q_vec)
    return multilabel_binarizer.inverse_transform(q_pred)

def search_menu():
    key = search(dct_read, input('Cari judul filmnya terlebih dahulu: '))
    if not key:
        print("Film tidak ditemukan")
        search_menu()
    else:
        tampil_hasil_pencarian(key)

def search(myDict, lookup):
    listKey =  []
    for key, value in myDict.items():
        if lookup in value['original_title']:
            listKey.append(key)
    return listKey

def tampil_hasil_pencarian(key):
    for i in key:
        print("Movie: ", dct_read[i]['original_title']+",", "id: ", i)

def repeat_menu():
    while True:
        try:
            response = input("Ingin mengulangi program [yes/no]? ")
            if response == "yes":
                pilih_menu()
            elif response == "no":
                print("Terima Kasih")
            else:
                raise Exception("Pilihan tidak tersedia")

            break
        except:
            print("Pilihan tidak tersedia")

def pilih_menu():
    print('1. Rekomendasi movie yang serupa berdasarkan judul film')
    print('2. Prediksi movie genre berdasarkan judul film')

    while True:
        try:
            question = int(input('Pilih menu [1/2], yang akan dilakukan: '))

            if question == 1:
                search_menu()
                print(get_recommendations(dct_read[int(input('Masukkan index film: '))]['original_title']))

                repeat_menu()
            elif question == 2:
                search_menu()
                k = indices[dct_read[int(input('Masukkan index film: '))]['original_title']]
                print("Movie: ", movies_indices['original_title'][k], "\nPredicted genre: ", infer_tags(movies_indices['overview'][k])), print("Actual genre: ",movies_indices['genres'][k], "\n")
                repeat_menu()
            else:
                raise Exception("Pilihan menu tidak tersedia!")
                
            break
        except:
            print("Pilihan menu tidak tersedia!")

pilih_menu()