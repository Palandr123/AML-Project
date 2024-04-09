from argparse import ArgumentParser
from pathlib import Path
import json
import re
import requests
from bs4 import BeautifulSoup
from parse import parse_prerequisites
from tqdm import tqdm


def get_args():
    parser = ArgumentParser(description="Crawl syllabus info to construct graph")
    parser.add_argument(
        "--url_bach",
        help="url of the bachelors syllabi",
        type=str,
    )
    parser.add_argument(
        "--url_ms",
        help="url of the masters syllabi",
        type=str,
    )
    parser.add_argument(
        "--output_path",
        help="output_path",
        type=Path,
        default="graph.json",
    )
    return parser.parse_args()


def parse_main_page(url: str) -> dict:
    mapping = {}
    parsed_data = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    refs = soup.find_all('a', href=True)

    pattern = r'CSE\d\d\d'
    for href_field in tqdm(refs):
        link_to_syllabi = re.match(pattern, href_field.text)
        if link_to_syllabi:
            prereq_list = {}
            href = href_field['href']
            code = link_to_syllabi[0]
            prereq_list['Code'] = link_to_syllabi[0]
            prereq_list['Title'] = href_field.text
            prereq_list['Prerequisites'] = []
            mapping[link_to_syllabi[0]] = href_field.text
            response = requests.get(href)
            soup_syllabi = BeautifulSoup(response.content, "html.parser")
            prereq = parse_prerequisites(soup_syllabi)
            prereq_sub = prereq['Prerequisite subjects']

            for prereq_text in prereq_sub:
                prereq_code = re.match(pattern, prereq_text)
                if prereq_code:
                    prereq_list['Prerequisites'].append(prereq_code[0])
            parsed_data.append(prereq_list)
    return parsed_data, mapping


def main() -> None:
    args = get_args()
    parsed_data_bach, bach_mapping = parse_main_page(args.url_bach)
    parsed_data_ms, ms_mapping = parse_main_page(args.url_ms)

    mapping = dict(list(bach_mapping.items()) + list(ms_mapping.items()))
    parsed_data = {'Code to title mapping': mapping, "Prerequisites graph": parsed_data_bach + parsed_data_ms}

    with open(str(args.output_path), "w", encoding="UTF-8") as f:
        json.dump(parsed_data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
