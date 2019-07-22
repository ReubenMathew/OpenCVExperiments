import cv2 
import numpy as np


cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([80,100,20])
	upper_red = np.array([255,250,250])

	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame,frame,mask = mask)

	kernel = np.ones((15,15),np.float32)/225 #smoothing by pixel average kernel
	smoothed = cv2.filter2D(res,-1,kernel) #apply smoothing filter

	#Gaussian Blur
	blur = cv2.GaussianBlur(res,(15,15),0)
	median = cv2.medianBlur(res,15,0)
	# cv2.imshow('frame',frame)
	# cv2.imshow('mask',mask)
	# cv2.imshow('res',res)
	cv2.imshow('smooth',smoothed)
	cv2.imshow('median',median)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()