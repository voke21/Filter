import numpy as np
from matplotlib import pyplot as plt

# 圆形高通滤波器
# def CirFltr(m,n,r):
#     Filter = np.zeros([m,n])
#     cx = int(m/2)
#     cy = int(n/2)
#     for ii in range(m):
#         for jj in range(n):
#             if (ii-cx)**2+(jj-cy)**2 < r**2:
#                 Filter[ii,jj] = 1
#     return Filter

# pic = CirFltr(512,512,100)
# plt.imshow(pic,cmap='gray')
# plt.show()

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

pic = RectxFilter(512,512,100)
plt.imshow(pic,cmap='gray')
#plt.show()

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

pic = RectyFilter(512,512,100)
plt.imshow(pic,cmap='gray')
#plt.show()

## 矩形孔
def RectxyFilter(m,n,d):
    return RectxFilter(m,n,d) * RectyFilter(m,n,d)

pic = RectxyFilter(512,512,200)
plt.imsave('Box.jpg',pic,cmap='gray')
plt.imshow(pic,cmap='gray')
plt.show()