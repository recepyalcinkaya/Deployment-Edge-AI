import cv2
import numpy as np

def preprocess(frame, target_size=(640, 640)):
    """Görüntüyü modele girmeden önce boyutlandırır."""
    resized = cv2.resize(frame, target_size)
    return resized

def postprocess(detections, threshold=0.5):
    """
    Hailo'dan gelen ham veriyi işler. 
    YOLOv11 post-process mimarisi modele göre değişebilir.
    """
    # Bu kısım modelin output layer yapısına göre özelleştirilmelidir
    # Şimdilik örnek bir çıktı döndürüyoruz
    boxes, scores, classes = [], [], []
    
    # Donanım tabanlı NMS (Non-Maximum Suppression) varsa direkt sonuçlar alınır
    # Yoksa burada NumPy ile manuel NMS yapılmalıdır.
    return boxes, scores, classes

def draw_boxes(frame, boxes, scores, classes):
    for box, score, cls in zip(boxes, scores, classes):
        x, y, w, h = box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"ID:{cls} {score:.2f}", (x, y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame
