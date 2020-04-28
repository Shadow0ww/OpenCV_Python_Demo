# 笛卡尔坐标转换为极坐标
#   通常利用极坐标变换来矫正图像中的圆形物体或倍包含在圆环中的物体
#   笛卡尔坐标系任意一点(x,y)，以(x',y')为中心，以下公式变换为极坐标系θor上的极坐标(θ,r):
#       r =  √((x - x')² + (y - y')²) ,θ = | 2π + arctan(y - y' ,x - x'), y - y'≤0
#                                            | arctan2(y - y' ,x - x'), y - y'＞0

# 例：(11, 13) 以(3, 5)为圆心进行极坐标变换
import math

r = math.sqrt(math.pow(11 - 3, 2) + pow(13 - 5, 2))
theta = math.atan2(13 - 5, 11 - 3) / math.pi * 180  # 转换为角度
print(r)
print(theta)

#   OpenCV提供函数：
#       cv2.cartToPolar(x, y[, magnitude[, angle[, angleInDegrees ]]])
#       __________________________________________________________________________
#       |   参数          | 解释                                                 |
#       |-----------------|------------------------------------------------------|
#       | x               | array数组且数据类型为浮点型、float32或float64        |
#       | y               | 和x相同尺寸的array数组                               |
#       | angleInDegrees  | 当值为True时，返回值angle是角度，反之是弧度          |
#       --------------------------------------------------------------------------

#  例：将(0,0)、(1,0)、(2,0)、(0,1)、(1,1)、(2,1)、(0,2)、(1,2)、(2,2)九个点以(1,1)为中心变换
#       先将原点坐标移动到(1,1)处
#       九个点的横纵坐标分别对应x,y的3*3的ndarray中，也可以都放在9*1的ndarray中，只要一一对应就行
import cv2
import numpy as np

x = np.array([[0, 1, 2], [0, 1, 2], [0, 1, 2]], np.float64) - 1
y = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]], np.float64) - 1
r, theta = cv2.cartToPolar(x, y, angleInDegrees=True)
print(r)
print(theta)

x2 = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2], np.float64) - 1
y2 = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2], np.float64) - 1
r2, theta2 = cv2.cartToPolar(x2, y2, angleInDegrees=True)
print(r2)
print(theta2)

# 极坐标转换为笛卡尔坐标
#   已知极坐标(θ,r)和笛卡尔坐标(x', y')
#       x = x' + r * cosθ
#       y = y' + r * sinθ
#   OpenCV提供函数：
#       cv2.polarToCart(magnitude, angle[, x[, y[, angleInDegrees ]]])
#       参数列表类似cartToPolar
#       注意：返回坐标是以(0,0)为中心的笛卡尔坐标，即已知(θ,r)和(x', y')，计算出的是(x-x', y-y')

#   例：已知极坐标(θ,r)中的(30, 10)、(31， 10)、(30，11)、(31, 11)其中θ以角度表示,变换中心(-12,15)

import cv2
import numpy as np

angle = np.array([[30, 31], [30, 31]], np.float32)
r = np.array([[10, 10], [11, 11]], np.float32)
x3, y3 = cv2.polarToCart(r, angle, angleInDegrees=True)
x3 += -12
y3 += 15
print(x3)
print(y3)
