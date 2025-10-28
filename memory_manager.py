import json, os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"preferred_colors": {}, "sustainability_bias": 0.5}
    with open(MEMORY_FILE) as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def update_memory(memory, item, feedback):
    color = item.get("color", "")
    if feedback == "like":
        memory["preferred_colors"][color] = min(1.0,
            memory["preferred_colors"].get(color, 0.5) + 0.1)
    else:
        memory["preferred_colors"][color] = max(0.0,
            memory["preferred_colors"].get(color, 0.5) - 0.1)
    save_memory(memory)
    return memory
