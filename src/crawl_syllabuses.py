from argparse import ArgumentParser
from pathlib import Path
import json
import re
import requests
from bs4 import BeautifulSoup
from parse import parse_syllabus
from tqdm import tqdm
import os


def get_args():
    parser = ArgumentParser(description="Crawl syllabus info to construct graph")
    parser.add_argument(
        "--url",
        help="url for syllabuses page",
        type=str,
    )
    parser.add_argument(
        "--output_dir",
        help="Output directory",
        type=Path,
        default="./syllabuses",
    )
    return parser.parse_args()


def main() -> None:
    args = get_args()

    if not os.path.exists(args.output_dir):
        raise Exception(f"Output directory {args.output_dir} does not exists")
    response = requests.get(args.url)
    soup = BeautifulSoup(response.content, "html.parser")
    refs = soup.find_all('a', href=True)

    pattern = r'CSE\d\d\d'
    for href_field in tqdm(refs):
        link_to_syllabi = re.match(pattern, href_field.text)
        if link_to_syllabi:
            code = link_to_syllabi[0]
            parsed_data = parse_syllabus(href_field['href'])

            with open(os.path.join(str(args.output_dir), f"{code}.json"), "w", encoding="UTF-8") as f:
                json.dump(parsed_data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
