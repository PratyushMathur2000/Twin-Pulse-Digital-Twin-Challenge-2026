#!/usr/bin/env python3
"""
Twin-Pulse AI Clinical Advisor & Diagnostic Co-Pilot
Supports:
1. Google Gemini (Cloud API / gemini-3.5-flash-lite)
2. LM Studio (http://localhost:1234/v1/chat/completions)
3. Ollama (http://localhost:11434/v1/chat/completions)
4. Deterministic CMBCD clinical protocol fallback
"""
import os
import json
import urllib.request

DEFAULT_LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"

def query_gemini_api(prompt_text: str, api_key: str = None) -> dict:
    key = api_key or os.environ.get("GEMINI_API_KEY")
    if not key:
        raise ValueError("Missing Gemini API key")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={key}"
    payload = {
        "system_instruction": {
            "parts": [{
                "text": "You are the Twin-Pulse Healthcare Digital Twin Clinical Advisor. Provide a concise, actionable clinical SOAP note and titration protocol."
            }]
        },
        "contents": [{"role": "user", "parts": [{"text": prompt_text}]}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 600}
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=8.0) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        reply = res["candidates"][0]["content"]["parts"][0]["text"]
        return {"source": "gemini_3.5_flash", "soap_note": reply}

def query_local_llm(patient_payload: dict, endpoint: str = DEFAULT_LM_STUDIO_URL, model: str = "local-model", api_key: str = None) -> dict:
    pid = patient_payload.get("patient_id", "PT-IND-001")
    prompt_text = f"Generate a clinical SOAP note and counterfactual plan for patient state: {json.dumps(patient_payload)}"
    
    # Try Gemini if key is provided or requested
    if api_key or os.environ.get("GEMINI_API_KEY") or "gemini" in model.lower():
        try:
            return query_gemini_api(prompt_text, api_key=api_key)
        except Exception:
            pass

    # Try local OpenAI-compatible endpoint
    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": "You are the Twin-Pulse Healthcare Digital Twin Clinical Co-Pilot."},
            {"role": "user", "content": prompt_text}
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
        return {
            "source": "deterministic_cmbcd_fallback",
            "soap_note": f"[TWIN-PULSE CMBCD PROTOCOL • {pid}] Restrict next meal bolus to <=45g low-GI carbs, maintain prescribed pharmacotherapy, and add a 15-min post-meal walk (+2,500 steps) to elevate vagal HRV and extend safe RUL window."
        }
