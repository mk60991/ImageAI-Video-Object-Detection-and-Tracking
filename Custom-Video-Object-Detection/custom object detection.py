# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 19:20:36 2018

@author: hp
"""

from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "C:\\Users\\hp\\Downloads\\imageAI objectDetectionByvideo2\\resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
#detector.loadModel(detection_speed="fast")

custom_objects = detector.CustomObjects(person=True, bicycle=True, motorcycle=True)

video_path = detector.detectCustomObjectsFromVideo(custom_objects=custom_objects, input_file_path=os.path.join(execution_path, "C:\\Users\\hp\\Downloads\\imageAI objectDetectionByvideo2\\input video\\traffic.mp4"),
                                output_file_path=os.path.join(execution_path, "C:\\Users\\hp\\Downloads\\imageAI objectDetectionByvideo2\\output video\\traffic_custom_detected")
                                , frames_per_second=20, log_progress=True)
print(video_path)
