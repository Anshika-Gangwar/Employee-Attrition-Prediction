import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="📊",
    layout="centered"
)

# Load the Model
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"

model = joblib.load(MODEL_PATH)

# Title
st.title("👨‍💼 Employee Attrition Predictor")

st.caption(
    "Estimate the likelihood of an employee leaving the company using a trained Machine Learning model."
)

st.divider()

#Sidebar
st.sidebar.title("About")

st.sidebar.info("""This application predicts employee attrition using a Random Forest model trained on the IBM HR Analytics dataset.""")

# Personal Information
st.header("👤 Personal Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=30,
        help="Employee's age"
    )

    gender = st.radio(
        "Gender",
        ["Male", "Female"],
        horizontal=True
    )

    marital_status = st.radio(
        "Marital Status",
        ["Single", "Married", "Divorced"],
        horizontal=True
    )

with col2:

    education = st.selectbox(
        "Education",
        [
            "1 - Below College",
            "2 - College",
            "3 - Bachelor",
            "4 - Master",
            "5 - Doctor"
        ]
    )

    education = int(education[0])

    education_field = st.selectbox(
        "Education Field",
        [
            "Life Sciences",
            "Medical",
            "Marketing",
            "Technical Degree",
            "Human Resources",
            "Other"
        ]
    )

st.divider()

# Job Information
st.header("💼 Job Information")

col1, col2 = st.columns(2)

with col1:

    department = st.selectbox(
        "Department",
        [
            "Sales",
            "Research & Development",
            "Human Resources"
        ]
    )

    job_role = st.selectbox(
        "Job Role",
        [
            "Sales Executive",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Sales Representative",
            "Research Director",
            "Human Resources"
        ]
    )

    job_level = st.select_slider(
        "Job Level",
        options=[1,2,3,4,5]
    )

    travel_option = st.radio(
        "Business Travel",
        [
            "Rarely",
            "Frequently",
            "No Travel"
        ],
        horizontal=True
    )

    travel_mapping = {
        "Rarely":"Travel_Rarely",
        "Frequently":"Travel_Frequently",
        "No Travel":"Non-Travel"
    }

    business_travel = travel_mapping[travel_option]

with col2:

    overtime = st.radio(
        "Over Time",
        ["Yes","No"],
        horizontal=True
    )

st.divider()

# Salary Information
st.header("💰 Salary Information")

col1, col2 = st.columns(2)

with col1:

    monthly_income = st.number_input(
        "Monthly Income",
        1000,
        20000,
        5000
    )

    daily_rate = st.number_input(
        "Daily Rate",
        100,
        1500,
        800
    )

    hourly_rate = st.number_input(
        "Hourly Rate",
        30,
        100,
        60
    )

with col2:

    monthly_rate = st.number_input(
        "Monthly Rate",
        2000,
        30000,
        15000
    )

    percent_salary_hike = st.slider(
        "Salary Hike (%)",
        10,
        25,
        15
    )

    stock_option_level = st.radio(
        "Stock Option",
        [0,1,2,3],
        horizontal=True
    )

st.divider()

# Experience
st.header("📈 Experience")

col1, col2 = st.columns(2)

with col1:

    total_working_years = st.number_input(
        "Total Working Years",
        0,
        40,
        10
    )

    years_at_company = st.number_input(
        "Years At Company",
        0,
        40,
        5
    )

    years_in_current_role = st.number_input(
        "Years In Current Role",
        0,
        20,
        3
    )

    distance_from_home = st.number_input(
        "Distance From Home (km)",
        1,
        30,
        5,
        help="Distance between home and workplace"
    )

with col2:

    years_since_last_promotion = st.number_input(
        "Years Since Last Promotion",
        0,
        15,
        1
    )

    years_with_curr_manager = st.number_input(
        "Years With Current Manager",
        0,
        20,
        3
    )

    num_companies_worked = st.number_input(
        "Companies Worked",
        0,
        10,
        2
    )

    training_times_last_year = st.number_input(
        "Training Last Year",
        0,
        10,
        3
    )

    performance_rating = st.radio(
        "Performance Rating",
        [1,2,3,4,5],
        horizontal=True
    )

st.divider()

# Employee Rating
st.header("⭐ Employee Ratings")

col1, col2 = st.columns(2)

with col1:

    job_involvement = st.slider(
        "Job Involvement",
        1,4,3
    )

    job_satisfaction = st.slider(
        "Job Satisfaction",
        1,4,3
    )

    environment_satisfaction = st.slider(
        "Environment Satisfaction",
        1,4,3
    )

with col2:

    relationship_satisfaction = st.slider(
        "Relationship Satisfaction",
        1,4,3
    )

    work_life_balance = st.slider(
        "Work-Life Balance",
        1,4,3
    )

st.divider()

# Predict
if st.button( 
     "🔍 Predict Attrition",
    use_container_width=True
    ):

    input_df = pd.DataFrame({
        "Age": [age],
        "BusinessTravel": [business_travel],
        "DailyRate": [daily_rate],
        "Department": [department],
        "DistanceFromHome": [distance_from_home],
        "Education": [education],
        "EducationField": [education_field],
        "EnvironmentSatisfaction": [environment_satisfaction],
        "Gender": [gender],
        "HourlyRate": [hourly_rate],
        "JobInvolvement": [job_involvement],
        "JobLevel": [job_level],
        "JobRole": [job_role],
        "JobSatisfaction": [job_satisfaction],
        "MaritalStatus": [marital_status],
        "MonthlyIncome": [monthly_income],
        "MonthlyRate": [monthly_rate],
        "NumCompaniesWorked": [num_companies_worked],
        "OverTime": [overtime],
        "PercentSalaryHike": [percent_salary_hike],
        "PerformanceRating": [performance_rating],
        "RelationshipSatisfaction": [relationship_satisfaction],
        "StockOptionLevel": [stock_option_level],
        "TotalWorkingYears": [total_working_years],
        "TrainingTimesLastYear": [training_times_last_year],
        "WorkLifeBalance": [work_life_balance],
        "YearsAtCompany": [years_at_company],
        "YearsInCurrentRole": [years_in_current_role],
        "YearsSinceLastPromotion": [years_since_last_promotion],
        "YearsWithCurrManager": [years_with_curr_manager]
    })  

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Employee is likely to leave the company.")
    else:
        st.success("✅ Employee is likely to stay with the company.")

    st.subheader("Prediction Confidence")

    c1, c2 = st.columns(2)

    c1.metric("Stay Probability", f"{probability[0]*100:.1f}%")
    c2.metric("Leave Probability", f"{probability[1]*100:.1f}%")

    with st.expander("View Input Data"):
        st.dataframe(input_df)