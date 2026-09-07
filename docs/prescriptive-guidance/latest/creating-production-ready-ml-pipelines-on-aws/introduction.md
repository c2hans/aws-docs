---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/creating-production-ready-ml-pipelines-on-aws/introduction.html
---

# Creating production-ready ML pipelines on AWS
<a name="introduction"></a>

*Chen Wu and Josiah Davis, Amazon Web Services*

Machine learning (ML) projects require a significant, multi-stage effort that includes modeling, implementation, and production to deliver business value and to solve real-world problems. Numerous alternatives and customization options are available at each step, and these make it  increasingly challenging to prepare an ML model for production within the constraints of your resources and budget. Over the past few years at Amazon Web Services (AWS), our Data Science team has worked with different industry sectors on ML initiatives. We identified pain points shared by many AWS customers, which originate from both organizational problems and technical challenges, and we have developed an optimal approach for delivering production-ready ML solutions.

This guide is for data scientists and ML engineers who are involved in ML pipeline implementations. It describes our approach for delivering production-ready ML pipelines. The guide discusses how you can transition from running ML models interactively (during development) to deploying them as a part of a pipeline (during production) for your ML use case. For this purpose, we have also developed a set of example templates (see the [ML Max project](https://github.com/awslabs/mlmax)), to accelerate the delivery of custom ML solutions to production, so you can get started quickly without having to make too many design choices.

## Overview
<a name="overview"></a>

The process for creating a production-ready ML pipeline consists of the following steps:
+ **Step 1. Perform EDA and develop the initial model – **Data scientists make raw data available in Amazon Simple Storage Service (Amazon S3), perform exploratory data analysis (EDA), develop the initial ML model, and evaluate its inference performance. You can conduct these activities interactively through Jupyter notebooks.
+ **Step 2. Create the runtime scripts – **You integrate the model with runtime Python scripts so that it can be managed and provisioned by an ML framework (in our case, Amazon SageMaker). This is the first step in moving away from the interactive development of a standalone model toward production. Specifically, you define the logic for preprocessing, evaluation, training, and inference separately.
+ **Step 3. Define the pipeline – **You define the input and output placeholders for each step of the pipeline. Concrete values for these will be supplied later, during runtime (step 5). You focus on pipelines for training, inference, cross-validation, and back-testing.
+ **Step 4. Create the pipeline – **You create the underlying infrastructure, including the AWS Step Functions state machine instance in an automated (nearly one-click) fashion, by using AWS CloudFormation.
+ **Step 5. Run the pipeline – **You run the pipeline defined in step 4. You also prepare metadata and data or data locations to fill in concrete values for the input/output placeholders that you defined in step 3. This includes the runtime scripts defined in step 2 as well as model hyperparameters.
+ **Step 6. Expand the pipeline – **You implement continuous integration and continuous deployment (CI/CD) processes, automated retraining, scheduled inference, and similar extensions of the pipeline.

The following diagram illustrates the major steps in this process.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/creating-production-ready-ml-pipelines-on-aws/images/guide-img/38c6f8a0-9908-46ce-9db4-ad6b4c4bc218/images/418882f7-3813-46b1-98d4-a64d37ec0c7a.png)
