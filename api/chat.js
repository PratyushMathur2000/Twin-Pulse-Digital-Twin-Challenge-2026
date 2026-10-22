// api/chat.js — Vercel Serverless Function for Twin-Pulse Gemini AI Advisor
export default async function handler(req, res) {
  // Enable CORS for web clients
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version, Authorization'
  );

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed. Use POST.' });
  }

  try {
    const { prompt, patient, metrics, scenario, history, clientApiKey } = req.body || {};
    
    // Priority: Server-side environment variable (100% secure), fallback to client-provided key
    const apiKey = process.env.GEMINI_API_KEY || clientApiKey;

    if (!apiKey) {
      return res.status(400).json({
        error: 'GEMINI_API_KEY is not configured on Vercel environment variables nor supplied in client settings.',
        code: 'MISSING_API_KEY'
      });
    }

    const systemInstruction = `You are the Twin-Pulse Healthcare Digital Twin Clinical Advisor & AI Diagnostic Copilot, an expert cardiometabolic digital twin physician grounded in the 2026 ICMR-INDIAB and ADA/KDIGO guidelines for Indian populations.
You evaluate coupled multi-organ dynamics (Pancreatic β-cell glycemic axis, Conduit arterial vascular tree, Autonomic cardiac HRV, and Hepatorenal filtration).
When analyzing the patient and counterfactual scenarios, provide structured, clinical, and actionable insights. Be concise, precise, and practical.`;

    const contents = [];
    if (Array.isArray(history)) {
      for (const msg of history.slice(-6)) {
        contents.push({
          role: msg.role === 'assistant' ? 'model' : 'user',
          parts: [{ text: msg.text || msg.content || '' }]
        });
      }
    }

    const patientContext = patient ? `Patient: ${patient.name} (${patient.id}, Phenotype: ${patient.phenotype || 'MONO'}, Age: ${patient.age || '48'}${patient.sex || 'M'}, City: ${patient.city || 'Mumbai'})
Baseline EHR: HbA1c ${patient.hba1c || '8.2'}%, Fasting Glu ${patient.fastingGlu || '154'} mg/dL, BMI ${patient.bmi || '23.8'}, eGFR ${patient.egfr || '74'}, FIB-4 ${patient.fib4 || '1.8'}` : '';

    const telemetryContext = metrics ? `Live Wearable Telemetry: CGM ${metrics.cgm} mg/dL, BP ${metrics.sbp}/${metrics.dbp} mmHg, HRV RMSSD ${metrics.hrv} ms, Strain PSI ${metrics.psi}/100, Predicted Safe Window (RUL) ${metrics.rulHours} hrs.` : '';

    const scenarioContext = scenario ? `What-If Simulation Sliders: Meal Carbs ${scenario.carbs}g, Medication Adherence ${scenario.meds}%, Sleep ${scenario.sleep}h, Steps ${scenario.steps}, Sympathetic Stress ${scenario.stress}/100.` : '';

    const userPrompt = `${patientContext}\n${telemetryContext}\n${scenarioContext}\n\nClinical Inquiry / Question: ${prompt}`;

    contents.push({
      role: 'user',
      parts: [{ text: userPrompt }]
    });

    const geminiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key=${apiKey}`;
    const response = await fetch(geminiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        system_instruction: { parts: [{ text: systemInstruction }] },
        contents: contents,
        generationConfig: {
          temperature: 0.3,
          maxOutputTokens: 900
        }
      })
    });

    if (!response.ok) {
      const errText = await response.text();
      return res.status(response.status).json({ error: `Gemini API error: ${errText}` });
    }

    const data = await response.json();
    const reply = data.candidates?.[0]?.content?.parts?.[0]?.text || 'No response generated.';

    return res.status(200).json({
      reply: reply,
      model: 'gemini-3.5-flash-lite',
      timestamp: new Date().toISOString()
    });
  } catch (err) {
    return res.status(500).json({ error: err.message || 'Server error' });
  }
}
