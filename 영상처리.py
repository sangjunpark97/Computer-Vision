# -*- coding: utf-8 -*-
"""영상처리.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sjoX4OO0BGLMyX8zf7DOk20m3Tx9BxEb
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2

image = cv2.imread('/content/drive/MyDrive/image/lena.bmp',cv2.IMREAD_UNCHANGED)
gray_image=np.zeros((512,512),np.uint8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
for i in range(0,512,1):
  for j in range(0,512,1):
    gray_image[i][j]+=image[i][j][0]*0.2
    gray_image[i][j]+=image[i][j][1]*0.5
    gray_image[i][j]+=image[i][j][2]*0.3
plt.title('original')
plt.imshow(gray_image,cmap="gray")

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2

image = cv2.imread('/content/drive/MyDrive/image/babbon_grey.bmp',cv2.IMREAD_COLOR)
print(image.shape)
for i in range(0,512,1):
  for j in range(0,512,1):
    image[i][j][0]=image[i][j][0]+50 
    image[i][j][1]=image[i][j][1]+50
    image[i][j][2]=image[i][j][2]+50

for i in range(0,512,1):
  for j in range(0,512,1):
    for k in range(0,3,1):
      if image[i][j][k]>255:
        image[i][j][k]=255
        
plt.title('original')
plt.imshow(image)

from google.colab import drive
drive.mount('/content/drive')
import copy
import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
image_array=np.zeros((128,128),np.uint8)
frame_array=[]
fps=30
path_out='/content/drive/MyDrive/image/video3.mp4'
path_in='/content/drive/MyDrive/image/babbon_grey.bmp'
image = cv2.imread(path_in,cv2.IMREAD_GRAYSCALE)
case=0
x=0
y=0
while 1:
  window=image[y:y+128,x:x+128].copy()
  frame_array.append(window)

  if x==128 and y==256:
    break
  else:
    if case==0:
      if x==384-y:
        case=1
        
      else:
        x+=8
    elif case==1:
      if y==x:
        case=2
        
      else:
        y+=8
    elif case==2:
      if x==384-y:
        case=3
        
      else:
        x-=8
    elif case==3:
      if y==128:
        case=0
        
      else:
        y-=8

plt.imshow(image,cmap='gray')
out = cv2.VideoWriter(path_out,cv2.VideoWriter_fourcc(*'DIVX'), fps, (128,128),isColor=False)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()
out

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2

inpath='/content/drive/MyDrive/image/babbon_grey.bmp'    # input image 경로
image=cv2.imread(inpath,cv2.IMREAD_GRAYSCALE)    # gray input image read
image=image.flatten()   # (512,512) image convert to 1 dimension
plt.hist(image,bins=255)  # plot input image's histogram / bins = '255' (0~255)

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2

inpath='/content/drive/MyDrive/image/lena_grey.bmp'
image=cv2.imread(inpath,cv2.IMREAD_GRAYSCALE)

ht=[]
print(image.shape)
index=np.zeros((256),dtype=int)
for j in range(0,512):
  for i in range(0,512):
    ht.append(image[j][i])
    index[image[j][i]]+=1
sump=sum(ht)
sumv=sum(index)

v=0
w0,w1,u0,u1=0,0,0,0

avg=sump/sumv
for i in range(0,256):
  v+=pow(i-avg,2)*index[i]/sumv

otsu=np.array([])
for t in range(0,256):
  w0,w1,u0,u1=0,0,0,0
  for i in range (1, t+1):
    w0+=index[i]/sumv
    u0+=i*index[i]/sump
  for j in range (t+1, 256):
    w1+=index[j]/sumv
    u1+=j*index[j]/sump
  otsu=np.append(otsu,v-(w0*w1*pow(u0-u1,2)))
result=otsu.argmin()
print(result)
for j in range(0,512):
  for i in range(0,512):
    if(image[j][i]>result):
      image[j][i]=255
    else:
      image[j][i]=0
plt.imshow(image,cmap='gray')
plt.title(result)
plt.show() 
print(index)

"""3주차 과제

1번
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
image1 = np.random.uniform(low=0.0, high=255.0, size=(512,512))
plt.imshow(image1,cmap='gray')

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
def noisemaker(M,N):
  image=np.random.normal(0,20,size=(M,N))
  return image
m=512
n=256
image=noisemaker(m,n)
plt.imshow(image,cmap='gray')

