import numpy as np

def detect_anomalies(series, threshold=3.0):
    data = np.array(series)
    mean = data.mean()
    std = data.std()

    if std == 0:
        return []

    z_scores = (data - mean) / std
    anomalies = [i for i, z in enumerate(z_scores) if abs(z) > threshold]

    return anomalies
