# IZMANTOTI INFORMĀCIJAS AVOTI
# https://stackoverflow.com/questions/34966541/how-can-one-display-an-image-using-cv2-in-python
# https://github.com/ultralytics/yolov5/issues/388 
# https://dev.to/andreygermanov/how-to-extract-all-detected-objects-from-image-and-save-them-as-separate-images-using-yolov82-and-opencv-3j99
# https://blog.roboflow.com/how-to-use-easyocr/
# https://builtin.com/data-science/python-ocr         
# https://stackoverflow.com/questions/41586429/opencv-saving-images-to-a-particular-folder-of-choice
# https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
# https://stackoverflow.com/questions/56368107/rotation-of-images
# https://stackoverflow.com/questions/41586429/opencv-saving-images-to-a-particular-folder-of-choice
# https://stackoverflow.com/questions/64202415/resize-rename-and-rotate-multiple-images-using-python
# https://stackoverflow.com/questions/66232972/remove-black-bars-excess-from-image-rotated-with-pil
# https://stackoverflow.com/questions/48248405/cannot-write-mode-rgba-as-jpeg
# https://github.com/ultralytics/ultralytics/issues/10264
# https://github.com/ultralytics/ultralytics/issues/10367
# https://github.com/ultralytics/ultralytics/issues/7864
# https://github.com/ultralytics/ultralytics/issues/7774
# https://pynative.com/python-rename-file/
# https://stackoverflow.com/questions/64970901/writing-filenames-into-an-array-in-python
# https://stackoverflow.com/questions/52873938/referring-to-arrays-from-another-function
# https://github.com/ultralytics/ultralytics/issues/5097
# https://stackoverflow.com/questions/72507868/how-to-read-the-text-by-easyocr-correctly
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory


from ultralytics import YOLO
import cv2
import easyocr
import os
from PIL import Image
import glob
import numpy as np

model = YOLO('C:/coding and apps/codes/runs/detect/train63/weights/best.pt')
path_with_video = 'video_testing_text_det.mp4'
path_with_frames = 'C:/coding and apps/codes/frame_folder'
path_for_yolo_trained_frames = 'C:/coding and apps/codes'
folder_name_with_detections = 'C:/coding and apps/codes/yolo_trained_frame_folder'
boxes = []
files_for_work=[]

'''
Funkcija, kas izgriež kadrus, šajā gadījumā tā ir iestatīta tā,
lai funkcija izgriež katru video sekundi, ja nepieciešams 
vairāk/mazāk kadrus, var mainīt mainīgo 'count'.
'''
def extracting_frames ():
    selected_video = cv2.VideoCapture(path_with_video)
    success, frame = selected_video.read()
    count = 0
    while success:
        selected_video.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
        success, frame = selected_video.read()
        
        cv2.imwrite('frame_folder/frame%d.jpg' % count, frame)
        print('Created new frame: ', success)
        count +=1

'''
Funkcija, ja nepieciešams pagriezt kadrus
'''
def rotating_frames (path_with_frames_folder) :
    for folder_w_images in glob.glob(os.path.join(path_with_frames_folder, "*.jpg")):
        opening_images = Image.open(folder_w_images).convert('RGB')
        rotaing_images = opening_images.rotate(-90, expand=True, fillcolor = (0,0,0,0))
        rotaing_images.save(folder_w_images)
        print('Rotated frames succesfully!')
'''
Šī funkcija aplūko katru attēlu un izmanto yolo, lai atpazītu zīmi.  Testēšanas laikā tiek veikta
pārbaude, ja zīmes klase atbilst izvēlētām, tiek saglabātas tās koordinātas. Nosaukums tiek saglabāts
un pievienots masīvam. Pēc tam vēlreiz caur visām failām, ja faila nosaukums ir masīvā, tas tiek pārdēvēts
uz citu nosaukumu turpmākajam darbam.
'''
def Yolo_train_on_ready_frames (path_with_frames_folder):
    global boxes, x1, x2, y1, y2, files_for_work
    for folder_w_images in glob.glob(os.path.join(path_with_frames_folder, "*.jpg")):
        open_images = Image.open(folder_w_images)
        results = model(open_images,
                        conf=0.75,
                        save=True,
                        project = path_for_yolo_trained_frames,
                        name = "yolo_trained_frame_folder",
                        exist_ok = True)
        
        for box in results[0].boxes:  
            cls = results[0].names[box.cls[0].item()]
            if cls == "44": # 44 ir ceļa zīmes nosaukums
                print("Road sign is detected.")
                cords = box.xyxy[0].tolist()
                score = box.conf[0].item() 
                x1, y1, x2, y2 = [round(x) for x in cords]
                boxes.append([x1, y1, x2, y2, score, cls])
                print("Road sign coordinates are: ", x1, y1, x2, y2)
                file_name_with_detection = os.path.basename(folder_w_images)
                files_for_work.append(file_name_with_detection)
                print ("Files for work are:", files_for_work)
            else:
                continue
    
'''
Šī funkcija apstrādā atlasīto kadru failus. Tā ņem lapu no izvēlētajiem kadriem un izgriež attēlu
atbilstoši iepriekš iegūtajām koordinātēm. Tā kā ceļa zīmes izmērs var būt atšķirīgs, labāk ir iestatīt
fiksētu izmēru, lai labāk atpazītu tekstu. Taču nākotnē ir nepieciešams uzlabot attēla kvalitāti, izmantojot papildu metodes.
'''

def Create_new_image_and_detect_text():
    for file in files_for_work:
        images = cv2.imread(os.path.join(folder_name_with_detections, file))
        cropping_image = images[int(y1):int(y2), int(x1):int(x2)]
        new_image_size = (300, 300)
        resize_img = cv2.resize(cropping_image, new_image_size)
        cv2.imwrite('Cropped_image.jpg', resize_img)
        reader = easyocr.Reader(['lv'])
        result = reader.readtext(resize_img, detail=0)
        print("Detected text:", result)
    

    
extracting_frames()
rotating_frames(path_with_frames)
Yolo_train_on_ready_frames(path_with_frames)
Create_new_image_and_detect_text()
