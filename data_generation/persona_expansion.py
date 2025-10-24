# mindwatch/data_generation/persona_expansion.py

import os
import json
import random
import time
import requests
from tqdm import tqdm
from base_personas import PERSONAS

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "zephyr"
OUTPUT_PATH = "data/generated/expanded_personas.json"

# Each original persona will be expanded into 5 variants (total ~150)
MULTIPLIER = 5


def expand_persona(persona, variation_id):
    prompt = (
    f"You are generating emotionally realistic *first-person personas* for a mental health journaling AI system.\n\n"
    f"Here is the original base persona:\n"
    f"- Name: {persona['name']}\n"
    f"- Age: {persona['age']}\n"
    f"- Emotional context: {persona['context']}\n"
    f"- Social engagement baseline (1–5): {persona['baseline_social']}\n"
    f"- Average screen time (hours/day): {persona['baseline_screen_time']}\n\n"
    f"Now create a **new persona** who is similar but distinct:\n"
    f"- Use a **different name** and a **slightly different emotional experience**\n"
    f"- Keep the age between **18 and 25**\n"
    f"- Adjust **social score** and **screen time** within realistic limits\n"
    f"- Write the **context as a short first-person paragraph**, as if the new persona is journaling about their mental health.\n"
    f"  Make it 2–3 sentences max, emotionally expressive, not a third-person biography.\n\n"
    f"Return ONLY a valid JSON object in this structure — no commentary, markdown, or formatting:\n"
    f'{{"name": "...", "age": ..., "context": "<first-person emotional paragraph>", '
    f'"baseline_social": ..., "baseline_screen_time": ...}}'
)


    response = requests.post(
        OLLAMA_API_URL,
        json={"model": MODEL_NAME, "prompt": prompt, "stream": False}
    )

    if response.status_code == 200:
        content = response.json().get("response", "").strip()
        try:
            variation = json.loads(content)
            variation["persona_id"] = f"{persona['persona_id']}_v{variation_id}"
            return variation
        except json.JSONDecodeError:
            print(f"[Warning] Failed to parse response:\n{content}")
            return None
    else:
        print(f"[Error] Ollama request failed: {response.text}")
        return None
        


# Expand personas
expanded = []

for persona in tqdm(PERSONAS, desc="Expanding personas"):
    expanded.append(persona)  # include the original
    for i in range(1, MULTIPLIER):
        variant = expand_persona(persona, i)
        if variant:
            expanded.append(variant)
        time.sleep(0.2)  # throttle requests to be safe

# Save output
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

with open(OUTPUT_PATH, "w") as f:
    json.dump(expanded, f, indent=2)

print(f"✅ Saved {len(expanded)} expanded personas to {OUTPUT_PATH}")