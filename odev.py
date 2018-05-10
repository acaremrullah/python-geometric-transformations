#Emrullah ACAR
import cv2
import numpy as np

def main():

    img = cv2.imread('profile.jpg')
    kernel = np.ones((5, 5), np.uint8)
    cv2.imshow('Original', img)

    #translation(img)
    #rotation(img)
    #scaling(img)
    #opening(img,kernel)
    #closing(img,kernel)
    #erosion(img,kernel)

def translation(img):

    num_rows, num_cols = img.shape[:2]
    translation_matrix = np.float32([ [1,0,50], [0,1,50] ]) #50 = kaç nokta kaydırılacak
    img_translation = cv2.warpAffine(img, translation_matrix, (num_cols, num_rows))
    cv2.imshow('Translation', img_translation)
    cv2.waitKey()

def scaling(img):

    img_scaled = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('Linear İnterpolasyon', img_scaled)
    img_scaled = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('Kubik Interpolasyon', img_scaled)
    img_scaled = cv2.resize(img, (450, 400), interpolation=cv2.INTER_AREA)
    cv2.imshow('Skewed', img_scaled)
    cv2.waitKey()

def rotation(img):
    num_rows, num_cols = img.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), 90, 1) #döndürülcek nokta, dönüş açısı, ölçekleme
    img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
    cv2.imshow('Rotation', img_rotation)
    cv2.waitKey()

def opening(img,kernel):
    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow('opening',open)
    cv2.waitKey()

def closing(img,kernel):
    close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('closing',close)
    cv2.waitKey()

def erosion(img,kernel):
    erozyon= cv2.erode(img, kernel, iterations=1)
    cv2.imshow('erosion', erozyon)
    cv2.waitKey()

main()