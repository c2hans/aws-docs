---
source_url: https://docs.aws.amazon.com/solutions/physical-climate-risk-assessment-on-aws/index.html
---

---
title: 'Guidance for Physical Climate Risk Assessment on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/physical-climate-risk-assessment-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Physical Climate Risk Assessment on AWS

## Overview

This Guidance provides a technical foundation to visualize and monitor key performance indicators (KPIs) for reporting on climate-related physical risks to your operations. In particular, it demonstrates how you can enrich physical assets using large-scale, high-quality climate projection datasets made available through the Amazon Sustainability Data Initiative (ASDI). Physical climate risk assessment provides critical insights into the expected impacts of climate change to businesses, organizations, and communities. Understanding the potential risks and consequences of climate change empowers decision-makers to create and execute effective strategies for adaptation and resilience.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/physical-climate-risk-assessment-on-aws.pdf)

![Architecture diagram](/images/solutions/physical-climate-risk-assessment-on-aws/images/physical-climate-risk-assessment-on-aws-1.png)

1. **Step 1**: Analysts and operations managers collect geo locations, such as latitudes and longitudes, of interested sites, in addition to site metadata, such as site type, square footage, and occupancy rate.
1. **Step 2**: Sustainability subject matter experts (SMEs) generate a config file, specifying climate models, scenarios, and metrics for physical climate risk assessment.
1. **Step 3**: Ingest data into the AWS Cloud using Amazon API Gateway or AWS Tools and SDKs.
1. **Step 4**: Store static files in a data lake using Amazon Simple Storage Service (Amazon S3). Use Amazon DynamoDB or Amazon Relational Database Service (Amazon RDS) to store site data and geo locations, depending on data consumption patterns. Use DynamoDB to track the state as data moves through the pipeline.
1. **Step 5**: AWS hosts a broad variety of high-quality climate datasets through the Amazon Sustainability Data Initiative (ASDI) to reduce barriers to data access and store large-scale sustainability datasets. These datasets are optimized for the cloud and accessible through public S3 buckets.
1. **Step 6**: Enrich site data with downscaled climate models from ASDI. Perform geospatial joins to extract metric statistics from raster climate data files using AWS Lambda. Export processed data to Amazon S3, and use AWS Glue Data Catalog to store the metadata of your datasets. Use AWS Step Functions to orchestrate data processing pipelines.
1. **Step 7**: Build a dashboard using Amazon QuickSight or custom web application using AWS Amplify to visualize physical climate risks related to your operations. Analysts can also directly query from Amazon Athena to gain insights on custom metrics.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

You can use Athena to query custom metrics for additional insights, which can then be implemented in a QuickSight dashboard for reporting or a custom widget in a web application. These insights can also help you infer which additional climate scenarios and metrics to include as part of the input. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Resources are protected by AWS Identity and Access Management (IAM) policies and roles, following the least-privilege access principle. Data ingested to the AWS Cloud is encrypted and transferred over HTTPS. AWS Key Management Service (AWS KMS) encrypts and protects data-at-rest. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance follows an event-driven architecture with loosely coupled dependencies, making it easy to isolate behaviors and increase resilience and agility. It uses managed serverless services such as Step Functions and Lambda to orchestrate the loosely coupled dependencies. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Services selected for this architecture are purpose-built. For example, Step Functions Distributed Map orchestrates large-scale parallel workloads. In this Guidance, it orchestrates data enrichment using large-scale raster datasets from ASDI. Additionally, QuickSight is a purpose-built business intelligence tool. It allows you to create charts with geographic locations. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Step Functions and Lambda only run when invoked by an event and automatically scale based on workload demand. You can also use the Amazon S3 Intelligent-Tiering storage class to automatically move data to the most cost-effective access tier in Amazon S3. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS hosts a broad variety of large-scale high-quality sustainability datasets through public S3 buckets. This Guidance uses cloud-optimized open data directly from these S3 buckets to enrich your location data. This means you don't need to store large datasets in your AWS environment, reducing your overhead maintenance. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Estimating physical climate heat risk with NASA Global Daily Downscaled Projections on ASDI**: This post shows an example architecture to query the downscaled climate projection data for locations, calculate cooling degree day (CDD) metrics, and visualize the output withAmazon QuickSight.

[Estimating physical climate heat risk with NASA Global Daily Downscaled Projections on ASDI](https://aws.amazon.com/blogs/publicsector/estimating-physical-climate-heat-risk-with-nasa-global-daily-downscaled-projections-on-asdi/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
