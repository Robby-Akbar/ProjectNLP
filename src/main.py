import pandas as pd

import pickle
dct_read = pickle.load(open("../params/title_movie.p", "rb"))

def search(myDict, lookup):
    listKey =  []
    for key, value in myDict.items():
        if lookup in value['original_title']:
            listKey.append(key)
    return listKey

def tampil_hasil_pencarian(key):
    for i in key:
        print("Movie: ", dct_read[i]['original_title']+",", "id: ", i)

def pilih_menu():
    print('1. Rekomendasi movie yang serupa berdasarkan judul film')
    print('2. Prediksi movie genre berdasarkan judul film')

    while True:
        try:
            question = int(input('Pilih menu [1/2], yang akan dilakukan: '))

            if question == 1:
                key = search(dct_read, input('Cari judul filmnya terlebih dahulu: '))
                tampil_hasil_pencarian(key)
            elif question == 2:
                print('Cool')
            else:
                raise Exception("Pilihan menu tidak tersedia!")

            break
        except:
            print("Pilihan menu tidak tersedia!")

pilih_menu()