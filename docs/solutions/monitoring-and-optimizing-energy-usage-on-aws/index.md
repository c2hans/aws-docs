---
source_url: https://docs.aws.amazon.com/solutions/monitoring-and-optimizing-energy-usage-on-aws/index.html
---

---
title: 'Guidance for Monitoring and Optimizing Energy Usage on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/monitoring-and-optimizing-energy-usage-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Monitoring and Optimizing Energy Usage on AWS

## Overview

This Guidance demonstrates how to monitor and optimize the energy use of industrial and/or building equipment in customer premises using AI/ML on AWS. From data ingestion to data processing and model training to inference, customers can use this guidance to maximize their energy consumption while driving energy cost reduction.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/monitoring-and-optimizing-energy-usage-on-aws.pdf)

![Architecture diagram](/images/solutions/monitoring-and-optimizing-energy-usage-on-aws/images/monitoring-and-optimizing-energy-usage-on-aws-1.png)

1. **Step 1**: Operations and Subject Matter Experts (SMEs) install the required sensors (such as Temperature sensors) on the equipment of interest. Sensor or asset metadata, and other supporting data (such as suppliers information), should also be located as a primary data source for Energy Use Optimization.
1. **Step 2**: Sensors transmit telemetry data to the Cloud through AWS IoT SiteWise Edge on AWS IoT Greengrass core. Supporting data and other metadata may come through AWS IoT Core, AWS IoT Device SDKs, or an Amazon Simple Storage Service (Amazon S3) upload in batch format through FTP or API.
1. **Step 3**: While sensor data (telemetry) are automatically ingested to an AWS IoT SiteWise Data Store through AWS IoT SiteWise Edge, other metadata, or batch internet of things (IoT) messages, can be collected through standard AWS IoT Core and Amazon Kinesis.
1. **Step 4**: AWS IoT SiteWise can act as a real-time data store for the sensor data. Other supporting information can be stored in a data lake (like Amazon S3) with scheduled extract, transform, and load (ETL) jobs built using AWS Glue. Asset and facility metadata can be stored as graph relationships in Amazon Neptune.
1. **Step 5**: With the processed data in the data lake and AWS IoT SiteWise, you can start training your Machine Learning (ML) model on Amazon SageMaker and AWS Batch. The trained model artifact can be packaged as a docker image in Amazon Elastic Container Service (Amazon ECS) for better scalability.
1. **Step 6**: Enrich the sensor data stored in AWS IoT SiteWise with asset model and model hierarchy. Build a real-time dashboard using AWS AppSync, AWS Amplify, Amazon Managed Grafana or Amazon QuickSight. Configure the dashboards or reports to monitor energy usage and track cost savings.
1. **Step 7**: ML-based recommended IoT setpoints, or other controllable knob settings, are deployed through SageMaker. Optionally, deploy edge models on AWS IoT Greengrass core.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-monitoring-and-optimizing-energy-usage-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance takes in real-time and batch telemetry data from IoT sensors, and trains a Machine Learning model to deliver recommendations to reduce energy usage. The model is stored as a model artifact in Amazon S3 and will trigger AWS CodePipeline to request human approval before deployment. This allows end users to question and validate the model recommendation with ease. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance encourages the use of role-based access with AWS Identity and Access Management (AWS IAM). This ensures only the appropriate people have access to the content. All roles are defined with least-privilege access, and all communications between services stay within the customer account. All data is encrypted both in-transit and at rest using AWS Key Management Service (AWS KMS). The data catalog in AWS Glue is encrypted. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS Glue, Amazon S3, and Neptune are all serverless, and will scale data access performance as data volume increases. Neptune also adjusts capacity to provide just the right amount of database resources that the application needs, avoiding the need to set up and manage any servers or data warehouses. Data is stored in a data lake that is built with an Amazon S3 bucket. Amazon S3 objects are stored across a minimum of three Availability Zones. This provides 99.999999999% durability of objects. Therefore, the Guidance is inherently resistant to failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

By using serverless technologies, you provision only the exact resources you use. AWS Glue and AWS Lambda only run when needed. Additionally, Neptune is a fully managed serverless graph database, which also scales according to demand to ensure just the right number of resources are needed to complete the job. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses serverless components such AWS Glue, Amazon S3, and Neptune. These services automatically scale up and down to meet demand, so you only pay for what you use. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

All resources in this Guidance are serverless and scale with use, which reduces the number of resources that are idle. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
