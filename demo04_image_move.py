#   图像几何变换两个关键点：
#       1.空间坐标变换
#       2.插值方法

#   在已知放射变换矩阵的基础上，OpenCV提供了函数：
#       cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])
#       __________________________________________________________________________
#       |   参数     | 解释                                                      |
#       |------------|-----------------------------------------------------------|
#       | src        | 输入图像矩阵                                              |
#       | M          | 2行3列的放射变换矩阵                                      |
#       | dsize      | 二元组(宽，高)，输出图像大小                              |
#       | flags      | 插值法：INTE_NEARST、INTE_LINEAR(默认)等                  |
#       | borderMode | 填充模式：BORDER_CONSTANT等                               |
#       | borderValue| 当borderMode=BORDER_CONSTANT时的填充值                    |
#       --------------------------------------------------------------------------

import numpy as np
import cv2
import sys
import math

# 主函数
if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
    else:
        print("Usage: python warpAffine.py image")

    cv2.imwrite("img.jpg", image)
    # 原图的高、宽
    h, w = image.shape[:2]
    # 仿射变换矩阵，缩小2倍
    A1 = np.array([[0.5, 0, 0], [0, 0.5, 0]], np.float32)
    d1 = cv2.warpAffine(image, A1, (w, h), borderValue=125)

    # 先缩小2倍，再平移
    A2 = np.array([[0.5, 0, w / 4], [0, 0.5, h / 4]], np.float32)
    d2 = cv2.warpAffine(image, A2, (w, h), borderValue=125)

    # 在d2的基础上，绕图像中心点旋转
    A3 = cv2.getRotationMatrix2D((w / 2.0, h / 2.0), 30, 1)
    d3 = cv2.warpAffine(image, A3, (w, h), borderValue=125)

    cv2.imshow("image", image)
    cv2.imshow("d1", d1)
    cv2.imshow("d2", d2)
    cv2.imshow("d3", d3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
