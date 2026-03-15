import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from matplotlib import pyplot as plt


# Himpunan anggota data suhu, kelembaban dan cahaya
x_suhu = np.arange(0, 51, 1)
suhu = ctrl.Antecedent(x_suhu, "Suhu")

x_kelembapan = np.arange(10, 101, 1)
kelembapan = ctrl.Antecedent(x_kelembapan, "Kelembapan")

x_kesesuaian = np.arange(0, 101, 1)
kesesuaian = ctrl.Antecedent(x_kesesuaian, "Kesesuaian")

""" x_cahaya = np.arange(0, 91, 1)
cahaya = ctrl.Antecedent(x_cahaya, "Cahaya")
 """
# Fungsi keanggotaan
suhu_dingin = fuzz.trapmf(x_suhu, [0, 0, 15, 25])
suhu_normal = fuzz.trapmf(x_suhu, [20, 26, 28, 35])
suhu_panas = fuzz.trapmf(x_suhu, [30, 37, 45, 50])
suhu['Dingin'] = fuzz.trapmf(suhu.universe, [0, 0, 15, 25])
suhu['Normal'] = fuzz.trapmf(suhu.universe, [20, 26, 28, 35])
suhu['Panas'] = fuzz.trapmf(suhu.universe, [30, 37, 45, 50])

kelembapan_basah = fuzz.trapmf(x_kelembapan, [10, 10, 20, 30])
kelembapan_lembab = fuzz.trapmf(x_kelembapan, [25, 40, 60, 75])
kelembapan_kering = fuzz.trapmf(x_kelembapan, [70, 80, 95, 100])
kelembapan['Basah'] = fuzz.trapmf(kelembapan.universe,  [10, 10, 20, 30])
kelembapan['Lembab'] = fuzz.trapmf(kelembapan.universe, [25, 40, 60, 75])
kelembapan['Kering'] = fuzz.trapmf(kelembapan.universe, [70, 80, 95, 100])

S1 = fuzz.trapmf()
S2 = fuzz.trapmf()
S3 = fuzz.trapmf()
N = fuzz.trapmf()

""" cahaya_gelap = fuzz.trapmf(x_cahaya, [0, 0, 20, 40])
cahaya_normal = fuzz.trapmf(x_cahaya, [35, 42, 45, 55])
cahaya_terang = fuzz.trapmf(x_cahaya, [50, 60, 80, 90])
cahaya['Gelap'] = fuzz.trapmf(cahaya.universe, [0, 0, 20, 40])
cahaya['Normal'] = fuzz.trapmf(cahaya.universe, [35, 42, 45, 55])
cahaya['Terang'] = fuzz.trapmf(cahaya.universe, [50, 60, 80, 90])
 """
# grafik plot yang dihasilkan
""" plt.plot(x_suhu, suhu_dingin, 'b', linewidth=1.5, label='Dingin')
plt.plot(x_suhu, suhu_normal, 'g', linewidth=1.5, label='Normal')
plt.plot(x_suhu, suhu_panas, 'r', linewidth=1.5, label='Panas')
plt.title('Derajat Keanggotaan Data Suhu')
plt.legend()
plt.grid()
plt.savefig("foto/derajat_keanggotaan_data_suhu.jpg",dpi=300)
plt.show()

plt.plot(x_kelembapan, kelembapan_basah, 'b', linewidth=1.5, label='Basah')
plt.plot(x_kelembapan, kelembapan_lembab, 'g', linewidth=1.5, label='Lembab')
plt.plot(x_kelembapan, kelembapan_kering, 'r', linewidth=1.5, label='Kering')
plt.title('Derajat Keanggotaan Data Kelembapan')
plt.legend()
plt.grid()
plt.savefig("derajat_keanggotaan_data_kelembapan.jpg",dpi=300)
plt.show()

plt.plot(x_cahaya, cahaya_gelap, 'b', linewidth=1.5, label='Gelap')
plt.plot(x_cahaya, cahaya_normal, 'g', linewidth=1.5, label='Normal')
plt.plot(x_cahaya, cahaya_terang, 'r', linewidth=1.5, label='Terang')
plt.title('Derajat Keanggotaan Data Cahaya')
plt.legend()
plt.grid()
plt.savefig("derajat_keanggotaan_data_cahaya.jpg",dpi=300)
plt.show() """

