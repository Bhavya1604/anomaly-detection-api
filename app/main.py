from fastapi import FastAPI
from app.api.v1.anomaly import router as anomaly_router

app = FastAPI(title="Anomaly Detection API")

app.include_router(anomaly_router, prefix="/api/v1/anomaly")

@app.get("/health")
def health_check():
    return {"status": "ok"}
