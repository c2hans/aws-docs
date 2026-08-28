---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/performing-tertiary-analysis-with-machine-learning-using-amazon-sagemaker.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Performing tertiary analysis with machine learning using Amazon SageMaker AI
<a name="performing-tertiary-analysis-with-machine-learning-using-amazon-sagemaker"></a>

 Creating machine learning (ML) training sets and training models, and generating ML predictions using genomics data can be done using AWS Glue and Amazon SageMaker AI. We’ll provide recommendations and a reference architecture for creating training sets, training models, and generating predictions using AWS Glue, Amazon SageMaker AI, and Amazon SageMaker AI Jupyter notebooks.

## Recommendations
<a name="recommendations-3"></a>

 When creating ML training sets, training ML models, and generating predictions, consider the following recommendations to optimize performance and cost.

 **Use AWS Glue extract, transform, and load (ETL) service to build your training sets**—AWS Glue is a fully managed ETL service that makes it easy for you to extract data from object files in Amazon Simple Storage Service (Amazon S3), transform the dataset adding features needed for training machine learning models, and write the resulting data to an Amazon S3 bucket.

 **Use Amazon SageMaker AI Autopilot to quickly generate model generation pipelines**—Amazon SageMaker AI Autopilot automatically trains and tunes the best machine learning models for classification or regression, based on your data while allowing you to maintain full control and visibility. Sagemaker Autopilot analyses the data and produces an execution plan that includes feature engineering, algorithm identification, hyperparameter optimization to select the best model, and deploys the model to an endpoint. The process of generating the models are transparent and the execution plan is made available to the users via automatically generated notebooks that users can review and modify.

 **Use Amazon SageMaker AI hosting services to host your machine learning models**—Amazon SageMaker AI provides model hosting services for model deployment and an HTTPS endpoint where your machine learning model is available to provide inferences.

 **Use Amazon SageMaker AI notebook instances to create notebooks, generate predictions, and test your deployed machine learning models**—Use Jupyter notebooks in your notebook instance to prepare and process data, write code to train models, deploy models to Amazon SageMaker AI hosting, and test or validate your models.

## Reference architecture
<a name="reference-architecture-3"></a>

![Tertiary analysis with machine learning using Amazon SageMaker AI reference architecture](http://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/images/image5.png)

 An AWS Glue job is used to create a machine learning training set. Jupyter notebooks are used to generate machine learning model generation pipelines, explore the datasets, generate predictions, and interpret the results.

 An AWS Glue job ingests data used for training a machine learning model, adds features used for training, and writes the resulting dataset to an Amazon S3 bucket. A Jupyter notebook is run to generate a machine learning pipeline using Amazon SageMaker AI Autopilot, generating two notebooks. These two notebooks capture the data structures and statistics, feature engineering steps, algorithm selection, hyperparameter tuning steps, and the deployment of the best performing model. Users have a choice to either use the plan recommended by SageMaker Autopilot or modify the generated notebook to influence the final results. A prediction notebook is used to generate predictions and evaluate model performance using a test dataset.

**Note**
 **Note:** To access an AWS Solutions Implementation providing an AWS CloudFormation template to automate the deployment of the solution in the AWS Cloud, see the [Genomics Tertiary Analysis and Machine Learning Using Amazon SageMaker AI](https://docs.aws.amazon.com/solutions/latest/genomics-tertiary-analysis-and-machine-learning-using-amazon-sagemaker/welcome.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
