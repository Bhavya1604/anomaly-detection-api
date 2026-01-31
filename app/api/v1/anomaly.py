from fastapi import APIRouter
from app.schemas.anomaly import AnomalyRequest
from app.models.anomaly_model import detect_anomalies

router = APIRouter()

@router.post("/detect")
def detect_anomaly(request: AnomalyRequest):
    anomalies = detect_anomalies(
        request.series,
        threshold=request.threshold
    )
    return {
        "anomalies": anomalies,
        "count": len(anomalies),
        "threshold_used": request.threshold
    }
