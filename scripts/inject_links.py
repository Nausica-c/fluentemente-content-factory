import yaml
import random

def load_linking_graph():
    with open("engine/linking_graph.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def get_links(cluster):

    graph = load_linking_graph()

    if cluster not in graph:
        return []

    pillar = graph[cluster]["pillar"]
    links = graph[cluster]["links"]

    return {
        "pillar": pillar,
        "links": random.sample(links, min(3, len(links)))
    }

if __name__ == "__main__":

    cluster = "travel"

    print(get_links(cluster))
