import math

def membership(x, a, b, c):
    if x <= a or x >= c: return 0
    elif x == b: return 1
    elif x < b: return (x - a) / (b - a)
    else: return (c - x) / (c - b)

def fuzzy_score(temp, formality, mood, item):
    """Compute fuzzy suitability score for a single item."""
    temp_map = {'cold': (0, 0, 15), 'cool': (10, 20, 25),
                'mild': (20, 25, 30), 'warm': (28, 35, 40)}
    formality_map = {'casual': (0, 0, 4), 'semi-formal': (3, 5, 7),
                     'formal': (6, 8, 10)}

    t_score = membership(temp, *temp_map[item['weather']])
    f_score = membership(formality, *formality_map[item['style']])
    m_score = membership(mood, 0, 5, 10)  # placeholder mood scale

    return round(0.4*t_score + 0.4*f_score + 0.2*m_score, 3)

def compute_fuzzy_scores(context, items):
    return {
        item["id"]: fuzzy_score(context["temperature"], context["formality"],
                                context["mood"], item)
        for item in items
    }
