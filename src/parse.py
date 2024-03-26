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


def parse_prerequisites(soup: BeautifulSoup) -> dict:
    prerequisites = {}
    prereq_section = soup.find('span', {'id': 'Prerequisites'})

    if prereq_section:
        prereq_subjects = soup.find('span', {'id': 'Prerequisite_subjects'}).parent.find_next_sibling()
        prereq_subjects_list = []
        if prereq_subjects.name == 'ul':
            for li in prereq_subjects.find_all('li'):
                prereq_subjects_list.append(li.text)
        
        prereq_topics = soup.find('span', {'id': 'Prerequisite_topics'}).parent.find_next_sibling()
        prereq_topics_list = []
        if prereq_topics.name == 'ul':
            for li in prereq_topics.find_all('li'):
                prereq_topics_list.append(li.text)
    prerequisites["Prerequisite subjects"] = prereq_subjects_list
    prerequisites["Prerequisite topics"] = prereq_topics_list
    return prerequisites


def parse_course_topics(soup: BeautifulSoup) -> dict:
    course_topics = {}
    course_topics_section = soup.find('span', {'id': 'Course_Topics'})
    if course_topics_section:
        course_topics_table = course_topics_section.parent.find_next_sibling()
        if course_topics_table.name == "table":
            for tr in course_topics_table.find_all('tr'):
                td = tr.find_all('td')
                if td and len(td) == 2:
                    td1, td2 = td
                    subtopic_list = []
                    for li in td2.find_all('li'):
                        subtopic_list.append(li.text)
                    course_topics[td1.text] = subtopic_list
    return course_topics


def parse_ilo(soup: BeautifulSoup) -> dict:
    intended_learning_outcomes = {}
    intended_learning_outcomes_section = soup.find('span', {'id': 'Intended_Learning_Outcomes_(ILOs)'})
    if intended_learning_outcomes_section:
        
        # Find Main purpose section
        main_purpose_section = soup.find('span', {'id': 'What_is_the_main_purpose_of_this_course?'})
        if main_purpose_section:
            main_purpose_section = main_purpose_section.parent.find_next_sibling()
            intended_learning_outcomes["What is the main purpose of this course?"] = main_purpose_section.text.strip()
            
        # Find ILO defined at 3 levels section
        ilo_3_levels_section = soup.find('span', {'id': 'ILOs_defined_at_three_levels'})
        intended_learning_outcomes["ILOs defined at three levels"] = {}
        if ilo_3_levels_section:
            
            # Level 1
            intended_learning_outcomes["ILOs defined at three levels"]\
            ["Level 1: What concepts should a student know/remember/explain?"]\
            = parse_ilo_levels(soup, "Level_1:_What_concepts_should_a_student_know.2Fremember.2Fexplain.3F")
            
            # Level 2
            intended_learning_outcomes["ILOs defined at three levels"]\
            ["Level 2: What basic practical skills should a student be able to perform?"]\
            = parse_ilo_levels(soup, "Level_2:_What_basic_practical_skills_should_a_student_be_able_to_perform.3F")
            
            # Level 3
            intended_learning_outcomes["ILOs defined at three levels"]\
            ["Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?"]\
            = parse_ilo_levels(soup, "Level_3:_What_complex_comprehensive_skills_should_a_student_be_able_to_apply_in_real-life_scenarios.3F")
    
    return intended_learning_outcomes


def parse_ilo_levels(soup: BeautifulSoup, _id: str) -> list:
    lvl = soup.find('span', {'id': _id})
    lvl_list = []
    if lvl and lvl.parent.find_next_sibling().find_next_sibling().name == 'ul':
        lvl_ul = lvl.parent.find_next_sibling().find_next_sibling()
        for li in lvl_ul.find_all('li'):
            lvl_list.append(li.text.strip())
    return lvl_list


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
    parsed_data["Prerequisites"] = parse_prerequisites(soup)
    
    # Find Course Topics
    parsed_data["Course Topics"] = parse_course_topics(soup)
    
    # Find ILO(Intended learning outcomes)
    parsed_data["Intended Learning Outcomes (ILOs)"] = parse_ilo(soup)
    
    return parsed_data


def main() -> None:
    args = get_args()
    parsed_data = parse_syllabus(args.url)
    
    with open(str(args.output_path), "w", encoding="UTF-8") as f:
        json.dump(parsed_data, f, indent=2, ensure_ascii=False)



if __name__ == "__main__":
    main()
