# 🧠 MindWatch

MindWatch is an AI-powered system designed to detect early signs of mental health decline by analyzing emotion trends, semantic drift, and behavioral signals over time. It offers personalized self-care suggestions and links to crisis support — without making clinical diagnoses.

## 🚀 Features
```
- Emotion classification (RoBERTa model)
- Semantic drift tracking using sentence embeddings
- Behavioral signal simulation (e.g., screen time, word count)
- Risk scoring with adaptive thresholds
- GPT-powered self-care nudges
- Hardcoded crisis helpline support
- (Optional) Streamlit frontend for journaling interface
```


## 🔍 What This Project Does

1. **Persona Expansion**  
   - Start with 30 base personas (e.g., students with different mental health contexts)
   - Use an LLM (Zephyr via Ollama) to generate 4–5 emotionally similar but distinct variations per persona
   - Total: ~150 emotionally varied synthetic personas

2. **Journal Generation (Current Phase)**  
   - For each persona, simulate 7 days of mental health journaling
   - Inject realistic emotion shifts (hopeful, reflective, anxious, etc.)
   - Output: ~1,050 journal entries grounded in emotional trajectory

3. **Next Steps (Upcoming)**
   - Score each journal entry for:
     - Emotion intensity
     - Drift from baseline
     - Risk levels (burnout, depressive markers, etc.)
   - Generate visualizations, embeddings, and behavior tags

---

## 🛠️ Tech Stack

- **LLM Inference**: [Ollama](https://ollama.com) running `zephyr` locally with GPU acceleration
- **Language**: Python 3.9
- **Data Management**: JSON output (for personas and journals)
- **Multithreading**: Used to parallelize journal generation safely
- **Notebook + CLI Pipelines**: Modular scripts for each step in `data_generation/` and `analysis/`

---


## 🔧 Setup
```
git clone https://github.com/aryaa-deshpande/mindwatch.git
cd mindwatch
pip install -r requirements.txt
```

## Hackathon

AI for Good Challenge – UB | Fall 2025
In partnership with TechBuffalo, UB School of Management, and UB IAD.