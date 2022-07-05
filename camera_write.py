import cv2



cap = cv2.VideoCapture(0)

i = 0


while True:
    ret, frame = cap.read()



    cv2.imshow('video', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

    elif key == ord("m"):
        print("save image")
        cv2.imwrite("./images/" + str(i) + '_result.jpg', frame)
        i = i + 1
        continue

cap.release()
cv2.destroyAllWindows()


