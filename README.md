# SPS-2759-Telecom-Customer-Churn-Prediction-powered-by-AWS-Sagemaker
# Purpose

The ability to predict that a particular customer is at a high risk of churning, while there is still time to do something about it, represents a huge additional potential revenue source for every online business. Besides the direct loss of revenue that results from a customer abandoning the business, the costs of initially acquiring that customer may not have already been covered by the customer’s spending to date. (In other words, acquiring that customer may have actually been a losing investment.) Furthermore, it is always more difficult and expensive to acquire a new customer than it is to retain a current paying customer.

# Proposed Solution:

Churn prediction helps in identifying those customers who are likely to leave a company. The main contribution of our work is to develop a churn prediction model which assists telecom operators to predict customers who are most likely subject to churn. Our solution builds & deploys a Machine Learning model to predict the customer churn using Amazon SageMaker and predictions can be obtained by using its Endpoint. We have created a python - flask application that interacts with the model deployed on AWS Sagemaker with the help of AWS API Gateway and AWS Lambda Services.

# Steps involved:

Upload data on Amazon S3
Model deployment on Amazon Sagemaker
Configuration on AWS Lamda
Working with Rest API through AWS API Gateway
Web Application in Flask
Language used: Python

