---
source_url: https://docs.aws.amazon.com/solutions/geospatial-insights-for-sustainability-on-aws/index.html
---

---
title: 'Guidance for Geospatial Insights for Sustainability on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/geospatial-insights-for-sustainability-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Geospatial Insights for Sustainability on AWS

## Overview

This Guidance helps customers observe land use changes using geospatial data to support supply chain best practices. Customers can monitor changes in forest density using an Amazon SageMaker geospatial capability that simplifies the process of analyzing satellite images for changes in vegetation. Results are stored, cataloged, and observable on Amazon QuickSight for customers to review.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/geospatial-insights-for-sustainability-on-aws.pdf)

![Architecture diagram](/images/solutions/geospatial-insights-for-sustainability-on-aws/images/geospatial-insights-for-sustainability-on-aws-1.png)

1. **Step 1**: Create a GeoJSON file for the supplier location in question.
1. **Step 2**: Use a notebook with Amazon SageMaker geospatial capability to baseline supplier locations. Select the Sentinel-2 data set, and run an Earth Observation Job (EOJ) on the supplier location, for the desired period of time.
1. **Step 3**: The processed results of your EOJ are stored into your destination Amazon Simple Storage Service (Amazon S3) bucket, as specified in the EOJ. The data is stored as both JSON and PNG files.
1. **Step 4**: To make the data available for a dashboard, use AWS Glue to create databases and tables (schema) to be queried using Amazon Athena.
1. **Step 5**: Create an Amazon CloudFront distribution to allow for the PNG images of the supplier location to be discoverable in Amazon QuickSight.
1. **Step 6**: Together, the JSON data and the images are available in a consolidated dashboard in QuickSight, where sustainability and procurement teams can observe changes in vegetation at the supplier location over time.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-geospatial-insights-for-sustainability-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance takes in a supplier location using GeoJSON, and processes geospatial imagery for that location to observe changes in vegetation which would be indicative of deforestation. This output is stored as both JSON and PNG files, so end users (Procurement and Sustainability teams) can interrogate the data to observe changes in vegetation with QuickSight. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses role-based access with AWS Identity and Access Management (IAM) and the Amazon S3 bucket has encryption enabled, is private, and blocks public access. The data catalog in AWS Glue has encryption enabled. All roles are defined with least-privilege, and all communications between services stay within the customer account. Administrators can control the notebook, and Athena and QuickSight data access through IAM roles. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS Glue, Amazon S3, and Athena are all serverless, and will scale data access performance as your data volume increases. Athena is serverless, so you can quickly query your data without having to set up and manage any servers or data warehouses. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

By using serverless technologies, you provision only the exact resources you use. Athena automatically runs queries in parallel, so most results come back within seconds, which means Sustainability and Procurement team end users can quickly get information about supplier locations. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses serverless components such as AWS Glue, Amazon S3, and Athena, services that automatically scale up and down to meet demand, so you only pay for what you use. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

With the exception of the SageMaker notebook (which will be set at a specific size), all other resources in this workload are serverless and scale with use, which reduces idle resources. Lifecyle configurations can be used to conclude the SageMaker notebook after inactivity. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Remote monitoring of raw material supply chains for sustainability with Amazon SageMaker geospatial capabilities**: This post demonstrates how to use SageMaker geospatial capabilities to easily baseline and monitor the vegetation type and density of areas where suppliers operate.

[Go to blog](https://aws.amazon.com/blogs/machine-learning/remote-monitoring-of-raw-material-supply-chains-for-sustainability-with-amazon-sagemaker-geospatial-capabilities/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
