# persona_expansion.py (Ollama version using Zephyr)

import json
import random
import time
import requests
from tqdm import tqdm
from pathlib import Path

# Load your base personas
from base_personas import PERSONAS

# Prompt template for Zephyr
CONTEXT_PROMPT = """
You are helping build synthetic journaling personas for a mental health journaling app.
Each persona has a basic psychological context: {base_context}

Your task is to generate {num_variants} emotional variations of this persona's journal entry scenario.
Each variation should:
- Feel like a real, specific moment in time
- Convey different emotional tones (e.g., anxious, hopeful, numb, spiraling, reflective)
- Be short (1–3 sentences max), as if copied from a real journal
- Avoid repetition and feel like different phases or experiences

Return ONLY the list of journal entry variations.
"""

# Run Zephyr via Ollama REST API
def query_zephyr(prompt, model="zephyr"):
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False}
    )
    return res.json().get("response", "")

# Main expansion script
def expand_personas(personas, variants_per=5, out_path="expanded_personas.json"):
    expanded = []

    for persona in tqdm(personas):
        base_context = persona["context"]

        # Generate prompt
        prompt = CONTEXT_PROMPT.format(
            base_context=base_context,
            num_variants=variants_per
        )

        # Call Ollama (Zephyr)
        try:
            response = query_zephyr(prompt)
            variants = [line.strip("-\n ") for line in response.split("\n") if line.strip()]
        except Exception as e:
            print(f"Failed on persona {persona['persona_id']}: {e}")
            variants = []

        expanded.append({
            "persona_id": persona["persona_id"],
            "name": persona["name"],
            "age": persona["age"],
            "base_context": base_context,
            "journal_variants": variants
        })

        # Be nice to your local machine
        time.sleep(1.5)

    # Save output
    Path("data/generated").mkdir(parents=True, exist_ok=True)
    with open(f"data/generated/{out_path}", "w") as f:
        json.dump(expanded, f, indent=2)

    print(f"Saved {len(expanded)} expanded personas to data/generated/{out_path}")

# Run it!
if __name__ == "__main__":
    expand_personas(PERSONAS)