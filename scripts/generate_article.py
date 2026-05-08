import argparse
import os
import yaml
from datetime import datetime

# =========================
# OUTPUT
# =========================

OUTPUT_DIR = "output/articles"

# =========================
# PATH SAFE BASE DIR
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# =========================
# UTILS
# =========================

def slugify(title: str):
    return title.lower().replace(" ", "-").replace("'", "")

def load_yaml(path):
    full_path = os.path.join(BASE_DIR, path)
    with open(full_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def load_template(path):
    full_path = os.path.join(BASE_DIR, path)
    with open(full_path, "r", encoding="utf-8") as file:
        return file.read()

def save_output(slug, content):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    path = os.path.join(OUTPUT_DIR, f"{slug}.md")

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"\n✅ Article generated: {path}")

# =========================
# CORE GENERATOR
# =========================

def build_article(title, cluster):

    slug = slugify(title)

    template = load_template("templates/article_template.md")

    cta_engine = load_yaml("engine/cta_engine.yaml")
    linking_graph = load_yaml("engine/linking_graph.yaml")

    # =========================
    # CTA (ITALIANO)
    # =========================

    cta_soft = cta_engine[cluster]["soft"][0]
    cta_medium = cta_engine[cluster]["medium"][0]
    cta_strong = cta_engine[cluster]["strong"][0]

    # =========================
    # INTERNAL LINKS
    # =========================

    links = linking_graph[cluster]["links"]

    # =========================
    # ITALIAN SEO CONTENT CORE
    # =========================

    article = template

    replacements = {

        # META
        "{{title}}": title,
        "{{slug}}": slug,
        "{{cluster}}": cluster,

        "{{primary_keyword}}": title.lower(),
        "{{secondary_keyword_1}}": f"{title.lower()} tips",
        "{{secondary_keyword_2}}": f"best {title.lower()}",

        # 🇮🇹 META DESCRIPTION ITALIANA
        "{{meta_description}}": f"Impara {title.lower()} con esempi pratici e spiegazioni semplici.",

        # STRUTTURA SEO
        "{{intent}}": "informational",
        "{{difficulty}}": "beginner",
        "{{reading_time}}": "10 min",
        "{{date}}": datetime.today().strftime("%Y-%m-%d"),

        # 🇮🇹 CONTENUTO ITALIANO
        "{{introduction}}": f"{title} è una delle competenze più utili per chi studia inglese.",

        "{{section_1}}": "Questa sezione spiega le basi e l’uso pratico dell’argomento.",

        "{{mistakes}}": "Molti studenti commettono errori comuni che rallentano i progressi.",

        "{{real_life_example}}": "Ecco un esempio reale per capire meglio come usare questa competenza.",

        "{{section_2}}": "Segui questi passaggi per migliorare in modo più rapido ed efficace.",

        "{{practical_tips}}": "La costanza è la chiave: pratica ogni giorno anche per pochi minuti.",

        # 💰 CTA ITALIANE
        "{{cta_soft}}": cta_soft,
        "{{cta_medium}}": cta_medium,
        "{{cta_strong}}": cta_strong,

        # 🔗 LINKING
        "{{related_links}}": "\n".join([f"- {link}" for link in links]),

    }

    # =========================
    # APPLY REPLACEMENTS
    # =========================

    for key, value in replacements.items():
        article = article.replace(key, value)

    # =========================
    # SAVE
    # =========================

    save_output(slug, article)

# =========================
# CLI ENTRYPOINT
# =========================

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--title", required=True)
    parser.add_argument("--cluster", required=True)

    args = parser.parse_args()

    build_article(args.title, args.cluster)
