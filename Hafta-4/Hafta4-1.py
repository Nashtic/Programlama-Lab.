#import os
#os.getcwd()

def get_words(my_file=u"C:\\Users\\Selahattin\\Documents\\data.txt"):
    my_list=[]
    f=open(my_file,"r+")
    contents=f.readlines()
    for line in contents:
        #print(line) #noktalardan sonra cümle cümle ayırma yapıyor.
        words=line.split(" ")
        for word in words:  #Kelimeleri tek tek alt alta yazıyor.
            #print(word)
            my_list.append(word) #Kaç kelime olduğunu yazdı.
    #print(contents) #string parse phyton
    f.close()
    return my_list

def get_hist(my_list):
    my_hist={}
    for w in my_list:
        if w in my_hist.keys():
            my_hist[w]=my_hist[w]+1
        else:
            my_hist[w]=1
    return my_hist


def get_files(path_1):
    file_s = [file for file in my_list if os.path.isfile(file)]
    return file_s

lst_1=get_words()
get_hist(lst_1)

import os
my_list=os.listdir()

for item in my_list:
    if os.path.isdir(item):
        print(item)
    if os.path.isfile(item):
        print(item)

dir_s =[dir for dir in my_list if os.path.isdir(dir)]    #dizileri al
file_s=[file for file in my_list if os.path.isfile(file)]  #dosyaları al

dir_s,file_s