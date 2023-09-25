import pyrebase
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
config = {
  "apiKey" : "AIzaSyCxiCUZFwtgBr56HlOx3XtT9Y0Q12uVABQ" ,
  "authDomain" : "dht11-ea471.firebaseapp.com" ,
  "databaseURL" : "https://dht11-ea471-default-rtdb.asia-southeast1.firebasedatabase.app" ,
  "projectId" : "dht11-ea471" ,
  "storageBucket" : "dht11-ea471.appspot.com" ,
  "messagingSenderId" : "106074029143" ,
  "appId" : "1:106074029143:web:bde3bb90c8cdbb38657712"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

cap = cv2.VideoCapture(0)
# Chụp một khung hình
ret, frame = cap.read()
time.sleep(3)
frame = cv2.resize(frame, (1920, 1080))

# Lưu khung hình vào một file
cv2.imwrite("5.jpg", frame,(cv2.IMWRITE_JPEG_QUALITY, 100))

# Đóng thiết bị chụp hình
cap.release()

img2 = cv2.imread("5.jpg")
cv2.imshow("aa",img2)

cv2.waitKey()
image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)


lower_values = [(30, 120, 40), (42, 80, 40), (63, 120, 40), (70, 150, 40), (75, 200, 40)]
upper_values = [(42, 255, 255), (63, 255, 255), (70, 255, 255), (75, 255, 255), (80, 255, 255)]

masks = []
for i in range(len(lower_values)):
    mask = cv2.inRange(image2, np.array(lower_values[i]), np.array(upper_values[i]))
    masks.append(mask)

mask_green = sum(masks)
#cv2.imshow('image',mask_green)
#plt.imshow('image',mask_green)
x2,y,w2,h2 = cv2.boundingRect(mask_green)
#print(x2,y,w2,h2)
h=0

if y > 808  and y < 827:
  h= (y-808)/(827-808)*2 + 14
elif y> 788 and y<808:
  h= (y-788)/(808-788)*2 + 16
elif y> 767and y< 788:
  h= (y-767)/(788-767)*2 + 18
elif y> 745 and y< 767:
  h= (y-745)/(767-745)*2 + 20
elif y> 723 and y< 745:
  h= (y-723)/(745-723)*2 + 22
elif y> 701and y< 723:
  h= (y-701)/(723-701)*2 + 24
elif y> 678 and y< 701:
  h= (y-678)/(701-678)*2 + 26
elif y> 656and y< 678:
  h= (y-656)/(678-656)*2 + 28
elif y> 630and y< 656:
  h= (y-630)/(656-630)*2 + 30
elif y>611 and y< 630:
  h= (y-611)/(630-611)*2 + 32
elif y> 589 and y< 611:
  h= (y-589)/(611-589)*2 + 34
elif y> 568and y< 589:
  h= (y-568)/(589-568)*2 + 36
elif y> 542and y< 568:
  h= (y-542)/(568-542)*2 + 38
elif y>521 and y< 542:
  h= (y-521)/(542-521)*2 + 40
elif y> 502 and y< 521:
  h= (y-502)/(521-502)*2 + 42
elif y> 477and y< 502:
  h= (y-477)/(502-477)*2 + 44
elif y> 454and y< 477:
  h= (y-454)/(477-454)*2 + 46
elif y>430 and y< 454:
  h= (y-430)/(454-430)*2 + 48
elif y> 413 and y< 430:
  h= (y-413)/(430-413)*2 + 50
elif y> 391and y< 413:
  h= (y-391)/(413-391)*2 + 52
elif y> 364and y< 391:
  h= (y-364)/(391-364)*2 + 54
elif y>341 and y< 364:
  h= (y-341)/(364-341)*2 + 56
elif y> 320 and y< 341:
  h= (y-320)/(341-320)*2 + 58
elif y> 297and y< 320:
  h= (y-297)/(320-297)*2 + 60
elif y> 274and y< 297:
  h= (y-274)/(297-274)*2 + 62
elif y>259 and y< 274:
  h= (y-259)/(274-259)*2 + 64
elif y> 229 and y< 259:
  h= (y-229)/(259-229)*2 + 66
elif y> 209and y< 229:
  h= (y-209)/(229-209)*2 + 68
elif y> 187and y< 209:
  h= (y-187)/(209-187)*2 + 70
elif y>169 and y< 187:
  h= (y-169)/(187-169)*2 + 72
elif y> 142 and y< 169:
  h= (y-142)/(169-142)*2 + 74
elif y> 120and y< 142:
  h= (y-120)/(142-120)*2 + 76
elif y> 98and y< 120:
  h= (y-98)/(120-98)*2 + 78
elif y>77 and y< 98:
  h= (y-77)/(98-77)*2 + 80
elif y>34 and y< 77:
  h= (y-34)/(77-34)*2 + 82

h=h-15
h = round(h,2)
print(h)
data = {"high": float(h)}

results = db.child("UsersData/l7FExvJ3j9PhjHUaHnHaMWbAqKk1").update(data)