"""2번"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
inpath1='/content/drive/MyDrive/image/lena_grey.bmp'
image1=cv2.imread(inpath1,cv2.IMREAD_GRAYSCALE)
mse=0
noise_image=noisemaker(512,512)+image1
for i in range(0,512):
  for j in range(0,512):
    mse+=pow((image1[i,j]-noise_image[i,j]),2)/512/512
print("MSE=",mse)
print("PSNR=",10*math.log10(255*255/mse))
plt.imshow(noise_image,cmap="gray")

"""3번"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2

def Box_maker(K):
  box=np.ones((K,K))/pow(K,2)
  return box

def G_filter(K,std):
  a=0
  G_filter=np.zeros((K,K),dtype=float)
  for i in range(0,K):
    for j in range(0,K):
      G_filter[i,j]=math.exp((math.pow(i-math.trunc(K/2),2)+math.pow(j-math.trunc(K/2),2))/(2*pow(std,2)))
      a+=G_filter[i,j]
  G_filter=G_filter/a
  return G_filter
filter1=Box_maker(5)
filter2=G_filter(5,10)
print(filter1)
print(filter2)

"""4번"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
inpath1='/content/drive/MyDrive/image/lena_grey.bmp'
image1=cv2.imread(inpath1,cv2.IMREAD_GRAYSCALE)
def zero_padding(image,n,p):
  p_image=np.zeros((n+2*p,n+2*p))
  for i in range(0,n):
    for j in range(0,n):
      p_image[i+p,j+p]=image[i,j]
  return p_image
  
def mirror_padding(image,n,p):
  p_image=np.zeros((n+2*p,n+2*p))
  for i in range(0,n):
    for j in range(0,n):
      p_image[i+p,j+p]=image[i,j]
  for i in range(0,p):
    for j in range(0,n):
      p_image[i,j+p]=image[p-i,j]
  for i in range(n,n+p):
    for j in range(0,n):
      p_image[i+p,j+p]=image[n-i,j]
  for i in range(0,n+2*p):
    for j in range(0,p):
      p_image[i,j]=p_image[i,2*p-j]
  for i in range(0,n+2*p):
    for j in range(n+p,n+2*p):
      p_image[i,j]=p_image[i,2*(n+p)-j]
  return p_image
  
p_image=zero_padding(image1,512,50)
plt.imshow(p_image,cmap="gray")

"""5번"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
inpath1='/content/drive/MyDrive/image/lena_grey.bmp'
image1=cv2.imread(inpath1,cv2.IMREAD_GRAYSCALE)


def image_filtering(image,N,K,std):
  G_filter=np.zeros((K,K),dtype=float)
  a=0
  for i in range(0,K):
    for j in range(0,K):
      G_filter[i,j]=math.exp((math.pow(i-math.trunc(K/2),2)+math.pow(j-math.trunc(K/2),2))/(2*pow(std,2)))
      a+=G_filter[i,j]
  G_filter=G_filter/a
  padded_image=np.pad(image, (K, K), 'edge')
  output_image=np.zeros((N,N))
  for i in range(0,N):
    for j in range(0,N):
          product=padded_image[i:i+K,j:j+K]*G_filter
          output_image[i,j]=product.sum()
  return output_image

filtered_image=image_filtering(image1,512,10,5)
plt.imshow(filtered_image,cmap="gray")

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
inpath1='/content/drive/MyDrive/image/lena_grey.bmp'
image1=cv2.imread(inpath1,cv2.IMREAD_GRAYSCALE)
def image_filtering(image,N,K):
  filter=np.ones((K,K))
  filter=filter/K/K
  padded_image=np.zeros((N+K,N+K))
  output_image=np.zeros((N,N))
  for x in range(0,N):
    for y in range(0,N):
      padded_image[x,y]=image[x,y]
  for x in range(0,N):
    for y in range(0,N):
      for i in range(0,K):
        for j in range(0,K):
          output_image[x,y]+=padded_image[i+x,j+y]*filter[i,j]
  return output_image
filtered_image=image_filtering(image1,512,10)
plt.imshow(filtered_image,cmap="gray")

