from argparse import ArgumentParser
from pathlib import Path
import json

import requests
from bs4 import BeautifulSoup


def get_args():
    parser = ArgumentParser(description="Parse syllabus content into JSON")
    parser.add_argument(
        "--url",
        help="url of the syllabus",
        type=str,
    )
    parser.add_argument(
        "--output_path",
        help="output_path",
        type=Path,
        default="syllabus.json",
    )
    return parser.parse_args()


def parse_syllabus(url: str) -> dict:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    if len(soup.title.text.split(":")) == 1:
        title = soup.title.text.split(":")[0].split("-")[0].strip()
    else: 
        title = soup.title.text.split(":")[1].split("-")[0].strip()
    parsed_data = {"Title": title}

    # Find Short Description
    short_description = soup.find('span', {'id': 'Short_Description'}).parent.find_next_sibling('p').text.strip()
    parsed_data["Short Description"] = short_description

    # Find Prerequisites
    prerequisites = {}
    prereq_section = soup.find('span', {'id': 'Prerequisites'})

    if prereq_section:
        prereq_lists = prereq_section.find_next('ul')
        if prereq_lists:
            for li in prereq_lists.find_all('li'):
                course, details = li.text.split(' — ')
                prerequisites[course.strip()] = details.strip()
    parsed_data["Prerequisites"] = prerequisites

    return parsed_data


def main() -> None:
    args = get_args()
    parsed_data = parse_syllabus(args.url)
    
    with open(str(args.output_path), "w", encoding="UTF-8") as f:
        json.dump(parsed_data, f, indent=2, ensure_ascii=False)



if __name__ == "__main__":
    main()
