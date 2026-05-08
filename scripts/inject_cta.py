import yaml
import random

def load_cta_engine():
    with open("engine/cta_engine.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def get_cta(cluster, intensity="medium"):

    cta_engine = load_cta_engine()

    if cluster not in cta_engine:
        return "Start learning English with Babbel"

    options = cta_engine[cluster][intensity]

    return random.choice(options)

if __name__ == "__main__":

    cluster = "beginner"

    print(get_cta(cluster))
