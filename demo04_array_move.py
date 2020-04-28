import cv2
import numpy as np

#   计算仿射矩阵：解方程组法、基本仿射矩阵相乘法
#   1.方程法
#       放射变换矩阵有六个未知数，只需要三组对应位置坐标，构造六个方程组成方程组即可解。
#       OpenCV提供函数 cv2.getAffineTransform(src, dst) 可计算src远点坐标到dst变换后的坐标的放射变换矩阵A
src = np.array([[0, 0], [200, 0], [0, 200]], np.float32)
dst = np.array([[0, 0], [100, 0], [0, 100]], np.float32)
A = cv2.getAffineTransform(src, dst)
print(A)

#   2.矩阵法
#       矩阵相乘法计算仿射矩阵，前提是需要知道基本仿射的变换步骤（平移、缩放、旋转）
#       如果先缩放再平移，则变换后的矩阵形式：
#               [[x'],[y'],[1]] = [[1,0,Tx],[0,1,Ty],[0,0,1]] *
#                                 [[Sx,0,0],[0,Sy,0],[0,0,1]] *
#                                 [[x],[y],[1]]
#       看出，仿射变换矩阵是平移矩阵 * 缩放矩阵得到的。
#           注：运算从右侧向左侧开始，即先缩放，再平移
#       Numpy使用dot函数实现矩阵乘法
#   例：先等比缩放2倍，然后再水平防线上移100

s = np.array([[0.5, 0, 0], [0, 0.5, 0], [0, 0, 1]])  # 缩放矩阵
t = np.array([[1, 0, 100], [0, 1, 200], [0, 0, 1]])  # 平移矩阵
A = np.dot(t, s)  # 矩阵相乘
print(A)

p = np.array([[100], [200], [1]])
B = np.dot(A, p)
print(B)

#       如果先以（X0，Y0）为中心进行缩放，再逆时针旋转α，则仿射变换矩阵：
#               A = [[1,0,Xo],[0,1,Yo],[0,0,1]] *
#                   ([[Cosα,Sinα,0],[-Sinα,Cosα,0],[0,0,1]] * [[Sx,0,0],[0,Sy,0],[0,0,1]]) *
#                   [[1,0,-Xo],[0,1,-Yo],[0,0,1]]
#        分析：先反向移动到原点，再缩放、旋转，最后再移动回来。
#       整理后：
#               A = [[ SxCosα, SySinα, (1-SxCosα)Xo-SyYoSinα],
#                    [-SxSinα, SyCosα, (1-SyCosα)Yo+SxXoSinα],
#                    [ 0      , 0      ,  1                     ]]
#       如果先逆时针旋转α，再缩放，则：
#               A = [[ SxCosα, SxSinα, (1-SxCosα)Xo-SxYoSinα],
#                    [-SySinα, SyCosα, (1-SyCosα)Yo+SyXoSinα],
#                    [ 0      , 0      ,  1                     ]]
#       如果还需要平移，则左乘一个平移仿射矩阵即可。
#       OpenCV提供函数 cv2.getRotationMatrix2D(center, angle, scale) 用于计算仿射变换矩阵，本质上还是矩阵相乘
#                       center：变换中心点坐标；angle：逆时针旋转角度（不是弧度）；scale：比例缩放系数；

#       例：以坐标点（40,50）为中心，逆时针旋转30°仿射变换矩阵：
A = cv2.getRotationMatrix2D((40, 50), 30, 0.5)
print(A.dtype)
print(A)


#   3.插值算法
#       （1）最邻近插值
#       （2）双线性插值
