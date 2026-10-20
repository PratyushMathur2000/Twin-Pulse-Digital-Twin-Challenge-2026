#!/usr/bin/env python3
"""
Twin-Pulse Health: Synthetic EHR + Wearable IoT Data Generator
==============================================================
Adapts the original Twin-Pulse industrial telemetry generator (`utils/data_generator.py`)
to healthcare for the Happiest Health Digital Twin Challenge 2026.

Generates fused static Electronic Health Records (Synthea-style) and dynamic
wearable IoT sensor streams across 4 Cardiometabolic-Based Chronic Disease (CMBCD)
archetypes grounded in the ICMR-INDIAB National Study (PMC12550443) and
CMBCD Digital Twin clinical trials (PMC12632027).
"""

import os
import json
import numpy as np
import pandas as pd


ARCHETYPES = [
    "Glycemic_T2D",        # Flagship: Type 2 Diabetes & Acute Glycemic Excursion Twin (Replaces Turbines)
    "Hemodynamic_HTN",     # Hypertension & Vascular Urgency Twin (Replaces Pumps)
    "Cardiac_CVD",         # Cardiovascular & Autonomic Arrhythmia Twin (Replaces Compressors)
    "HepaticRenal_CKD",    # MASLD Fatty Liver & CKD Progression Twin (Replaces Generators)
]

# ICMR-INDIAB Study (PMC12550443) Obesity Subtype Distribution in India:
# MONO: 43.3%, MOO: 28.3%, MHNO: 26.6%, MHO: 1.8%
OBESITY_PHENOTYPES = ["MONO", "MOO", "MHNO", "MHO"]
PHENOTYPE_PROBS = [0.433, 0.283, 0.266, 0.018]

INDIAN_CITIES = [
    "Bengaluru", "Mumbai", "Chennai", "Delhi NCR", "Hyderabad",
    "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Kochi"
]


