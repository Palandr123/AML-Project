import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(page_title='AML Project', page_icon="🧊")

st.markdown("""
# AML Project Syllabus generation

Below is the result of generated syllabus in json format
""")


# -- Models to use:
model_list = ['mistral-7b', 'gemma-2b']
# Title the app
# st.title('Syllabus generation')

st.sidebar.markdown("## Select Model and what to generate")

# -- Set time by GPS or event
select_model = st.sidebar.selectbox('Choose the model',
                                    model_list)

# -- What to generate
course_title = st.sidebar.text_input('Course title')

titles_list = ['Course topics', 'ILO', 'Grading']
titles = st.sidebar.multiselect('What to generate', titles_list)

show_full_course_titles = st.sidebar.checkbox('Show full course names')
course_names = ['Introduction to Programming I', 'Introduction to Programming II',
                'Theoretical Computer Science', 'Operating Systems', 'Databases']
course_codes = ['CSE101', 'CSE102', 'CSE103', 'CSE105', 'CSE106']

if show_full_course_titles:
    course_list = [f"{code}: {name}" for code, name in zip(course_codes, course_names)]
else:
    course_list = course_codes
prerequisites = st.sidebar.multiselect('Prerequisites', course_list)

course_description = st.sidebar.text_area('Course description:')

generated_id = 1


if 'generated_syllabuses' not in st.session_state:
    st.session_state['generated_syllabuses'] = []


def generate_syllabus():

    generated_data = {
        'foo': 'bar',
        'baz': 'boz',
        'stuff': [
            'stuff 1',
            'stuff 2',
            'stuff 3',
            'stuff 5',
        ],
    }
    if select_model == 'mistral-7b':
        # mistral-7b inference
        generated_data['Model'] = 'mistral-7b'
        pass
    elif select_model == 'gemma-2b':
        # gemma-2b inference
        generated_data['Model'] = 'gemma-2b'
        pass

    idx = 1 if st.session_state['generated_syllabuses'] == [] else st.session_state['generated_syllabuses'][-1][0] + 1

    st.session_state['generated_syllabuses'].append((idx, generated_data))
    if len(st.session_state['generated_syllabuses']) > 5:
        st.session_state['generated_syllabuses'] = st.session_state['generated_syllabuses'][-5:]


st.button('Generate!', on_click=generate_syllabus)

st.subheader('Last 5 generated syllabuses')
for idx, json_data in st.session_state['generated_syllabuses']:
    st.write(f"Syllabus #{idx}")
    st.json(json_data)


