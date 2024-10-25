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
|survival|	Survival|	0 = No, 1 = Yes|
|pclass|	Ticket class|	1 = 1st, 2 = 2nd, 3 = 3rd|
|sex|	Sex| Male, Female|	
|Age|	Age| in years| 20, 25, 40, ...|	
|sibsp|	number of siblings / spouses aboard the Titanic| 0, 1, 2, ...|	
|parch|	number of parents / children aboard the Titanic	| 0, 1, 2, ...|
|ticket|	Ticket number|A/5 21171, ...|
|fare|	Passenger fare| 7.25|	
|cabin|	Cabin number| C85, F42, ...|	
|embarked|	Port of Embarkation|	C = Cherbourg, Q = Queenstown, S = Southampton|

### Task
I am going to build the classification model to predict the survival change of passenger based on above descrised characteristics.

### Access
- The dataset is first downloaded from Kaggle (link: https://www.kaggle.com/c/titanic/data)
- Next, dataset is uploaded to my github and then copy the link of raw data
- Read the dataset using Dataset.Tabular.from_delimited_files

## Automated ML
1. Setting the automl
- Experiment timeout minutes: 20 minnutes timeout
- Max concurrent iterations: 5 times
- Primary metric: AUC weighted

2. Automl config:
- Task: classification task
- Label column: Survived
- Featurization: auto feature engineer
- Debug log: automl_errors.log

### Results
1. Dataset registered in workspace
![image](https://github.com/user-attachments/assets/ca1b89fe-4e63-42b4-b088-1854e420b8d4)


2. Register the best model
![image](https://github.com/user-attachments/assets/f41f17f9-8aa2-46a6-af47-f40bca5af826)


3. RunDetails
![image](https://github.com/user-attachments/assets/464e9c87-9530-4381-abac-a751dd2e6c74)


4. Best model
![image](https://github.com/user-attachments/assets/070daa46-6458-4d63-9ba6-46b22a8aeaf0)



5. Estimator
![image](https://github.com/user-attachments/assets/207dbbf6-96ac-4bc3-bd45-e88bde3dbf26)



## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
