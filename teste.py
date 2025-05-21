import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold

#trocar essa url pelo caminho da base spam de vocês.
Spam = pd.read_csv("Cadernos Grupo Python\\Validação Cruzada\\spam.csv")
XSpam = Spam.loc[:, Spam.columns != "type"]
YSpam = Spam["type"]

kfSpam = StratifiedKFold(n_splits=10, shuffle=True, random_state=11).split(XSpam, YSpam)

kfSpamLista = list(kfSpam)

for i, (train, test) in enumerate(kfSpamLista, 1):
    print(train)
    print(test)
    print(f"K: {i}\nTreino: {len(train)}\nTeste: {len(test)}")
    if i == 3:
        break

