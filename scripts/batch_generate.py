import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from generate_article import build_article
from keyword_engine import generate_titles   # 👈 QUESTO È IL PEZZO IMPORTANTE

def run_batch(cluster, number):

    # 🔥 qui generi titoli SEO veri
    titles = generate_titles(cluster, int(number))

    for title in titles:

        print(f"Generating: {title}")

        build_article(title, cluster)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--cluster", required=True)
    parser.add_argument("--number", required=True)

    args = parser.parse_args()

    run_batch(args.cluster, args.number)
