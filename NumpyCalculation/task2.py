import numpy as np

# 创建一个 8× 8 矩阵全 0 矩阵 mat1
arr = np.zeros((8, 8))
# 把 1、 3、 5、 7 行的 0、 2、 4、 6 列的元素设置为 1
for i in range(arr.shape[0]):
    if i%2 != 0:
        for j in range(arr.shape[1]):
            if j%2 == 0:
                arr[i][j] = 1
mat1 = np.matrix(arr)

# 创建生成两个2*2 矩阵 mat2 和 mat3 并计算矩阵的乘积
mat2 = np.matrix(np.random.randint(1, 10, (2, 2)))
mat3 = np.matrix(np.random.randint(1, 10, (2, 2)))
mat2_3 = mat2  * mat3

# 创建方阵 mat4，求其转置矩阵 mat5，并计算它们的行列式值
mat4 = np.matrix(np.random.randint(1, 10, (3, 3)))
mat5 = np.transpose(mat4)
det4 = np.linalg.det(mat4)
det5 = np.linalg.det(mat5)

# 创建矩阵 mat6， 对其进行奇异值分解
mat6 = np.matrix(np.random.randint(1, 10, (3, 3)))
u, s, v = np.linalg.svd(mat6)
print(mat6, '\n')
print(u, '\n\n', s, '\n\n', v, '\n\n')
mat6_verif = u * np.diag(s) * v
print(mat6_verif)

# 求出 mat6*mat6.T 的特征值和特征向量
e, v = np.linalg.eig(mat6 * mat6.T)
print(e, v, sep='\n\n')
print("酉方阵u 与 特征向量v是否相等：", np.isclose(u, v), sep='\n')
print("一般对角阵s 与 特征值e的平方根是否相等：", np.isclose(s, e ** 0.5))