# Personalized Food-Exercise Recommendation for Diabetics Management
### By offering individualized diet and exercise suggestions based on age, weight, and type of diabetes, this app assists persons with diabetes in managing their health. Constructed using the Streamlit library, it provides a user-friendly, data-driven platform to help people make better lifestyle decisions and enhance their wellbeing.

## Project Overview

This project is a **Streamlit-based web application** designed to assist people with diabetes by providing personalized food and exercise recommendations based on their age, weight, and type of diabetes. The app also educates users about diabetes types, symptoms, causes, and management.

The application addresses a real-world healthcare challenge: **empowering diabetic patients with tailored lifestyle guidance** to better manage their condition and improve quality of life.

## Project Objective

* **Problem to solve:** Diabetes patients often struggle to find personalized dietary and exercise advice that matches their specific condition and body profile. This app bridges that gap by providing customized recommendations.

* **Domain:** Medical / Health Informatics

* **Key features:**

  * Personalized food recommendations per diabetes type, age, and weight.
  * Exercise recommendations with embedded demonstration videos.
  * Educational content about diabetes types and management.
  * User-friendly, interactive interface using Streamlit.

## User Interface Design (Mockups)

* The UI is divided into two main pages accessible via sidebar navigation:

  1. **Home:** Displays educational content about diabetes.
  2. **Services:** Input form for patient details and displays personalized recommendations.

* Inputs include:

  * Name, Age, Gender, Weight, Type of Diabetes
  * Choice between food, exercise, or both recommendations

* Output sections show:

  * Daily food plan organized by day and meal type.
  * Exercise suggestions with categories and embedded YouTube videos.

* Custom CSS is applied for a clean, accessible look with color-coded recommendation boxes and clear section headers.

*(Mockups were initially sketched in PowerPoint/hand-drawn and translated into Streamlit layout.)*


## Project Planning and Research

* Conducted research on diabetes management guidelines from reputable sources including Google Health, medical literature, and diabetes organizations.
* Collected and structured weekly food charts and exercise recommendation data for four diabetes types.
* Designed interval matching logic to map user age and weight to appropriate recommendations.
* Planned code structure for modularity and scalability.

## Implementation Details

* **Language & Framework:** Python 3, Streamlit for UI, pandas for data handling.
* **Data Sources:** Excel files containing curated food and exercise plans based on diabetes type, age, and weight intervals.
* **Key Components:**

  * Data loading and validation from Excel.
  * Interval matching function to select correct age and weight intervals.
  * Filtering recommendations by diabetes type.
  * Dynamic UI components for input and displaying results.
  * Embedded YouTube videos for exercise guidance.

## Challenges Faced and Solutions

* **Challenge:** Mapping continuous user inputs (age, weight) to discrete interval categories in datasets.

  * **Solution:** Developed a robust `match_interval()` function that accurately matches inputs to interval labels, including open-ended intervals like "60+".

* **Challenge:** Ensuring smooth UI experience with conditional content display.

  * **Solution:** Used Streamlit's reactive widgets and conditional rendering to show/hide content based on user selections.

* **Challenge:** Handling missing or unmatched data combinations gracefully.

  * **Solution:** Added user warnings when no recommendations are found for given inputs.

## How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/diabetes-management-app.git
   cd diabetes-management-app
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Place the required Excel files in the project root:

   * `Type1_Diabetes_Weekly_Food_Chart.xlsx`
   * `Type2_Diabetes_Weekly_Food_Chart.xlsx`
   * `Prediabetic_Weekly_Food_Chart.xlsx`
   * `Gestational_Diabetes_Weekly_Food_Chart.xlsx`
   * `Exercise_Recommendation.xlsx`
4. Run the app:

   ```bash
   streamlit run app.py
   ```
5. Access the app in your browser at `http://localhost:8501`

## Code Structure

```
app.py                            # Main Streamlit app
Type1_Diabetes_Weekly_Food_Chart.xlsx
Type2_Diabetes_Weekly_Food_Chart.xlsx
Prediabetic_Weekly_Food_Chart.xlsx
Gestational_Diabetes_Weekly_Food_Chart.xlsx
Exercise_Recommendation.xlsx
requirements.txt                 # Dependencies list
README.md                       # This documentation
```
## Future Work

* Add user profile and data persistence.
* Incorporate blood glucose tracking and integrate with real-time monitoring devices.
* Expand recommendation database with more granular food and exercise options.
* Implement AI-powered personalized meal and fitness plans.
* Multi-language support for wider accessibility.

## References

* Google Health
* Diabetes organizations and guidelines
* ChatGPT and DeepSeek for initial research and content generation
* YouTube videos for exercise demonstrations

## Presentation and Pitch

* Demonstrated the app’s ability to deliver tailored lifestyle advice based on patient input.
* Explained the problem, the technical approach, and the user-friendly interface.
* Highlighted challenges and how they were overcome.
* Discussed potential for future development and real-world impact.

## Contact

Developed by SHIVA GOUD KOPPULA
Email: shhivaagoudkoppula@gmail.com
GitHub: 
LinkedIn: (https://linkedin.com/in/shhivaa-koppula)
