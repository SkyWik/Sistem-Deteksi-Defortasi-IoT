import numpy as np

def generate_satellite_patch_features(driver_type="mining"):
    """
    Membuat simulasi vektor fitur spasial-spektral gabungan dari:
    - Sentinel-1 SAR (Backscatter VV/VH intensity)
    - Sentinel-2 Optical (NDVI, NBR, RGB)
    """
    np.random.seed(hash(driver_type) % 2**32)
    
    # 8-dim vektor fitur: [NDVI_before, NDVI_after, SAR_VV, SAR_VH, NBR_burn, Road_line_density, Water_index, Texture_entropy]
    base_features = {
        "mining": [0.8, 0.1, 0.85, 0.90, 0.2, 0.4, 0.6, 0.88],
        "large_agri": [0.85, 0.2, 0.30, 0.25, 0.1, 0.9, 0.1, 0.30],
        "small_agri": [0.75, 0.3, 0.45, 0.40, 0.1, 0.3, 0.1, 0.65],
        "road": [0.80, 0.2, 0.70, 0.75, 0.1, 0.95, 0.1, 0.40],
        "fire": [0.82, 0.05, 0.20, 0.15, 0.95, 0.1, 0.0, 0.70],
        "flood": [0.78, 0.10, 0.05, 0.02, 0.05, 0.1, 0.95, 0.20]
    }
    
    features = base_features.get(driver_type, base_features["mining"])
    noise = np.random.normal(0, 0.05, size=len(features))
    return np.clip(np.array(features) + noise, 0, 1)
