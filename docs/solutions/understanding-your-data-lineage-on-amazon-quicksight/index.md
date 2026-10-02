---
source_url: https://docs.aws.amazon.com/solutions/understanding-your-data-lineage-on-amazon-quicksight/index.html
---

---
title: 'Guidance for Understanding Your Data Lineage on Amazon QuickSight'
canonical_url: https://docs.aws.amazon.com/solutions/understanding-your-data-lineage-on-amazon-quicksight/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Understanding Your Data Lineage on Amazon QuickSight

## Overview

This Guidance demonstrates how to trace and better understand your data lineage in Amazon QuickSight. It does this through a combination of AWS services that replace complex scripting with an AWS CloudFormation template. This allows you to visualize and analyze the usage and relationships of data sources and datasets. Previously, complex scripts were required to trace connections between these assets. QuickSight assets needed manual evaluation to validate migration. Manual checks of dashboards were also needed when evaluating changes in data schemas, filters, parameters, or visuals. This manual process did not scale well and risked production failures by missing impacted dashboards. With this new automated architecture, you can reduce the time spent tracing QuickSight data lineage from weeks to minutes.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/understanding-your-data-lineage-on-amazon-quicksight.pdf)

![Architecture diagram](/images/solutions/understanding-your-data-lineage-on-amazon-quicksight/images/understanding-your-data-lineage-on-amazon-quicksight-1.png)

1. **Step 1**: An AWS Lambda function reads the metadata for all Amazon QuickSight data sources, datasets, analyses, and dashboards in the AWS account.
1. **Step 2**: The Lambda function stores the metadata as flat files in an Amazon Simple Storage (Amazon S3) bucket.
1. **Step 3**: The Lambda function generates individual Amazon Athena tables for the metadata of data sources, datasets, analyses and dashboards.
1. **Step 4**: The Lambda function constructs new datasets and a QuickSight dashboard called the Data Lineage Dashboard. This visualizes data lineage, objects, and resource information in QuickSight using the Athena tables.
1. **Step 5**: Users access QuickSight to view the Data Lineage Dashboard and derive insights.
1. **Step 6**: When users view the Data Lineage Dashboard, QuickSight issues queries to the Athena tables.
1. **Step 7**: Athena runs the queries, accesses the data in the Amazon S3 bucket, and returns the results to QuickSight to render the Data Lineage Dashboard.
1. **Step 8**: An Amazon EventBridge rule invokes the Lambda function when users create or update a data source, dataset, analysis, or dashboard in QuickSight.
1. **Step 9**: The Lambda function reads the new or revised resource metadata from QuickSight and adds to the Amazon S3 bucket. The Data Lineage Dashboard can then access this added metadata through QuickSight.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-data-lineage-with-amazon-quicksight)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The AWS CloudFormation stack combined with the Lambda function enable logging of resource provisioning, errors, and user activity. This enables consistent measurement of operations and identification of improvement. Other services used in this Guidance include AWS CloudTrail and Amazon CloudWatch that automatically capture the Lambda function's logs and errors. The provisioned Athena and Quicksight services also log user API calls in CloudTrail. The Lambda function logs errors like API failures, throttling, or rate limits to CloudWatch. CloudFormation templates deploy the automated infrastructure, logging any failures to CloudWatch for review. If a resource fails provisioning, CloudFormation rolls back other resources. All the services in this architecture support configurable logging to CloudWatch or CloudTrail, allowing tracking and customization as needed for your operational requirements. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Access to data is secured through AWS Identity and Access Management (IAM) policies granting permission only to authorized users. The Amazon S3 bucket has a policy allowing access solely to the IAM role used by QuickSight and Athena. Resources are private by default, and can only be modified with IAM identity-based policies. The QuickSight Data Lineage Dashboard is private to one user initially, who can optionally share with additional authorized users. The data in the Amazon S3 bucket has private access restricted only to QuickSight and Athena using IAM roles. No other identities are granted access to the data by this architecture, helping to ensure security. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The AWS services in this Guidance are serverless, using managed AWS endpoints and DNS to support a highly available network topology with AWS handling service failures and recovery automatically. Specifically, the CloudFormation stack automates provisioning, rolling back all resources if one fails. The CloudFormation stack also provisions required resources except Athena tables, deleting all but QuickSight on failure or deletion. CloudFormation logs provisioning and errors available in CloudTrail and CloudWatch. The Amazon S3 bucket stores recoverable QuickSight metadata, Athena provides high availability across Availability Zones, and QuickSight utilizes AWS reliability features. The Lambda function is stateless, using Amazon S3 for invocations; Lambda logs invocations and errors to CloudWatch. Finally, the serverless services scale automatically based on usage. Amazon S3 scales with data, Athena and QuickSight with usage, and additional Lambda functions are invoked by QuickSight updates. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services chosen are purpose-built for this data lineage use case. First, QuickSight is a serverless service that integrates with Athena to query data in Amazon S3. The QuickSight dashboard allows you to gain insights about your QuickSight resources and data lineage. You can build additional Athena views or QuickSight datasets based on the Athena tables to query or visualize more information. Second, the Lambda function provides on-demand compute when QuickSight resources are created or updated. Third, the services deploy in the same Region to reduce latency and data transfer costs. Finally, the managed serverless services scale automatically based on usage, with scaling and maintenance handled by AWS. This optimized architecture allows you to focus on data lineage insights rather than performance management. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance utilizes managed AWS services to eliminate maintenance overhead and the need for third-party licensing. By leveraging these optimized and automated AWS services, costs are reduced through serverless usage and reduced data transfer. Also, the services deploy in the same Region to minimize data transfer charges, and QuickSight has no data transfer fees. The serverless services run only as needed. Athena invokes when the Data Lineage Dashboard is accessed. The Amazon S3 bucket contains just flat files of QuickSight metadata. Lambda runs once initially and then only when invoked by QuickSight resource updates through EventBridge. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The architecture uses sustainable AWS services that scale on demand. Athena invokes only when users access the QuickSight datasets, automatically scaling with usage. The Lambda function runs during initial setup, then only when QuickSight resources are created or modified. Data storage in Amazon S3 is cost-effective and auto-scalable. Data remains in Amazon S3 and is accessed only when required. The serverless services provision computation only when invoked, avoiding continuous hardware allocation. This optimized on-demand resource usage enhances sustainability while automated scaling, serverless services, and Amazon S3 storage minimize environmental impacts. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
