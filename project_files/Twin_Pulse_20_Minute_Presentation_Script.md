# Twin-Pulse: 20-Minute Video Presentation Script
**Happiest Health Digital Twin Challenge 2026 | Reimagining Healthcare in India Summit, Bengaluru**  
**Team:** Twin-Pulse (SVKM's NMIMS, Mumbai)  
**Presenters:** Pratyush Mathur (Team Leader) & Aryan Jain (Team Member)  
**Live Platform Reference:** [https://twin-pulse-digital-twin-challenge-2-two.vercel.app/](https://twin-pulse-digital-twin-challenge-2-two.vercel.app/)

---

## ⏱️ Video Structure & Timing Outline

| Act | Timestamp | Title | Primary Speaker | Key Visuals & Demos |
| :--- | :--- | :--- | :--- | :--- |
| **I** | `00:00 – 03:00` | **The Indian Healthcare Crisis & The "Thin-Fat" Paradox** | Pratyush Mathur | Title slide, ICMR-INDIAB data graphics, phenotype comparison |
| **II** | `03:00 – 06:15` | **The Twin-Pulse Paradigm: Two-Stream Data Fusion** | Aryan Jain | Solution architecture diagram, EHR + Wearable IoT stream fusion |
| **III** | `06:15 – 13:00` | **Live Workstation Demonstration: Clinician's Cockpit** | Pratyush Mathur | 3D Twin, 2-Hr CGM Cone, What-If perturbation sliders, interactive outcome modals |
| **IV** | `13:00 – 15:30` | **Population Health & Triage at Scale: 100-Patient Cohort** | Aryan Jain | Ward Triage board, sorting, patient drawer, FHIR R4 & SOAP export |
| **V** | `15:30 – 18:00` | **Biophysical ODE Physics, 3-Stage ML, & Technical Rigor** | Aryan Jain | Model Validation tab, 80/20 holdout metrics, closed-loop flowchart |
| **VI** | `18:00 – 20:00` | **Clinical Evidence, DPDP Compliance, & Vision for India** | Pratyush & Aryan | Remission clinical trial data, DPDP Act 2023 compliance, closing appeal |

---

## Act I: The Indian Healthcare Crisis & The "Thin-Fat" Paradox
**Time:** `00:00 – 03:00` (3 Minutes)  
**Speaker:** Pratyush Mathur (Team Leader)  
**Focus:** Hook the judges, establish clinical gravity, cite ICMR-INDIAB, explain why conventional care fails.

```
[VISUAL CUE: 00:00 - 00:25]
Camera on Pratyush (full screen or picture-in-picture with title slide). 
Lower third: "Pratyush Mathur — Team Leader | SVKM's NMIMS, Mumbai".
Slide background: Clean dark/warm Sahara aesthetic with Twin-Pulse emblem and 
"Twin-Pulse: Cardiometabolic Digital Twin Workstation — Happiest Health 2026".
```

**PRATYUSH:**  
"Respected jury members, clinicians, and health-tech leaders at the Reimagining Healthcare in India Summit 2026. My name is Pratyush Mathur, and together with my co-founder Aryan Jain from SVKM's NMIMS, Mumbai, we are honored to present **Twin-Pulse**—an in-silico, real-time Cardiometabolic Digital Twin workstation built specifically for the unique physiological and clinical landscape of India.

India is currently recognized as the diabetes capital of the world, home to over 101 million individuals living with Type 2 Diabetes, and another 136 million with prediabetes. But behind these staggering macro-statistics lies a fatal clinical blindspot in standard care."

```
[VISUAL CUE: 00:25 - 01:20]
Cut to graphic: ICMR-INDIAB Study Data (PMC12550443).
Side-by-side visual comparing Western Obese patient (high BMI) vs. 
Asian Indian "Thin-Fat" patient (normal BMI < 25, high visceral fat, high HOMA-IR).
```

**PRATYUSH (cont.):**  
"In conventional outpatient practice, screening and risk stratification rely almost exclusively on Body Mass Index—BMI. In Western populations, high BMI correlates directly with metabolic syndrome. But in India, that assumption is clinically dangerous.

The nationally representative **ICMR-INDIAB study**, surveying over 113,000 Indian adults, proved that **43.3% of the Indian population exhibits the Metabolically Obese Non-Obese—or `MONO`—phenotype**. These are individuals with a completely normal BMI below 25 kg/m², but who harbor severe visceral adiposity, high hepatic insulin resistance, elevated HOMA-IR, and atherogenic dyslipidemia. 

Compared to metabolically healthy peers, a non-obese Indian with the `MONO` phenotype has a **6.9-fold higher risk of Type 2 Diabetes**, a **1.77-fold higher risk of Coronary Artery Disease**, and a **1.81-fold higher risk of Chronic Kidney Disease**. In fact, over 57% of these patients present with multi-organ metabolic failure drivers simultaneously.

Yet today, standard clinical practice treats these as four completely disconnected specialties: the diabetologist prescribes metformin; the cardiologist treats hypertension with an ARB; the nephrologist monitors microalbuminuria; and the patient only receives an intervention *after* an acute glycemic spike, a stroke, or renal decompensation has already occurred."

```
[VISUAL CUE: 01:20 - 03:00]
Transition to high-level system render or screen recording of the 
Twin-Pulse 3D human point cloud with pulsing organ nodes.
```

**PRATYUSH (cont.):**  
"What clinicians desperately need is not another static EHR dashboard or another isolated smartwatch app. What doctors need is a **predictive, continuous Digital Twin**—a computational biophysical replica of the patient that couples their historical EHR with dynamic wearable telemetry to forecast adverse events hours before they manifest, test non-pharmacological and clinical interventions in-silico, and give the clinician a quantifiable **Safe Clinical Window**.

Recent clinical trials published in leading Indian medical literature across nearly 2,200 patients have demonstrated that sensor-coupled cardiometabolic digital twins lower mean HbA1c by up to **2.9%**, expand Time-in-Range from 69% to 87%, and achieve **over 72% diabetes remission** at one year.

Today, we are thrilled to show you that Twin-Pulse does not just conceptualize this future—we have engineered, validated, and deployed it. I will now hand over to Aryan to walk you through our two-stream data fusion architecture."

---

## Act II: The Twin-Pulse Paradigm & Two-Stream Data Fusion
**Time:** `03:00 – 06:15` (3 Minutes 15 Seconds)  
**Speaker:** Aryan Jain (Team Member)  
**Focus:** Address the rubric criterion directly: demonstrate the fusion of Stream 1 (Static EHR) and Stream 2 (Dynamic IoT Wearables).

```
[VISUAL CUE: 03:00 - 03:30]
Camera cuts to Aryan Jain (picture-in-picture).
Lower third: "Aryan Jain — Team Member | SVKM's NMIMS, Mumbai".
Main screen shows: System Architecture Diagram (Closed-Loop Healthcare Digital Twin).
Highlighting Stream 1 (EHR) on the left and Stream 2 (IoT) on the right converging into the Fusion Layer.
```

**ARYAN:**  
"Thank you, Pratyush. To satisfy the core foundation of a true clinical digital twin, Twin-Pulse is architected around the **Cardiometabolic-Based Chronic Disease (CMBCD)** framework, solving the challenge of fusing two fundamentally different temporal data streams:

First, **Stream 1: Static and Historical EHR Data**. This represents the patient's baseline pathological substrate:
* **Demographics:** Age, Sex, and Indian geographic location across 10 metro hubs.
* **Past Clinical Diagnoses:** Historical staging across 4 organ archetypes—Glycemic T2D, Hemodynamic Hypertension, Autonomic CVD, and Hepatorenal CKD.
* **Comprehensive Lab Chemistry:** Fasting glucose, HbA1c, HOMA-IR, complete lipid profiling (triglycerides, HDL, LDL, TG/HDL ratio), renal eGFR calculated via the 2021 CKD-EPI formula, and hepatic FIB-4 fibrosis scores.
* **Genetic & Familial Markers:** First-degree family history of diabetes, paired with explicit ICMR-INDIAB phenotype classification into `MONO`, `MOO`, or `MHNO`."

```
[VISUAL CUE: 03:30 - 04:45]
Highlight Stream 2 on screen: Pulsing green live wearable sensors.
Show diagrams/icons of CGM, PPG Cuffless BP, HRV, Sleep, Steps.
```

**ARYAN (cont.):**  
"Second, **Stream 2: Dynamic, Real-Time Wearable and IoT Telemetry**. This captures the continuous, hour-by-hour lifestyle perturbations of daily life:
* **Continuous Glucose Monitoring (CGM):** Real-time interstitial glucose sampled at 100 Hz alongside its instantaneous rate-of-change velocity in milligrams per deciliter per minute.
* **Cuffless Photoplethysmography (PPG) Hemodynamics:** Continuous beat-to-beat Systolic and Diastolic Blood Pressure.
* **Autonomic Heart Rate Variability:** Time-domain root mean square of successive difference—$r\text{MSSD}$—paired with resting heart rate and optical pulse oximetry ($\text{SpO}_2$).
* **Continuous Lifestyle Tracking:** Nocturnal sleep duration, sleep efficiency percentage representing sleep architecture continuity, 24-hour step volume from tri-axial accelerometers, and nutritional carbohydrate logging."

```
[VISUAL CUE: 04:45 - 06:15]
Show the Fusion Math & Feature Schema graphic (`feature_schema.json` 28-dimensional vector).
Show the mathematical interaction formula:
Dynamic Meal Carbs + Dynamic Steps * 1/(Static HOMA-IR) = Simulated Trajectory.
```

**ARYAN (cont.):**  
"Now, how does Twin-Pulse fuse these two streams? 

In our pipeline, fusion is not just showing two charts next to each other. Fusion occurs both **biophysically** and **statistically**:

In our mathematical solver, dynamic perturbations—such as a 95-gram carbohydrate meal—are dynamically modulated by the patient’s static baseline insulin sensitivity ($S_I = 1 / \text{HOMA-IR}$) and baseline beta-cell reserve. If an Asian Indian patient exhibits the `MONO` phenotype with a high baseline HOMA-IR of 3.8, that 95-gram meal triggers an aggressive, prolonged postprandial spike past 220 mg/dL. The exact same meal in an insulin-sensitive patient produces a blunted, safe curve.

Simultaneously, in our machine learning pipeline, our `prepare_features` engine ingests a **28-dimensional harmonized feature vector** combining 13 static EHR markers and 15 dynamic sensor signals. Every single inference—whether predicting an adverse event, classifying clinical progression, or calculating the Safe Clinical Window—is a joint mathematical function of both historical disease burden and live sensor dynamics.

Let us now move directly into our live production environment so Pratyush can walk you through the Clinician's Cockpit."

---

## Act III: Live Workstation Demonstration — The Clinician's Cockpit
**Time:** `06:15 – 13:00` (6 Minutes 45 Seconds)  
**Speaker:** Pratyush Mathur  
**Focus:** Live interactive demo of `https://twin-pulse-digital-twin-challenge-2-two.vercel.app/`. Show the 3D twin, 2-Hr forecast, What-If perturbation sliders, comparative cards, and detail modal.

```
[VISUAL CUE: 06:15 - 06:45]
Switch screen share to LIVE BROWSER:
URL: https://twin-pulse-digital-twin-challenge-2-two.vercel.app/
Point out the top header: Brand Emblem SVG Logo, Navigation Tabs, 
Patient Selector, and Settings Wheel.
Show Patient "Rajesh Sharma (PT-IND-001)".
```

**PRATYUSH:**  
"Thank you, Aryan. You are looking at the live, production deployment of Twin-Pulse, hosted on Vercel and accessible from any desktop, tablet, or hospital workstation with zero client-side installation. Notice our brand emblem in the top header—representing continuous cardiometabolic pulse wave coupling.

Let us examine our index patient: **Rajesh Sharma**, a 48-year-old male from Mumbai. 

Immediately in the Patient Dossier, you observe the concrete separation and fusion of the two required streams:
* In the left card, **`STREAM 1: STATIC EHR (Synthea)`**: Rajesh has an HbA1c of 8.2%, a HOMA-IR of 3.8 indicating severe insulin resistance, an eGFR of 74 mL/min, and a BMI of 23.8 kg/m². Despite having a normal BMI, his ICMR-INDIAB phenotype tag is prominently flagged as **`MONO`**—Metabolically Obese Non-Obese.
* Directly adjacent, with a pulsing green telemetry beacon, is **`STREAM 2: LIVE WEARABLES (IoT)`**: His in-vivo CGM reads 164 mg/dL, his cuffless blood pressure is 138/88 mmHg, autonomic HRV is 34 ms, nocturnal sleep was restricted at 5.5 hours, and his 24-hour steps sit at only 3,800."

```
[VISUAL CUE: 06:45 - 07:45]
Cursor moves down to the Compact 64px Metric Ribbon and 3D Anatomical Twin.
Rotate the 3D Anatomical Twin with the mouse (show full 360-degree rotation, 
point-cloud, wireframe, arterial flow particles, and vagus nerve filaments).
Point to the live 250 Hz Lead II ECG canvas beating in real time.
```

**PRATYUSH (cont.):**  
"Above the fold, the clinician has a zero-scroll operational overview:
1. Our **Compact 64px Metric Ribbon** displays his composite cardiometabolic strain: 48 out of 100.
2. Directly in the center is our **3D Hemodynamic and Anatomical Twin**. Built in Three.js and rendered at a crisp 60 frames per second, it renders over 4,500 anatomical point-cloud particles, skeletal wireframes, and pulsing arterial particles. Notice the color-coded anatomical rings representing his 4 organ systems: Pancreatic beta-cells, Conduit aorta, Autonomic cardiac plexus, and Hepatorenal filtration.
3. To the right, our canvas-based **250 Hz Lead II ECG Strip** runs live, calculating real-time heart rate and QT interval intervals continuously."

```
[VISUAL CUE: 07:45 - 09:30]
Scroll slightly to bring the "2-Hour CGM Postprandial Forecast" and 
"What-If Physiology Perturbation Simulator" into full focus.
```

**PRATYUSH (cont.):**  
"Now let us look at our flagship chronic condition module: **Type 2 Diabetes & Postprandial Glycemic Excursion**.

Beneath the 3D twin, you see the **2-Hour CGM Horizon Forecaster**. Rajesh has just consumed a meal. The historical solid orange line plots his last 60 minutes of sensor data. Our forecaster projects the next 120 minutes with a shaded 95% confidence cone. Notice the prediction: without intervention, his glucose will peak at **224 mg/dL**—breaching the 200 mg/dL acute adverse threshold within 45 minutes.

Now, watch what happens when a clinician or diabetes educator uses our **What-If Counterfactual Physiology Simulator**.

Let us simulate a simple, non-pharmacological lifestyle intervention.
Currently, Rajesh's meal had **95 grams of carbohydrates**. Watch the screen as I drag the Carbohydrate slider down to **45 grams**."

```
[ACTION CUE: 08:45 - 09:30]
PRATYUSH DRAGS THE "Meal Carbs" SLIDER FROM 95g DOWN TO 45g.
Point cursor to the live green delta badge appearing next to the peak: 
"224 -> 148 mg/dL (-76 mg/dL)".
Show the dotted green simulated curve diverging from the dashed gray baseline.
```

**PRATYUSH (cont.):**  
"Instantly—with zero cloud latency—our in-browser biophysical solver recalculates the Bergman Minimal Model differential equations. 

Look at the live delta badge that appeared: his forecasted peak drops from **224 mg/dL down to 148 mg/dL—a 76 mg/dL reduction**. The simulated green trajectory stays comfortably within his target Time-in-Range. 

Now let us add **15 minutes of post-meal walking** by dragging the Daily Steps slider from 3,800 to 7,500 steps, and restoring his nocturnal sleep to 7.5 hours. Look at his adverse event probability: it collapses from 42% down to 14%, and his **Safe Clinical Window expands from 4.2 hours to over 16 hours**."

```
[VISUAL CUE: 09:30 - 11:30]
Scroll to "Comparative Intervention Outcomes & 6-Hour Response" section.
Point to the 4 Organ Subsystem Pills (Pancreatic, Hepatic, Microvascular, Autonomic).
Click on the "Pancreatic Beta-Cell" pill -> Detail Modal pops up.
```

**PRATYUSH (cont.):**  
"Directly below, we provide the **Comparative Intervention Outcomes & 6-Hour Response** panel, giving doctors rigorous mathematical transparency. 

Notice the four organ subsystem pills:
* Pancreatic $\beta$-Cell
* Hepatic Insulin Resistance
* Microvascular Tone
* Autonomic Vagal Recovery

Watch what happens when I click on **Pancreatic $\beta$-Cell**. 

A comprehensive biophysical modal opens. The clinician sees:
1. The **Mathematical Formulation**: The exact coupled differential equations—Bergman Minimal Model parameters: glucose effectiveness ($p_1$), insulin action decay ($p_2$), and beta-cell sensitivity ($p_3$).
2. The **Clinical & Biological Role**: How glucose excursions damage microvasculature.
3. The **ICMR-INDIAB & ADA Guideline Protocol**: Recommending complex carbohydrates with a glycemic index below 55 and GLP-1 receptor agonist initiation for high visceral-adiposity phenotypes.
4. And one-click simulation buttons like **'AI Auto-Optimize'** and **'Simulate Postprandial Spike'**."

```
[ACTION CUE: 11:30 - 12:15]
Close the modal (press Escape or click outside).
Click on "Stage 1 Event Risk" comparison card.
Show the detail modal displaying LightGBM 96.7% recall calibration, hazard delta (-24%), 
and ICMR-INDIAB clinical recommendations. Close modal.
```

**PRATYUSH (cont.):**  
"Every single comparison card in this grid is fully interactive. Clicking **Stage 1 Event Risk** reveals the LightGBM classifier calibration and hazard reduction from 42% to 18%. Clicking **Stage 3 Safe Window** reveals the Weibull hazard formulation forecasting time-to-threshold breach.

Finally, in the top right, clicking the **Settings Wheel ⚙️** gives clinicians full control:
* Toggling between Sahara Warm Editorial and Dark Clinical Mode.
* Exporting full **HL7 FHIR R4 JSON Bundles** containing observation resources for static labs and continuous wearable telemetry.
* Generating instant **Clinical SOAP Consultation Notes** ready for copy-pasting into any hospital EHR system.

I will now hand back to Aryan to show how Twin-Pulse scales from an individual digital twin to managing an entire hospital ward or outpatient cohort."

---

## Act IV: Population Health & Triage at Scale — 100-Patient Cohort
**Time:** `13:00 – 15:30` (2 Minutes 30 Seconds)  
**Speaker:** Aryan Jain  
**Focus:** Demonstrate Tab 2 (100-Patient Ward Triage), sorting, filtering, patient inspection drawer, and CSV export.

```
[VISUAL CUE: 13:00 - 13:30]
Pratyush/Aryan clicks on Tab 2: "100-Patient Ward Triage" in the top bar.
The screen smoothly switches to the 100-patient table.
Point out search bar, stage filter pills, summary metrics, and export button.
```

**ARYAN:**  
"A digital twin is only as valuable as its ability to scale across healthcare delivery systems. Here in **Tab 2: 100-Patient Ward Triage**, Twin-Pulse aggregates 100 fully synthetic, DPDP Act 2023-compliant Indian digital twins—from `PT-IND-001` to `PT-IND-100`.

Notice that every single patient has a unique Indian identity, demographic profile, and realistic clinical parameters reflecting authentic ICMR-INDIAB epidemiology across Mumbai, Bengaluru, Delhi, Chennai, and Hyderabad.

Doctors and triage nurses can immediately filter the entire ward:
* By **CMBCD Progression Stage**: Controlled (Stage 1), Subclinical Drift (Stage 2), Overt Dysregulation (Stage 3), or Acute Crisis Imminent (Stage 4).
* By **Phenotype**: Filtering specifically for the 43 non-obese `MONO` patients who might look healthy in a routine physical exam but have critical visceral strain.
* Or sorting by **Safe Clinical Window (Time-to-Threshold)**, ensuring the most unstable patients appear at the very top of the ICU or ward priority list."

```
[ACTION CUE: 13:30 - 14:45]
Aryan clicks on a patient row (e.g., PT-IND-004: "Vikram Malhotra" or PT-IND-012).
Show the slide-out Patient Inspection Drawer on the right.
Demonstrate one-click "Load into 3D Cockpit" button.
```

**ARYAN (cont.):**  
"Clicking on any patient row slides out our **Instant Patient Inspection Drawer**. Without losing their place in the ward list, the clinician sees:
* Complete Stream 1 EHR labs (HbA1c, HOMA-IR, eGFR, Lipids, Phenotype).
* Complete Stream 2 live wearable telemetry (CGM, Blood Pressure, HRV, Sleep, Steps).
* The AI-calculated Adverse Event Hazard and Time-to-Threshold.
* And with a single click on **'Load Patient into Twin Cockpit'**, the entire 3D anatomical twin, What-If simulation engine, and CGM horizon instantly recalibrate to that patient's physiology.

Clinicians can also click **'Export Cohort CSV'** to generate longitudinal epidemiological reports for public health research or hospital administration."

```
[VISUAL CUE: 14:45 - 15:30]
Show the CSV download or click Export Cohort CSV.
Transition to Tab 3: Model Validation & Architecture.
```

**ARYAN (cont.):**  
"Now let us examine the mathematical and machine learning rigor backing every prediction on this screen."

---

## Act V: Biophysical Physics, 3-Stage ML, & Technical Rigor
**Time:** `15:30 – 18:00` (2 Minutes 30 Seconds)  
**Speaker:** Aryan Jain  
**Focus:** Demonstrate Tab 3 (Model Validation & Architecture), the interactive Solution Architecture flowchart, 80/20 holdout split benchmarks, and edge AI runtime.

```
[VISUAL CUE: 15:30 - 16:30]
Camera on Tab 3: "Model Validation & Architecture".
Scroll to the top: "Closed-Loop Healthcare Digital Twin Solution Architecture".
Point to the animated SVG flowchart with pulsing nodes and animated flow lines.
Click on Node 1 (Stream 1 EHR) and Node 4 (ODE Coupling Engine) to show interactive inspection.
```

**ARYAN:**  
"Here in **Tab 3: Model Validation & Architecture**, we present our complete system architecture and empirical benchmark validation.

At the very top is our **Closed-Loop Solution Flowchart**. You can trace the continuous loop:
1. **Stream 1 Static EHR** and **Stream 2 Dynamic Wearables** ingest into our harmonization layer.
2. The signals pass into our **Multi-Organ Physiological Coupling Engine**, running continuous Bergman Minimal Model and Windkessel differential equations.
3. The coupled states feed into our **3-Stage Prognostic Machine Learning Engine**.
4. The outputs drive the **Clinician Workstation, What-If Simulator, and AI Copilot**.
5. Clinical interventions close the loop by altering patient telemetry back in the real world."

```
[VISUAL CUE: 16:30 - 17:30]
Scroll to the Holdout Validation Benchmark Cards.
Highlight the 4 benchmark metric cards with primary and secondary metrics.
```

**ARYAN (cont.):**  
"To guarantee that Twin-Pulse generalizes to real-world patients without overfitting, our machine learning pipeline was trained and evaluated on a strict **patient-grouped 80/20 holdout split**:
* 80 training patients comprising 1,200 longitudinal windows.
* 20 completely unseen test patients comprising 300 longitudinal windows.

Here are our holdout validation metrics:
1. **Stage 1 (Adverse Event Classifier):** Achieves **96.74% Recall** and a **0.9418 F1-Score**. In clinical medicine, recall is the most critical metric—a false negative could mean an unpredicted diabetic ketoacidosis or stroke. With 96.7% recall, virtually zero crises are missed, with an inference latency of just **0.035 milliseconds**.
2. **Stage 2 (CMBCD Progression Ensemble):** A soft-voting ensemble across Random Forest and Gradient Boosted trees achieving a **0.9209 Macro F1-Score** and 91.33% multi-class accuracy across all four stages.
3. **Stage 3 (Safe Clinical Window / Time-to-Threshold Regressor):** Achieves an **$R^2$ of 0.9607** with a Mean Absolute Error of **6.15 hours** across a 168-hour forecast horizon.
4. **2-Hour CGM Forecaster:** Generates postprandial glycemic trajectories with an **RMSE of just 11.2 mg/dL**."

```
[VISUAL CUE: 17:30 - 18:00]
Scroll down to the Technical Specifications & On-Device AI cards.
Show LM Studio / Ollama toggle and Vercel serverless integration.
```

**ARYAN (cont.):**  
"Critically, all biophysical ODE integrations and counterfactual slider calculations run **100% client-side in standard JavaScript at 100 Hz**. 

For hospital environments with strict data air-gapping, Twin-Pulse connects directly to on-device LLMs via **LM Studio (`:1234`)** or **Ollama (`:11434`)**, with our deployed Vercel serverless function (`/api/chat`) providing seamless cloud Gemini intelligence when connected. 

Let us now conclude with the clinical impact and regulatory vision of Twin-Pulse."

---

## Act VI: Clinical Evidence, DPDP Compliance, & Vision for India
**Time:** `18:00 – 20:00` (2 Minutes)  
**Speakers:** Pratyush Mathur & Aryan Jain (Dual Presentation)  
**Focus:** Clinical trial grounding, DPDP Act 2023 compliance, business scalability, closing call to action.

```
[VISUAL CUE: 18:00 - 19:00]
Both Pratyush and Aryan on camera (split screen or side-by-side).
Background slide: "Clinical Evidence & National Healthcare Impact".
Key bullet points: 2.9% HbA1c reduction, 72.7% Remission, DPDP 2023 Compliance.
```

**PRATYUSH:**  
"As future healthcare leaders from SVKM's NMIMS, we designed Twin-Pulse not as an academic exercise, but as a clinically viable, commercially deployable solution.

Our underlying physiological model is directly supported by published clinical evidence from Indian digital twin trials:
* Lowering patient HbA1c by an average of **1.8% to 2.9%** without increasing hypoglycemic events.
* Elevating CGM Time-in-Range from 69.7% to **86.9%**.
* And achieving **72.7% Type 2 Diabetes remission** and **60% hypertension remission** within 12 months."

**ARYAN:**  
"Furthermore, Twin-Pulse is engineered from the ground up for the **Digital Personal Data Protection (DPDP) Act 2023** and Indian healthcare privacy:
* All 100 patients in our reference triage are fully synthetic, mathematically generated from Synthea EHR templates and ICMR-INDIAB statistics, containing zero protected health information.
* Because our 3D engine, biophysical ODE solver, and inference scoring run client-side in the browser, sensitive patient telemetry never has to leave the hospital perimeter.
* When exporting to national digital health registries like the **Ayushman Bharat Digital Mission (ABDM)**, our HL7 FHIR R4 export engine ensures seamless, interoperable compliance."

```
[VISUAL CUE: 19:00 - 20:00]
Final closing slide:
"Twin-Pulse: Cardiometabolic Digital Twin Workstation"
Live Demo: twin-pulse-digital-twin-challenge-2-two.vercel.app
GitHub: github.com/PratyushMathur2000/Twin-Pulse-Digital-Twin-Challenge-2026
Team: Pratyush Mathur (mr.mathurpratyush@gmail.com) | Aryan Jain (ajain070912@gmail.com)
SVKM's NMIMS, Mumbai
```

**PRATYUSH:**  
"By combining the precision of static EHR lab chemistry with the immediacy of dynamic IoT wearables, Twin-Pulse turns reactive healthcare into predictive, proactive precision medicine. It equips Indian physicians with an intuitive co-pilot to save lives, prevent end-organ complications, and reverse chronic disease before it becomes irreversible.

We invite the esteemed jury to test our live deployment at **twin-pulse-digital-twin-challenge-2-two.vercel.app**, inspect our open-source codebase on GitHub, and join us in reimagining healthcare for over a billion lives.

Thank you very much."

**ARYAN:**  
"Thank you."

---

## 🎬 Director's Recording & Rehearsal Checklist

To ensure your recording looks and sounds like a winning presentation, follow these practical steps:

### 1. Screen Recording Setup
* **Resolution:** Set screen to **1920x1080 (1080p)** at 60 FPS in OBS Studio or Loom.
* **Browser Mode:** Open Chrome in full screen (`F11`), with bookmark bar hidden.
* **Zoom Level:** Keep Chrome zoom at **100%** (or 90% if you want maximum above-the-fold visibility).
* **Audio:** Use a clean dedicated microphone with background noise cancellation enabled.

### 2. Live Demo Rehearsal Actions
* **At 06:45:** Grab the 3D twin with the mouse, rotate 180 degrees slowly to show the point-cloud particles and vagus nerve filaments.
* **At 08:45:** Move the **Meal Carbs slider** from 95g to 45g with a deliberate, smooth mouse drag; pause for 2 seconds while pointing to the green delta badge (`-76 mg/dL`).
* **At 11:30:** Click the **Pancreatic $\beta$-Cell** pill to trigger the modal; pause for 3 seconds to highlight the ODE mathematical formula; close with `Escape`.
* **At 11:50:** Click the **Stage 1 Event Risk** card to show the LightGBM 96.7% recall explanation; close.
* **At 13:30:** In the Ward Triage tab, click on `PT-IND-004` to trigger the slide-out inspection drawer; click **Load into Cockpit** to show how Tab 1 immediately updates.

### 3. Backup Video Fallback
* If local network speeds stutter during screen recording, record the browser interaction locally using `index.html` or review the pre-captured screenshots in `scratch/screenshots_live_cards/` as backup slide assets.
