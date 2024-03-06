import cv2
camera_id = 0 
cap = cv2.VideoCapture(camera_id)
img1 = cv2.imread(r'C:\Users\USER\Documents\Zalo Received Files\Nhat6mui.jpg',-1)
while True:
    # lay khung hinh hien tai ^-^
    ret , frame = cap.read()

    cv2.rectangle (frame, (23,45),(45,78), (0, 0, 255), 2, cv2.LINE_AA, 0)  # Chống răng cưa
    cv2.rectangle(frame, (70, 10), (50, 20), (0, 255, 0), 2, cv2.LINE_8, 0)  # Đường nét đứt
    cv2.rectangle(frame , (130, 10), (50, 20), (255, 0, 0), 2, cv2.LINE_4, 0)
     
     #chinh lai kich thuoc anh
    imgresize = cv2.resize(img1,(100,250),interpolation = cv2.INTER_CUBIC )
    cv2.imshow ("ve các hình chữ nhật khác nhau", frame)
    cv2.imshow("anh ",imgresize)
    if cv2.waitKey(1) & 0xFF == ord ('q'): 
        break
cap.release()
cv2.destroyAllWindows()