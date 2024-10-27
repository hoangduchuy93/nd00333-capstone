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
1. Dataset description:
- The titanic survival dataset consists of 12 features (including 1 target variable) and 891 records.
- The number of survival passengers and not survival passengers in the dataset is 342 and 549. So the survival rate around 38% in the dataset
- I am going to build the classification model to predict the survival change of passenger based on above descrised characteristics.

2. Hyperparameter:
- Download the dataset from Kaggle and create the dataset to workspace
- Choose the hyper params (C and max_iters) and submit the run, get the best run accuracy
- Register the best model

3. Automl
- Get the same dataset
- Config the automl setting(primary metrics, max iters, timeout)
- Register the best model
- Compare the accuracy of automl and hyperparameter

4. Deploy the best model
- After getting the accuracy between automl and hyper parameter, choose the model with the better accuracy to deploy
- From the best run, download the enrironment and the score.py script, ready to feed to Inference config.
- Check the status of endpoint deployment is healthy
- Send the post request to endpoint to get the response. Compare the prediction with the ground truth values.

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

![image](https://github.com/user-attachments/assets/91d70308-3d3f-4b6a-832e-ceb9e595cda7)




2. Register the best model

The best model is Voting Ensemble. The best accuracy is 84%

![image](https://github.com/user-attachments/assets/ea648095-b39c-4a1e-a7b1-312d252b82d5)

Some models accuracy of automl

![image](https://github.com/user-attachments/assets/e085a721-6c7b-4f53-bf58-710c31994b4b)

![image](https://github.com/user-attachments/assets/42b3ee11-7d7a-4e48-ad6c-1b548ad72c54)



3. RunDetails

![image](https://github.com/user-attachments/assets/464e9c87-9530-4381-abac-a751dd2e6c74)

The run is completed

![image](https://github.com/user-attachments/assets/e9e76d37-6402-4652-8e22-be942c2343c8)


4. Best model

![image](https://github.com/user-attachments/assets/37cbd702-eb4c-4863-8c37-23bb8c85d895)





## Hyperparameter Tuning
For the hyper parameter, I choose Logistic regression as the classifier model.
The target of the dataset is survival change (0/1). The script for processing data and prepare the training testing is provided in scrip train.py.
The parameter for the task:
- C: the regularization strenght. Input the random floating-point from 0.05 to 0.1.
- Max iteration: Select the random iteration of 16, 32, 64, 128 times.

### Results
The best run get the accuracy around 73% with the C value of 0.07 and the max inter of 64

![image](https://github.com/user-attachments/assets/858b0df9-2914-4f8a-8934-53857f34fa36)




RunDetails

![image](https://github.com/user-attachments/assets/0b588484-3a09-46dd-8b47-51bce7f9632c)

The run is finished

![image](https://github.com/user-attachments/assets/5ef77094-a9cc-461c-b8ca-ce144b282cdf)

Best run

![image](https://github.com/user-attachments/assets/6f0f3025-1c03-4226-aaf2-4ec05a0db3ea)

***Improvement plan for hyperparameter***
- Try different set of hyperparameter setting C and max_iter. For the C can try uniform range between (1 and 5) to see any improvement inperformace. The max_iter can be set to 100 or 200 to evaluate the performance can increase or not.
- Try different model like tree based model and boosting model like XGBoost, CatBoost, LightGBM. In many cases the boosting model can provide the better accuracy
- Try to use Early stopping to get the best model accuracy if the accuracy is started to decrease.

## Model Deployment
1. Choose the best model to deploy
The automl accuracy is 84%

![image](https://github.com/user-attachments/assets/80142876-e2bb-4e53-b2e3-5685be0011da)

The hyperparam accuracy is 73%

![image](https://github.com/user-attachments/assets/bce6d9db-8c3c-4da6-b433-8373e0addc9c)


==> We can choose the best model from automl to deploy to get the best performance. The automl accuracy is about 10% higher than hyperparameter tuning. So I will deploy to webservice the automl and also enable the applicatin insights.
We need to pass the environment and the score scrip to Inference config. Then config the Azure Container Instance ACI with cpu_cores = 1 and memory_gb = 1. 

2. The deployement is sucessfully with status healthy

![image](https://github.com/user-attachments/assets/8951bf41-70ff-43c7-9555-fd033cdea6cc)




3. REST Endpoint and Application insights enable

![image](https://github.com/user-attachments/assets/f4008cff-e2d1-4d0e-af0a-c5855124c485)




4. Sample data for testing
I randomly send 2 Passenger information to endpoint. The data sending to endpoint is looking like this:
`{'data':
[{'PassengerId': 1, 'Pclass': 3, 'Name': 'Braund, Mr. Owen Harris', 'Sex': 'male', 'Age': 22.0, 'SibSp': 1, 'Parch': 0, 'Ticket': 'A/5 21171', 'Fare': 7.25, 'Cabin': None, 'Embarked': 'S'},
{'PassengerId': 2, 'Pclass': 1, 'Name': 'Cumings, Mrs. John Bradley (Florence Briggs Thayer)', 'Sex': 'female', 'Age': 38.0, 'SibSp': 1, 'Parch': 0, 'Ticket': 'PC 17599', 'Fare': 71.2833, 'Cabin': 'C85', 'Embarked': 'C'}]}`


The prediction and expected result are:
Get 2 passenger information and post request to endpoint

![image](https://github.com/user-attachments/assets/1e55564b-ec5e-43f6-ad6b-6f29d4ba034d)



## Screen Recording
Here is the link to the video demo: https://www.youtube.com/watch?v=_pD04FNIrYQ&t=77s

