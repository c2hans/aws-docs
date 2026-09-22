---
source_url: https://docs.aws.amazon.com/solutions/subscriber-churn-prediction-and-retention-on-aws/index.html
---

---
title: 'Guidance for Subscriber Churn Prediction and Retention on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/subscriber-churn-prediction-and-retention-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Subscriber Churn Prediction and Retention on AWS

## Overview

This Guidance leverages Machine Learning (ML) techniques to build churn prediction models that identify subscribers who are high risk to churn and their key drivers. This can help Communication Service Providers to personalize offerings and retain subscribers.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/guidance/architecture-diagrams/subscriber-churn-prediction-and-retention-on-aws.pdf)

![Architecture diagram](/images/solutions/subscriber-churn-prediction-and-retention-on-aws/images/subscriber-churn-prediction-and-retention-on-aws-1.png)

1. **Step 1**: Telecom data is collected into an Amazon Simple Storage Service (Amazon S3) object storage bucket. Data includes call data records (CDRs), billing data, and data from customer care.
1. **Step 2**: A churn model is trained on the labelled data set, tested and tuned, then deployed using Amazon SageMaker.
1. **Step 3**: For every churn inference event, Amazon SageMaker Clarify identifies the important feature to the model to determine churn likelihood.
1. **Step 4**: Churn model predictions and explainability reports are exported to an Amazon S3 bucket by using an AWS Lambda function.
1. **Step 5**: Amazon Quicksight visualizes the model and explainability data, allowing for interactive analysis and identification of trends and decision support of who to send a churn retention offer. Amazon Athena is used by Amazon QuickSight to access the Amazon S3 data.
1. **Step 6**: The telecom analyst can then decide how to act on the insight and can use Amazon Pinpoint to send out subscriber retention offers.
1. **Step 7**: Telecom applications can also incorporate near real-time churn prediction by calling the Amazon SageMaker hosting endpoint.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Telecom data is used to identify the churn propensity of a telecom subscriber. This aligns with business objective. A custom machine learning (ML) model is trained in the cloud on customer data to determine churn. Results of the model and feature importance is visualized in QuickSight to help business analysts identify trends to provide decision support of who to approach with a customer retention offer. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All data is encrypted both in motion and at rest. Encrypted Amazon S3 buckets store data and SageMaker can only access that data by using the VPC (and not the internet). Training is done in secure containers and the results are stored in encrypted S3 buckets. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

SageMaker hosting is used to server the trained model, which takes advantage of multiple Availability Zones and elastic Scaling groups. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Serverless technology is used where possible. SageMaker Endpoints can scale up and down as needed to ensure the minimum number of instances needed are running. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

SageMaker endpoints can scale up and down as needed to ensure the minimum number of instances needed are running. Instance sizes are measured by using SageMaker Instance Recommender to make sure costs are minimized. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By extensively using managed services and dynamic scaling, we minimize the environmental impact of the backend services. All compute instances are sized to provide maximum utility. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