# Data masukkan: nilai suhu, kelembaban, dan cahaya
#service_score = 9.5
#food_score = 4.0
nilai_suhu = 29
nilai_kelembaban = 83
#nilai_cahaya = 43

kategori_suhu_dingin = fuzz.interp_membership(x_suhu, suhu_dingin, nilai_suhu)
kategori_suhu_normal = fuzz.interp_membership(x_suhu, suhu_normal, nilai_suhu)
kategori_suhu_panas = fuzz.interp_membership(x_suhu, suhu_panas, nilai_suhu)

kategori_kelembaban_basah = fuzz.interp_membership(x_kelembapan, kelembapan_basah, nilai_kelembaban)
kategori_kelembaban_lembab = fuzz.interp_membership(x_kelembapan, kelembapan_lembab, nilai_kelembaban)
kategori_kelembaban_kering = fuzz.interp_membership(x_kelembapan, kelembapan_kering, nilai_kelembaban)

""" kategori_cahaya_gelap = fuzz.interp_membership(x_cahaya, cahaya_gelap, nilai_cahaya)
kategori_cahaya_normal = fuzz.interp_membership(x_cahaya, cahaya_normal, nilai_cahaya)
kategori_cahaya_terang = fuzz.interp_membership(x_cahaya, cahaya_terang, nilai_cahaya)
 """
# Whole config
fig_scale_x = 2.0
fig_scale_y = 1.5
fig = plt.figure(figsize=(6.4 * fig_scale_x, 4.8 * fig_scale_y))
row = 2
col = 3

plt.subplot(row, col, 1)
plt.title("Kualitas Suhu")
plt.plot(x_suhu, suhu_dingin, label="dingin", marker=".")
plt.plot(x_suhu, suhu_normal, label="normal", marker=".")
plt.plot(x_suhu, suhu_panas, label="panas", marker=".")
plt.plot(nilai_suhu, 0.0, label="nilai suhu", marker="D")
plt.plot(nilai_suhu, kategori_suhu_dingin, label="kategori dingin", marker="o")
plt.plot(nilai_suhu, kategori_suhu_normal, label="kategori normal", marker="o")
plt.plot(nilai_suhu, kategori_suhu_panas, label="kategori panas", marker="o")
plt.legend(loc="upper left")

plt.subplot(row, col, 2)
plt.title("Kualitas Kelembaban")
plt.plot(x_kelembapan, kelembapan_basah, label="basah", marker=".")
plt.plot(x_kelembapan, kelembapan_lembab, label="lembab", marker=".")
plt.plot(x_kelembapan, kelembapan_kering, label="kering", marker=".")
plt.plot(nilai_kelembaban, 0.0, label="nilai kelembaban", marker="D")
plt.plot(nilai_kelembaban, kategori_kelembaban_basah, label="kategori basah", marker="o")
plt.plot(nilai_kelembaban, kategori_kelembaban_kering, label="kategori kering", marker="o")
plt.plot(nilai_kelembaban, kategori_kelembaban_lembab, label="kategori lembab", marker="o")
plt.legend(loc="upper left")

plt.subplot(row, col, 3)
plt.title("Kesesuaian")
plt.plot(x_kesesuaian, tip_low, label="low", marker=".")
plt.plot(x_tip, tip_middle, label="middle", marker=".")
plt.plot(x_tip, tip_high, label="high", marker=".")
plt.legend(loc="upper left")

""" plt.subplot(row, col, 3)
plt.title("Kualitas Cahaya")
plt.plot(x_cahaya, cahaya_gelap, label="gelap", marker=".")
plt.plot(x_cahaya, cahaya_normal, label="normal", marker=".")
plt.plot(x_cahaya, cahaya_terang, label="terang", marker=".")
plt.plot(nilai_cahaya, 0.0, label="nilai cahaya", marker="D")
plt.plot(nilai_cahaya, kategori_cahaya_gelap, label="kategori gelap", marker="o")
plt.plot(nilai_cahaya, kategori_cahaya_normal, label="kategori normal", marker="o")
plt.plot(nilai_cahaya, kategori_cahaya_terang, label="kategori terang", marker="o")
plt.legend(loc="upper left")
 """
