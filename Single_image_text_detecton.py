# IZMANTOTI INFORMĀCIJAS AVOTI
# https://stackoverflow.com/questions/34966541/how-can-one-display-an-image-using-cv2-in-python
# https://github.com/ultralytics/yolov5/issues/388 
# https://dev.to/andreygermanov/how-to-extract-all-detected-objects-from-image-and-save-them-as-separate-images-using-yolov82-and-opencv-3j99
# https://blog.roboflow.com/how-to-use-easyocr/
# https://builtin.com/data-science/python-ocr         --- FOR EDITING IMAGE


from ultralytics import YOLO
import cv2
import easyocr

model = YOLO('C:/coding and apps/codes/runs/detect/train63/weights/best.pt')
selected_image = cv2.imread('C:/coding and apps/codes/Testing images/test_img1.jpg')
results = model(selected_image, save=True, conf=0.75)

boxes = []
for box in results[0].boxes:  
    cls = results[0].names[box.cls[0].item()]
    if cls == "44": # 44 ir ceļa zīmes nosaukums
        print("-- ZONA road sign is detected --")
        cords = box.xyxy[0].tolist()
        score = box.conf[0].item() 
        x1, y1, x2, y2 = [round(x) for x in cords]
        boxes.append([x1, y1, x2, y2, score, cls])
    else:
        print("-- Needed road signs are not detected --")
        exit() # ja nav detektēta konkrēta ceļa zīme, tad vienkarši nevajag turpināt

#print("x1:", x1, "y1:", y1, "x2:", x2, "y2:", y2)

image_from_bb = cv2.imwrite("Road_sign_in_bb.jpg",selected_image[y1:y2,x1:x2,:])
read_created_image = cv2.imread("Road_sign_in_bb.jpg")
reader = easyocr.Reader(['lv'])
result = reader.readtext(read_created_image, detail=0)

print("Detected text:", result)
