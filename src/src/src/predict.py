print("AI Modulation Classifier")

feature1=float(input("Feature1: "))
feature2=float(input("Feature2: "))

if feature1 < 1.5:
    print("BPSK")

elif feature1 < 2.5:
    print("QPSK")

elif feature1 < 3.5:
    print("16QAM")

else:
    print("64QAM")