"""FL3
1. Design the edge detection system. 

A. Use Sobel mask. 

B. Input : image 

C. Output : gradient map (dx, dy), edge strength map, edge orientation map, final edge map
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
inpath='/content/drive/MyDrive/image/lena_grey.bmp'
image=cv2.imread(inpath,cv2.IMREAD_GRAYSCALE)

image=np.pad(image,((1,1),(1,1)),'edge')
sobel_mx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
sobel_my=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
grad_map_dx=np.zeros((512,512))
grad_map_dy=np.zeros((512,512))
strength_map=np.zeros((512,512),dtype='float')
orient_map=np.zeros((512,512),dtype='float')
for y in range(0,512):
  for x in range(0,512):
    for k in range(-1,2):
      for l in range(-1,2):
        grad_map_dx[y,x]+=sobel_mx[k+1,l+1]*image[k+y,l+x]
        grad_map_dy[y,x]+=sobel_my[k+1,l+1]*image[k+y,l+x]
    strength_map[y,x]=math.sqrt(grad_map_dx[y,x]**2+grad_map_dy[y,x]**2)
    orient_map[y,x]=math.atan(grad_map_dy[y,x]/grad_map_dx[y,x])

plt.imshow(strength_map,cmap="gray")

"""2번
2. Canny edge detector. 

A. Use OpenCV canny edge detector, and compare the result with the edge map by Sobel 
mask in problem 1. 
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
inpath='/content/drive/MyDrive/image/lena_grey.bmp'
img = cv2.imread(inpath,cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img,100,150)
plt.imshow(edges,cmap = 'gray')
plt.title('100,150')
plt.show()

"""3. Design image scaling system. 

A. Design bilinear scaling function. 

B. Input : image (MxN), scaling factor (k>0) 

C. Output : kM x kN scaled image 
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
inpath='/content/drive/MyDrive/image/lena_grey.bmp'
image=cv2.imread(inpath,cv2.IMREAD_GRAYSCALE)

def bilinear_scaling(image,M,N,k):
  scaled_image=np.zeros((M*k,N*k))
  for y in range(0,M):
    for x in range(0,N):
      scaled_image[y*k,x*k]=image[y,x]
      for b in range(0,k):
        for a in range(0,k):
          if(a!=0 or b!=0):
            scaled_image[y*k+b,x*k+a]=((k-a)*((k-b)*scaled_image[y*k-k,x*k-k]+b*scaled_image[y*k,x*k-k])+a*((k-b)*scaled_image[y*k-k,x*k]+b*scaled_image[y*k,x*k]))/k/k
  return scaled_image

scaled_image=bilinear_scaling(image,512,512,4)

plt.imshow(scaled_image,cmap='gray')
for i in range(30,45):
  for j in range(30,45):
    print(scaled_image[i,j],end='  ')
  print()

# problem 3

image = cv2.imread('/content/drive/MyDrive/image/lena_grey.bmp',cv2.IMREAD_GRAYSCALE)
plt.imshow(image, cmap='gray')
plt.title('original')
plt.show()

N,M = image.shape
k = 3
scaled_img = np.zeros((k*N+k,k*M+k))

for y in range(N):
  for x in range(M):
    scaled_img[k*x,k*y] = image[x,y]
    for j in range(k):
      for i in range(k):
        if i!=0 or j!=0:
          scaled_img[k*x+i,k*y+j] = ((k-i)*((k-j)*image[x,y]+(j)*image[x,y+1]) + i*((k-j)*image[x+1,y]+j*image[x+1,y+1]))/k


      

plt.imshow(scaled_img, cmap='gray')
plt.title('scaled image')
plt.show()

"""4. Design image transform system. 

A. Design perspective transform function, where nearest-neighbor (NN) interpolation method 
to fill out the hole. 

B. Input : image, 3x3 matrix with DoF=8 (number of parameters) 

C. Output : transformed image. 

D. Example. 
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
inpath='/content/drive/MyDrive/image/lena_grey.bmp'
image=cv2.imread(inpath,cv2.IMREAD_GRAYSCALE)

def tf_function(F,X):
  y=np.matmul(F,X)
  return y

