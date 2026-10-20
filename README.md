# Deforestation Alert & Driver Classification System (AI & Satellite Imagery)

Repositori ini merupakan implementasi studi kasus dari resume **Sesi 6: Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI** (Pemateri: Bart Slagter - Wageningen University & Research).

Sistem ini memodelkan klasifikasi otomatis pemicu (*direct drivers*) deforestasi berdasarkan data citra satelit gabungan (Sentinel-1 Radar & Sentinel-2 Optik) menggunakan arsitektur **Convolutional Neural Network (CNN)**.

---

## 📌 Studi Kasus & Implementasi Teori dari Resume

Sistem pemantauan konvensional hanya mampu mendeteksi *lokasi* hilangnya tutupan pohon, namun tidak mengetahui *penyebabnya*. Repositori ini menyelesaikan tantangan tersebut dengan mengimplementasikan:

1. **Multi-Source Satellite Data Processing (Sentinel-1 & Sentinel-2)**
   - **Sentinel-1 (Radar/SAR):** Menembus tutupan awan tropis dan mendeteksi perubahan struktur/tekstur permukaan tanah.
   - **Sentinel-2 (Optik):** Menganalisis indeks vegetasi (NDVI) dan variasi spektral warna (RGB/NIR).

2. **Convolutional Neural Network (CNN) Classifier**
   - Mengklasifikasikan pola spasial dari citra satelit ke dalam 6 kategori pemicu utama:
     - 🏗️ **Mining** (Pertambangan)
     - 🚜 **Large-scale Agriculture** (Pertanian Skala Besar)
     - 🌾 **Smallholder Agriculture** (Pertanian Skala Kecil)
     - 🛣️ **Road Construction** (Pembuatan Jalan)
     - 🔥 **Forest Fire** (Kebakaran Hutan)
     - 🌊 **Natural / Flood** (Banjir / Faktor Alam)

3. **Infrastruktur & Evaluasi Model**
   - Dirancang agar kompatibel dengan alur kerja **Google Earth Engine (GEE)** dan **Vertex AI**.
   - Menyediakan antarmuka web interaktif untuk visualisasi hasil inferensi dan skor probabilitas klasifikasi.

---

## 🛠️ Struktur Repositori

```text
deforestation_ai_monitoring/
├── app.py              # Server web FastAPI untuk antarmuka & inferensi model
├── model.py            # Arsitektur CNN PyTorch / TensorFlow & pipeline klasifikasi
├── dataset_sim.py      # Generator simulasi citra satelit Sentinel-1 (Radar) & Sentinel-2 (Optik)
├── static/
│   ├── index.html      # Dashboard UI interaktif
│   ├── style.css       # Styling UI (Dark mode & Responsive)
│   └── script.js       # Integrasi API & visualisasi grafik probabilitas
├── requirements.txt    # Dependensi Python
└── README.md           # Dokumentasi proyek
```

---

## 🚀 Cara Menjalankan

1. **Clone & Install Dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Jalankan Aplikasi Server:**
   ```bash
   python app.py
   ```

3. **Buka di Browser:**
   Akses `http://localhost:8000` untuk membuka dashboard simulasi klasifikasi driver deforestasi.
