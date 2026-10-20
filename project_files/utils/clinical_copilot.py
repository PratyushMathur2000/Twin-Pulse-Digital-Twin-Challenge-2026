#!/usr/bin/env python3
"""
Twin-Pulse Local AI Clinical Co-Pilot (Adapted from 5_AI_Diagnostic_Agent.py & 6_Settings.py)
Supports LM Studio (http://localhost:1234/v1/chat/completions) and Ollama (http://localhost:11434/v1/chat/completions)
with zero-downtime deterministic CMBCD clinical protocol fallback.
"""
import json
import urllib.request

DEFAULT_LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"

def query_local_llm(patient_payload: dict, endpoint: str = DEFAULT_LM_STUDIO_URL, model: str = "local-model") -> dict:
    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": "You are the Twin-Pulse Healthcare Digital Twin Clinical Co-Pilot."},
            {"role": "user", "content": f"Generate a clinical SOAP note for patient state: {json.dumps(patient_payload)}"}
        ],
        "temperature": 0.2,
        "max_tokens": 400
    }).encode("utf-8")
    try:
        req = urllib.request.Request(endpoint, data=body, headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=3.5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {"source": "local_llm", "soap_note": data["choices"][0]["message"]["content"]}
    except Exception:
        pid = patient_payload.get("patient_id", "PT-IND-001")
        return {
            "source": "deterministic_cmbcd_fallback",
            "soap_note": f"[TWIN-PULSE CMBCD PROTOCOL • {pid}] Restrict next meal bolus to <=45g low-GI carbs, maintain prescribed pharmacotherapy, and add a 15-min post-meal walk (+2,500 steps) to elevate vagal HRV and extend safe RUL window."
        }