def tf_system(image,M,N,matrix):

  max=0
  for y in range(0,M):
    for x in range(0,N):
      X=np.array([[x],[y],[1]],dtype='float')
      Y=tf_function(matrix,X)
      if(max<round(Y[0,0]/Y[2,0])):
        max=round(Y[0,0]/Y[2,0])
      if(max<round(Y[1,0]/Y[2,0])):
        max=round(Y[1,0]/Y[2,0])
  tf_image=np.zeros((max+2,max+2))

  for y in range(0,M-1):
    for x in range(0,N-1):
      
      X=np.array([[x],[y],[1]],dtype='float')
      Xru=np.array([[x+1],[y],[1]],dtype='float')
      Xld=np.array([[x],[y+1],[1]],dtype='float')
      Xrd=np.array([[x+1],[y+1],[1]],dtype='float')
      
      Y=tf_function(matrix,X)
      Yru=tf_function(matrix,Xru)
      Yld=tf_function(matrix,Xld)
      Yrd=tf_function(matrix,Xrd)
      
      x1=round(Y[0,0]/Y[2,0])
      y1=round(Y[1,0]/Y[2,0])
      x2=round(Yru[0,0]/Yru[2,0])
      y2=round(Yru[1,0]/Yru[2,0])
      x3=round(Yld[0,0]/Yld[2,0])
      y3=round(Yld[1,0]/Yld[2,0])
      x4=round(Yrd[0,0]/Yrd[2,0])
      y4=round(Yrd[1,0]/Yrd[2,0])
      xn=x2-x1
      yn=y3-y1
      
      tf_image[y1,x1]=image[round(X[1,0]),round(X[0,0])]
      tf_image[y2,x2]=image[round(Xru[1,0]),round(Xru[0,0])]
      tf_image[y3,x3]=image[round(Xld[1,0]),round(Xld[0,0])]
      tf_image[y4,x4]=image[round(Xrd[1,0]),round(Xrd[0,0])]
      
      for j in range(0,yn):
        for i in range(0, xn):
          if(j!=0 or i!=0):
            if(round(j/yn)==0 and round(i/xn)==0):
              tf_image[y1+j,x1+i]=tf_image[y1,x1]
            elif(round(j/yn)==0 and round(i/xn)==1):
              tf_image[y1+j,x1+i]=tf_image[y2,x2]
            elif(round(j/yn)==1 and round(i/xn)==0):
              tf_image[y1+j,x1+i]=tf_image[y3,x3]
            else:
              tf_image[y1+j,x1+i]=tf_image[y4,x4]
  return tf_image

#def nn_interpolation(image):
matrix=np.array([[2    ,0 ,0],[  3    ,2 ,0],[  0 ,0 ,1]])
#matrix=np.array([[5    ,0 ,0],[  0   ,5 ,0],[  0 ,0 ,1]])

tf_image=tf_system(image,512,512,matrix)
plt.imshow(tf_image,cmap='gray')
for i in range(50,61):
  for j in range(0,30):
    print(tf_image[i,j],end='  ')
  print()

"""FL4

3. Design a part of SIFT method. 

A. Design an image pyramid and find its difference map. 

B. Input : Image 

C. Output : Image pyramid and difference map. 
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
inpath='/content/drive/MyDrive/image/lena_grey.bmp'
image=cv2.imread(inpath,cv2.IMREAD_GRAYSCALE)

def G_filtering(image,N,K,std):
  G_filter=np.zeros((K,K),dtype=float)
  a=0
  for i in range(0,K):
    for j in range(0,K):
      G_filter[i,j]=np.exp(-((i-(K//2))**2+(j-(K//2))**2)/(2*(std**2)))
  G_filter=G_filter/np.sum(G_filter)
  padded_image=np.pad(image, (K, K), 'edge')
  output_image=np.zeros((N,N))
  for i in range(0,N):
    for j in range(0,N):
          product=padded_image[i:i+K,j:j+K]*G_filter
          output_image[i,j]=product.sum()
  return output_image

def down_sampling(image,M,N):
  a=int(M/2)
  b=int(N/2)
  scaled_image=np.zeros((a,b))
  for y in range(0,a):
    for x in range(0,b):
      scaled_image[y,x]=image[y*2,x*2]
  return scaled_image
def SIFT_method(image,M,N):
  o0=image
  o1=down_sampling(image,M,N)
  o00=G_filtering(o0,M,10,1.6)
  o01=G_filtering(o0,M,10,2.0159)
  o02=G_filtering(o0,M,10,2.5398)
  o03=G_filtering(o0,M,10,3.2)
  o04=G_filtering(o0,M,10,4.0317)
  o05=G_filtering(o0,M,10,5.0797)

  o10=G_filtering(o1,int(M/2),10,1.6)
  o11=G_filtering(o1,int(M/2),10,2.0159)
  o12=G_filtering(o1,int(M/2),10,2.5398)
  o13=G_filtering(o1,int(M/2),10,3.2)
  o14=G_filtering(o1,int(M/2),10,4.0317)
  o15=G_filtering(o1,int(M/2),10,5.0797)

  dmap00=o01-o00
  dmap01=o02-o01
  dmap02=o03-o02
  dmap03=o04-o02
  dmap04=o05-o04

  dmap10=o11-o10
  dmap11=o12-o11
  dmap12=o13-o12
  dmap13=o14-o12
  dmap14=o15-o14

  
  return o00,o01,o02,o03,o04,o05,o10,o11,o12,o13,o14,o15,dmap00,dmap01,dmap02,dmap03,dmap04,dmap10,dmap11,dmap12,dmap13,dmap14

o00,o01,o02,o03,o04,o05,o10,o11,o12,o13,o14,o15,dmap00,dmap01,dmap02,dmap03,dmap04,dmap10,dmap11,dmap12,dmap13,dmap14 =SIFT_method(image,512,512)
plt.imshow(o00,cmap='gray')

plt.imshow(dmap10,cmap='gray')

plt.imshow(dmap11,cmap='gray')

plt.imshow(dmap12,cmap='gray')

plt.imshow(dmap13,cmap='gray')

plt.imshow(dmap14,cmap='gray')

"""FL

