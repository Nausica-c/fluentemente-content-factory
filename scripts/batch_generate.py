import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from generate_article import build_article
def run_batch(cluster, number):

    for i in range(int(number)):

        title = f"{cluster.capitalize()} Guide {i+1}"

        print(f"Generating: {title}")

        build_article(title, cluster)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--cluster", required=True)
    parser.add_argument("--number", required=True)

    args = parser.parse_args()

    run_batch(args.cluster, args.number)
