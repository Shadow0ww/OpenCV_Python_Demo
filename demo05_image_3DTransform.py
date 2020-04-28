#   类似仿射变换函数，OpenCV提供函数：
#       cv2.warpPerspective(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])
#   使用方法也类似，只是输入仿射变换矩阵从2行3列编程3行3列
#   显示效果类似将一幅图“放在”任何不规则的四边形中。

import cv2
import sys
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1], cv2.IMREAD_ANYCOLOR)
    else:
        print("Usage: python roate.py image")

    # 原图的高、宽
    h, w = image.shape[:2]
    # 原始图四个点与投影变换对应的点
    src = np.array([[0, 0], [w - 1, 0], [0, h - 1], [w - 1, h - 1]], np.float32)
    dst = np.array([[50, 50], [w / 3, 50], [50, h - 1], [w - 1, h - 1]], np.float32)
    # 计算投影变换矩阵
    P = cv2.getPerspectiveTransform(src, dst)
    # 利用计算出的投影变换矩阵进行投降的投影变换
    r = cv2.warpPerspective(image, P, (w, h), borderValue=125)
    # 显示原图和投影效果
    cv2.imshow("image", image)
    cv2.imshow("warpPerspective", r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
