import pandas as pd
import numpy as np
import math
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error,mean_squared_error


"""
•	Frekans, Hertz cinsinden
•	Saldiri açisi, derece cinsinden
•	Metre cinsinden akor uzunluğu
•	Serbest akiş hizi, metre/saniye cinsinden.
•	Yer değiştirme kalinliği, metre cinsinden.
Sonuç özelliği:
•	Desibel cinsinden ölçeklendirilmiş ses basinci seviyesi. (kisaltmasi, SBS)

"""

#Normalizasyon = np.linalg.norm(data)
#Standar Sapma = np.std(data)
#Aritmetik medlama = np.average(data)
#Medyan = np.median(data)

dataFile = open("C:/xampp/htdocs/genta/Hasil_Tanaman_with_status - hasil_tanaman.csv")
data = pd.read_csv(dataFile)

def minColumn(data,collumn : int,begin : int,end: int):
    _list = []
    for i in range (begin,end):
        _list.append(data.iloc[:,collumn].to_list()[i])
    return min(_list)
def maxColumn(data,collumn : int,begin : int,end: int):
    _list = []
    for i in range (begin,end):
        _list.append(data.iloc[:,collumn].to_list()[i])
    return max(_list)
def fullDataWithRange(data,collumn : int,begin : int,end: int):
    _list = []
    for i in range (begin,end):
        _list.append(data.iloc[:,collumn].to_list()[i])
    return _list

def fullCollumn(data,collumn : int):
    _list = []
    for i in range (0,1502):
        _list.append(data.iloc[:,collumn].to_list()[i])
    return _list

# Değişkenlerin oluşturulması
x_time = np.array(fullCollumn(data,0))
x_id = np.array(fullCollumn(data,1))
x_suhu = np.array(fullCollumn(data,2))
x_kelembaban_tanah = np.array(fullCollumn(data,3))
x_kelembaban_udara = np.array(fullCollumn(data,4))
x_cahaya = np.array(fullCollumn(data,5))
x_status = np.array(fullCollumn(data,10))

# Üyelik fonksiyonlarının oluşturulması

frekans_low = mf.trimf(x_Frekans, [0, 3500, 7000])
frekans_med = mf.trimf(x_Frekans, [4800, 9400, 14000])
frekans_high = mf.trimf(x_Frekans, [10000, 15000, 20000])

saldiriAcisi_low = mf.trimf(x_SaldiriAcisi, [0, 4, 8])
saldiriAcisi_med = mf.trimf(x_SaldiriAcisi, [6, 10.5, 15])
saldiriAcisi_high = mf.trimf(x_SaldiriAcisi, [10, 17, 23])

akorUzunlugu_low = mf.trimf(x_AkorUzunlugu, [0.01, 0.05, 0.12])
akorUzunlugu_med = mf.trimf(x_AkorUzunlugu, [0.09, 0.16, 0.23])
akorUzunlugu_high = mf.trimf(x_AkorUzunlugu, [0.2, 0.25, 0.308])

serbestAkisHizi_low = mf.trimf(x_SerbestAkisHizi, [28, 36, 45])
serbestAkisHizi_med = mf.trimf(x_SerbestAkisHizi, [40, 50, 60])
serbestAkisHizi_high = mf.trimf(x_SerbestAkisHizi, [53, 68, 80])

yerDegistirme_low = mf.trimf(x_YerDegistirme, [0.0003, 0.01, 0.025])
yerDegistirme_med = mf.trimf(x_YerDegistirme, [0.015, 0.03, 0.042])
yerDegistirme_high = mf.trimf(x_YerDegistirme, [0.03, 0.045, 0.06])

sesBasinci_low = mf.trimf(x_SesBasinci, [100, 110, 120])
sesBasinci_high = mf.trimf(x_SesBasinci, [130 , 135, 143])

# Veri görselleştirme

fig, (ax0, ax1, ax2,ax3,ax4,ax5) = plt.subplots(nrows = 6, figsize =(10, 10))

ax0.plot(x_Frekans, frekans_low, 'r', linewidth = 1, label = 'Düşük')
ax0.plot(x_Frekans, frekans_med, 'g', linewidth = 1, label = 'med')
ax0.plot(x_Frekans, frekans_high, 'b', linewidth = 1, label = 'Yüksek')
ax0.set_title('Frekans')
ax0.legend()