1. Design a function to compute an integral image (적분영상). 

A. Input : Image 

B. Output : Integral image 
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
inpath='/content/drive/MyDrive/image/lena_grey.bmp'
image=cv2.imread(inpath,cv2.IMREAD_GRAYSCALE)
def integral(input):
  row, col= input.shape
  output=np.zeros((row,col))
  for i in range(row):
    for j in range(col):
      output[i,j]=np.sum(input[0:i,0:j])
  return output

output=integral(image)

"""2. Design a filter with only addition and subtraction by using integral image. 

A. Input : Image, box filter (8x8) as below. 

B. Output : filtered image 
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
inpath='/content/drive/MyDrive/image/lena_grey.bmp'
image=cv2.imread(inpath,cv2.IMREAD_GRAYSCALE)

def filtering(integral_img,i,j,M,N):
  tmp=integral_img[i-1,j-1]-integral_img[i-1,i+N-1]+integral_img[i+M-1,j+K-1]-integral_img[i+M-1,i-1]
  return tmp

def filter(image,integral_img,n):
  image=np.pad(image,((0,8),(0,8)),'edge')
  if(i!=0 and j!=0):
    if(n==0):
      image[i,j]=filtering(integral_img,i,j,8,4)-filtering(integral_img,i,j+4,8,4)
    elif(n==1):
      image[i,j]=filtering(integral_img,i,j,4,8)-filtering(integral_img,i+4,j,4,8)
    elif(n==2):
      image[i,j]=filtering(integral_img,i,j,4,4)-filtering(integral_img,i+4,j,4,4)+filtering(integral_img,i+4,j+4,4,4)-filtering(integral_img,i,j+4,4,4)
    else:
      image[i,j]=filtering(integral_img,i,j,8,2)-2*filtering(integral_img,i,j+2,8,4)+filtering(integral_img,i,j+6,8,2)
  return image

"""3. Design a filter for k-means algorithm, and apply it to the image.

A. Input : Any types of data, k (number of partition)

