import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 矩形滤波器
## x方向
def RectxFilter(m,n,d):
    Filter = np.zeros([m,n])
    cx = int(m/2)  # x-center
    cy = int(n/2)
    hd = int(d/2)
    for ii in range(m):
        for jj in range(n):
            if abs(ii-cx) < hd:
                Filter[ii,jj] = 1
    return Filter

## y方向
def RectyFilter(m,n,d):
    Filter = np.zeros([m,n])
    cx = int(m/2)  # x-center
    cy = int(n/2)
    hd = int(d/2)
    for ii in range(m):
        for jj in range(n):
            if abs(jj-cy) < hd:
                Filter[ii,jj] = 1
    return Filter

# 插入待处理图像
Img = plt.imread("Lena512.bmp",'gray')
# print(Img.shape)
m,n = Img.shape

# 建立网格
x = np.linspace(0,m,m)
y = np.linspace(0,n,n)
x,y = np.meshgrid(x,y)
z = np.cos(20*x)
## 调制图像
## =====
plt.figure(num=1, figsize=(12, 6))
plt.subplot(121)
plt.imshow(np.abs(z),'gray')
plt.title("调制图")
# 调制原图
Nimg = Img + z * 100

plt.subplot(122)
plt.imshow(np.abs(Nimg),'gray')
plt.title("调制后对象")
plt.show()

# 建立第二个窗口
# =====
plt.figure(num=2, figsize=(12, 6))
# 调制后图像频谱
fft_Img = np.fft.fft2(Nimg)
fft_Img = np.fft.fftshift(fft_Img)
plt.subplot(131)
plt.imshow(np.log(1+abs(fft_Img)**2),'gray')
plt.title("调制后对象频谱")
# 构建带通滤波器
d1 = 220
d2 = 120
Flt = 1-(RectyFilter(m,n,d1)-RectyFilter(m,n,d2))
plt.subplot(132)
plt.imshow(Flt,'gray')
plt.title("滤波器")
# 进行滤波
fft_Img = fft_Img*Flt
RSR_Img = np.fft.ifft2(fft_Img)
plt.subplot(133)
plt.imshow(abs(RSR_Img),'gray')
plt.title("滤波后图像")
plt.show()
