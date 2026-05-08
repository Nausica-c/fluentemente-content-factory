import yaml

def load_seo_rules():
    with open("engine/seo_rules.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def validate_title(title):

    rules = load_seo_rules()

    min_chars = rules["seo"]["title"]["min_characters"]
    max_chars = rules["seo"]["title"]["max_characters"]

    length = len(title)

    if length < min_chars:
        return f"⚠️ Title too short ({length} chars)"

    if length > max_chars:
        return f"⚠️ Title too long ({length} chars)"

    return "✅ Title SEO optimized"

def generate_meta_description(keyword):

    return f"Learn {keyword} with practical examples, useful tips and easy explanations."

if __name__ == "__main__":

    title = "How to Learn English Fast"

    print(validate_title(title))

    print(generate_meta_description(title.lower()))
