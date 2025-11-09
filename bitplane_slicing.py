import cv2
import numpy as np

def int2bitarray(img):
    arr = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            arr.append(np.binary_repr(img[i][j], width=8))
    return arr

img = cv2.imread('./lena.png',0)
arr = np.array(int2bitarray(img))
arr = arr.reshape(img.shape)

plane = np.zeros((img.shape))
for k in range(0,8):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            plane[i,j]=int(arr[i,j][k])
    cv2.imwrite('./Bitplane'+str(7-k)+'.png',plane*255)
    print('\nbit plane '+str(7-k)+' done!')
