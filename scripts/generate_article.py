import argparse
import os
import yaml
from datetime import datetime

OUTPUT_DIR = "output/articles"

def slugify(title):
    return title.lower().replace(" ", "-").replace("'", "")

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def load_template(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def save_output(slug, content):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    path = f"{OUTPUT_DIR}/{slug}.md"

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"\n✅ Article generated: {path}")

def build_article(title, cluster):

    slug = slugify(title)

    template = load_template("templates/article_template.md")

    cta_engine = load_yaml("engine/cta_engine.yaml")
    linking_graph = load_yaml("engine/linking_graph.yaml")

    cta_soft = cta_engine[cluster]["soft"][0]
    cta_medium = cta_engine[cluster]["medium"][0]
    cta_strong = cta_engine[cluster]["strong"][0]

    links = linking_graph[cluster]["links"]

    article = template

    replacements = {
        "{{title}}": title,
        "{{slug}}": slug,
        "{{cluster}}": cluster,
        "{{primary_keyword}}": title.lower(),
        "{{secondary_keyword_1}}": f"{title.lower()} tips",
        "{{secondary_keyword_2}}": f"best {title.lower()}",
        "{{meta_description}}": f"Learn {title.lower()} with practical examples and easy explanations.",
        "{{intent}}": "informational",
        "{{difficulty}}": "beginner",
        "{{reading_time}}": "10 min",
        "{{date}}": datetime.today().strftime("%Y-%m-%d"),

        "{{introduction}}": f"{title} is one of the most useful skills for English learners.",
        "{{section_1}}": "This section explains the foundations and practical usage.",
        "{{mistakes}}": "Many learners make the same mistakes when studying this topic.",
        "{{real_life_example}}": "Here is a realistic real-world example.",
        "{{section_2}}": "Follow these practical steps to improve faster.",
        "{{practical_tips}}": "Practice daily and focus on consistency.",
        "{{exercise_block}}": "Try writing 5 sentences using today's structure.",
        "{{section_3}}": "Daily speaking and repetition are essential.",
        "{{daily_routine}}": "Spend at least 15 minutes every day practicing.",
        "{{recommended_methods}}": "Use shadowing, spaced repetition and active recall.",

        "{{faq_question_1}}": f"What is the best way to learn {title.lower()}?",
        "{{faq_answer_1}}": "Practice consistently using practical examples.",

        "{{faq_question_2}}": f"How long does it take to improve {title.lower()}?",
        "{{faq_answer_2}}": "Most learners see progress after a few weeks of consistent practice.",

        "{{faq_question_3}}": f"Can beginners learn {title.lower()}?",
        "{{faq_answer_3}}": "Yes, beginners can improve step by step with the right method.",

        "{{conclusion}}": f"{title} becomes easier with daily exposure and practice.",

        "{{cta_soft}}": f"> 🚀 {cta_soft}",
        "{{cta_medium}}": f"> 🔥 {cta_medium}",
        "{{cta_strong}}": f"> ✅ {cta_strong}",

        "{{internal_link_block_1}}":
            f"- Related: {links[0]}\n- Related: {links[1]}",

        "{{internal_link_block_2}}":
            f"- Explore more: {links[2]}",

        "{{related_article_1}}": links[0],
        "{{related_article_2}}": links[1],
        "{{related_article_3}}": links[2],
    }

    for key, value in replacements.items():
        article = article.replace(key, value)

    save_output(slug, article)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--title", required=True)
    parser.add_argument("--cluster", required=True)

    args = parser.parse_args()

    build_article(args.title, args.cluster)
