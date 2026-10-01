---
source_url: https://docs.aws.amazon.com/solutions/building-a-predictive-responsible-gaming-model-on-amazon-sagemaker/index.html
---

---
title: 'Guidance for Building a Predictive Responsible Gaming Model on Amazon SageMaker'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-predictive-responsible-gaming-model-on-amazon-sagemaker/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Building a Predictive Responsible Gaming Model on Amazon SageMaker

## Overview

This Guidance shows how you can build and train an ML model using Amazon SageMaker AI to predict problematic gambling behavior. Using your own player data, an impartial ML model can be trained, then deployed for inference. This model creates a risk score for your players, predicting problematic play in near real time. As a result, you can intervene proactively to facilitate early support and prevention of harm.

## Benefits

### Protect players through predictive insights

Implement automated early warning systems that identify at-risk gambling patterns before they become problematic. Transform player behavioral data into actionable protective measures that support responsible gaming intiatives.

### Strengthen regulatory compliance measures

Help support efforts to meet evolving responsible gaming regulations with data-driven player protection systems. Demonstrate proactive responsibility through comprehensive behavioral analysis and automated monitoring.

### Scale player protection efficiently

Process and analyze large volumes of player data while maintaining strict security requirements. Focus on player safety while the infrastructure automatically handles computational demands.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively build this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/a-predictive-responsible-gaming-model-using-amazon-sagemaker-ai.pdf)

![Architecture diagram](/images/solutions/building-a-predictive-responsible-gaming-model-on-amazon-sagemaker/images/building-a-predictive-responsible-gaming-model-on-amazon-sagemaker-1.png)

1. **Step 1**: The Jupyter notebook retrieves raw training and test data, which includes betting activity metrics, from the Amazon Simple Storage Service (Amazon S3) bucket using the Notebook AWS Identity and Access Management (IAM) role. The notebook visualizes the data to help understand the requirements and expected predictions of the training data.
1. **Step 2**: Use the Jupyter notebook to explore and analyze the data. Preprocess the data to encode categorical data and address multicollinearity, data leakage, and oddly distributed, missing, or unbalanced data. Split the data into training, validation, and test datasets, and upload the datasets to the Amazon S3 training data bucket.
1. **Step 3**: Specify the Amazon Elastic Container Registry (Amazon ECR) location for the Amazon SageMaker AI implementation of XGBoost, an open source implementation of the gradient boosted trees algorithm. The AWS built-in implementation has a smaller memory footprint, better logging, improved hyperparameter validation, and a bigger set of metrics than the original versions.
1. **Step 4**: Create a training job using the Amazon SageMaker AI XGBoost algorithm managed container.
1. **Step 5**: During training, the Amazon SageMaker AI managed training job downloads the input datasets from the S3 bucket to each training instance.
1. **Step 6**: After the training job finishes, validate the model based on the validation dataset. In case of successful validation, the model is deployed as an Amazon SageMaker AI inference endpoint.
1. **Step 7**: Invoke the deployed model to determine the probability that a player's gambling behavior is problematic. Validate predictions against the test data with a customer-configured threshold. Identification of problematic behavior may require further action from the customer to protect the player.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-a-predictive-responsible-gaming-model-using-amazon-sagemaker)

## Related content

- **Train responsible gaming inference models for sports betting with Amazon SageMaker**: This blog post demonstrates how to use Amazon SageMaker to build and deploy responsible gaming machine learning models that can detect problematic gambling behavior in sports betting applications.

[Learn more](https://aws.amazon.com/blogs/industries/train-responsible-gaming-inference-models-for-sports-betting-with-amazon-sagemaker/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
