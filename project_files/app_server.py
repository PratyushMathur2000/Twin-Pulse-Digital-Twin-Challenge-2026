#!/usr/bin/env python3
"""
Twin-Pulse Health v3.1 — FastAPI Backend & Zero-Dependency Local Server
=======================================================================
Serves the 3D Human Digital Twin Cockpit (`ui/twin_pulse_clinical_dashboard.html`),
the 3-Stage Cardiometabolic ML Engine (`/api/v1/predict`), and the Local AI Proxy
(`/api/v1/copilot` -> LM Studio :1234 / Ollama :11434 with automatic clinical fallback).
If FastAPI/Uvicorn are not installed, automatically falls back to Python's built-in HTTP server.
"""
import os
import sys
import json
import webbrowser
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "utils"))

from utils.digital_twin_engine import AdaptableCMBCDTwinEngine, FEATURE_COLUMNS
from utils.clinical_copilot import query_local_llm

UI_PATH = os.path.join(BASE_DIR, "ui", "twin_pulse_clinical_dashboard.html")
DATA_CSV = os.path.join(BASE_DIR, "data", "twin_pulse_cardiometabolic_ehr_wearable_data.csv")
EHR_CSV = os.path.join(BASE_DIR, "data", "synthea_ehr_patients.csv")
METRICS_JSON = os.path.join(BASE_DIR, "saved_models", "model_evaluation_metrics.json")

df_all = pd.read_csv(DATA_CSV)
twin_engine = AdaptableCMBCDTwinEngine(seed=42).fit(df_all)

try:
    from fastapi import FastAPI
    from fastapi.responses import FileResponse
    from fastapi.middleware.cors import CORSMiddleware

    app = FastAPI(title="Twin-Pulse Healthcare Digital Twin v3.1", version="3.1.0")
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

    @app.get("/")
    def index():
        return FileResponse(UI_PATH)

    @app.get("/api/v1/health")
    def health():
        with open(METRICS_JSON) as f:
            m = json.load(f)
        return {"status": "ok", "version": "3.1.0", "metrics": m}

    @app.get("/api/v1/cohort")
    def cohort():
        df_ehr = pd.read_csv(EHR_CSV)
        return {"count": len(df_ehr), "patients": df_ehr.to_dict(orient="records")}

    @app.post("/api/v1/predict")
    def predict(patient_state: dict):
        return twin_engine.predict_single_patient(patient_state)

    @app.post("/api/v1/copilot")
    def copilot(payload: dict):
        endpoint = payload.get("endpoint", "http://localhost:1234/v1/chat/completions")
        model = payload.get("model", "local-model")
        return query_local_llm(payload, endpoint=endpoint, model=model)

    HAS_FASTAPI = True
except ImportError:
    app = None
    HAS_FASTAPI = False


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    url = f"http://localhost:{port}"
    print(f"Starting Twin-Pulse v3.1 Local Server at {url} ...")
    try:
        webbrowser.open(url)
    except Exception:
        pass

    if HAS_FASTAPI:
        try:
            import uvicorn
            uvicorn.run(app, host="127.0.0.1", port=port)
            sys.exit(0)
        except ImportError:
            pass

    # Built-in Python stdlib HTTP server fallback (works with zero pip installs)
    import http.server
    class TwinHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path in ("/", "/index.html"):
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                with open(UI_PATH, "rb") as f:
                    self.wfile.write(f.read())
            elif self.path == "/api/v1/health":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                with open(METRICS_JSON, "rb") as f:
                    self.wfile.write(f.read())
            else:
                super().do_GET()

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length).decode("utf-8") if length else "{}"
            payload = json.loads(raw or "{}")
            if self.path == "/api/v1/copilot":
                res = query_local_llm(payload)
            else:
                res = twin_engine.predict_single_patient(payload)
            body = json.dumps(res).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(body)

    with http.server.HTTPServer(("127.0.0.1", port), TwinHandler) as httpd:
        print(f"Serving 3D Human Twin Cockpit on {url} (Press Ctrl+C to stop)")
        httpd.serve_forever()
