import cv2
import sys
import numpy as np

# 将RGB彩色图转化为三维ndarray


if __name__ == "__main__":
    # 输入图像矩阵
    if len(sys.argv) > 1:
        img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
    else:
        print("Usge:python imgToArray.py imageFile")

    # 得到三个颜色通道
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    # 显示三个颜色通道灰度图
    # cv2.imshow("b", b)
    # cv2.imshow("g", g)
    # cv2.imshow("r", r)

    # 输出三个颜色图片(其他全部为零则为单色)
    img2 = img.copy()
    img2[:, :, (1, 2)] = 0
    cv2.imshow("b2", img2)
    img3 = img.copy()
    img3[:, :, (0, 2)] = 0
    cv2.imshow("g2", img3)
    img4 = img.copy()
    img4[:, :, (0, 1)] = 0
    cv2.imshow("r2", img4)

    # 灰度化图片
    # 公式：gray = [0.114, 0.587, 0.299]*[[b], [g], [r]]
    im_gray = 0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]

    print(img.dtype)
    print(im_gray.dtype)

    print(img.shape)
    print(im_gray.shape)

    cv2.imshow("im_gray", np.uint8(im_gray))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
