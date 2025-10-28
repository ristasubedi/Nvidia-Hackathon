from flask import Flask, render_template, request, jsonify
import json, subprocess
import requests
from fuzzy_logic import compute_fuzzy_scores
from quantum_map import compute_quantum_scores
from memory_manager import load_memory
from config import get_nvidia_headers, get_api_config

app = Flask(__name__)

def combine_scores(fuzzy, quantum, memory, items):
    combined = {}
    for item in items:
        base = 0.6*fuzzy[item["id"]] + 0.4*quantum[item["id"]]
        color = item["color"]
        if color in memory["preferred_colors"]:
            base += 0.05*memory["preferred_colors"][color]
        combined[item["id"]] = round(min(base, 1.0), 3)
    return combined

def call_nvidia_ai(context, combined_scores, memory):
    """Call NVIDIA API for AI recommendations with fallback to local Ollama"""
    prompt = f"""
You are a sustainable fashion AI stylist.
User context: {json.dumps(context, indent=2)}
Suitability scores: {json.dumps(combined_scores, indent=2)}
User memory: {json.dumps(memory, indent=2)}
Recommend the best outfit and explain briefly in JSON:
{{"outfit": "...", "reason": "..."}}.
"""
    
    # Try NVIDIA API first
    try:
        config = get_api_config()
        headers = get_nvidia_headers()
        
        payload = {
            "model": config["default_model"],
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": config["temperature"],
            "max_tokens": config["max_tokens"],
            "stream": False
        }
        
        response = requests.post(
            f"{config['nvidia_base_url']}/chat/completions",
            headers=headers,
            json=payload,
            timeout=config["timeout"]
        )
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
        else:
            print(f"NVIDIA API error: {response.status_code} - {response.text}")
            raise Exception(f"NVIDIA API returned {response.status_code}")
            
    except Exception as nvidia_error:
        print(f"NVIDIA API failed: {nvidia_error}")
        
        # Fallback to local Ollama
        try:
            result = subprocess.run(
                ["ollama", "run", "mistral", prompt],
                capture_output=True, text=True, timeout=30
            )
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            return '{"outfit": "Navy Blazer + White Shirt", "reason": "Classic formal combination suitable for your preferences"}'
        except Exception as ollama_error:
            print(f"Ollama fallback failed: {ollama_error}")
            return f'{{"outfit": "Error", "reason": "Both NVIDIA API and local AI unavailable"}}'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/recommend', methods=['POST'])
def get_recommendation():
    try:
        # Get user input
        data = request.json
        context = {
            "temperature": int(data.get('temperature', 20)),
            "formality": int(data.get('formality', 5)),
            "mood": int(data.get('mood', 5)),
            "occasion": data.get('occasion', 'casual outing')
        }
        
        # Load fashion database and memory
        items = json.load(open("fashion_db.json"))
        memory = load_memory()
        
        # Compute scores
        fuzzy = compute_fuzzy_scores(context, items)
        quantum = compute_quantum_scores(context, items)
        combined = combine_scores(fuzzy, quantum, memory, items)
        
        # Get AI recommendation
        ai_result = call_nvidia_ai(context, combined, memory)
        
        # Return comprehensive response
        return jsonify({
            'context': context,
            'fuzzy_scores': fuzzy,
            'quantum_scores': quantum,
            'combined_scores': combined,
            'ai_recommendation': ai_result,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/api/items')
def get_items():
    try:
        items = json.load(open("fashion_db.json"))
        return jsonify(items)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)