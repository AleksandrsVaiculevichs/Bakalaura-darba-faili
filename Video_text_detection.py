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
# https://stackoverflow.com/questions/39622281/capture-one-frame-from-a-video-file-after-every-10-seconds
# https://stackoverflow.com/questions/67480573/how-to-append-in-list-in-python-without-overwriting
# https://labex.io/tutorials/python-how-to-extract-specific-elements-from-a-list-of-tuples-using-a-lambda-function-in-python-415784
# https://forum.opencv.org/t/how-to-identify-the-correct-coordinates-for-cropping-image/8381
# https://stackoverflow.com/questions/10941229/convert-list-of-tuples-to-list
# https://stackoverflow.com/questions/42074311/loop-through-directory-of-images-and-rotate-them-all-x-degrees-and-save-to-direc

from ultralytics import YOLO
import cv2
import easyocr
import os
from PIL import Image
import glob

model = YOLO('C:/coding and apps/codes/runs/detect/train63/weights/best.pt')
path_with_video = 'C:/coding and apps/codes/Text_detection/video_testing_text_det2.mp4'
path_with_frames = 'C:/coding and apps/codes/frame_folder'
path_for_yolo_trained_frames = 'C:/coding and apps/codes'
folder_name_with_detections = 'C:/coding and apps/codes/yolo_trained_frame_folder'
folder_with_cropped = 'C:/coding and apps/codes/Folder_with_cropped_frames'
boxes = []
files_for_work=[]


'''
Funkcija, kas izgriež kadrus, šajā gadījumā tā ir iestatīta tā,
lai funkcija izgriež katru video sekundi, ja nepieciešams 
vairāk/mazāk kadrus, var mainīt if funkciju.
'''
def extracting_frames ():
    selected_video = cv2.VideoCapture(path_with_video)
    success = True
    fps = int(selected_video.get(cv2.CAP_PROP_FPS))
    count = 0

    while success:
        success, frame = selected_video.read()
        if count%(1*fps) == 0:
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
un pievienots masīvam.
'''
def Yolo_train_on_ready_frames (path_with_frames_folder):
    global boxes, files_for_work
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
                for i in enumerate(cords):
                    boxes.append(i)
                file_name_with_detection = os.path.basename(folder_w_images)
                files_for_work.append(file_name_with_detection)
                print ("Files for work are:", files_for_work)
            else:
                continue
    
'''
Sākotnēji yolo izveido tuples list, kas izskatās apmēram šādi: [(1, coord), (2, coord)...], 
tātad cipari viens, divi... šaja gadījumā ir koordinātes apzimējumi, tas ir x1, x2, y1 un y2.
Šī funkcija vispirms sadala koordinātas no šīs lapas uz updating_boxes, kas tagad izskatās šādi:
[(coord, coord, coord, coord), (coord, coord, ...)]. Un pēc tam, tā kā ir ērtāk izmantot lielu koordinātu lapu,
tā tālāk sadala tuples lapu uz convert_to_list, kas tagad izskatās šādi: [coord, coord, coord, coord, ...].
Pēc tam tas printē visus rezultātus.
'''

def Convert_list_of_tuples_to_list():
        updating_boxes = []
        global convert_to_list
        for coord in range(0, len(boxes),4):
            groupping = boxes[coord:coord+4]
            coordinate = dict(groupping)
            updating_boxes.append((int(coordinate[0]), int(coordinate[1]), int(coordinate[2]), int(coordinate[3])))
        
        convert_to_list = list(sum(updating_boxes, ()))
        
        print ("Standart yolo coordinates in tuples:", boxes)
        print()
        print ("List of coordinates in tuples:", updating_boxes)
        print()
        print ("Converted list of coordinates:", convert_to_list)
        print()

'''
šī funkcija iterē caur darba failiem, kuros ir saglabāti nosaukumi, nolasa attēlu nosaukumu, ņemot vērā pilnu ceļu.
Pēc tam ar katru jaunu iterāciju tiek aprēķinātas 4 koordinātas lapā, no sākuma līdz beigām un katru reizi par +4.
Tas ir iespējams, jo visas koordinātas nav sakārtotas un seko viena aiz otrai vienmērīgi, kas ļauj tās izmantot šādā veidā.
Pēc tam iterē pār šīm koordinātēm, aprēķina x1, x2, y1, y2 un izgriež attēlu atbilstoši kadru koordinātēm.
Pēc tam teksta labākai atpazīšanai var mainīt attēla izmēru, un vēl stradāt ar attēla kvalitātes uzlabojumiem, principā pietiek
ar 300 x 300 izmēru, un attēls tiek saglabāts jaunā mapē.
'''

def Crop_images_and_read_text():
    for i,file in enumerate(files_for_work):
        images = cv2.imread(os.path.join(folder_name_with_detections, file))
        coordinate_start = i*4
        coordinate_end = coordinate_start+4
        full_coord = convert_to_list[coordinate_start:coordinate_end]
        for i in range(0, len(full_coord), 4):
            x1,y1,x2,y2 = full_coord[i:i+4]
            cropping_images = images[y1:y2, x1:x2]
            new_image_size = (300, 300)
            resize_img = cv2.resize(cropping_images, new_image_size)
            cv2.imwrite(f'Folder_with_cropped_frames/cropped_{file}.jpg', resize_img)
            print ("Cropped coordinates in frame:", file)

'''
Un šeit iterējot caur visām failām var izmantot OCR un detektēt tekstu.
'''

def Reading_text():
    for file in os.listdir(folder_with_cropped):
        cropped_frames = cv2.imread(os.path.join(folder_with_cropped, file))
        reader = easyocr.Reader(['lv'])
        result = reader.readtext(cropped_frames, detail=0)
        print(f"Detected text for cropped frame {file}:", result)
    

extracting_frames()
rotating_frames(path_with_frames)
Yolo_train_on_ready_frames(path_with_frames)
Convert_list_of_tuples_to_list()
Crop_images_and_read_text()
Reading_text()
