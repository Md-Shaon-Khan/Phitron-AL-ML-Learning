# ------ Personal Resume App (Advanced with placeholders) ------
import streamlit as st
import pandas as pd

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["About", "Skills", "Experience", "Education", "Contact"])

# Data for skills
skills = {
    "Python": 0.9,
    "Machine Learning": 0.85,
    "Data Visualization": 0.8,
    "SQL": 0.75,
    "Big Data": 0.6,
}

# Header with name and title
st.title("?anyname")
st.subheader("Data Scientist")

if section == "About":
    st.markdown(f"""
    Experienced data scientist with strong skills in analytics, machine learning, and storytelling with data.
    Passionate about turning data into actionable insights.
    """)

elif section == "Skills":
    st.header("Skills Overview")
    for skill, level in skills.items():
        st.write(f"{skill}")
        st.progress(level)
    df_skills = pd.DataFrame({
        "Skill": list(skills.keys()),
        "Proficiency": list(skills.values())
    })
    st.bar_chart(df_skills.set_index("Skill"))

elif section == "Experience":
    st.header("Work Experience")

    with st.expander(f"Data Scientist | ?anycompanyname | Jan 2021 - Present"):
        st.write(f"""
        - Developed predictive models that increased sales by 15%.
        - Automated data pipelines saving 10+ hours/week.
        - Collaborated with cross-functional teams to deploy ML models in production.
        """)

    with st.expander(f"Data Analyst | ?anycompanyname | Jun 2018 - Dec 2020"):
        st.write(f"""
        - Created dashboards that improved decision-making.
        - Analyzed customer data to improve retention by 12%.
        """)

elif section == "Education":
    st.header("Education")
    st.write(f"**M.S. in Data Science** — University of Data, 2020")
    st.write(f"**B.S. in Computer Science** — Tech University, 2017")

elif section == "Contact":
    st.header("Get in Touch")
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Email")
        phone = st.text_input("Phone")
    with col2:
        linkedin = st.text_input("LinkedIn URL")
        portfolio = st.text_input("Portfolio URL")

    message = st.text_area("Message")

    if st.button("Send"):
        st.success("Thanks for reaching out! I'll get back to you soon.")

# Save and refresh.
# ------ streamlit run