import streamlit as st
import pandas as pd
import os

# Load Data
try:
    food_data = {
        "Type 1 Diabetes": pd.read_excel("Type1_Diabetes_Weekly_Food_Chart.xlsx"),
        "Type 2 Diabetes": pd.read_excel("Type2_Diabetes_Weekly_Food_Chart.xlsx"),
        "Prediabetes": pd.read_excel("Prediabetic_Weekly_Food_Chart.xlsx"),
        "Gestational Diabetes": pd.read_excel("Gestational_Diabetes_Weekly_Food_Chart.xlsx")
    }
    exercise_df = pd.read_excel("Exercise_Recommendation.xlsx")
except FileNotFoundError:
    st.error("❌ Required Excel files not found.")
    st.stop()

# Helper functions
def match_interval(value, intervals):
    for interval in intervals:
        if interval.endswith('+') and value >= int(interval.rstrip('+')):
            return interval
        try:
            start, end = map(int, interval.split('-'))
            if start <= value <= end:
                return interval
        except:
            continue
    return None

def get_food_chart(age, weight, dtype):
    df = food_data[dtype]
    ai = match_interval(age, df["Age Interval"].unique())
    wi = match_interval(weight, df["Weight Interval"].unique())
    return df[(df["Age Interval"] == ai) & (df["Weight Interval"] == wi)] if ai and wi else pd.DataFrame()

def get_exercise_chart(age, weight, dtype):
    ai = match_interval(age, exercise_df["Age Interval"].unique())
    wi = match_interval(weight, exercise_df["Weight Interval"].unique())
    mapped_type = {
        "Type 1 Diabetes": "Type 1",
        "Type 2 Diabetes": "Type 2",
        "Prediabetes": "Prediabetes",
        "Gestational Diabetes": "Gestational"
    }.get(dtype, dtype)
    if ai and wi:
        df_filtered = exercise_df[
            (exercise_df["Age Interval"].str.strip() == ai) &
            (exercise_df["Weight Interval"].str.strip() == wi) &
            (exercise_df["Diabetes Type"].str.strip().str.lower() == mapped_type.strip().lower())
        ]
        return df_filtered
    return pd.DataFrame()

