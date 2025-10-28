import numpy as np

def quantum_feature_map(temp, formality, alpha=np.pi, beta=np.pi/2):
    """Encode temperature and formality into 4D quantum-like features."""
    Tn = temp / 40.0
    Fn = formality / 10.0
    return np.array([np.cos(alpha*Tn), np.sin(alpha*Tn),
                     np.cos(beta*Fn), np.sin(beta*Fn)])

def similarity(user_vec, item_vec):
    return float(np.dot(user_vec, item_vec) /
                 (np.linalg.norm(user_vec) * np.linalg.norm(item_vec)))

def compute_quantum_scores(context, items):
    """Return quantum similarity for each item."""
    u_vec = quantum_feature_map(context["temperature"], context["formality"])
    results = {}
    for item in items:
        i_vec = quantum_feature_map(item["formality"], context["formality"])
        results[item["id"]] = round(similarity(u_vec, i_vec), 3)
    return results
