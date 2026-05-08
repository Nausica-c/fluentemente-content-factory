import yaml
import random

def load_keyword_engine():

    with open("engine/keyword_engine.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def to_italian_title(text: str):

    text = text.lower()

    # traduzioni base SEO → italiano
    text = text.replace("how to", "come")
    text = text.replace("best", "migliore")
    text = text.replace("guide", "guida")
    text = text.replace("learn", "imparare")
    text = text.replace("study", "studiare")
    text = text.replace("english", "inglese")

    return text

def generate_titles(cluster: str, n: int = 10):

    data = load_keyword_engine()

    if cluster not in data:
        raise ValueError(f"Cluster non trovato: {cluster}")

    seeds = data[cluster]["seed_topics"]
    intents = data[cluster]["intents"]

    titles = []

    for _ in range(n):

        topic = random.choice(seeds)
        intent_type = random.choice(list(intents.keys()))
        pattern = random.choice(intents[intent_type]["patterns"])

        raw_title = pattern.replace("{topic}", topic)

        italian_title = to_italian_title(raw_title)

        titles.append(italian_title.capitalize())

    return titles


if __name__ == "__main__":

    print(generate_titles("method", 5))
