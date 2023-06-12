from retinaface import RetinaFace
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import time
start_time = time.time()
obj = DeepFace.verify(img1_path = 'images/1.jpg', img2_path = 'images/2.jpg', model_name = 'Facenet512', detector_backend = 'retinaface', enforce_detection=False)
end_time = time.time()

elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time)
print(obj['verified'])