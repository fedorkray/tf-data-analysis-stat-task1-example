import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    y = np.log(abs(x - 187))
    y_mean = np.mean(y)
    y_var = np.var(y)
    sigma2_hat = np.maximum(y_var - np.log(y_var/y_mean**2 + 1), 1e-6)
    alpha_hat = np.exp(y_mean - sigma2_hat/2)
    return x.mean() # Ваш ответ