# Streamlit Configuration
st.set_page_config(page_title="Personalized Food & Exercise Recommendation for Diabetics Management", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .title-bar {
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            padding: 2rem;
            border-radius: 10px;
            color: white;
            text-align: center;
        }
        .section-header {
            background-color: #e8f5e9;
            padding: 10px;
            border-radius: 8px;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .recommendation-box {
            background-color: #ffffff;
            border-left: 6px solid #388e3c;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 8px;
        }
        .footer {
            margin-top: 40px;
            padding: 10px;
            text-align: center;
            font-size: 13px;
            color: #888;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="title-bar">
    <h1> Personalized Food & Exercise Recommendation for Diabetics Management</h1>
    <p><em>Powering Health Through Personalized Food & Exercise Insights</em></p>
</div>
""", unsafe_allow_html=True)

# Navigation
menu = st.sidebar.radio(" Navigation", ["Home", "Services"])

# HOME PAGE
if menu == "Home":
    st.markdown('<div class="section-header"><h4>📚 About Diabetes</h4></div>', unsafe_allow_html=True)
    st.markdown("""
    **What is Diabetes?**  
    Diabetes is a long term medical condition that occurs when the body That cannot properly manage blood sugar (glucose) levels.
    Glucose is an essential source of energy, but it needs insulin and hormone produced by the pancreas to enter into the cells. 
    In people with diabetes, either the body does not make enough insulin or it can not use insulin effectively, 
    leading to high levels of sugar in the blood.

    ---

    ### 🔍 Types of Diabetes

    #### 1. Type 1 Diabetes
    - **Definition:** Type 1 diabetes is an autoimmune condition where the body’s immune system mistakenly attacks and 
    destroys the insulin producing cells in the pancreas. As a result of this , the body makes little to no insulin.

    - **Cause:** It is primarily caused by genetic factors and environmental triggers like viral infections. 
        It often develops in children and young adults, though it can occur at any age.
    - **Symptoms:** Common symptoms include frequent urination, increased thirst, unexplained weight loss, fatigue, and blurred vision.
    - **Remedies:** Type 1 diabetes cannot be cured, but it can be managed through daily insulin injections, 
       a healthy diet, regular physical activity, and continuous blood sugar monitoring.

    #### 2. Type 2 Diabetes
    - **Definition:** Type 2 diabetes occurs when the body becomes resistant to insulin or when the pancreas does not produce enough insulin. 
        It is the most common form of diabetes.
    - **Cause:** It is often linked to poor lifestyle habits such as unhealthy eating, physical inactivity, obesity, and genetics. 
        It mostly affects adults but is increasingly seen in children.
    - **Symptoms:** Symptoms develop slowly and include fatigue, frequent urination, excessive thirst, slow wound healing, and tingling in hands or feet.
    - **Remedies:** Management includes lifestyle changes like a balanced diet, exercise, weight loss, and medications or insulin therapy if needed.

    #### 3. Prediabetes
    - **Definition:** Prediabetes is a condition where blood sugar levels are higher than normal but not high enough to be diagnosed as type 2 diabetes. 
        It acts as a warning sign.
    - **Cause:** It is caused by insulin resistance due to excess weight, poor eating habits, sedentary lifestyle, and genetic factors.
    - **Symptoms:** Most people with prediabetes show no symptoms. In some cases, they may feel slightly more tired or thirsty than usual.
    - **Remedies:** Prediabetes can often be reversed through healthy eating, increased physical activity, weight management, and regular screening.

    #### 4. Gestational Diabetes
    - **Definition:** Gestational diabetes occurs during pregnancy when hormonal changes make the body less responsive to insulin.
    It usually disappears after childbirth but increases the risk of developing type 2 diabetes later.

    - **Cause:** It’s primarily caused by pregnancy-related hormonal shifts that impair insulin action. 
        Risk increases if the woman is overweight or has a family history of diabetes.
    - **Symptoms:** Most women show no noticeable symptoms. It’s usually detected through routine blood sugar tests during pregnancy.
    - **Remedies:** It can be managed through a specially planned diet, regular moderate exercise, and monitoring blood sugar levels.
        In some cases, insulin or medication may be required.
    ---

    🔎 **Data Sources:** Google, ChatGPT, Perplexity, DeepSeek, YouTube  
    """)

# SERVICES PAGE
if menu == "Services":
    st.markdown('<div class="section-header"><h4>📋 Enter Patient Details</h4></div>', unsafe_allow_html=True)

    name = st.text_input("👤 Name")
    age = st.number_input("🎂 Age", min_value=1, max_value=120, value=30, step=1)
    gender = st.selectbox("⚧️ Gender", ["Male", "Female", "Other"])
    weight = st.number_input("⚖️ Weight (kg)", min_value=10, max_value=200, value=60, step=1)
    dtype = st.selectbox("💉 Type of Diabetes", list(food_data.keys()))
    rec_type = st.radio("🔎 Show Recommendations for", ["Food", "Exercise", "Both"])

    if st.button("Get Recommendations"):
        if rec_type in ["Food", "Both"]:
            st.markdown('<div class="section-header"><h4>🥗 Food Recommendations</h4></div>', unsafe_allow_html=True)
            fdf = get_food_chart(age, weight, dtype)
            if not fdf.empty:
                for day in fdf['Day'].unique():
                    day_df = fdf[fdf['Day'] == day]
                    st.markdown(f"### 📅 {day}")
                    for _, row in day_df.iterrows():
                        st.markdown(f'<div class="recommendation-box"><strong>{row["Meal"]}</strong>: {row["Food Recommendation"]}</div>', unsafe_allow_html=True)
                st.success(f"💧 Daily Water Intake: {fdf['Water Intake'].iloc[0]} ml")
            else:
                st.warning("⚠️ No food recommendation found for the input combination.")

        if rec_type in ["Exercise", "Both"]:
            st.markdown('<div class="section-header"><h4>🏃 Exercise Recommendations</h4></div>', unsafe_allow_html=True)
            edf = get_exercise_chart(age, weight, dtype)
            if not edf.empty:
                for _, row in edf.iterrows():
                    st.markdown(f'<div class="recommendation-box"><strong>{row["Category"]}</strong>: {row["Exercise"]}</div>', unsafe_allow_html=True)
                    if pd.notna(row['YouTube Link']) and row['YouTube Link'].startswith("http"):
                        st.video(row['YouTube Link'])
            else:
                st.warning("⚠️ No exercise recommendation found for the input combination.")

# Footer
st.markdown('<div class="footer">© 2025 Diabetes Assistant | Built by SHIVA GOUD KOPPULA</div>', unsafe_allow_html=True)
