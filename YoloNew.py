import cv2
import numpy as np


object_count =[];
object_name =[];

class YoloNew:
    

        
    def __init__(self,img=None):
        self.img=img
    def detectIMG(self):
        # Load Yolo
        net = cv2.dnn.readNet("data/yolov3.weights", "data/yolov3.cfg")
        classes = []
        with open("data/coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]
        # print(classes)
        print(len(classes))
        layer_names = net.getLayerNames()

# https://stackoverflow.com/a/72040137
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        
        # # # Loading image
        img = cv2.imread(self.img)#"E:\\PROJECTS\\random_images\\traffic.jpg")
        img = cv2.resize(img, None, fx=0.2, fy=.2)
        height, width, channels = img.shape
        
        # # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        for b in blob:
            for n, img_blog in enumerate(b):
                cv2.imshow(str(n), img_blog)
        
        net.setInput(blob)
        outs = net.forward(output_layers)
        print(outs)
        
        
        cv2.imshow("Image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()                                     
        
        # # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.43:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
        #            cv2.circle(img,(center_x, center_y), 50, (0,255,0),2)
                    ####### Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
        #            cv2.rectangle(img,(x, y),(x+w,y+h) , (0,255,0),2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
                    
        print(len(boxes))            
        number_objects_detected=len(boxes)
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.4)
        print(indexes)
        
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                print(label)
                YoloNew.sort_and_type(label)
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
        
        
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def get_array_of_objects_name_with_count(self):
        a=[]
        print('inside the total get')
        for i in range(len(object_name)):
#            a.append(i)
            a.append(f'{object_name[i]} {object_count[i]}')
        for i in range(len(a)):
            print(a[i])
        YoloNew.clear_objects()
        return a    
 
        
    def sort_and_type(lbl):    
        if lbl not in object_name:
            object_name.append(lbl)
            i=object_name.index(lbl)
            object_count.append(0)
            object_count[i]+=1
        else:
            i=object_name.index(lbl)
            object_count[i]+=1

    def clear_objects():
        
        object_count.clear()
        object_name.clear()
        
        
    def detectVideo(self):
        # Load Yolo
        net = cv2.dnn.readNet("data/yolov3.weights", "data/yolov3.cfg")
        classes = []
        with open("data/coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]
        # print(classes)
        print(len(classes))
        layer_names = net.getLayerNames()

# https://stackoverflow.com/a/72040137
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        
        video_capture = cv2.VideoCapture(0)#camera number
        video_capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            # # # Loading image
            img =frame
            img = cv2.resize(img, None, fx=1.5, fy=1.5)
            height, width, channels = img.shape
            
            # # Detecting objects
            blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            # for b in blob:
            #     for n, img_blog in enumerate(b):
            #         cv2.imshow(str(n), img_blog)
            
            net.setInput(blob)
            outs = net.forward(output_layers)
            print(outs)
            
                                         
            
            # # Showing informations on the screen
            class_ids = []
            confidences = []
            boxes = []
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.43:
                        # Object detected
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)
                        # cv2.circle(img,(center_x, center_y), 50, (0,255,0),2)
                        ####### Rectangle coordinates
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
                        cv2.rectangle(img,(x, y),(x+w,y+h) , (0,255,0),2)
                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)
                        
            print(len(boxes))            
            number_objects_detected=len(boxes)
            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.4)
            print(indexes)
            
            font = cv2.FONT_HERSHEY_PLAIN
            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    print(label)
                    YoloNew.sort_and_type(label)
                    color = colors[i]
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                    cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
            
            
            cv2.imshow('Video', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()
        
       
                
                
    