ax1.plot(x_SaldiriAcisi, saldiriAcisi_low, 'r', linewidth = 1, label = 'Düşük')
ax1.plot(x_SaldiriAcisi, saldiriAcisi_med, 'g', linewidth = 1, label = 'med')
ax1.plot(x_SaldiriAcisi, saldiriAcisi_high, 'b', linewidth = 1, label = 'Yüksek')
ax1.set_title('Saldırı Açısı')
ax1.legend()

ax2.plot(x_AkorUzunlugu, akorUzunlugu_low, 'r', linewidth = 1, label = 'Düşük')
ax2.plot(x_AkorUzunlugu, akorUzunlugu_med, 'g', linewidth = 1, label = 'med')
ax2.plot(x_AkorUzunlugu, akorUzunlugu_high, 'b', linewidth = 1, label = 'Yüksek')
ax2.set_title('Akor Uzunluğu')
ax2.legend()

ax3.plot(x_SerbestAkisHizi, serbestAkisHizi_low, 'r', linewidth = 1, label = 'Düşük')
ax3.plot(x_SerbestAkisHizi, serbestAkisHizi_med, 'g', linewidth = 1, label = 'med')
ax3.plot(x_SerbestAkisHizi, serbestAkisHizi_high, 'b', linewidth = 1, label = 'Yüksek')
ax3.set_title('Serbest Akış Hızı')
ax3.legend()

ax4.plot(x_YerDegistirme, yerDegistirme_low, 'r', linewidth = 1, label = 'Düşük')
ax4.plot(x_YerDegistirme, yerDegistirme_med, 'g', linewidth = 1, label = 'med')
ax4.plot(x_YerDegistirme, yerDegistirme_high, 'b', linewidth = 1, label = 'Yüksek')
ax4.set_title('Yer Değiştirme')
ax4.legend()

ax5.plot(x_SesBasinci, sesBasinci_low, 'r', linewidth = 1, label = 'Düşük')
ax5.plot(x_SesBasinci, sesBasinci_high, 'b', linewidth = 1, label = 'Yüksek')
ax5.set_title('Ses Basıncı')
ax5.legend()

#Kullanıcı Girdisi
input_Frekans = 10000
input_SaldiriAcisi = 0
input_AkorUzunlugu = 0.3048
input_SerbestAkisHizi = 71.3
input_YerDegistirme = 0.00266337

frekans_fit_low = fuzz.interp_membership(x_Frekans, frekans_low, input_Frekans)
frekans_fit_med = fuzz.interp_membership(x_Frekans, frekans_med, input_Frekans)
frekans_fit_hig = fuzz.interp_membership(x_Frekans, frekans_high, input_Frekans)

saldiriAcisi_fit_low = fuzz.interp_membership(x_SaldiriAcisi, saldiriAcisi_low, input_SaldiriAcisi)
saldiriAcisi_fit_med = fuzz.interp_membership(x_SaldiriAcisi, saldiriAcisi_med, input_SaldiriAcisi)
saldiriAcisi_fit_hig = fuzz.interp_membership(x_SaldiriAcisi, saldiriAcisi_high, input_SaldiriAcisi)

akorUzunlugu_fit_low = fuzz.interp_membership(x_AkorUzunlugu, akorUzunlugu_low, input_AkorUzunlugu)
akorUzunlugu_fit_med = fuzz.interp_membership(x_AkorUzunlugu, akorUzunlugu_med, input_AkorUzunlugu)
akorUzunlugu_fit_hig = fuzz.interp_membership(x_AkorUzunlugu, akorUzunlugu_high, input_AkorUzunlugu)

serbestAkisHizi_fit_low = fuzz.interp_membership(x_SerbestAkisHizi, serbestAkisHizi_low, input_SerbestAkisHizi)
serbestAkisHizi_fit_med = fuzz.interp_membership(x_SerbestAkisHizi, serbestAkisHizi_med, input_SerbestAkisHizi)
serbestAkisHizi_fit_hig = fuzz.interp_membership(x_SerbestAkisHizi, serbestAkisHizi_high, input_SerbestAkisHizi)

