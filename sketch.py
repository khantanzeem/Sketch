import cv2

img_location = 'E:\photos'
file_name = '\ecc1.jpg'

img = cv2.imread(img_location+file_name)
imP = cv2.resize(img, (630,630))  


gray_image= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_gray_image = 255 - gray_image

blurred_image = cv2.GaussianBlur(inverted_gray_image,(21,21),0)
inverted_blurred_image = 255 - blurred_image

pencil_sketch_image = cv2.divide(gray_image,inverted_blurred_image, scale = 256.0)
imS = cv2.resize(pencil_sketch_image, (650,650))  
cv2.imshow('Original photo', imP)
cv2.imshow('Sketch Photo', imS)
cv2.waitKey(0)