# =======================================
# Mamdani (max-min) inference method:
# * min because of logic 'and' connective.
# 1) low_degree <-> tip_low
# 2) middle_degree <-> tip_middle
# 3) high_degree <-> tip_high

#S1 = sangat sesuai -> Lahan tidak mempunyai faktor pembatas 
# yang berarti atau nyata terhadap
# penggunaan secara berkelanjutan,
# atau faktor pembatas yang bersifat
# minor dan tidak akan mereduksi
# produktivitas lahan secara nyata.

# suhu= 16-27
# kelembaban = >42
# S1 = suhu dingin & kelembaban basah
# 

#S2 = cukup sesuai -> Lahan mempunyai faktor pembatas,
# dan faktor pembatas ini akan
# berpengaruh terhadap produktivitasnya,
# memerlukan tambahan masukan
# (input). Pembatas tersebut biasanya
# dapat diatasi oleh petani sendiri.

# suhu = 13-16 atau 27-30
# kelembaban = 36-42

#S3 = sesuai marginal -> Lahan mempunyai faktor pembatas
# yang berat, dan faktor pembatas ini
# akan berpengaruh terhadap produktivitasnya,
# memerlukan tambahan
# masukan yang lebih banyak daripada
# lahan yang tergolong S2. Untuk
# mengatasi faktor pembatas pada S3
# memerlukan modal tinggi, sehingga
# perlu adanya bantuan atau campur
# tangan (intervensi) pemerintah atau
# pihak swasta. Tanpa bantuan tersebut
# petani tidak mampu mengatasinya.

# suhu = 10-13 atau 30-35
# kelembaban = 25-36

#N = tidak sesuai -> lahan yang tidak sesuai (N) karena
# mempunyai faktor pembatas yang
# sangat berat dan/atau sulit diatasi.

# suhu = <10 atau >35
# kelembaban = <25


# =======================================
# bad food OR bad service
low_degree = np.fmax(service_low_degree, food_low_degree)
# medium service
middle_degree = service_middle_degree
# good food OR good service
high_degree = np.fmax(service_high_degree, food_high_degree)

plt.subplot(row, col, 4)
plt.title("Some Fuzzy Rules")
t = ("bad food or bad service <-> bad\n"
     "medium service <-> middle\n"
     "good food or good service <-> good")
plt.text(0.1, 0.5, t)

activation_low = np.fmin(low_degree, tip_low)
activation_middle = np.fmin(middle_degree, tip_middle)
activation_high = np.fmin(high_degree, tip_high)

plt.subplot(row, col, 5)
plt.title("Tip Activation: Mamdani Inference Method")

plt.plot(x_tip, activation_low, label="low tip", marker=".")
plt.plot(x_tip, activation_middle, label="middle tip", marker=".")
plt.plot(x_tip, activation_high, label="high tip", marker=".")
plt.legend(loc="upper left")

# Apply the rules:
# * max for aggregation, like or the cases
aggregated = np.fmax(
    activation_low,
    np.fmax(activation_middle, activation_high))

# Defuzzification
tip_centroid = fuzz.defuzz(x_tip, aggregated, 'centroid')
tip_bisector = fuzz.defuzz(x_tip, aggregated, 'bisector')
tip_mom = fuzz.defuzz(x_tip, aggregated, "mom")
tip_som = fuzz.defuzz(x_tip, aggregated, "som")
tip_lom = fuzz.defuzz(x_tip, aggregated, "lom")

print(tip_centroid)
print(tip_bisector)
print(tip_mom)
print(tip_som)
print(tip_lom)

plt.subplot(row, col, 6)
plt.title("Aggregation and Defuzzification")
plt.plot(x_tip, aggregated, label="fuzzy result", marker=".")
plt.plot(tip_centroid, 0.0, label="centroid", marker="o")
plt.plot(tip_bisector, 0.0, label="bisector", marker="o")
plt.plot(tip_mom, 0.0, label="mom", marker="o")
plt.plot(tip_som, 0.0, label="som", marker="o")
plt.plot(tip_lom, 0.0, label="lom", marker="o")
plt.legend(loc="upper left")

plt.savefig("img/7-tipping-problem-mamdani.png")
plt.show()
