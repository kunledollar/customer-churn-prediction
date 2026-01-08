# Customer Churn Prediction

## Overview
This project predicts customer churn (customer attrition) using supervised machine learning techniques.
It is an academic / capstone-style project focused on demonstrating an end-to-end applied ML workflow.

## Dataset
Telco Customer Churn dataset (public dataset).

## Project Structure
- data/: raw and processed data
- notebooks/: main analysis notebook
- src/: helper preprocessing and modeling functions

## Exploratory Data Analysis

### Customer Churn Distribution
![Customer Churn Distribution](https://raw.githubusercontent.com/kunledollar/customer-churn-prediction/main/images/churn_distribution.png)

### Tenure vs Churn
![Tenure vs Churn](https://raw.githubusercontent.com/kunledollar/customer-churn-prediction/main/images/tenure_vs_churn.png)


## Approach
- Data loading and cleaning
- Feature engineering
- Model training
- Model evaluation

## Models Used
- Logistic Regression

## Evaluation Metric
- ROC-AUC
  
## Results
- The Random Forest model outperformed the Logistic Regression baseline.
- ROC-AUC was used as the primary evaluation metric to handle class imbalance.
- Customer tenure emerged as a strong indicator of churn risk.

## Tools
Python, Pandas, NumPy, scikit-learn, Jupyter Notebook
