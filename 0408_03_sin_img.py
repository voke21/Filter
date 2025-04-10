import numpy as np
from matplotlib import pyplot as plt

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

# pic = RectxFilter(512,512,100)
# plt.imshow(pic,cmap='gray')
# plt.show()
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

# pic = RectyFilter(512,512,100)
# plt.imshow(pic,cmap='gray')
# plt.show()

Img = plt.imread("Lena512.bmp",'gray')
# print(Img.shape)
m,n = Img.shape

x = np.linspace(0,m,m)
y = np.linspace(0,n,n)
x,y = np.meshgrid(x,y)
z = np.cos(20*x)

# plt.subplot(121)
# plt.imshow(abs(z),'gray')

Nimg = Img + z * 2000

# plt.subplot(122)
# plt.imshow(abs(Nimg),'gray')
# plt.show()

plt.subplot(121)
fft_Img = np.fft.fft2(Nimg)
fft_Img = np.fft.fftshift(fft_Img)
# plt.imshow(np.log(1+abs(fft_Img)**2),'gray')
d1 = 220
d2 = 100
Flt = 1-(RectxFilter(m,n,d1)-RectxFilter(m,n,d2))
plt.imshow(Flt)

fft_Img = fft_Img*Flt
RSR_Img = np.fft.ifft2(fft_Img)
plt.subplot(122)
plt.imshow(abs(RSR_Img),'gray')
plt.show()