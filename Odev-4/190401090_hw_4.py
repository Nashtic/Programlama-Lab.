'''

    @author : Selahattin Ahmed Ataşoğlu - 190401090

    28.04.2020 - Salı - 12.20

'''


def insertItemToHeap(myheap_1, item):  #Eklenmek isteneni heap durumumdaki arraye heap olacak şekilde ekler.
    myheap_1.append(item)                 #Bu fonksiyonla eleman ekledikten sonra tekrar heap haline getirilir.
    index_value = len(myheap_1) - 1
    if index_value <= 0:
        return
    parent_value = (index_value - 1) // 2
    while parent_value >= 0 and myheap_1[parent_value] > myheap_1[index_value]:
        myheap_1[parent_value], myheap_1[index_value] = myheap_1[index_value], myheap_1[parent_value]
        index_value = parent_value
        parent_value = (index_value - 1) // 2


def removeItemFrom(myheap_1):  # Heapten son elemanı silen fonksiyondur.
    index = len(myheap_1)
    if index <= 0:                   # Eğer hiçbir eleman kalmadıysa silinecek bir şey yoktur.
        print("Heapte hiç eleman yok...")         # Uyarı mesajı verir.
        return                       # Tekrar kontrol için return yapar.
    myheap_1.pop()

def heapi_sirala(dizi):  #Heap kullanılacak array'i alır ve sort ettikten sonra değerini döndürür
    dizi = dizi.copy()      # Array hiç değiştirilmeden aynı şekilde kopyalanarak array değişkenine yazılır.
    heap_olustur(dizi)
    sorted_array = []   # Sıralı olarak yazdırılacak dizi için yer ayırılır.
    for _ in range(len(dizi)):         # Bu işlem array'in uzunluğu boyunca devam edecektir.
        dizi[0], dizi[-1] = dizi[-1], dizi[0]
        sorted_array.append(dizi.pop())
        min_heapify_function(dizi, 0)
    return sorted_array


def min_heapify_function(array, i):  #Diziyi heap haline getirir, parentlarla karşılaştırma işlemi yapılır.
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify_function(array, smallest)


def heap_olustur(array):  # (n/2) den 0'a kadar olan düğümleri minheapfy'a aktarır. n = array uzunluğu.
    for p in reversed(range(len(array) // 2)):
        min_heapify_function(array, p)




dizi_1 = [8, 10, 3, 4, 7, 15, 1, 2, 16]     # Kullanacağımız dizimiz.
heap_olustur(dizi_1)                        # Dizinin Heap buildi yapılır.
print(dizi_1)

insertItemToHeap(dizi_1, 22)             # Heap'e elle yeni itemlar eklenir.
insertItemToHeap(dizi_1, 6)
insertItemToHeap(dizi_1, 13)
insertItemToHeap(dizi_1, 8)
insertItemToHeap(dizi_1, 14)
insertItemToHeap(dizi_1, -59)
insertItemToHeap(dizi_1, 5)
insertItemToHeap(dizi_1, 96)
insertItemToHeap(dizi_1, -4)
insertItemToHeap(dizi_1, -2)

removeItemFrom(dizi_1)               # Itemların eklenmesinden sonra heapteki en son eleman bir bir silinir.
removeItemFrom(dizi_1)
removeItemFrom(dizi_1)
removeItemFrom(dizi_1)
removeItemFrom(dizi_1)
removeItemFrom(dizi_1)
removeItemFrom(dizi_1)
removeItemFrom(dizi_1)

print(dizi_1)
print(sorted(dizi_1))