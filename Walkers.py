import cv2


# Create our body classifier
body_classifier= cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')



# Loop once video is successfully loaded
while True:
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    
    # Pass frame to our body classifier
    bodies = body_classifiers.detectMultiScale(gray,1.2,3)
    
    
    # Extract bounding boxes for any bodies identified
    

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break
for (x,y,w,h) in faces:
  cv2.rectangle(img,(x,y),(x+w,y+h),(300,40,0),10)  
  roi_color = img[y:y+h, x:x+w]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
  cv2.imwrite("face.jpg",roi_color)

cv2.imshow('img',img)

      
       
cv2.destroyAllWindows()