def generate_cardiometabolic_cohort(n_patients: int = 100, windows_per_patient: int = 15, seed: int = 42) -> pd.DataFrame:
    """
    Generates a longitudinal fused dataset of Static EHR + Dynamic Wearable Telemetry
    for `n_patients` across `windows_per_patient` time steps (1,500 total records).
    """
    rng = np.random.default_rng(seed)
    records = []

    for pid in range(1, n_patients + 1):
        patient_id = f"PT-IND-{pid:03d}"
        archetype = ARCHETYPES[(pid - 1) % len(ARCHETYPES)]
        phenotype = rng.choice(OBESITY_PHENOTYPES, p=PHENOTYPE_PROBS)
        sex = rng.choice(["M", "F"], p=[0.52, 0.48])
        age = int(rng.integers(26, 74))
        city = rng.choice(INDIAN_CITIES)
        family_history_dm = int(rng.random() < (0.48 if phenotype in ["MONO", "MOO"] else 0.18))

        # Static EHR Anthropometrics conditioned on ICMR-INDIAB Phenotype
        if phenotype == "MONO":
            # Metabolically Obese Non-Obese ("Thin-Fat" Asian Indian Phenotype: BMI < 25 but high visceral fat/insulin resistance)
            bmi = round(float(rng.normal(22.4, 1.4)), 1)
            bmi = float(np.clip(bmi, 18.5, 24.8))
            waist_cm = round(float(rng.normal(89.5 if sex == "M" else 82.5, 4.5)), 1)
        elif phenotype == "MOO":
            # Metabolically Obese Obese (BMI >= 25 + metabolic syndrome)
            bmi = round(float(rng.normal(29.2, 2.6)), 1)
            bmi = float(np.clip(bmi, 25.1, 38.0))
            waist_cm = round(float(rng.normal(98.0 if sex == "M" else 92.0, 5.5)), 1)
        elif phenotype == "MHO":
            # Metabolically Healthy Obese
            bmi = round(float(rng.normal(27.1, 1.5)), 1)
            bmi = float(np.clip(bmi, 25.0, 32.0))
            waist_cm = round(float(rng.normal(84.0 if sex == "M" else 78.0, 4.0)), 1)
        else:
            # MHNO: Metabolically Healthy Non-Obese
            bmi = round(float(rng.normal(20.6, 1.5)), 1)
            bmi = float(np.clip(bmi, 18.0, 24.5))
            waist_cm = round(float(rng.normal(75.0 if sex == "M" else 70.0, 4.0)), 1)

        # Static EHR Lab Panel conditioned on Archetype & Phenotype
        metabolic_load = (
            (0.35 if phenotype == "MONO" else 0.55 if phenotype == "MOO" else 0.10)
            + (0.15 if family_history_dm else 0.0)
            + (age - 25) * 0.005
        )

        hba1c = round(float(np.clip(
            rng.normal(5.4 + metabolic_load * 3.8 + (0.9 if archetype == "Glycemic_T2D" else 0.2), 0.55),
            4.8, 11.8
        )), 2)
        homa_ir = round(float(np.clip(
            rng.normal(1.6 + metabolic_load * 5.2 + (1.2 if archetype == "Glycemic_T2D" else 0.3), 0.8),
            0.8, 12.5
        )), 2)
        triglycerides = int(np.clip(
            rng.normal(105 + metabolic_load * 130, 28),
            65, 380
        ))
        hdl_c = int(np.clip(
            rng.normal((48 if sex == "M" else 54) - metabolic_load * 16, 5.5),
            26, 74
        ))
        ldl_c = int(np.clip(
            rng.normal(95 + metabolic_load * 55 + (15 if archetype == "Cardiac_CVD" else 0), 18),
            60, 220
        ))
        egfr = round(float(np.clip(
            rng.normal(102 - (age - 30) * 0.65 - metabolic_load * 28 - (14 if archetype == "HepaticRenal_CKD" else 0), 8.0),
            28.0, 120.0
        )), 1)
        fib4_index = round(float(np.clip(
            rng.normal(0.85 + metabolic_load * 1.6 + (0.65 if archetype == "HepaticRenal_CKD" else 0), 0.32),
            0.40, 4.80
        )), 2)

        # Baseline patient trajectory drift rate
        patient_drift = float(rng.uniform(0.01, 0.06) * (1.25 if phenotype in ["MONO", "MOO"] else 0.65))

        for step in range(windows_per_patient):
            # Dynamic Wearable & Lifestyle Perturbations over time
            progression = np.clip(metabolic_load + step * patient_drift + rng.normal(0, 0.06), 0.05, 1.35)

            meal_carbs_g = int(np.clip(rng.normal(58 + progression * 35, 18), 15, 160))
            med_adherence = round(float(np.clip(rng.normal(0.92 - progression * 0.28, 0.08), 0.20, 1.00)), 2)
            sleep_hours = round(float(np.clip(rng.normal(7.4 - progression * 1.6, 0.6), 3.8, 9.2)), 1)
            sleep_efficiency_pct = round(float(np.clip(rng.normal(89.0 - progression * 16.0, 4.0), 52.0, 98.0)), 1)
            steps_24h = int(np.clip(rng.normal(8200 - progression * 4200, 1400), 800, 16000))

            # Dynamic Wearable Biometrics (CGM, PPG Blood Pressure, HRV, Heart Rate, SpO2)
            cgm_glucose = round(float(np.clip(
                88.0
                + (hba1c - 5.2) * 24.5
                + meal_carbs_g * 0.68
                - med_adherence * 38.0
                - (steps_24h / 1000.0) * 3.1
                + rng.normal(0, 8.5),
                62.0, 340.0
            )), 1)

            cgm_roc = round(float(np.clip(
                (meal_carbs_g - 50) * 0.032 - (med_adherence - 0.5) * 1.4 + rng.normal(0, 0.35),
                -2.8, 4.2
            )), 2)

            wearable_sbp = int(np.clip(
                110
                + progression * 42
                + (14 if archetype == "Hemodynamic_HTN" else 0)
                + (7.0 - sleep_hours) * 3.8
                - (med_adherence - 0.5) * 18.0
                + rng.normal(0, 5.0),
                96, 205
            ))
            wearable_dbp = int(np.clip(
                70 + (wearable_sbp - 110) * 0.48 + rng.normal(0, 3.5),
                58, 128
            ))

            hrv_rmssd_ms = round(float(np.clip(
                64.0
                - progression * 34.0
                - (8.0 if archetype == "Cardiac_CVD" else 0.0)
                - max(0.0, cgm_glucose - 140.0) * 0.08
                + (sleep_efficiency_pct - 75.0) * 0.35
                + rng.normal(0, 3.8),
                11.0, 92.0
            )), 1)

            resting_hr_bpm = int(np.clip(
                62 + (80.0 - hrv_rmssd_ms) * 0.42 + progression * 12.0 + rng.normal(0, 3.0),
                50, 118
            ))
            spo2_pct = round(float(np.clip(rng.normal(97.8 - progression * 2.1, 0.6), 91.0, 100.0)), 1)

            # Organ-Specific Stress Indices (0 to 100%)
            glycemic_stress = float(np.clip(
                ((cgm_glucose - 95.0) / 165.0) * 55.0 + max(0.0, cgm_roc) * 11.0 + ((hba1c - 5.2) / 5.0) * 34.0,
                2.0, 99.0
            ))
            vascular_stress = float(np.clip(
                ((wearable_sbp - 112.0) / 75.0) * 65.0 + ((wearable_dbp - 72.0) / 45.0) * 35.0,
                2.0, 99.0
            ))
            cardiac_stress = float(np.clip(
                ((70.0 - hrv_rmssd_ms) / 55.0) * 55.0 + ((resting_hr_bpm - 60.0) / 48.0) * 25.0 + ((ldl_c - 80.0) / 120.0) * 20.0,
                2.0, 99.0
            ))
            hepatic_renal_stress = float(np.clip(
                ((110.0 - egfr) / 75.0) * 50.0 + ((fib4_index - 0.7) / 3.2) * 35.0 + ((triglycerides - 90.0) / 240.0) * 15.0,
                2.0, 99.0
            ))

            # Composite Cardiometabolic Degradation Score (analogous to Twin-Pulse Asset Degradation %)
            weights = {
                "Glycemic_T2D": (0.48, 0.20, 0.18, 0.14),
                "Hemodynamic_HTN": (0.18, 0.48, 0.20, 0.14),
                "Cardiac_CVD": (0.18, 0.22, 0.46, 0.14),
                "HepaticRenal_CKD": (0.20, 0.16, 0.16, 0.48),
            }[archetype]

            composite_degradation_pct = round(float(np.clip(
                weights[0] * glycemic_stress
                + weights[1] * vascular_stress
                + weights[2] * cardiac_stress
                + weights[3] * hepatic_renal_stress
                + rng.normal(0, 2.2),
                3.0, 99.0
            )), 1)

            # Stage 2 Target: 4-Stage CMBCD Progression State (Mirrors Twin-Pulse 4-Stage Health State)
            # 0: Stage 1 - Controlled / Baseline Risk (<35%)
            # 1: Stage 2 - Predisease Subclinical Drift (35-62%)
            # 2: Stage 3 - Overt Disease Dysregulation (62-82%)
            # 3: Stage 4 - Acute Complication Imminent (>82%)
            if composite_degradation_pct < 35.0:
                cmbcd_stage = 0
                cmbcd_stage_label = "Stage 1: Controlled / Baseline"
            elif composite_degradation_pct < 62.0:
                cmbcd_stage = 1
                cmbcd_stage_label = "Stage 2: Subclinical Drift"
            elif composite_degradation_pct < 82.0:
                cmbcd_stage = 2
                cmbcd_stage_label = "Stage 3: Overt Dysregulation"
            else:
                cmbcd_stage = 3
                cmbcd_stage_label = "Stage 4: Acute Crisis Imminent"

            # Stage 1 Target: Binary Adverse Event Flag (Next 2h Glycemic Excursion or 24h Cardiometabolic Crisis)
            adverse_event_logit = (
                (composite_degradation_pct - 66.0) * 0.18
                + (1.2 if cgm_glucose >= 210.0 or cgm_roc >= 1.8 else 0.0)
                + (1.2 if wearable_sbp >= 165 else 0.0)
                + (1.1 if hrv_rmssd_ms <= 22.0 else 0.0)
            )
            adverse_event_prob_true = 1.0 / (1.0 + np.exp(-adverse_event_logit))
            adverse_event_flag = int(adverse_event_prob_true >= 0.50)

            # Stage 3 Target: Time-to-Threshold (RUL Equivalent in Hours before critical threshold breach, 1 to 168h / 7 days)
            time_to_threshold_hours = round(float(np.clip(
                168.0 * ((100.0 - composite_degradation_pct) / 97.0) ** 1.35
                - max(0.0, cgm_roc) * 6.5
                + rng.normal(0, 2.4),
                1.0, 168.0
            )), 1)

            records.append({
                "Patient_ID": patient_id,
                "Window_Step": step + 1,
                "CMBCD_Archetype": archetype,
                "Obesity_Phenotype": phenotype,
                "Age": age,
                "Sex": sex,
                "City": city,
                "Family_History_DM": family_history_dm,
                "BMI_kg_m2": bmi,
                "Waist_Circumference_cm": waist_cm,
                "EHR_HbA1c_pct": hba1c,
                "EHR_HOMA_IR": homa_ir,
                "EHR_Triglycerides_mg_dL": triglycerides,
                "EHR_HDL_mg_dL": hdl_c,
                "EHR_LDL_mg_dL": ldl_c,
                "EHR_eGFR_mL_min": egfr,
                "EHR_FIB4_Index": fib4_index,
                "Meal_Carbs_g": meal_carbs_g,
                "Med_Adherence_Score": med_adherence,
                "Sleep_Hours": sleep_hours,
                "Sleep_Efficiency_pct": sleep_efficiency_pct,
                "Steps_24h": steps_24h,
                "CGM_Glucose_mg_dL": cgm_glucose,
                "CGM_ROC_mg_dL_min": cgm_roc,
                "Wearable_SBP_mmHg": wearable_sbp,
                "Wearable_DBP_mmHg": wearable_dbp,
                "HRV_RMSSD_ms": hrv_rmssd_ms,
                "Resting_HR_bpm": resting_hr_bpm,
                "SpO2_pct": spo2_pct,
                "Glycemic_Stress_Index": round(glycemic_stress, 1),
                "Vascular_Stress_Index": round(vascular_stress, 1),
                "Cardiac_Stress_Index": round(cardiac_stress, 1),
                "HepaticRenal_Stress_Index": round(hepatic_renal_stress, 1),
                "Composite_Degradation_pct": composite_degradation_pct,
                "Adverse_Event_Flag": adverse_event_flag,
                "CMBCD_Stage_Code": cmbcd_stage,
                "CMBCD_Stage_Label": cmbcd_stage_label,
                "Time_To_Threshold_Hours": time_to_threshold_hours,
            })

    return pd.DataFrame(records)


if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    df = generate_cardiometabolic_cohort(n_patients=100, windows_per_patient=15, seed=42)
    csv_path = os.path.join(out_dir, "twin_pulse_cardiometabolic_ehr_wearable_data.csv")
    df.to_csv(csv_path, index=False)
    print(f"Generated {len(df)} records across {df['Patient_ID'].nunique()} virtual patients -> {csv_path}")
    print("Obesity Phenotype Breakdown:")
    print(df.groupby("Obesity_Phenotype")["Patient_ID"].nunique())
    print("\nCMBCD Stage Distribution:")
    print(df["CMBCD_Stage_Label"].value_counts())
