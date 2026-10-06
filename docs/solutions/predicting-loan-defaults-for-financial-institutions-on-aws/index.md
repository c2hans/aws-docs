---
source_url: https://docs.aws.amazon.com/solutions/predicting-loan-defaults-for-financial-institutions-on-aws/index.html
---

---
title: 'Guidance for Predicting Loan Defaults for Financial Institutions on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/predicting-loan-defaults-for-financial-institutions-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Predicting Loan Defaults for Financial Institutions on AWS

## Overview

This Guidance helps financial institutions use AWS services for automated machine learning (ML) to predict loan defaults with minimal effort. Bad loans can have adverse effects on a bank’s net financial performance and lending potential. Using serverless and ML services, business analysts can quickly determine loan risks without high costs or the need to build code. This results in proactive credit risk management, mitigation of credit risks, profit maximization, and improved regulatory compliance.

## How it works

This architecture shows how to predict loan defaults using AWS AutoML and serverless technology.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/predicting-loan-defaults-for-financial-institutions-on-aws.pdf)

![Architecture diagram](/images/solutions/predicting-loan-defaults-for-financial-institutions-on-aws/images/predicting-loan-defaults-for-financial-institutions-on-aws-1.png)

1. **Step 1**: Source loan data from different data sources, such as external data sources or AWS services, including Amazon Relational Database Service (Amazon RDS) and Amazon Redshift.
1. **Step 2**: Import the raw tabular data files into Amazon Simple Storage Service (Amazon S3) directly or use Amazon AppFlow to automate the data movement.
1. **Step 3**: Data scientists or ML teams can use Amazon SageMaker Studio, an integrated development environment (IDE) for ML to perform and manage ML steps.
1. **Step 4**: Optionally, you can use Amazon SageMaker Data Wrangler for ML data preparation, joining, and insights and create an Amazon SageMaker AutoPilot job for training, tuning, and deploying the ML model.
1. **Step 5**: Automatically build, train and tune the best ML model using SageMaker AutoPilot. Select the best model from a leaderboard for model performance and accuracy requirements. Deploy this model to production with just one click using Amazon SageMaker Hosting or iterate with the recommended models in SageMaker Studio.
1. **Step 6**: Share the best model in one click with business teams using Amazon SageMaker Model Sharing.
1. **Step 7**: Business teams or analysts can use Amazon SageMaker Canvas, import the model, and generate accurate ML predictions on their own—without requiring any ML experience or having to write a single line of code.
1. **Step 8**: External application(s) can use Amazon API Gateway and AWS Lambda to invoke SageMaker endpoint using SageMaker Hosting for inference request.
1. **Step 9**: Store the inference results in Amazon S3. Build interactive business dashboards and paginated reports on inference data using Amazon QuickSight.
1. **Step 10**: Monitor training jobs and model endpoints either in SageMaker Studio or using Amazon CloudWatch metrics.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses Amazon AppFlow, a fully managed integration service that helps you securely transfer data between different services. This Guidance also uses SageMaker Data Wrangler, SageMaker Autopilot, and cloud-native support and integration for Amazon S3, facilitating the preparation and transformation of your dataset. With SageMaker Autopilot, you can retrain and deploy your model with updated datasets as needed. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance requires an AWS Identity and Access Management (IAM) account, which restricts access and permissions to the minimum required permissions for the service to function. Additionally, this Guidance has server-side encryption through either Amazon S3 or AWS Key Management Service (AWS KMS). [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance supports durable storage through Amazon S3 and automatic scaling through SageMaker. You can also monitor SageMaker through CloudWatch, which converts raw data into readable metrics in near real time and sets alarms for when you reach thresholds. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses SageMaker Autopilot, which can generate notebooks to manage multiple automatic-ML jobs and experiments. You can edit these notebooks as needed, and features like explainability help you better understand the model. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses serverless services such as Lambda and services that scale to match demand, such as SageMaker Autopilot, Amazon RDS, Amazon Redshift, and Amazon S3, so you only pay for the resources you need. You can also choose between on-demand pricing, a savings plan, or a combination of the two for further cost savings. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses Amazon SageMaker Model Monitor, which can automate your model drift detection, thereby reducing resource usage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
