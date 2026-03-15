from simpful import *

FS = FuzzySystem()

# Define fuzzy sets for the variable suhu
""" S_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=15), term="dingin")
S_2 = FuzzySet(function=Triangular_MF(a=16, b=26, c=30), term="normal")
S_3 = FuzzySet(function=Triangular_MF(a=31, b=37, c=45), term="panas") 
LVSuhu = LinguisticVariable([S_1, S_2, S_3], concept="Kualitas Suhu", universe_of_discourse=[0,50]) """
LVSuhu = AutoTriangle(3, terms=['dingin', 'normal', 'panas'], universe_of_discourse=[10,35])
FS.add_linguistic_variable("Suhu", LVSuhu)
#LVSuhu.plot()

 # Define fuzzy sets for the variable kelembapan
""" K_1 = FuzzySet(function=Triangular_MF(a=0, b=10, c=20, d=30), term="basah")
K_2 = FuzzySet(function=Triangular_MF(a=25, b=40, c=60, d=70), term="lembap")
K_3 = FuzzySet(function=Triangular_MF(a=25, b=40, c=60, d=90), term="lembap")
LVKelembapan = LinguisticVariable([K_1, K_2], concept="Kualitas Kelembapan", universe_of_discourse=[0,90]) """
LVKelembapan = AutoTriangle(3, terms=['kering', 'lembap', 'basah'], universe_of_discourse=[0,100])
FS.add_linguistic_variable("Kelembapan", LVKelembapan)
#LVKelembapan.plot()

 # Define output crisp
""" KS_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=30), term="S1") 
KS_2 = FuzzySet(function=Triangular_MF(a=0, b=0, c=45), term="S2")
KS_3 = FuzzySet(function=Triangular_MF(a=0, b=0, c=60), term="S3")
KS_N = FuzzySet(function=Triangular_MF(a=0, b=0, c=75), term="N") """
LVoutput = AutoTriangle(4, terms=['S1','S2','S3','N'], universe_of_discourse=[0,26]) 
#FS.add_linguistic_variable("Kesesuaian", LinguisticVariable([KS_1, KS_2, KS_3, KS_N], universe_of_discourse=[0,100]))
FS.add_linguistic_variable("Kesesuaian", LVoutput)
#LVoutput.plot()

# Define the fuzzy rules
RULE1 = "IF (Suhu IS dingin) AND (Kelembapan IS lembap) THEN (Kesesuaian IS S1)"
RULE2 = "IF (Suhu IS dingin) OR (Suhu IS normal) AND (Kelembapan IS lembap) THEN (Kesesuaian IS S2)"
RULE3 = "IF (Suhu IS dingin) OR (Suhu IS panas) AND (Kelembapan IS lembap) THEN (Kesesuaian IS S3)"
RULE4 = "IF (Suhu IS dingin) OR (Suhu IS panas) AND (Kelembapan IS basah) THEN (Kesesuaian IS N)"

 # Add fuzzy rules to the fuzzy reasoner object
FS.add_rules([RULE1, RULE2, RULE3, RULE4])

 # Set antecedent values
FS.set_variable("Suhu", 25)
FS.set_variable("Kelembapan", 89)

 # Perform Mamdani inference and print output
print(FS.Mamdani_inference(["Kesesuaian"]))
