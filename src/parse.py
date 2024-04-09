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


def parse_table(soup: BeautifulSoup) -> list:
    table_list = []
    if soup.name == 'table':
        th = soup.find_all('th')
        for tr in soup.find_all('tr'):
            td = tr.find_all('td')
            if td and len(td) == len(th):
                table_list.append({th[i].text.strip(): td[i].text.strip() for i in range(len(th))})
    return table_list


def parse_list(soup: BeautifulSoup) -> list:
    list_list = []
    if soup.name in ['ol', 'ul']:
        for li in soup.find_all('li'):
            list_list.append(li.text)
    return list_list


def parse_prerequisites(soup: BeautifulSoup) -> dict:
    prerequisites = {}
    prereq_section = soup.find('span', {'id': 'Prerequisites'})
    prereq_subjects_list = []
    prereq_topics_list = []
    if prereq_section:
        try:
            prereq_subjects = soup.find('span', {'id': 'Prerequisite_subjects'}).parent.find_next_sibling()
            prereq_subjects_list = parse_list(prereq_subjects)

            prereq_topics = soup.find('span', {'id': 'Prerequisite_topics'}).parent.find_next_sibling()
            prereq_topics_list = parse_list(prereq_topics)
            
        except AttributeError:
            prereq_subjects = prereq_section.parent.find_next_sibling()
            if prereq_subjects and prereq_subjects.name == 'ul':
                for li in prereq_subjects.find_all('li'):
                    prereq_subjects_list.append(li.text)
                    
    prerequisites["Prerequisite subjects"] = prereq_subjects_list
    prerequisites["Prerequisite topics"] = prereq_topics_list
    return prerequisites


def parse_course_topics(soup: BeautifulSoup) -> list:
    course_topics_list = []
    course_topics_section = soup.find('span', {'id': 'Course_Topics'})
    if course_topics_section:
        course_topics_table = course_topics_section.parent.find_next_sibling()
        if course_topics_table.name == "table":
            th = course_topics_table.find_all('th')
            if th:
                th1, th2 = th
                
            for tr in course_topics_table.find_all('tr'):
                course_topics = {}
                td = tr.find_all('td')
                if td and len(td) == 2:
                    td1, td2 = td
                    subtopic_list = []
                    for li in td2.find_all('li'):
                        subtopic_list.append(li.text)
                    course_topics[th1.text.strip()] = td1.text
                    course_topics[th2.text.strip()] = subtopic_list
                    course_topics_list.append(course_topics)
    return course_topics_list


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


def parse_grading(soup: BeautifulSoup) -> dict:
    grading_range_soup = soup.find('span', {'id': 'Course_grading_range'})
    grading = {}
    
    grading_range = []
    if grading_range_soup and grading_range_soup.parent.find_next_sibling().name == 'table':
        grading_range_soup = grading_range_soup.parent.find_next_sibling()
        grading_range = parse_table(grading_range_soup)
    grading['Course grading range'] = grading_range
    
    grading_breakdown_soup = soup.find('span', {'id': 'Course_activities_and_grading_breakdown'})
    grading_breakdown = []
    if grading_breakdown_soup and grading_breakdown_soup.parent.find_next_sibling().name == 'table':
        grading_breakdown_soup = grading_breakdown_soup.parent.find_next_sibling()
        grading_breakdown = parse_table(grading_breakdown_soup)
    grading['Course activities and grading breakdown'] = grading_breakdown
    
    grading_reccomendations_soup = soup.find('span', {'id': 'Recommendations_for_students_on_how_to_succeed_in_the_course'})
    grading_reccomendations = []
    if grading_reccomendations_soup:
        grading_reccomendations_soup = grading_reccomendations_soup.parent.find_next_sibling()
        while grading_reccomendations_soup.name == 'p':
            grading_reccomendations.append(grading_reccomendations_soup.text.strip())
            grading_reccomendations_soup = grading_reccomendations_soup.find_next_sibling()
    grading['Recommendations_for_students_on_how_to_succeed_in_the_course'] = grading_reccomendations
    
    return grading


def parse_single_resource(soup: BeautifulSoup, _id: str) -> list:
    resource_soup = soup.find('span', {'id': _id})
    resource = []
    
    if resource_soup:
        resource_soup = resource_soup.parent.find_next_sibling()
        if resource_soup and resource_soup.name == 'ul':
            for li in resource_soup.find_all('li'):
                resource.append(li.text)
    return resource
    
    