B. Output : k centroid 
"""

from google.colab import drive
drive.mount('/content/drive')
import random
import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
inpath='/content/drive/MyDrive/image/lena_grey.bmp'
image=cv2.imread(inpath,cv2.IMREAD_GRAYSCALE)

def initial(input,k):
  pixels=[]
  
  row, col=input.shape
  channel=1
  N=np.zeros((row,col))
  M=np.zeros((row,col))
  for i in range(2*k):
    pixel=random.randrange(0,512)
    pixels.append(pixel)
  pixels=np.reshape(pixels,(k,1,2))
  pixels=np.array(pixels)
  print(pixels.shape)
  for i in range(row):
    for j in range(col):
      dist=[]
      for K in range(k):
        d=np.sqrt((i-pixels[K,0,0])**2+(j-pixels[K,0,1])**2)
        dist.append(d)
      n=dist.index(min(dist))
      M[i,j]=n
      N[i,j]=255/k*n
  return N,M, pixels

def K_means(input, N, M, k, iteration, pixels):
  row, col=input.shape
  tmp=np.zeros((k))
  counter=np.zeros((k))
  P=np.zeros((row,col))
  m_pixels= pixels.copy()
  #print(M)
  for i in range (row):
    for j in range (col):
      for K in range(k):
        if M[i,j]==K :
          counter[K]+=1
          tmp[K]=tmp[K]+input[i,j]
  for K in range(k):
    tmp[K]=tmp[K]/counter[K]
  #print(tmp)
  #print(pixels)
  d=10000
  for p in range(iteration):
    pixels=m_pixels.copy()
    for i in range(row):
      for j in range(col):
        for K in range(k):
          if M[i,j]==K:
            if input[i,j]==round(tmp[K]):
              d0=np.sqrt((i-pixels[K,0,0])**2+(j-pixels[K,0,1])**2)
              if (d0<d): 
                d=d0
                m_pixels[K,0,0]=i
                m_pixels[K,0,1]=j
    print(m_pixels)
    for i in range(row):
      for j in range(col):
        dist=[]
        for K in range(k):
          d=np.sqrt((i-m_pixels[K,0,0])**2+(j-m_pixels[K,0,1])**2)
          dist.append(d)
        n=dist.index(min(dist))
        M[i,j]=n
        P[i,j]=255/k*n
  return P

N,M,pixels=initial(image,10)
P=K_means(image,N,M,10,1,pixels)
P1=K_means(image,N,M,10,2,pixels)
P2=K_means(image,N,M,10,3,pixels)
plt.imshow(N,cmap='gray')

plt.imshow(P,cmap='gray')

plt.imshow(P1,cmap='gray')

plt.imshow(P2,cmap='gray')

import random
import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
height=np.array((170,172,167,180,188,162))
weight=np.array((50.5,71.1,61.3,88.4,69.8,58.2))
age=np.array((29,33,37,44,46,35))
score=np.array((80,93,72,88,85,69))
data= np.stack((height,weight,age,score))

def Euclidean(data):
  average=np.mean(data,axis=1)
  key,value=data.shape
  d=np.zeros(value)
  for i in range(key):
    for j in range(value):
      d[j]+=(data[i,j]-average[i])**2
  return average,np.sqrt(d)

def Mahalanobis(data):
  average=np.mean(data,axis=1)
  var=np.var(data,axis=1)
  cov=np.cov(data, bias=True)
  cov_inv=np.linalg.inv(cov)
  Tdata=data.T
  p=np.zeros((6,4))
  for i in range(6):
    p[i]=Tdata[i]-average
  d=np.zeros((6))
  for i in range(6):
    d[i]=p[i]@cov_inv@p[i].T
  return cov,np.sqrt(d)

average, d1=Euclidean(data)
print("average :",average)
print("Euclidean distance :",d1)
cov,d2=Mahalanobis(data)
print("Mahalanobis distance :",d2)

import random
import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
inpath='/content/drive/MyDrive/image/lena_grey.bmp'
image=cv2.imread(inpath,cv2.IMREAD_GRAYSCALE)

def G_filter(K,std):
  G_filter=np.zeros((K,K),dtype=float)
  T=K//2
  for i in range(0,K):
    for j in range(0,K):
      G_filter[i,j]=np.exp(-((i-(T))**2+(j-(T))**2)/(2*(std**2)))
  G_filter=G_filter/np.sum(G_filter)
  return G_filter

def conv(img1,img2,size):
  row,col=img1.shape
  padded_image=np.pad(img1, ((0, size),(0,size)), 'edge')
  output_image=np.zeros((row,col),dtype=int)
  for i in range(0,row):
      for j in range(0,col):
            product=padded_image[i:i+size,j:j+size]*img2
            output_image[i,j]=product.sum()
  return output_image

def Harris(image,size,k):
  corner=[]
  orient=[]
  G=G_filter(size,1)
  
  dy,dx=np.gradient(image)
  row, col =image.shape
  lyy=conv(dy*dy,G,size)
  lxy=conv(dx*dy,G,size)
  lxx=conv(dx*dx,G,size)
  for y in range(row):
    for x in range(col):
      detA=lxx[y,x]*lyy[y,x]-lxy[y,x]**2
      traceA=lxx[y,x]+lyy[y,x]
      C=detA-k*(traceA**2)
      if(C>50000):
        corner.append([y,x])
  G=G_filter(5,1)
  orient=np.zeros((36))
  for y,x in corner:
    L=image[y-2:y+3,x-2:x+3]*G
    for iy in range(1,4):
      for ix in range(1,4):
        theta[iy-1,ix-1]=math.atan2(L[iy,ix-1]-L[iy,ix+1],L[iy-1,ix]-L[iy+1,ix])
        orient[theta//10]+=1
        major_orient=np.argmax(orient)
  return corner,orient
corner,orient=Harris(image,3,0.05)
print(orient)
print(corner)
orient=np.array(orient)
orient=(orient*180/np.pi+360)%360
plt.hist(orient,bins=36,range=((orient.min(),orient.max())),rwidth=0.8)
plt.show()