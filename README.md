# 🎨 AI Fashion Stylist

An intelligent fashion recommendation system that combines fuzzy logic, quantum-inspired algorithms, and AI language models to provide personalized outfit suggestions.

## ✨ Features

- **Multi-Algorithm Scoring**: Combines fuzzy logic and quantum-inspired feature mapping
- **AI-Powered Recommendations**: Uses NVIDIA API (with Ollama fallback) for intelligent styling advice
- **Memory System**: Learns and adapts to user preferences over time
- **Web Interface**: Beautiful, responsive frontend with real-time controls
- **Sustainability Focus**: Considers environmental impact in recommendations
- **Versatile Database**: 50+ diverse fashion items across all categories

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- NVIDIA API key (get one at [NVIDIA Developer](https://developer.nvidia.com/))
- Ollama (optional, for local AI fallback)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ristasubedi/Nvidia-Hackathon.git
   cd Nvidia-Hackathon
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask numpy requests
   ```

4. **Configure API key**
   ```bash
   cp config.template.py config.py
   # Edit config.py and add your NVIDIA API key
   ```

5. **Run the application**
   ```bash
   python app_web.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5001`

## 🧠 How It Works

### 1. Fuzzy Logic Scoring
- Evaluates clothing items based on temperature, formality, and mood
- Uses triangular membership functions for smooth transitions
- Handles uncertainty in fashion preferences

### 2. Quantum-Inspired Feature Mapping
- Encodes user preferences into quantum-like feature vectors
- Computes similarity using cosine distance
- Provides alternative perspective on item matching

### 3. Memory Management
- Tracks user color preferences over time
- Adjusts recommendations based on past feedback
- Enables personalized styling experience

### 4. AI Integration
- **Primary**: NVIDIA Llama-3.1 Nemotron 70B model via API
- **Fallback**: Local Mistral model via Ollama
- Generates contextual outfit explanations

## 📊 API Endpoints

### `POST /api/recommend`
Get personalized fashion recommendations

**Request Body:**
```json
{
  "temperature": 20,
  "formality": 5,
  "mood": 6,
  "occasion": "networking dinner"
}
```

**Response:**
```json
{
  "context": {...},
  "fuzzy_scores": {...},
  "quantum_scores": {...},
  "combined_scores": {...},
  "ai_recommendation": "...",
  "status": "success"
}
```

### `GET /api/items`
Retrieve all fashion items in the database

## 🎯 Usage Examples

### Casual Day Out
- **Temperature**: 25°C
- **Formality**: 2/10
- **Mood**: 7/10
- **Occasion**: Casual outing

**Expected**: Jeans, t-shirt, sneakers with comfort-focused reasoning

### Business Meeting
- **Temperature**: 20°C
- **Formality**: 8/10
- **Mood**: 5/10
- **Occasion**: Work meeting

**Expected**: Suit, dress shirt, formal shoes with professional reasoning

## 🏗️ Project Structure

```
Nvidia-Hackathon/
├── app.py              # Original command-line version
├── app_web.py          # Flask web application
├── config.py           # Configuration (create from template)
├── config.template.py  # Configuration template
├── fashion_db.json     # Fashion items database
├── fuzzy_logic.py      # Fuzzy logic algorithms
├── quantum_map.py      # Quantum-inspired calculations
├── memory_manager.py   # User preference memory
├── templates/
│   └── index.html      # Web interface
└── requirements.txt    # Python dependencies
```

## 🧪 Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **AI**: NVIDIA API, Ollama
- **Algorithms**: Fuzzy Logic, Quantum-inspired Computing
- **Data**: JSON database with 50+ fashion items

## 🔧 Configuration Options

Edit `config.py` to customize:

- **API Settings**: NVIDIA API key, model selection, timeouts
- **Scoring Weights**: Adjust fuzzy/quantum/memory influence
- **Web Server**: Host, port, debug mode settings
- **Fashion Database**: File paths and memory settings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Hackathon Project

This project was created for the NVIDIA Hackathon, showcasing the integration of:
- NVIDIA's powerful language models
- Advanced algorithmic approaches (fuzzy logic + quantum-inspired computing)
- Modern web development practices
- AI-driven user experience design

## 🔮 Future Enhancements

- [ ] Image recognition for outfit visualization
- [ ] Weather API integration for automatic temperature setting
- [ ] Social sharing features
- [ ] Mobile app development
- [ ] Advanced sustainability metrics
- [ ] Style trend analysis
- [ ] User profile management
- [ ] Outfit history and favorites

---
