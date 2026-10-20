from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

from model import DeforestationDriverCNN
from dataset_sim import generate_satellite_patch_features

app = FastAPI(title="Deforestation Driver AI Monitoring")

# Mount folder static
app.mount("/static", StaticFiles(directory="static"), name="static")

model = DeforestationDriverCNN()

class AnalysisRequest(BaseModel):
    driver_scenario: str  # mining, large_agri, small_agri, road, fire, flood

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.post("/api/analyze")
def analyze_deforestation_alert(req: AnalysisRequest):
    valid_scenarios = ["mining", "large_agri", "small_agri", "road", "fire", "flood"]
    if req.driver_scenario not in valid_scenarios:
        raise HTTPException(status_code=400, detail="Skenario tidak valid")
    
    features = generate_satellite_patch_features(req.driver_scenario)
    prediction = model.predict(features)
    
    return {
        "status": "success",
        "scenario_input": req.driver_scenario,
        "satellite_sensors": {
            "sentinel_1_sar": "Active (Radar VV/VH)",
            "sentinel_2_optical": "Active (NDVI / RGB)"
        },
        "analysis_result": prediction
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
