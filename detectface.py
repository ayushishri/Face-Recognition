import cv2

face_cascade=cv2.CascadeClassifier("C:\opencv-master\opencv-master\data\haarcascades_cuda\haarcascade_frontalface_default.xml")
color_img=cv2.imread('team.jpg',1)

img=cv2.cvtColor(color_img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(img,1.1,5)

print (len(faces))


for x,y,w,h in faces:
	color_img=cv2.rectangle(color_img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("title",color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()