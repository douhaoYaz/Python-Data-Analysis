import numpy as np
import cv2 as cv
from PIL import Image

# 读入图像，获得像素 RGB 值
img = cv.imread("lena.jpg")
r = img[:, :, 2]
g = img[:, :, 1]
b = img[:, :, 0]

# 将图像转换为灰度图
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# 构建虚拟深度值depth，其取值范围为0~100，此处先预设为10
depth = 10

# 利用梯度函数来获得 x 轴和 y 轴的梯度
grad = np.gradient(img_gray)
grad_x, grad_y = grad
print(grad_x, grad_y, sep='\n\n')

# 根据深度调整 x 和 y 方向的梯度值，同时也是对深度值的归一化
grad_x *= depth/100
grad_y *= depth/100

# 预设虚拟光源俯角和方位角的弧度值，求出光源对 x、 y、 z 轴的影响
vec_el = np.pi / 2.3    # Elevation的弧度表示
vec_az = np.pi /4       # Azimuth的弧度表示
# np.cos(vec_el)为单位光线在地平面上的投影长度
dx = np.cos(vec_el) * np.cos(vec_az)
dy = np.cos(vec_el) * np.sin(vec_az)
dz = np.sin(vec_el)

# 光源归一化后将梯度转化为灰度
# 构造x和y轴梯度的三维归一化单位坐标系
# 获取图像平面的单位法向量
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A
# 梯度与光源相互作用，将梯度转化为灰度
grey = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)

# 为避免数据越界，将生成的灰度值裁剪至0~255之间
grey = grey.clip(0, 255)

#  图像重构，并显示
img_final = Image.fromarray(grey.astype('uint8'))
img_final.save("./newImage.jpg")
