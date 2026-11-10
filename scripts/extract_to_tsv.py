import argparse
import json
import random
import csv

parser = argparse.ArgumentParser()

parser.add_argument("json_file", type=str)
parser.add_argument("num_posts_to_output", type=int)
parser.add_argument("--seed", "-s", type=int, default=None)
parser.add_argument("-o", "--output", required=True, type=str)

args = parser.parse_args()


with open(args.json_file, "r", encoding = "utf-8") as f:
    data = json.load(f)

posts = data["data"]["children"]

sample_size = min(args.num_posts_to_output, len(posts))
random.seed(args.seed)
selected_posts = random.sample(posts, sample_size)

with open(args.output, "w", encoding = "utf-8") as f:
    writer = csv.writer(f, delimiter = "\t")

    writer.writerow(["name", "title", "coding"])

    for post in selected_posts:
        name = post["data"]["name"]
        title = post["data"]["title"]

        title = title.replace("\t", " ").replace("\n", " ").replace("\r", " ")

        writer.writerow([name, title, ""])




print("Number of posts:", len(posts))
print("Requested sample size:", args.num_posts_to_output)
print("output completed")

