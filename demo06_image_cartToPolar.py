# 利用极坐标变换对图像进行变换
#   先了解Numpy中的tile(a, (m, n)) 函数：
#       该函数返回矩阵是m*n个a平铺而成的。

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.tile(a, (2, 3))  # 将a分别在垂直方向和水平方向复制2次、三次
print(b)

# 现通过定义polar函数实现图像的极坐标变换，其中：
#   I代表输入图像；
#   center代表坐标变换中心；
#   r为一个二元元组，代表最小距离和最大距离
#   theta是角度范围，默认[0,360]，注意角度不是弧度
#   rstep代表r的变换步长
#   thetastep代表角度变换步长，默认1/4
#   对于灰度值的插值，使用临近插值方法，也可用其他方法。
import cv2


def polar(I, center, r, theta=(0, 360), rstep=1, thetastep=360.0 / (180 * 8)):
    # 得到距离最小、最大范围。
    minr, maxr = r
    # 角度的最小范围
    mintheta, maxtheta = theta
    # 输出图像的高、宽
    H = int((maxr - minr) / rstep + 1)
    W = int((maxtheta - mintheta) / thetastep + 1)
    O = 125 * np.ones((H, W), I.dtype)
    cx, cy = center
    # 极坐标变换
    r = np.linspace(minr, maxr, H)
    r = np.tile(r, (W, 1))
    r = np.transpose(r)  # 矩阵转置
    theta = np.linspace(mintheta, maxtheta, W)
    theta = np.tile(theta, (H, 1))  # 垂直方向重复H次，水平1次
    x, y = cv2.polarToCart(r, theta, angleInDegrees=True)
    # 最近邻插值
    for i in range(H):
        for j in range(W):
            px = int(round(x[i][j]) + cx)
            py = int(round(y[i][j]) + cy)
            if ((px >= 0 and px <= W - 1) and (py >= 0 and py <= H - 1)):
                O[i][j] = I[py][px]
            else:
                O[i][j] = 125  # 灰色
    return O


#   利用图像进行转换
import cv2
import numpy as np
import sys

# 主函数
if __name__ == "__main__":
    print("---------------Hello python ------------")
    if len(sys.argv) > 1:
        I = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
    else:
        print("Usage: python polar.py image")
        exit()
        # 图像宽高
    H, W = I.shape[:2]
    # 极坐标中心(大概的中心)(watch1:247, 241;watch2:237, 243)
    cx, cy = W / 2, H / 2
    center = (cx, cy)
    # 中心涂黑
    cv2.circle(I, (int(cx), int(cy)), 10, (0.0, 0, 0), 3)
    # circleIn = cv2.circle(I, center=center, radius=int(min(H, W) / 4), color=0, thickness=-1)
    # 距离的最小、最大半径
    # r = (130, 240)
    r = (0, min(cx, cy))
    O = polar(I, center, r)
    # 旋转
    O = cv2.flip(O, 0)
    # 显示原图和输出图像
    cv2.imshow("I", I)
    cv2.imshow("O", O)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# 圆形填充
# circleIn = cv2.circle(I, center=(cx , cy ), radius=int(min(height, width) / 3), color=0, thickness=-1)
#   center 表示的是中心点坐标
#   radius 表示的是半径
#   thickness = -1时表示把圆填满
#   thickness = 正数时表示线的粗细


# 翻转
# flip(src, flipCode[, dst])
#   flipCode	    Anno
#   1	            水平翻转
#   0	            垂直翻转
#   -1	            水平垂直翻转


# numpy.linspace(start, stop[, num=50[, endpoint=True[, retstep=False[, dtype=None]]]]])
#   返回在指定范围内的均匀间隔的数字（组成的数组），也即返回一个等差数列
#   start - 起始点，stop - 结束点，num - 元素个数，默认为50，
#   endpoint - 是否包含stop数值，默认为True，包含stop值；若为False，则不包含stop值
#   retstep - 返回值形式，默认为False，返回等差数列组，若为True，则返回结果(array([`samples`, `step`])),
#   dtype - 返回结果的数据类型，默认无，若无，则参考输入数据类型。
