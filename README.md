# Project-6
Overview

This project focuses on analyzing retail sales data, performing data preprocessing, visualization, and building predictive models. It includes data cleaning, feature engineering, exploratory data analysis, and applying machine learning techniques to predict sales. The project uses Python libraries such as Pandas, Matplotlib, Seaborn, Prophet, and Scikit-learn.

Dataset

Files Used:

    Train Dataset (train.csv): Contains historical sales data for training models.

    Test Dataset (test.csv): Includes data for testing and prediction.

    Store Dataset (store.csv): Provides metadata about stores.

Key Features:

    Sales: Target variable representing sales revenue.

    Customers: Number of customers.

    Promo: Indicator for promotional campaigns.

    StateHoliday: Information about holidays.

    Date: Date of sales data.

CompetitionDistance: Distance to competitors.

Steps and Methodology

1. Data Loading and Exploration

     Loaded data using Pandas.

     Displayed basic statistics and data structure with .info() and .describe().

     Identified missing values using heatmaps.

2. Data Cleaning

     Mapped and filled missing values for categorical variables like StateHoliday.

     Handled missing numerical values with appropriate statistics (mean for distances, median for others).

     Addressed outliers using Interquartile Range (IQR) technique.

3. Data Visualization

     Visualized correlations and trends using:

     Heatmaps for null value distribution.

     Bar plots for categorical distributions.

     Time-series plots for trends in sales and customers.

4. Feature Engineering:

Added new features:

    Day_Name: Day of the week.

    Weekends: Indicator for weekends.

Aggregated features like average sales and customers by day.

5. Predictive Modeling

     Applied Scikit-learn and Prophet for predictive analysis.

   Models used include:

         Linear Regression

         Decision Tree Regressor

         Random Forest Regressor

         Performed hyperparameter tuning and cross-validation.

6. Machine Learning Pipeline

    Created a Scikit-learn pipeline with the following steps:

    Encoding: OrdinalEncoder for categorical variables.

    Scaling: StandardScaler for numerical features.

    Transformation: PowerTransformer for normalizing data.

    Modeling: RandomForestRegressor.

    Evaluated models using R-squared metrics.

7. Model Serialization

       Saved the final model pipeline using Python's Pickle module for deployment.

Results:

     Identified key features influencing sales such as promotional campaigns.

    Improved model accuracy by applying feature transformations.

     Created visualizations to highlight trends and patterns in sales data.

Dependencies

Python Libraries:
    pandas
    numpy
    matplotlib
    seaborn
    scikit-learn
    prophet 
    scipy 
    pickle

Acknowledgments:
     Developed using open-source libraries and resources.
