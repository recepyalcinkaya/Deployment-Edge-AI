import cv2
from hailo_inference import HailoInference
from utils import preprocess, postprocess, draw_boxes

def main():
    MODEL_PATH = "models/yolov11n.hef"
    
    # 1. Hailo'yu başlat
    print("🚀 Hailo Inference Motoru Başlatılıyor...")
    hailo_engine = HailoInference(MODEL_PATH)
    
    # 2. Kamerayı Aç (Raspberry Pi Camera veya USB)
    cap = cv2.VideoCapture(0)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        
        # 3. Ön İşleme
        input_frame = preprocess(frame)
        
        # 4. Donanım Hızlandırmalı Çıkarım (Hailo AI HAT+)
        raw_results = hailo_engine.run_inference(input_frame)
        
        # 5. Son İşleme (NMS ve Koordinat Çevrimi)
        boxes, scores, classes = postprocess(raw_results)
        
        # 6. Görselleştirme
        output_frame = draw_boxes(frame, boxes, scores, classes)
        
        # Sonucu göster (Docker'da GUI için X11 ayarı gerekir)
        cv2.imshow("Hailo RPi5 ADAS Perception", output_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
