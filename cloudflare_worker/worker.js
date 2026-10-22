/**
 * Twin-Pulse Cloudflare Worker Proxy for Google Gemini
 * ======================================================
 * Securely forwards clinical inquiries to Gemini 3.5 Flash without exposing
 * your Gemini API key in frontend code.
 * 
 * 1-Minute Cloudflare Deployment:
 * 1. Go to your Cloudflare Dashboard -> "Workers & Pages" -> "Create Application" -> "Create Worker".
 * 2. Name it (e.g., `twin-pulse-ai`) and paste this code into the editor.
 * 3. Go to Worker "Settings" -> "Variables and Secrets".
 * 4. Click "Add" under Environment Variables / Secrets:
 *      Variable Name: GEMINI_API_KEY
 *      Value: <Paste your Gemini API key here>
 *      (Encrypt / mark as Secret)
 * 5. Click "Save and Deploy".
 * 6. Copy the Worker URL (e.g. `https://twin-pulse-ai.<your-account>.workers.dev`)
 *    and paste it into the Twin-Pulse AI Settings in the dashboard!
 */

export default {
  async fetch(request, env, ctx) {
    // Handle CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type, Authorization",
        },
      });
    }

    if (request.method !== "POST") {
      return new Response(JSON.stringify({ error: "Method not allowed. Use POST." }), {
        status: 405,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
      });
    }

    try {
      const apiKey = env.GEMINI_API_KEY;
      if (!apiKey) {
        return new Response(JSON.stringify({
          error: "GEMINI_API_KEY secret is not set in this Cloudflare Worker environment."
        }), {
          status: 500,
          headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
        });
      }

      const body = await request.json();
      const { prompt, patient, metrics, scenario, history } = body;

      const systemInstruction = `You are the Twin-Pulse Healthcare Digital Twin Clinical Advisor & AI Diagnostic Copilot, an expert cardiometabolic digital twin physician grounded in the 2026 ICMR-INDIAB and ADA/KDIGO guidelines for Indian populations.
You evaluate coupled multi-organ dynamics (Pancreatic β-cell glycemic axis, Conduit arterial vascular tree, Autonomic cardiac HRV, and Hepatorenal filtration).
When analyzing the patient and counterfactual scenarios, provide structured, clinical, and actionable insights. Be concise, precise, and practical.`;

      const contents = [];
      if (Array.isArray(history)) {
        for (const msg of history.slice(-6)) {
          contents.push({
            role: msg.role === "assistant" ? "model" : "user",
            parts: [{ text: msg.text || msg.content || "" }]
          });
        }
      }

      const patientContext = patient ? `Patient: ${patient.name} (${patient.id}, Phenotype: ${patient.phenotype || 'MONO'}, Age: ${patient.age || '48'}${patient.sex || 'M'}, City: ${patient.city || 'Mumbai'})
Baseline EHR: HbA1c ${patient.hba1c || '8.2'}%, Fasting Glu ${patient.fastingGlu || '154'} mg/dL, BMI ${patient.bmi || '23.8'}, eGFR ${patient.egfr || '74'}, FIB-4 ${patient.fib4 || '1.8'}` : '';

      const telemetryContext = metrics ? `Live Wearable Telemetry: CGM ${metrics.cgm} mg/dL, BP ${metrics.sbp}/${metrics.dbp} mmHg, HRV RMSSD ${metrics.hrv} ms, Strain PSI ${metrics.psi}/100, Predicted Safe Window (RUL) ${metrics.rulHours} hrs.` : '';

      const scenarioContext = scenario ? `What-If Simulation Sliders: Meal Carbs ${scenario.carbs}g, Medication Adherence ${scenario.meds}%, Sleep ${scenario.sleep}h, Steps ${scenario.steps}, Sympathetic Stress ${scenario.stress}/100.` : '';

      const userPrompt = `${patientContext}\n${telemetryContext}\n${scenarioContext}\n\nClinical Inquiry / Question: ${prompt}`;

      contents.push({
        role: "user",
        parts: [{ text: userPrompt }]
      });

      const candidateModels = ["gemini-2.5-flash", "gemini-1.5-flash", "gemini-2.0-flash"];
      let reply = null;
      let usedModel = null;
      let lastError = null;

      for (const model of candidateModels) {
        try {
          const geminiUrl = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
          const response = await fetch(geminiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              system_instruction: { parts: [{ text: systemInstruction }] },
              contents: contents,
              generationConfig: {
                temperature: 0.3,
                maxOutputTokens: 900
              }
            })
          });

          if (response.ok) {
            const data = await response.json();
            reply = data.candidates?.[0]?.content?.parts?.[0]?.text;
            if (reply) {
              usedModel = model;
              break;
            }
          } else {
            lastError = await response.text();
          }
        } catch (err) {
          lastError = err.message;
        }
      }

      if (!reply) {
        return new Response(JSON.stringify({ error: `Gemini API invocation failed: ${lastError}` }), {
          status: 502,
          headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
        });
      }

      return new Response(JSON.stringify({
        reply: reply,
        model: usedModel,
        timestamp: new Date().toISOString()
      }), {
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
      });
    } catch (err) {
      return new Response(JSON.stringify({ error: err.message || "Worker error" }), {
        status: 500,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
      });
    }
  }
};
