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

sample_sizes = [1000, 1000, 100, 10]
mse_thresholds = [0.231, 0.0231, 0.0573, 0.232]

for i in range(len(sample_sizes)):
x = np.random.lognormal(2, 0.5, sample_sizes[i]) + 187
alpha = estimate_alpha(x)
mse = ((alpha - 2)**2)
if mse < mse_thresholds[i]:
print(f"Test {i+1}: Passed")
else:
print(f"Test {i+1}: Failed")
