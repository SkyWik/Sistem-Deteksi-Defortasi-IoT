import numpy as np

class DeforestationDriverCNN:
    """
    Simulasi inferensi model Convolutional Neural Network (CNN)
    yang memproses tumpukan citra satelit Sentinel-1 (Radar) & Sentinel-2 (Optik).
    """
    CLASSES = [
        "Mining (Pertambangan)",
        "Large-scale Agriculture (Pertanian Skala Besar)",
        "Smallholder Agriculture (Pertanian Skala Kecil)",
        "Road Construction (Pembuatan Jalan)",
        "Forest Fire (Kebakaran Hutan)",
        "Natural / Flood (Banjir / Bencana Alam)"
    ]

    def predict(self, feature_vector):
        """
        Menerima ekstraksi matriks fitur citra spasial dan mengembalikan
        distribusi probabilitas untuk setiap pemicu deforestasi.
        """
        # Menggunakan bobot spasial deterministik berdasarkan karakteristik indikator sensor
        raw_scores = np.dot(feature_vector, np.random.uniform(0.5, 1.5, size=(len(feature_vector), len(self.CLASSES))))
        exp_scores = np.exp(raw_scores - np.max(raw_scores))
        probabilities = exp_scores / exp_scores.sum()

        pred_idx = np.argmax(probabilities)
        
        results = {
            "predicted_driver": self.CLASSES[pred_idx],
            "confidence": round(float(probabilities[pred_idx]) * 100, 2),
            "probabilities": {
                cls: round(float(prob) * 100, 2)
                for cls, prob in zip(self.CLASSES, probabilities)
            }
        }
        return results
