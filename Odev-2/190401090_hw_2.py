import sys

input,output=sys.argv[1],sys.argv[2]

def dict_ile_frekans(list_2):

    dict_frekans = {}

    for item in list_2:
        item=int(item)
        if item in dict_frekans :
            dict_frekans[item] = dict_frekans[item] + 1
        else:
            dict_frekans[item] = 1

    print(dict_frekans)
    return dict_frekans

def bubble_sort(list_1):

    n = len(list_1)

    for i in range(n):
        for j in range(0, n - i - 1):
            if list_1[j] > list_1[j + 1]:
                list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]

    return list_1

def dict_ile_mod(my_hist_d):

    max_frekans = -1
    mod = -1

    for key_deger in my_hist_d.keys():
        if my_hist_d[key_deger] > max_frekans:
            max_frekans = my_hist_d[key_deger]
            mod = key_deger

    return mod,max_frekans

def medyan_bul(dizi_1):

    dizi_1 = bubble_sort(dizi_1)

    if len(dizi_1)%2 == 1:
        orta = int(len(dizi_1)/2)+1
        return dizi_1[orta-1]
    else:
        medyan1,medyan2=dizi_1[int(len(dizi_1)/2)],dizi_1[int(len(dizi_1)/2)-1]
        return (medyan1+medyan2)/2

def liste_ortalamasi(liste_1):

    toplam = 0
    value = 0

    for item in liste_1:
        toplam += int(item)
        value += 1
    return int(toplam/value)

with open(input+"input_hw_2.csv", "r") as dosya:

    veri = []
    veri_1 = dosya.read()
    veri_line = veri_1.split(';')
    veri.append(veri_line)
    tarih = []
    bol = []

    for i in range(3, len(veri_line), 3):
        bol.append(veri_line[i].split("-"))

    tum_aylar = []

    for i in range(len(bol)):
        tum_aylar.append(int(bol[i][1]))

bubble_sort(tum_aylar)
value_2 = dict_ile_frekans(tum_aylar)
son_liste = [value_2[i] for i in value_2]


with open(output+"190401090_hw_2_output.txt", "w") as dosya:

    dosya.write("Medyan :"+ "" + str(medyan_bul(son_liste))+"\n")
    dosya.write("Ortalama:" + ""+ str(liste_ortalamasi(son_liste)))
