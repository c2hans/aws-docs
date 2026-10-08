---
source_url: https://docs.aws.amazon.com/solutions/connected-customer-journey-hub-on-aws/index.html
---

---
title: 'Guidance for Connected Customer Journey Hub on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/connected-customer-journey-hub-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Connected Customer Journey Hub on AWS

## Overview

This Guidance helps to create a single source of truth of customer touch points to automatically understand and extract customer linked information from siloed, raw, and disparate data.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/connected-customer-journey-hub-on-aws.pdf)

![Architecture diagram](/images/solutions/connected-customer-journey-hub-on-aws/images/connected-customer-journey-hub-on-aws-1.png)

1. **Step 1**: Data is ingested from multiple data sources across telco's engagement channels and systems of record through batch, streaming, and/or API-based mechanisms.
1. **Step 2**: Data is loaded in parallel to AWS Neptune and Amazon Simple Storage Service (Amazon S3). AWS Lambda calls either deterministic or probabilistic identity resolver machine learning (ML) models deployed on Amazon SageMaker real-time interface endpoints based on Neptune Stream data. The identity resolved data is upserted into Amazon S3.
1. **Step 3**: Amazon Athena connector is used for querying journey milestone data on Neptune. This data is then converted into a Gremlin query and stored in Amazon DynamoDB along with trigger criteria. This query is triggered as new vertices and edges are created or updated on Neptune. Based on the result, journey milestone vertices and edges are created/updated.
1. **Step 4**: The journey frequency analyzer returns the top journeys along with the number of times each journey step happened based on the event of interest chosen by the customer experience (CX) strategist as the start or end of the journey.
1. **Step 5**: The journey similarity analyzer returns the count and details of other customers who have gone through very similar journeys.
1. **Step 6**: A number of journey propensity models are trained and deployed on SageMaker using the data on Neptune. These models are invoked using Neptune ML queries. Example propensity models include churn, personalization, fraud, and customer satisfaction score prediction.
1. **Step 7**: The website static files are deployed on Amazon S3 and distributed globally using Amazon CloudFront. The website is secured using AWS WAF.
1. **Step 8**: The journey key performance indicator (KPI) visualizer exposes an API, which allows the Amazon QuickSight dashboards to be embedded into the CCJ insights dashboard.
1. **Step 9**: All the extracted journey data is presented via insights dashboards or the APIs and widgets can be integrated to the communication service provider's (CSP) choice of system of engagement.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Telecoms data is ingested using data pipelines built using AWS Cloud Development Kit (AWS CDK), AWS CloudFormation, and serverless application model (SAM). Continuous integration/continuous delivery (CI/CD) toolsets such as AWS CodePipeline are used to orchestrate deployment and promote code through environments. AWS Glue Studio, AWS Step Functions, and AWS Glue DataBrew are used to provide orchestration of the data operations lifecycle. SageMaker pipelines are used to orchestrate the ML lifecycle. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All data is encrypted both in motion and at rest. Encrypted Amazon S3 buckets store data. Neptune database is also encrypted and is secured in a private subnet within the VPC. SageMaker can only access that data via the VPC and not via the internet. Training is done in secure containers and the results are stored in encrypted S3 buckets. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Neptune is deployed across multiple availability zones. SageMaker hosting is used to server the trained model, which takes advantage of multiple Availability Zones (AZs) and Elastics scaling groups. All other services are serverless, which means that they are inherently highly available across multiple AZs in a region. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Serverless technology is used where possible. In the case of Neptune, autoscaling is configured to deal with unpredictable read patterns. SageMaker endpoints can scale up and down as needed to ensure the minimum number of instances needed are running. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Serverless services are used where possible, making sure that customers pay for only the resources consumed. Lambda power tuning is used to optimize cost while maintaining performance. Autoscaling is used in Neptune to automatically turn off read replicas when not being used. SageMaker endpoints can scale up and down as needed to ensure the minimum number of instances needed are running. Instance sizes are measured by using SageMaker Inference Recommender to make sure costs are minimized. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By extensively utilizing managed services and dynamic scaling, we minimize the environmental impact of the backend services. All compute instances are right-sized to provide maximum utility. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