def parse_resources(soup: BeautifulSoup) -> dict:
    resources_soup = soup.find('span', {'id': 'Resources,_literature_and_reference_materials'})
    resources = {}
    
    resources['Open access resources'] = parse_single_resource(soup, 'Open_access_resources')
    resources['Closed access resources'] = parse_single_resource(soup, 'Closed_access_resources')
    resources['Software and tools used within the course'] = parse_single_resource(soup, 'Software_and_tools_used_within_the_course')
    return resources


def parse_activities_and_teaching_methods(soup: BeautifulSoup) -> list:
    activities_soup = soup.find('span', {'id': 'Activities_and_Teaching_Methods'})
    activities = []
    
    if activities_soup:
        activities_soup = activities_soup.parent.find_next_sibling()
        activities = parse_table(activities_soup)
    return activities


def parse_activities_within_section(soup: BeautifulSoup) -> dict:
    '''
    Don't use it please
    Absolute mess
    '''
    activities_section_soup = soup.find('span', {'id': 'Formative_Assessment_and_Course_Activities'})
    activities_section = {}
    
    if activities_section_soup:
        # Find ongoing performance assessment
        ongoing_performance_soup = soup.find('span', {'id': 'Ongoing_performance_assessment'})
        if ongoing_performance_soup:
            ongoing_performance_soup = ongoing_performance_soup.parent.find_next_sibling()
            ongoing_performance = {}
            while ongoing_performance_soup.name in ['h4', 'p'] and ongoing_performance_soup.find_next_sibling().name == 'table':
                section_name = ongoing_performance_soup.text.strip()
                ongoing_performance_soup = ongoing_performance_soup.find_next_sibling()
                ongoing_performance[section_name] = parse_table(ongoing_performance_soup)
                ongoing_performance_soup = ongoing_performance_soup.find_next_sibling()
            activities_section['Ongoing performance assessment'] = ongoing_performance

        # Find final assessment
        final_assessment_soup = soup.find('span', {'id': 'Final_assessment'})
        if final_assessment_soup:
            final_assessment_soup = final_assessment_soup.parent.find_next_sibling()
            final_assessment = {}
            #print(final_assessment_soup.name)
            #print(final_assessment_soup.find_next_sibling().name)
            while final_assessment_soup.name in ['h4', 'p'] and final_assessment_soup.find_next_sibling().name in ['ol', 'ul']:
                #print(final_assessment_soup.name)
                #print(final_assessment_soup.find_next_sibling().name)
                section_name = final_assessment_soup.text.strip()
                final_assessment_soup = final_assessment_soup.find_next_sibling()
                final_assessment[section_name] = parse_list(final_assessment_soup)
                final_assessment_soup = final_assessment_soup.find_next_sibling()
            activities_section['Final assessment'] = final_assessment
    return activities_section
    
def parse_syllabus(url: str) -> dict:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    if len(soup.title.text.split(":")) == 1:
        title = soup.title.text.split(":")[0].split("-")[0].strip()
    else: 
        title = soup.title.text.split(":")[1].split("-")[0].strip()
    parsed_data = {"Title": title}

    # Find Short Description
    short_description = soup.find('span', {'id': 'Short_Description'})
    if short_description is None:
        short_description = soup.find('span', {'id': 'Course_outline'})
        
    if short_description:
        short_description = short_description.parent.find_next_sibling('p').text.strip()
    parsed_data["Short Description"] = short_description

    # Find Prerequisites
    parsed_data["Prerequisites"] = parse_prerequisites(soup)
    
    # Find Course Topics
    parsed_data["Course Topics"] = parse_course_topics(soup)
    
    # Find ILO(Intended learning outcomes)
    parsed_data["Intended Learning Outcomes (ILOs)"] = parse_ilo(soup)
    
    # Find Grading data
    parsed_data["Grading"] = parse_grading(soup)
    
    # Find Resources
    parsed_data["Resources, literature and reference materials"] = parse_resources(soup)
    
    # Find acrivities
    parsed_data["Activities and Teaching Methods"] = parse_activities_and_teaching_methods(soup)
    
    # Activities within each section
    parsed_data["Formative Assessment and Course Activities"] = parse_activities_within_section(soup)
    return parsed_data


def main() -> None:
    args = get_args()
    parsed_data = parse_syllabus(args.url)
    
    with open(str(args.output_path), "w", encoding="UTF-8") as f:
        json.dump(parsed_data, f, indent=2, ensure_ascii=False)



if __name__ == "__main__":
    main()
