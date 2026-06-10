import numpy as np
import pandas as pd

np.random.seed(42)

data = []

for _ in range(1000):

    modulation = np.random.choice(
        ['BPSK','QPSK','16QAM','64QAM']
    )

    if modulation == 'BPSK':
        f1 = np.random.normal(1,0.2)
        f2 = np.random.normal(0.5,0.2)

    elif modulation == 'QPSK':
        f1 = np.random.normal(2,0.2)
        f2 = np.random.normal(1.5,0.2)

    elif modulation == '16QAM':
        f1 = np.random.normal(3,0.2)
        f2 = np.random.normal(2.5,0.2)

    else:
        f1 = np.random.normal(4,0.2)
        f2 = np.random.normal(3.5,0.2)

    data.append([f1,f2,modulation])

df = pd.DataFrame(
    data,
    columns=['feature1','feature2','label']
)

print(df.head())
