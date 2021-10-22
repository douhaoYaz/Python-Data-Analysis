import numpy as np

# 创建一个数值范围为 0~1，间隔为 0.01 的数组 arr1
arr1 = np.arange(0, 1, 0.01)
# print("arr1::")
# print(arr1)

# 创建 100 个服从正态分布的随机数 arr2
arr2 = np.random.standard_normal(100)
# print("arr2:")
# print(arr2)

# 对创建的两个数组 arr1 和 arr2 进行四则运算
plus = arr1 + arr2
minus = arr1 - arr2
multi = arr1 * arr2
divid = arr1 / arr2
# print(divid)

# 将arr2数组重新排列为10行10列的arr3
arr3 = arr2.reshape(10, 10)
# print(arr3)

# 对创建的数组 arr3 进行简单的统计分析
print("arr3纵轴的和：")
print(arr3.sum(axis=0))

print("arr3横轴的和：")
print(arr3.sum(axis=1))

print("arr3的和：")
print(arr3.sum())

print("arr3的均值：")
print(arr3.mean())

print("arr3的标准差：")
print(arr3.std())

print("arr3的方差：")
print(arr3.var())