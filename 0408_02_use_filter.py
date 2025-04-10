import numpy as np
from matplotlib import pyplot as plt

# 圆形高通滤波器
def CirFltr(m,n,r):
    Filter = np.zeros([m,n])
    cx = int(m/2)
    cy = int(n/2)
    for ii in range(m):
        for jj in range(n):
            if (ii-cx)**2+(jj-cy)**2 < r**2:
                Filter[ii,jj] = 1
    return Filter

pic = CirFltr(512,512,100)
#plt.imshow(pic,cmap='gray')
#plt.show()

# Img = plt.imread("Lena512.bmp",'gray')
# #print(Img.shape)
# m,n = Img.shape

# 高通滤波实现边缘提取
Img = plt.imread("Box.jpg",'gray')
print(Img.shape)
m,n,k = Img.shape
Img = Img[:, :,0]

fft_Img = np.fft.fft2(Img)
fft_Img = np.fft.fftshift(fft_Img)  # 中心化，中心高频 

# low_pass Filtering
d = 50
FILT_Img = fft_Img * (1-CirFltr(m,n,d))
plt.subplot(121)
plt.imshow(np.log(1+abs(FILT_Img)**2),'gray')  # 光学平方，log提升对比度高的低些，小的高些

# 成像，逆变换
Inver_Img = np.fft.ifft2(FILT_Img)
plt.subplot(122)
plt.imshow(abs(Inver_Img)**2,'gray')
plt.show()