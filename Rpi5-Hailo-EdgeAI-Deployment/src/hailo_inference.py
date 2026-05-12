import numpy as np
from hailo_platform import PcieDevice, HEF, InferModel

class HailoInference:
    def __init__(self, hef_path):
        # 1. Hailo Cihazını Bul ve Bağlan
        self.target = PcieDevice()
        
        # 2. HEF (Hailo Executable Format) dosyasını yükle
        self.hef = HEF(hef_path)
        
        # 3. Infer Model konfigürasyonu
        self.infer_model = self.target.create_infer_model(hef_path)
        self.infer_model.set_hw_latency_measurement(True)
        
        # Giriş ve çıkış kuyruklarını ayarla
        self.configure_params = self.infer_model.configure()
        self.output_queue = self.configure_params.output_queue
        self.input_queue = self.configure_params.input_queue

    def run_inference(self, frame):
        # Görüntüyü modelin giriş boyutuna getir (Örn: 640x640)
        # Not: Hailo modelleri genellikle uint8 bekler
        input_data = {self.infer_model.input_name: np.expand_dims(frame, axis=0)}
        
        with self.infer_model.run(input_data) as result:
            # Donanımdan gelen ham sonuçları al
            output_data = result.get_outputs()
            return output_data

    def __del__(self):
        # Kaynakları serbest bırak
        self.target.release()
