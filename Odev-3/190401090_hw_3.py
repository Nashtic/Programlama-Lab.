"""
20.04.2020 Monday 23:22:54

@author : Selahattin Ahmed Atasoglu  190401090

Subject : Poisson Distribution with Phyton (Using sympy and matplotlib libraries)
"""

from sympy import Symbol, factorial  # Kütüphanelerin import edilmesi.
from sympy import pprint
import sympy as sym
import matplotlib.pyplot as plt
import sympy.plotting as syp

Lambda = Symbol('lambda')            # Lambda'nın sembolizasyonu
k = Symbol('k')                      # k kadar istenilen olay sayısı


part1 = Lambda**k                    # Lambda^k işleminin yapıldığı kısım.
part2 = sym.exp(-Lambda)             # e^(-Lambda) işleminin yapıldığı kısım.
part3 = sym.factorial(k)             # k! işleminin yapıldığı kısım.


poisson_distribution_func1 = part1*part2            # (Lambda^k)*(e^(-Lambda)) (bölümün üzerinde kalan kısmın işlemleri ve tanımlanması.)
poisson_distribution_func2 = part3                  # k! (bölümün altında kalan kısmın işlemleri ve tanımlanması.)

poisson_distribution_func_total = poisson_distribution_func1/poisson_distribution_func2             # Fonkisyonun tüm partlarının bir ara getirilmesi.

pprint(poisson_distribution_func_total)         # Fonksiyonun günlük yaşamda kullandığımız şekilde yazımı.

syp.plot(poisson_distribution_func_total.subs({Lambda:7}),(k,0,10),title="Poisson Distribution")            # sympy.plotting kütüphanesi ile grafiğin çizdirilmesi.

x_values = []
y_values = []

for value in range(20):                # for in range döngüsü ile grafiğin hangi aralıkta fonksiyonun kullanılacağının belirlenmesi.

    y = poisson_distribution_func_total.subs({Lambda: 7, k: value}).evalf()
    y_values.append(y)          # Listeye ekleme kısmı.
    x_values.append(value)

    print(value, y)

plt.plot(x_values, y_values)
plt.show()                      #Matplotlib kütüphanesiyle yazdırılan grafik.
