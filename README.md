# Capstone Project - Azure Machine Learning Engineer

This project is the classification problem using both hyperparameters HyperDrive and AutoML to get the best model and deploy the model. I will be using both hyperdrive and automl API from Azure to build this project. The datasetis about Titanic passenger survival possibility,where I get the data from Kaggle. The project involves the following step:
1. Choose a dataset (here is Titanic passenger survival possibility)
2. Import dataset into workspace
3. Train model using:
    - Automated ML
    - HyperDrive
4. Compare model the performance
5. Deploy the best model
6. Test model End point

## Dataset
The dataset is downloaded from Kaggle with link: https://www.kaggle.com/c/titanic/data
In this problem, we are asked to build a classification model that answers the question: "what sorts of people were more likely to survive?" using passenger data (ie name, age, gender, socio-economic class, etc).

### Overview
|Variable|	Definition|	Key|
|--------|------------|----|
|Survived|	Survival|	True/False|
|Pclass|	Ticket class|	1 = 1st, 2 = 2nd, 3 = 3rd|
|Sex|	Sex| Male, Female|	
|Age|	Age| in years| 20, 25, 40, ...|	
|SibSp|	number of siblings / spouses aboard the Titanic| 0, 1, 2, ...|	
|Parch|	number of parents / children aboard the Titanic	| 0, 1, 2, ...|
|Ticket|	Ticket number|A/5 21171, ...|
|Fare|	Passenger fare| 7.25|	
|Cabin|	Cabin number| C85, F42, ...|	
|Embarked|	Port of Embarkation|	C = Cherbourg, Q = Queenstown, S = Southampton|

### Task
I am going to build the classification model to predict the survival change of passenger based on above descrised characteristics.

### Access
- The dataset is first downloaded from Kaggle (link: https://www.kaggle.com/c/titanic/data)
- Next, dataset is uploaded to my github and then copy the link of raw data
- Read the dataset using Dataset.Tabular.from_delimited_files

## Automated ML
1. Setting the automl
- Experiment timeout minutes: 30 minnutes timeout
- Max concurrent iterations: 5 times
- Primary metric: accuracy

2. Automl config:
- Task: classification task
- Label column: Survived
- Featurization: auto feature engineer
- Debug log: automl_errors.log

### Results
1. Dataset registered in workspace

![image](https://github.com/user-attachments/assets/ca1b89fe-4e63-42b4-b088-1854e420b8d4)


2. Register the best model

The best model is Voting Ensemble. The best accuracy is 83.7%

![image](https://github.com/user-attachments/assets/3bc281bb-6c52-48c0-97be-57a7b886b390)



3. RunDetails

![image](https://github.com/user-attachments/assets/464e9c87-9530-4381-abac-a751dd2e6c74)


4. Best model

![image](https://github.com/user-attachments/assets/37cbd702-eb4c-4863-8c37-23bb8c85d895)






## Hyperparameter Tuning
I apply the logistics regression with 2 parameters:
- C: the regularization strenght. Input the random floating-point from 0.05 to 0.1.
- Max iteration: Select the random iteration of 16, 32, 64, 128 times.

### Results
The best run get the accuracy around 73% with the C value of 0.07 and the max inter of 64

![image](https://github.com/user-attachments/assets/a627c413-7b6f-4478-9298-6f8e073406c5)


RunDetails

![image](https://github.com/user-attachments/assets/fbe62ea8-cbc6-416c-ae84-5abbee67fa34)

Best run

![image](https://github.com/user-attachments/assets/78648762-0072-4144-8678-83373f86d0fb)



## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
