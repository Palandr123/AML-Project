import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import os

from syllabus_generator import generate_syllabus

os.environ["HF_TOKEN"] = st.secrets["HF_TOKEN"]


st.set_page_config(page_title="AML Project", page_icon="🧊")

st.markdown(
    """
# AML Project Syllabus generation

Need assistance in filling syllabus sections? Try LLM-powered Syllabus Generator!

To generate your syllabus:
  1. Choose model for generation
  2. Enter course title and short course description
  3. Choose what part of syllabus you want to generate
  4. Click `Generate!` below and copy you result as json!
"""
)


# -- Models to use:
model_list = ["gemma-2b-it", "gemma-2b-it-finetuned", "gemma-7b-it"]
# Title the app
# st.title('Syllabus generation')

st.sidebar.markdown("## Select Model and what to generate")

# -- Set time by GPS or event
select_model = st.sidebar.selectbox("Choose the model", model_list)

# -- Course info
course_title = st.sidebar.text_input(
    "Course title",
    # placeholder="Advanced Machine Learning"
)
course_description = st.sidebar.text_area(
    "Course description:",
    # placeholder="Course covers advanced topics in ML such as advanced types of GANs, bayesian inference, modern LLM and their quantization and finetuning, etc.",
)

# -- What to generate
titles_list = ["Course topics", "ILO", "Final Assessment"]
field_to_generate = st.sidebar.selectbox("What to generate", titles_list)

show_full_course_titles = st.sidebar.checkbox("Show full course names")
course_names = [
    "Introduction to Programming I",
    "Introduction to Programming II",
    "Theoretical Computer Science",
    "Operating Systems",
    "Databases",
]
course_codes = ["CSE101", "CSE102", "CSE103", "CSE105", "CSE106"]

if show_full_course_titles:
    course_list = [f"{code}: {name}" for code, name in zip(course_codes, course_names)]
else:
    course_list = course_codes
prerequisites = st.sidebar.multiselect("Prerequisites", course_list)


generated_id = 1


if "generated_syllabuses" not in st.session_state:
    st.session_state["generated_syllabuses"] = []


def generate():
    generated_data = generate_syllabus(
        select_model,
        field_to_generate,
        course_title,
        course_description,
    )

    idx = (
        1
        if st.session_state["generated_syllabuses"] == []
        else st.session_state["generated_syllabuses"][-1][0] + 1
    )

    st.session_state["generated_syllabuses"].append((idx, generated_data))
    if len(st.session_state["generated_syllabuses"]) > 5:
        st.session_state["generated_syllabuses"] = st.session_state[
            "generated_syllabuses"
        ][-5:]


st.button("`Generate!`", on_click=generate)

st.subheader("Last 5 generated syllabuses")
for idx, json_data in st.session_state["generated_syllabuses"]:
    st.write(f"Syllabus #{idx}")
    st.json(json_data)
