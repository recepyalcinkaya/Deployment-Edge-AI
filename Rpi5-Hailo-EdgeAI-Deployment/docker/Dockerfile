# Raspberry Pi 5 (ARM64) için resmi Python imajı
FROM python:3.10-slim-bullseye

# Sistem bağımlılıklarını kur (OpenCV ve Hailo için gerekli)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libhailo-rt \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini oluştur
WORKDIR /app

# Bağımlılıkları kopyala ve kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY . .

# Hailo donanımına erişim için çevre değişkenleri
ENV HAILO_ACCELERATOR_DEVICE=/dev/hailo0

# Uygulamayı çalıştır
CMD ["python", "main.py"]
