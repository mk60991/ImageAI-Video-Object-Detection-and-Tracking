# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 18:45:12 2018

@author: hp
"""

from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "C:\\Users\\hp\\Downloads\\imageAI object DetectionByVideo\\resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "C:\\Users\\hp\\Downloads\\imageAI object DetectionByVideo\\input video\\traffic.mp4"),
                                output_file_path=os.path.join(execution_path, "C:\\Users\\hp\\Downloads\\imageAI object DetectionByVideo\\output video\\traffic_detected")
                                , frames_per_second=20, log_progress=True)
print(video_path)