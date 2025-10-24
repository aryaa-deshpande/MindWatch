import random

# Persona bank
PERSONAS = [
    {
        "persona_id": f"p_{i:03}",
        "name": random.choice(["Aisha", "Ryan", "Maya", "Samir", "Kavya", "Leo", "Jin", "Sara", "Tariq"]),
        "age": random.randint(19, 25),
        "context": random.choice([
            "Just moved to college, feeling isolated",
            "Struggling with academic pressure",
            "Recently went through a breakup",
            "Having trouble with social anxiety",
            "Feeling overwhelmed by responsibilities"
        ]),
        "baseline_social": random.randint(2, 5),
        "baseline_screen_time": round(random.uniform(1.5, 3.0), 1)
    }
    for i in range(30)
]