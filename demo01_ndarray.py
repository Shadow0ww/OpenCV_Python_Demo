import numpy as np

# 1. 构造二维ndarray
z = np.zeros((2, 4), np.uint8)
#   打印z类型
print(type(z))
#   打印二维数组
print(z)

#   构造数组:2行4列都是1
o = np.ones((2, 4), np.int32)
print(o)

#   初始化一个浮点矩阵
m = np.array([[4, 12, 3, 1],
              [10, 12, 14, 29]], np.float32)
print(m)

# 2. 初始化一个浮点矩阵
m2 = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8]],
    [[10, 11, 12, 13], [14, 15, 16, 17]]
], np.float32)
print(m2)

# 3. ndarray的成员变量
#   数组尺寸
print(m.shape)
print(m2.shape)
#   数组数据类型
print(o.dtype)
print(m.dtype)

# 4. 访问ndarray中的值
#   取值（点）
print(m[1, 3])
print(m2[1, 1, 0])
#   取值（行）
print(m[1, :])
print(m2[1, 1, :])
#   取值（列）
print(m[:, 3])
print(m2[:, 1, 0])
print(m2[:, :, 0])

# 5. ndarray加法(uint8最大255，超过则取模-1)
src1 = np.array([[23, 123, 90], [100, 250, 0]], np.uint8)
src2 = np.array([[125, 150, 60], [100, 10, 40]], np.uint8)
dst = src1 + src2
print(dst)
print(type(dst))

#   加法（不同数据类型，取数字范围大的）
src2 = np.array([[125, 150, 60], [100, 10, 40]], np.float32)
dst = src1 + src2
print(dst)

#   使用OpenCV中的add函数完成加法计算
import cv2

dst = cv2.add(src1, src2, dtype=cv2.CV_32F)
print(dst)

# 6. ndarray减法(uint8最小0，低于则取模+1)
src1 = np.array([[23, 123, 90], [100, 250, 0]], np.uint8)
src2 = np.array([[125, 150, 60], [100, 10, 40]], np.uint8)
dst = src1 - src2
print("6:")
print(dst)

# 7. ndarray点乘法(矩阵对应位置相乘)
src1 = np.array([[23, 123, 90], [100, 250, 0]], np.uint8)
src2 = np.array([[125, 150, 60], [100, 10, 40]], np.float32)
dst = src1 * src2
print("7:")
print(dst)
# 或
dst = np.multiply(src1, src2)
print(dst)

# 8. ndarray点除法
src1 = np.array([[23, 123, 90], [100, 250, 0]], np.uint8)
src2 = np.array([[125, 150, 60], [100, 10, 40]], np.uint8)
dst = src2 / src1
print("8:")
print(dst)  # 0/40 ，否是uint8则 = 0，其他情况返回inf
print(dst.dtype)
src1 = src1.astype(np.float32)  # 改变数据类型
dst = src2 / src1
print(dst)  # 0/40 ，否是uint8则 = 0，其他情况返回inf
print(dst.dtype)

# 9. ndarray乘法(点乘用*或multiply，矩阵乘法用dot函数)
src3 = np.array([[1, 2, 3], [4, 5, 6]], np.uint8)
src4 = np.array([[6, 5], [4, 3], [2, 1]], np.uint8)
print("9:")
dst = np.dot(src3, src4)
print(dst)

# 10. 指数和对数运算
#   对矩阵中每个数值进行运算，可以用for循环，但是OpenCV提供exp和log函数封装（注意：数据类型只能是CV_32F/CV_64F）
#   Numpy也提供了exp和log函数，且ndarray数据类型随意，返回值类型为float或double
src5 = np.array([[6, 5], [4, 3]], np.uint8)
dst2 = np.exp(src5)  # 返回e的n次方
dst3 = np.log(src5)  # 返回ln
print("10:")
print(dst2)
print(dst3)
print(dst3.dtype)

# 11. 幂指数和开平方运算
#   对矩阵中每个数值进行运算，可以用for循环，但是OpenCV提供pow和sqrt函数封装
#   （注意：sqrt数据类型只能是CV_32F/CV_64F；pow类型不限）
#   Numpy也提供了power
src = np.array([[25, 40], [10, 100]], np.uint8)
dst1 = np.power(src, 2)  # 对每个数值进行幂指数运算
print("11:")
print(dst1)
print(dst1.dtype)
dst1 = np.power(src, 2.0)  # 2改为2.0数据类型会不同
print(dst1)
print(dst1.dtype)

# 12.    其他：OpenCV和Numpy还有很多矩阵运算函数，如绝对值、求逆、取最大值等函数
