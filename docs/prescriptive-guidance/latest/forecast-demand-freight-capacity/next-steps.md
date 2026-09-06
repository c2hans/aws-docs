---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/forecast-demand-freight-capacity/next-steps.html
---

# Next steps
<a name="next-steps"></a>

Before you implement this demand forecasting solution on AWS, it is recommended that you evaluate the problem you are trying to solve. It's a good idea to bring the business owners and data scientists together to brainstorm whether the problem can be solved by an ML model. It is critical to understand what datasets you have and the length of historical data available. It is also important for the business owners to collaborate with the data scientists to provide domain knowledge, identify useful features, and help create those features. The reliability of the model increases with the number of relevant features that you can create, which provides a more accurate forecast.

To build this architecture on AWS, begin by setting up an AWS account and provisioning the necessary services, such as Amazon Simple Storage Service (Amazon S3) for data storage and Amazon SageMaker AI for machine learning model training. Next, identify and collect the internal and external data sources that will be used as input features for the forecasting model. Store this data in Amazon S3 and use the data processing capabilities in SageMaker AI to preprocess and prepare the data for model training. In SageMaker AI, use automatic model tuning and distributed training capabilities to train and optimize the forecasting models. You can also use AWS services such as AWS Step Functions or AWS Lambda to set up a pipeline that periodically retrains the forecasting models with the latest data. After retraining, initiate a batch transform job in SageMaker AI to generate the forecast results, which you store in Amazon S3. Use Amazon Quick to visualize and monitor the forecast results generated from the batch transform job.
