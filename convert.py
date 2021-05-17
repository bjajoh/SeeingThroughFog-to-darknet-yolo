import os
import numpy as np
from glob import glob                                                           
from pathlib import Path
from tqdm import tqdm

#YOLO Labels: <object-class> <x> <y> <width> <height>

dataset_root_path = '/your_mom/SeeingThroughFog/'

def convert_to_yolo(line, label_path):
    try:
        output_path = dataset_root_path+'cam_stereo_left_lut/'+Path(label_path).stem+'.txt'
        #print(line.split()[0], '  ',line.split()[4] ,'  ',line.split()[5], '  ', line.split()[6], '  ', line.split()[7])
        f = open(output_path, "a")
        img_height = 1024
        img_width = 1920

        obj_class = -1
        if(line.split()[0] == 'Pedestrian'):
            obj_class = 0
        elif(line.split()[0] == 'RidableVehicle'):
            obj_class = 1
        elif(line.split()[0] == 'PassengerCar'):
            obj_class = 2

        if(obj_class != -1):
            width = float(line.split()[6])-float(line.split()[4])
            height = float(line.split()[7])-float(line.split()[5])
            x_center = float(line.split()[4]) + (width)/2
            y_center = float(line.split()[5]) + (height)/2
            #print('class: ', line.split()[0], 'x: ', x_center, '  y: ', y_center, '  height: ', height, '  width: ', width)
            #print('class: ', obj_class, '  x: ', x_center/img_width, '  y: ', y_center/img_height, '  height: ', height/img_height, '  width: ', width/img_width)
            f.write(str(obj_class)+' '+str(x_center/img_width)+' '+str(y_center/img_height)+' '+str(width/img_width)+' '+str(height/img_height)+'\n')
            f.close()
    except:
        print("Couldn't convert: ", Path(label_path).stem)
        
#label_path = rgb_labels[0]
rgb_labels = glob(dataset_root_path+'gt_labels/cam_left_labels_TMP/*.txt')
for label_path in tqdm(rgb_labels):
    with open(label_path) as f:
        for line in f:
            convert_to_yolo(line, label_path)
