# import numpy as np
# # 数据
# years = [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001]
# Y = np.array([137.16, 124.56, 107.91, 102.96, 125.24, 162.45, 217.43, 253.42, 251.07, 285.85, 327.26])
# X1 = np.array([1181.4, 1375.7, 1501.2, 1700.6, 2026.6, 2577.4, 3496.2, 4283.0, 4838.9, 5160.3, 5425.1])
# X2 = np.array([115.96, 133.35, 128.21, 124.85, 122.49, 129.86, 139.52, 140.44, 139.12, 133.35, 126.39])
# # 构建 X 矩阵
# X = np.column_stack((np.ones(len(Y)), X1, X2))
# # 计算参数估计值
# beta_hat = np.linalg.inv(X.T @ X) @ X.T @ Y
# print("估计的参数值：")
# print("beta_0:", beta_hat[0])
# print("beta_1:", beta_hat[1])
# print("beta_2:", beta_hat[2])


import numpy as np
from scipy.optimize import fsolve

def equation(x):
    return 0.0001 * x*x - 0.0714 * x +8.8
# 猜测一个初始值
initial_guess =100
root = fsolve(equation, initial_guess)
print(root)