# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 21:38:29 2026

@author: User
"""

import pandas as pd

df = pd.read_csv(
    r"C:\Users\User\Documents\HIST_PAINEL_COVIDBR_\HIST_PAINEL_COVIDBR_.csv",
    sep=";"
)

print(df.head())