yerDegistirme_fit_low = fuzz.interp_membership(x_YerDegistirme, yerDegistirme_low, input_YerDegistirme)
yerDegistirme_fit_med = fuzz.interp_membership(x_YerDegistirme, yerDegistirme_med, input_YerDegistirme)
yerDegistirme_fit_hig = fuzz.interp_membership(x_YerDegistirme, yerDegistirme_high, input_YerDegistirme)

#BOXPLOT
"""
data.plot(
    kind='box', 
    subplots=True, 
    sharey=False, 
    figsize=(10, 6)
)

# increase spacing between subplots
plt.subplots_adjust(wspace=0.5) 
plt.show()
"""

rule1 = (np.fmin(np.fmin(np.fmax(np.fmin(frekans_low, saldiriAcisi_low),np.fmin(akorUzunlugu_low, serbestAkisHizi_low)), yerDegistirme_low), sesBasinci_low))
rule2 =(np.fmin(np.fmin(np.fmax(np.fmin(frekans_low, saldiriAcisi_low),np.fmin(akorUzunlugu_low, serbestAkisHizi_low)), yerDegistirme_med), sesBasinci_low))
rule3 =(np.fmin(np.fmin(np.fmax(np.fmin(frekans_low, saldiriAcisi_low),np.fmin(akorUzunlugu_low, serbestAkisHizi_med)), yerDegistirme_low), sesBasinci_high))
rule4 =(np.fmin(np.fmin(np.fmax(np.fmin(frekans_low, saldiriAcisi_low),np.fmin(akorUzunlugu_high, serbestAkisHizi_low)), yerDegistirme_high), sesBasinci_high))



out_strong = np.fmax(rule1, rule2)
out_poor = np.fmax(rule3, rule4)

sesBasinci = np.zeros_like(x_SesBasinci)

fig, ax0 = plt.subplots(figsize = (7, 4))
ax0.fill_between(x_SesBasinci, sesBasinci, out_poor, facecolor = 'r', alpha = 0.7)
ax0.plot(x_SesBasinci, sesBasinci_low, 'r', linestyle = '--')
ax0.fill_between(x_SesBasinci, sesBasinci, out_strong, facecolor = 'g', alpha = 0.7)
ax0.plot(x_SesBasinci, sesBasinci_high, 'g', linestyle = '--')
ax0.set_title('Ses Basıncı')

plt.tight_layout()

#Çıkış değeri tahmini
out_brake = np.fmax(out_poor, out_strong)

defuzzified  = fuzz.defuzz(x_SesBasinci, out_brake, 'centroid')

result = fuzz.interp_membership(x_SesBasinci, out_brake, defuzzified)

# Sonuç
cikisDegeri = defuzzified
print("(Ses Basıncı)Çıkış Değeri:", cikisDegeri)

# Veri görselleştirme

fig, ax0 = plt.subplots(figsize=(7, 4))

ax0.plot(x_SesBasinci, sesBasinci_low, 'b', linewidth = 0.5, linestyle = '--')
ax0.plot(x_SesBasinci, sesBasinci_high, 'g', linewidth = 0.5, linestyle = '--')
ax0.fill_between(x_SesBasinci, sesBasinci, out_brake, facecolor = 'Orange', alpha = 1)
ax0.plot([defuzzified , defuzzified], [0, result], 'k', linewidth = 1.5, alpha = 0.9)
ax0.set_title('Ağırlık Merkezi ile Durulaştırma')

plt.tight_layout()

plt.show()
predicted = []

sesBasıncıDegerleri = np.array(fullCollumn(data,5)).tolist()
for i in range(0,1502):
    predicted.append(cikisDegeri - sesBasıncıDegerleri[i])
    
#Weighted Average Method 
sum = 0
for i in range(0,1502):
    sum = sum + sesBasıncıDegerleri[i]

WAM = sum / 1503

MSE = np.square(np.subtract(sesBasıncıDegerleri,predicted)).mean() 
 
RMSE = math.sqrt(MSE)
print("RMSE:")
print(RMSE)
print("MSE:")
print(MSE)
print("WAM:")
print(WAM)
print("Program Tamamlandı.")