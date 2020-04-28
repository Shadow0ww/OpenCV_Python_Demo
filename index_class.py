# 【1】  基本元素ndarray
# 1. 构造二维ndarray
# 2. 初始化一个浮点矩阵
# 3. ndarray的成员变量
# 4. 访问ndarray中的值
# 5. ndarray加法
# 6. ndarray减法
# 7. ndarray点乘法
# 8. ndarray点除法
# 9. ndarray乘法
# 10. 指数和对数运算
# 11. 幂指数和开平方运算
# 12. 其他：OpenCV和Numpy还有很多矩阵运算函数，如绝对值、求逆、取最大值等函数

# 【2】  图片读取、转化灰度图
#   灰度图转化为ndarray（利用OpenCV的imread函数）（灰度0~255,0黑\255白）
#       imread(const string\&filename, int flags=1)

# 【3】  RGB彩色图
#   将RGB彩色图转化为三维ndarray
#       cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
#   得到三个颜色通道
#   输出三个颜色图片(其他全部为零则为单色)

# 【4】  仿射矩阵
#   计算仿射矩阵：解方程组法、基本仿射矩阵相乘法
#   1.方程法
#       A = cv2.getAffineTransform(src, dst)
#   2.矩阵法
#       OpenCV提供函数 cv2.getRotationMatrix2D(center, angle, scale) 用于计算仿射变换矩阵，本质上还是矩阵相乘

# 【5】  三维变换
#   通过二维投影变换对此物体三维变换进行模型化，这就是专用的二维投影变换
#       M = cv2.getPerspectiveTransform(src, dst)
#   类似仿射变换函数，OpenCV提供函数：
#       cv2.warpPerspective(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])
#   显示效果类似将一幅图“放在”任何不规则的四边形中。
