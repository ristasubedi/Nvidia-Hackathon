import json, subprocess
from fuzzy_logic import compute_fuzzy_scores
from quantum_map import compute_quantum_scores
from memory_manager import load_memory


def combine_scores(fuzzy, quantum, memory, items):
    combined = {}
    for item in items:
        base = 0.6*fuzzy[item["id"]] + 0.4*quantum[item["id"]]
        color = item["color"]
        if color in memory["preferred_colors"]:
            base += 0.05*memory["preferred_colors"][color]
        combined[item["id"]] = round(min(base, 1.0), 3)
    return combined

def call_mistral_local(context, combined_scores, memory):
    prompt = f"""
You are a sustainable fashion AI stylist.
User context: {json.dumps(context, indent=2)}
Suitability scores: {json.dumps(combined_scores, indent=2)}
User memory: {json.dumps(memory, indent=2)}
Recommend the best outfit and explain briefly in JSON:
{{"outfit": "...", "reason": "..."}}.
"""
    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True, text=True
    )
    return result.stdout.strip()

def main():
    context = {"temperature": 20, "formality": 5, "mood": 6,
               "occasion": "networking dinner"}
    items = json.load(open("fashion_db.json"))
    memory = load_memory()

    fuzzy = compute_fuzzy_scores(context, items)
    quantum = compute_quantum_scores(context, items)
    combined = combine_scores(fuzzy, quantum, memory, items)

    print("\n===== FUZZY SCORES =====")
    for k, v in fuzzy.items():
        print(f"{k}: {v}")

    print("\n===== QUANTUM SCORES =====")
    for k, v in quantum.items():
        print(f"{k}: {v}")

    print("\n===== COMBINED SCORES (Fuzzy + Quantum + Memory Bias) =====")
    for k, v in combined.items():
        print(f"{k}: {v}")

    print("\n===== CALLING MISTRAL =====\n")
    result = call_mistral_local(context, combined, memory)
    print("Mistral Output:\n", result)

if __name__ == "__main__":
    main()
