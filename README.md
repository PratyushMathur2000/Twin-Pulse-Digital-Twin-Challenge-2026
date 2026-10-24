# Twin-Pulse: Cardiometabolic Digital Twin Workstation

**Submission for the Happiest Health Digital Twin Challenge 2026**  
*Reimagining and Reforming Healthcare in India Summit 2026, Bengaluru*

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-success?style=for-the-badge&logo=vercel)](https://twin-pulse-digital-twin-challenge-2-two.vercel.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![FastAPI](https://img.shields.io/badge/API-FastAPI%20REST-009688.svg?style=for-the-badge&logo=fastapi)](project_files/app_server.py)

> 🌐 **Live Production Deployment:** [https://twin-pulse-digital-twin-challenge-2-two.vercel.app/](https://twin-pulse-digital-twin-challenge-2-two.vercel.app/)  
> *Zero-setup, fully responsive clinician cockpit featuring real-time 3D anatomical visualization, 6-hour counterfactual What-If simulator, and 100-patient Indian cohort triage.*

## 1. Team Details

* **Team Name:** Twin-Pulse
* **Institution:** SVKM's NMIMS, Mumbai (Second Year)
* **Team Members (2 Members):**
  * **Pratyush Mathur (Team Leader)** — Second Year, SVKM's NMIMS, Mumbai
  * **Aryan Jain (Team Member)** — Second Year, SVKM's NMIMS, Mumbai

## 2. Clinical Problem & Indian Healthcare Context

Standard care in India manages Type 2 Diabetes (T2D), Hypertension (HTN), Dyslipidemia, and Chronic Kidney Disease (CKD) in isolated clinical silos, typically intervening only after an acute glycemic excursion or vascular event occurs. Screening by Body Mass Index (BMI) alone misses a large proportion of high-risk Indian patients:

* **The Asian Indian "Thin-Fat" (`MONO`) Phenotype:** The nationally representative [ICMR-INDIAB Study (n = 113,043)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12550443/) showed that **43.3% of Indian adults exhibit the Metabolically Obese Non-Obese (`MONO`) phenotype** (normal BMI < 25 kg/m² with high visceral adiposity, elevated HOMA-IR, and atherogenic dyslipidemia), while **28.3% exhibit the Metabolically Obese Obese (`MOO`) phenotype**.
* **Multi-Organ Risk Escalation:** Compared to metabolically healthy individuals, non-obese `MONO` Indians carry a **6.90x higher risk of Type 2 Diabetes**, a **1.77x higher risk of Coronary Artery Disease (CAD)**, and a **1.81x higher risk of Chronic Kidney Disease (CKD)**, with **57.4% presenting three or more overlapping metabolic drivers simultaneously** ([ICMR-INDIAB Study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12550443/)).
* **Clinical Impact of Digital Twinning:** In Indian clinical cohorts (n = 1,853 and n = 319), continuous sensor + EHR digital twins lowered mean HbA1c by **1.8% to 2.9%**, improved Continuous Glucose Monitor (CGM) Time-in-Range from **69.7% to 86.9%**, and achieved **72.7% diabetes remission** and **60% hypertension remission** at 1 year ([Cardiometabolic Digital Twin Systematic Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12632027/)).

## 3. Solution Overview

**Twin-Pulse** is a real-time clinical Digital Twin workstation and FastAPI microservice grounded in the **Cardiometabolic-Based Chronic Disease (CMBCD)** model. It fuses static Electronic Health Records (Synthea / HL7 FHIR R4) with continuous wearable telemetry to power a 3-stage machine learning prognosis pipeline, an interactive 3D anatomical twin, a counterfactual "What-If" simulator, a 4-organ physiological sandbox, and an on-device Clinical AI Advisor.

### Core Workstation Capabilities

1. **3D Hemodynamic & Anatomical Twin Cockpit:** 60 FPS interactive 3D human point-cloud, skeletal wireframe, vagus nerve filaments, and arterial flow particles coupled with real-time organ strain across 4 physiological subsystems:
   * **Pancreatic β-Cell & Glycemic Axis (`Glycemic_T2D` — Flagship Module)**
   * **Systemic Arterial Tree & Conduit Aorta (`Hemodynamic_HTN`)**
   * **Cardiac Autonomic & Coronary Axis (`Cardiac_CVD`)**
   * **Hepatic-Renal Filtration Axis (`HepaticRenal_CKD`)**
2. **AI-Driven Multi-Organ Sandbox & 6-Hour Counterfactual Trajectory:** Compares patient baseline against simulated or AI-optimized interventions across all 4 organ subsystems, plotting 6-hour post-meal glycemic and blood pressure trajectories and providing one-click **AI Auto-Optimize Twin** remission targets.
3. **Counterfactual "What-If" Physiology Simulator:** Zero-latency perturbation sliders for meal carbohydrate load (g), medication adherence (%), nocturnal sleep duration (hrs), daily physical activity (steps), and sympathetic stress load (0–100), plus one-click clinical presets (*Meal Spike*, *Poor Sleep*, *Optimal Care*).
4. **Clinical AI Advisor & Local AI CDS Studio:** Always-visible clinical advisor generating proactive nutrition, pharmacotherapy, and vagal recovery orders alongside structured SOAP notes and HL7 FHIR R4 bundles. Supports direct connection to local LLMs via **LM Studio (`:1234`)**, **Ollama (`:11434`)**, or the **FastAPI Proxy (`:8000`)** with automatic zero-downtime fallback to the built-in CMBCD Advisor Engine.
5. **100-Patient Population Cohort Triage:** Interactive ward and outpatient triage board across 100 synthetic Indian digital twins (`PT-IND-001` to `PT-IND-100`) with search, archetype/stage filtering, slide-out patient inspection drawer, and CSV export.

## 4. System Architecture

```text
+---------------------------------------------------------------------------------------------------+
|                           DATA INGESTION & PRIVACY SANDBOX LAYER                                  |
|    (DPDP Act 2023 & HIPAA Compliant Synthetic Cohort: 100 Indian Patients, 1,500 Windows)         |
+-------------------------------------------------+-------------------------------------------------+
                                                  |
                  +-------------------------------+-------------------------------+
                  |                                                               |
                  v                                                               v
+-----------------------------------+                           +-----------------------------------+
| STREAM 1: STATIC / HISTORICAL EHR |                           | STREAM 2: DYNAMIC WEARABLE / IoT  |
| - Synthea Demographics & City     |                           | - Continuous Glucose (CGM mg/dL)  |
| - ICMR-INDIAB Phenotype (MONO/MOO)|                           | - CGM Velocity (mg/dL/min)        |
| - BMI & Waist Circumference (cm)  |                           | - Cuffless PPG BP (SBP/DBP mmHg)  |
| - HbA1c (%), Fasting Glu, HOMA-IR |                           | - Autonomic HRV (RMSSD ms) & HR   |
| - Lipids (TG, HDL, LDL, TG/HDL)   |                           | - Nocturnal Sleep Duration (hrs)  |
| - Renal eGFR & Hepatic FIB-4      |                           | - 24h Step Count & Meal Carbs (g) |
+-----------------+-----------------+                           +-----------------+-----------------+
                  |                                                               |
                  +-------------------------------+-------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                     PHYSIOLOGICAL COUPLING & 4-ORGAN SANDBOX ENGINE                               |
|  [1] Pancreatic (Glycemic_T2D)  [2] Vascular (Hemodynamic_HTN)  [3] Cardiac_CVD  [4] HepaticRenal |
|  Coupled ODEs & Interactions: Bergman Minimal Model, Windkessel SVR, Vagal HRV, eGFR/FIB-4 Wear   |
+-------------------------------------------------+-------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                        3-STAGE PROGNOSTIC ML ENGINE & FASTAPI MICROSERVICE                        |
|  - Stage 1 Adverse Event Classifier: 2-hr glycemic (>200 mg/dL) / 24-hr crisis (96.74% Recall)    |
|  - Stage 2 CMBCD 4-Stage Soft-Voting Ensemble: Stage 1 to Stage 4 staging (0.9209 Macro F1)       |
|  - Stage 3 Safe Clinical Window (Time-to-Threshold / TTT) Regressor: Hours to threshold breach (R² = 0.9607, 6.15h) |
+-------------------------------------------------+-------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                     CLINICIAN WORKSTATION & LOCAL AI ADVISOR (SAHARA V6)                          |
|  - 3D Anatomical Twin + Real-Time 250 Hz Lead II ECG + 2-Hr CGM Horizon Cone                      |
|  - AI-Driven 4-Organ Sandbox, 6-Hr Counterfactual Trajectory & What-If Perturbation Sliders       |
|  - Clinical AI Advisor (LM Studio / Ollama / Built-In CMBCD Fallback) + HL7 FHIR R4 Bundle Export |
+---------------------------------------------------------------------------------------------------+
```

## 5. Holdout Validation Benchmarks

Evaluated on a strict patient-grouped 80/20 holdout split (80 training patients = 1,200 longitudinal windows; 20 unseen test patients = 300 longitudinal windows):

| Model Component | Clinical Prediction Target | Primary Metric | Secondary Metrics | Inference Latency |
| :--- | :--- | :--- | :--- | :--- |
| **Stage 1: Adverse Event Classifier** | Imminent 2-hr hyperglycemic spike (>200 mg/dL) or 24-hr hypertensive/cardiac crisis | **96.74% Recall** | **0.9418 F1-Score**, 91.75% Precision, 96.33% Accuracy | **0.035 ms** |
| **Stage 2: CMBCD 4-Stage Ensemble** | 4-class progression staging (*Stage 1: Stable*, *Stage 2: Drift*, *Stage 3: Overt*, *Stage 4: Critical*) | **0.9209 Macro F1** | **91.33% Accuracy** (S1: 0.937, S2: 0.910, S3: 0.896, S4: 0.941) | **0.042 ms** |
| **Stage 3: Safe Clinical Window (TTT) Regressor** | Continuous forecast of hours remaining (1–168h) before threshold breach | **R² = 0.9607** | **MAE = 6.15 Hours**, RMSE = 7.59 Hours | **0.028 ms** |
| **2-Hour CGM Horizon Forecaster** | Postprandial glycemic trajectory with 95% confidence cone | **RMSE = 11.2 mg/dL** | 94.10% Sensitivity, 92.60% Specificity | **1.80 ms** |

## 6. Repository Structure & Key Deliverables

This repository is curated to maintain a lean, production-ready architecture for Vercel deployment while preserving all reproducible ML training pipelines, biophysical ODE simulation models, and synthetic clinical cohorts:

```text
Twin-Pulse-Digital-Twin-Challenge-2026/
├── api/
│   └── chat.js                     # Vercel Serverless Function (Gemini AI Clinical Advisor proxy)
├── project_files/
│   ├── data/
│   │   ├── synthea_ehr_patients.csv                        # 100 Indian Patient EHR Cohort (DPDP & HIPAA compliant)
│   │   └── twin_pulse_cardiometabolic_ehr_wearable_data.csv # 1,500 Continuous In-Vivo Wearable Windows
│   ├── saved_models/
│   │   ├── feature_schema.json                             # 28-Biomarker Clinical Feature Definitions
│   │   ├── model_evaluation_metrics.json                   # Holdout 80/20 Benchmark Evaluation Records
│   │   ├── stage1_adverse_event_classifier.pkl             # Imminent Glycemic Spike / Crisis Classifier (96.7% Recall)
│   │   ├── stage2_cmbcd_stage_ensemble.pkl                 # CMBCD 4-Stage Soft-Voting Progression Ensemble (0.9209 F1)
│   │   └── stage3_time_to_threshold_rul.pkl                # Safe Clinical Window (TTT) Hazard Regressor (R² = 0.96)
│   ├── ui/
│   │   └── twin_pulse_clinical_dashboard.html              # Standalone UI reference archive
│   ├── utils/
│   │   ├── clinical_copilot.py                             # CMBCD Clinical Expert Reasoning Engine
│   │   ├── data_generator.py                               # ICMR-INDIAB Synthea Patient Generator
│   │   └── digital_twin_engine.py                          # 100 Hz RK4 Physiological Coupling ODE Engine
│   ├── app_server.py                                       # Local FastAPI REST Microservice
│   ├── requirements.txt                                    # Python environment dependencies
│   └── verify_setup.py                                     # Automated environment verification script
├── .gitignore                                              # Version control ignore definitions
├── index.html                                              # KEY FINAL DELIVERABLE: Live Twin Cockpit (Vercel)
├── LICENSE                                                 # MIT Open-Source License
├── README.md                                               # Clinical Documentation & Submission Dossier
└── vercel.json                                             # Vercel Single-Page & Clean-URL Routing Rules
```

## 7. Live Web Deployment & Local Quickstart

### 🌐 Live Production Application
Access the complete interactive digital twin workstation directly in your web browser:
* **Live Deployment URL:** [https://twin-pulse-digital-twin-challenge-2-two.vercel.app/](https://twin-pulse-digital-twin-challenge-2-two.vercel.app/)
* **Zero-Setup Hosting:** Deployed on Vercel with automated CI/CD pipeline from `main`.
* **Zero Cloud Latency:** High-performance client-side biophysical solver (100 Hz RK4 ODE integration, 60 FPS Three.js point-cloud, and real-time counterfactual trajectories running entirely in-browser).

### 💻 Local Execution
To run the workstation locally, simply open `index.html` in any web browser or serve it locally:
```bash
# Option A: Open directly in your browser
open index.html   # macOS / Linux
start index.html  # Windows

# Option B: Run via local Python HTTP server
python -m http.server 8080
# Navigate to http://localhost:8080
```

### 🔬 Optional Local LLM Studio / Ollama Integration
To connect your local AI clinical co-pilot:
* **LM Studio:** Start server on port `http://localhost:1234/v1` (e.g., Llama 3 / Meditron).
* **Ollama:** Start Ollama on port `http://localhost:11434` (`ollama run llama3`).
* In the workstation top bar, click the **Settings Wheel** ⚙️ or view the Clinical Advisor panel to toggle Local AI mode. If unavailable, the dashboard automatically falls back to its built-in rule-based CMBCD clinical expert system.

## 8. License

Released under the **MIT Open-Source License**. Copyright (c) 2026 Pratyush Mathur & Aryan Jain (SVKM's NMIMS, Mumbai).
