import argparse
import json
import random
import csv

parser = argparse.ArgumentParser()

parser.add_argument("json_file", type=str)
parser.add_argument("num_posts_to_output", type=int)
parser.add_argument("--seed", "-s", type=int, default=None)
parser.add_argument("-o", "--output", required=True, type=str)
parser.add_argument("--exclude", action = "append", default = [])


args = parser.parse_args()


with open(args.json_file, "r", encoding = "utf-8") as f:
    data = json.load(f)

posts = data["data"]

excluded_names = set()

for file in args.exclude:
    with open(file, "r", encoding = "utf-8") as f:
        reader = csv.DictReader(f, delimiter = "\t")

        for row in reader:
            excluded_names.add(row["name"])

filtered_posts = [
    post for post in posts
    if post["name"] not in excluded_names
]

num_excluded = len(posts) - len(filtered_posts)

sample_size = min(args.num_posts_to_output, len(filtered_posts))
random.seed(args.seed)
selected_posts = random.sample(filtered_posts, sample_size)

with open(args.output, "w", encoding = "utf-8") as f:
    writer = csv.writer(f, delimiter = "\t")

    writer.writerow(["name", "title", "coding"])

    for post in selected_posts:
        name = post["name"]
        title = post["title"]

        title = title.replace("\t", " ").replace("\n", " ").replace("\r", " ")

        writer.writerow([name, title, ""])




print("Number of posts:", len(posts))
print("Number of excluded posts:", num_excluded)
print("Number of eligible posts:", len(filtered_posts))
print("Requested sample size:", args.num_posts_to_output)
print("Actual sample size:", len(selected_posts))
print("Output completed")

