# Chicago Car Crashes

## Table of Contents
1. [Chicago Car Crashes Predictions With Logistic Regression & Decision Trees](#chicago-car-crashes-predictions-with-logistic-regression--decision-trees)
2. [Author](#author-maureen-wanjeri-august-2024)
3. [Overview](#overview)
4. [Business Problem](#business-problem)
5. [Data Understanding](#data-understanding)
   - [Datasets](#datasets)
   - [Key Steps in Data Understanding](#key-steps-in-data-understanding)
6. [Data Preparation](#data-preparation)
7. [Modeling](#modeling)
   - [Baseline Model](#baseline-model)
   - [Baseline Decision Tree Model Accuracy](#baseline-decision-tree-model-accuracy)
8. [Results](#results)
   - [Visualizations](#visualizations)
9. [Conclusion](#conclusion)
10. [Recommendations](#recommendations)
11. [Possible Next Steps](#possible-next-steps)
12. [For More Information](#for-more-information)
13. [Structure of Repository](#structure-of-repository)

## Chicago Car Crashes Predictions With Decision Tress

### Author: Maureen Wanjeri, August 2024

## Overview
![Sunset view of the Chicago Skyway tollbooths at the entrance to the Chicago southbound city limits](readme_images/640px-ChicagoSkyway1104.jpg) <br />

This project aims to build a machine learning classifier to predict the primary contributory cause of car accidents in Chicago, using data on vehicle details, road conditions, and information about the people involved in the accidents. By analyzing various factors, the model provides insights that can help the Vehicle Safety Board and the City of Chicago identify key patterns and implement targeted interventions to reduce traffic accidents and improve road safety. This multi-class classification problem requires careful handling of imbalanced data and feature engineering to ensure accurate and actionable predictions.

**Key Stakeholders**
Vehicle Safety Board: Interested in identifying and mitigating the most common causes of traffic accidents to improve vehicle and road safety.

City of Chicago: Seeks to reduce the number of traffic accidents and improve public safety through data-driven decision-making and targeted interventions.





## Business Problem

![Police process the fatal crash Wednesday at 87th Street and Cottage Grove Avenue in Chicago that sent drivers and passengers in other vehicles to hospitals. Terrence Antonio James/Chicago Tribune/TNS/Getty Images](readme_images/221124014742-01-chicago-crash-112322-restricted.jpg)

The City of Chicago faces a persistent challenge with traffic accidents, which result in numerous injuries, fatalities, and financial losses each year. The complexity of these incidents, driven by a wide array of factors including road conditions, vehicle characteristics, and human behavior, makes it difficult for authorities to accurately identify the root causes and implement effective prevention strategies. This project seeks to address this issue by developing a machine learning model that can predict the primary contributory cause of car accidents. By analyzing detailed data on the vehicles involved, the people in the cars, and the environmental conditions at the time of the accidents, the model aims to uncover patterns and insights that can inform policy decisions. The ultimate goal is to equip the Vehicle Safety Board and City of Chicago officials with actionable information to reduce the occurrence and severity of traffic accidents, enhancing public safety and optimizing resource allocation for traffic management and accident prevention initiatives.


## Data Understanding
The project uses the following datasets:

- [Traffic Crashes - Crashes](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if)
- [Traffic Crashes - People](https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d)
- [Traffic Crashes - Vehicles](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3)

The data used in this project was sourced from the City of Chicago's public data portal. It includes three primary datasets:

-Traffic Crashes - Crashes: Contains detailed information on crash incidents, including location, time, and severity.
-Traffic Crashes - People: Provides information about the individuals involved in each crash, including their role (driver, passenger, etc.), age, and injury status.
-Traffic Crashes - Vehicles: Includes details about the vehicles involved in each crash, such as type, make, model, and vehicle defects.

**Key Steps in Data Understanding**

Initial Exploration: Reviewed the datasets to understand the structure, key variables, and relationships between the datasets.

Data Cleaning: Addressed missing values and data inconsistencies, and merged the datasets to create a unified dataset for modeling.

Feature Selection: Identified key features that are most likely to impact the primary contributory cause of accidents.

![image](https://github.com/user-attachments/assets/a43ab4cb-120e-4084-a06c-a7342c7ba68a)
![image](https://github.com/user-attachments/assets/22f7fa23-ce8f-4bdd-bc1d-af8b7b298e0d)
![image](https://github.com/user-attachments/assets/c976fadd-0a41-4f47-bd2f-31851d3a13d1)
![image](https://github.com/user-attachments/assets/b9981a3c-5e06-4a90-a659-66cfadb0ee5b)
![image](https://github.com/user-attachments/assets/582cecc9-81b1-4a61-8c9c-8813aecb254a)
![image](https://github.com/user-attachments/assets/8b4120ce-2f5c-405e-adee-00b39d5a63b3)
![image](https://github.com/user-attachments/assets/4ae5a24c-08ee-4027-abb5-914fd4a5e870)
![image](https://github.com/user-attachments/assets/8f33ea68-3135-48b1-9796-0205bf6b9109)
![image](https://github.com/user-attachments/assets/d4f3e4a2-8aee-4bb5-8884-59b6d3007d77)
![image](https://github.com/user-attachments/assets/703c9a65-6538-4692-8e11-d0605f4d8f3b)
![image](https://github.com/user-attachments/assets/8ef2b8fb-3872-49c2-95f0-1ba542161088)
![image](https://github.com/user-attachments/assets/71e7209a-603b-4322-8b87-ef69b9bf9ed2)
![image](https://github.com/user-attachments/assets/94c45ac2-2c13-4113-a2d4-de44f7b1abea)
![image](https://github.com/user-attachments/assets/e4fc8f17-5adb-4210-82ed-3cab774db5ac)
![image](https://github.com/user-attachments/assets/d201644c-dd4b-497a-b729-a22c88274d73)
![image](https://github.com/user-attachments/assets/b1212926-da90-4863-b147-56834a734de8)
![image](https://github.com/user-attachments/assets/59fc4293-77b0-4c82-8028-9f6924162418)
![image](https://github.com/user-attachments/assets/af711a01-53d0-40b9-bc2a-0f70bec3ef40)


 
## Data Preparation

During data preparation, the following steps were taken:

-Handling Missing Values: Missing values were addressed using imputation methods, or the columns were dropped if deemed irrelevant to the analysis.

-Feature Engineering: New features were created based on domain knowledge, such as interaction terms between key variables like speed limit and vehicle type.

-Feature Encoding: Categorical variables were converted into numerical format using one-hot encoding.

-Feature Scaling: Numerical features were standardized to ensure they contribute equally to the model's predictions.

-Data Splitting: The data was split into training and testing sets to evaluate model performance.

![image](https://github.com/user-attachments/assets/a1415fc7-b09e-4cd9-88d6-df03634f1c67)



## Modeling

Developed a basic model using a Decision Tree to predict the main cause of car accidents in Chicago.
Model Performance:
Prediction Accuracy: The model was able to accurately predict most cases where there was no indication of injury, as seen in the confusion matrix.
Model Quality: The ROC curve, which measures the model’s ability to differentiate between classes, showed a strong performance with a score of 0.91.
Challenges Encountered
Memory Constraints:
While trying to improve the model and test other types like Logistic Regression, we faced significant memory limitations.
These limitations meant we couldn't run more complex models or tune the existing model further.
Impact on Project:
Due to these technical challenges, we were only able to present results from the baseline Decision Tree model without further refinements or additional models.
Conclusion
Despite the challenges, the baseline Decision Tree model provided valuable insights, but further work is needed with more robust resources to refine and expand the analysis.

![image](https://github.com/user-attachments/assets/3ce3e493-3f89-4f32-927f-f82154dab520)
![image](https://github.com/user-attachments/assets/9595bd6c-ebcb-490d-96d0-15b435bf60dc)

## Results

The final model achieved an accuracy of 95% on the test set, indicating a strong performance in predicting the primary contributory cause of car accidents. The tuned Decision Tree model showed improvements over the baseline, particularly in precision and recall for most of the classes.

**Visualizations**

Confusion Matrix: A confusion matrix was created to visualize the model’s performance across different classes.

ROC Curves: ROC curves and AUC scores were plotted to evaluate the model’s performance in distinguishing between different classes.


### Conclusion
The Decision Tree model, after hyperparameter tuning, provided a robust classifier capable of predicting the primary contributory cause of car accidents with high accuracy. The insights from this model can help the Vehicle Safety Board and the City of Chicago identify key risk factors and implement targeted safety measures.

### Recommendations
Enhanced Road Safety Programs: Focus on the most common causes identified by the model, such as driving at excessive speeds or in poor weather conditions.

Targeted Interventions: Deploy more traffic control measures in areas identified as high-risk by the model.

Public Awareness Campaigns: Increase public awareness around the major contributory factors to accidents, as predicted by the model.

### Possible Next Steps
Model Refinement: Explore more advanced ensemble techniques, like Random Forest or Gradient Boosting, to potentially improve model performance.

Real-Time Prediction: Develop an application that provides real-time predictions based on live data from traffic sensors and weather stations.

Integration with Policy Making: Work closely with city officials to integrate the model’s predictions into the decision-making process for urban planning and traffic management.


## For More Information

Detailed documentation of the data, methodologies, and code used in this project is available upon request.

## Repository Structure
```bash
Project-Ph3-Chicago-Car-Crashes-Prediction-main/
├── notebooks/
│   └── main_index.ipynb       # Main Jupyter Notebook with code and analysis
├── readme_images/             # Images used in the README.md
├── visuals/                   # Visualizations generated during the analysis
├── Non_technical_Presentation/ # Folder containing slides or presentations for a non-technical audience
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation (this file)
