---
source_url: https://docs.aws.amazon.com/solutions/patient-entity-resolution-with-aws-healthlake/index.html
---

---
title: 'Guidance for Patient Entity Resolution with AWS HealthLake'
canonical_url: https://docs.aws.amazon.com/solutions/patient-entity-resolution-with-aws-healthlake/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Patient Entity Resolution with AWS HealthLake

## Overview

This Guidance shows how to use AWS Entity Resolution to perform patient entity resolution on healthcare data stored in AWS HealthLake. With HealthLake, you can establish comprehensive patient profiles with confidence scores, facilitating more accurate data management and maintaining data integrity across your environment. Furthermore, by integrating machine learning capabilities, this Guidance can assist you in identifying and linking disparate patient records across data sources, a key step in processes such as Master Data Management (MDM) or Enterprise Master Patient Index (EMPI).

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/patient-360-on-aws.pdf)

![Architecture diagram](/images/solutions/patient-entity-resolution-with-aws-healthlake/images/patient-entity-resolution-with-aws-healthlake-1.png)

1. **Step 1**: Patients will use mobile devices to manage their healthcare data. Patients will input data manually by uploading photos of medical records and through future wearables. All data interactions will occur through Amazon API Gateway and AWS Lambda.
1. **Step 2**: Health data from multiple sources will be added to Amazon Neptune.
1. **Step 3**: When patients upload pictures of medical records, such as a lab report or diagnosis, the text will be extracted from the image using Amazon Artificial Intelligence (AI) services, and data will be sent to Neptune.
1. **Step 4**: Patients will authorize providers with view access for a duration of time (such as 90 days) to their medical records. A token will be managed in Amazon DynamoDB to represent provider authorization and expiry.
1. **Step 5**: The payor will enrich the patient data from other sources. The data may come from the payor's source systems or from Amazon HealthLake if the payor has one set up.
1. **Step 6**: The provider will have access to a secure portal for accessing the patient's authorized 360 medical records.
1. **Step 7**: Providers will also have the ability to add medical episode and other relevant information to the patient data.
1. **Step 8**: Data captured in Neptune will be added to the payor's data lake and used for generating personalized medical tips for the patient.
1. **Step 9**: The payor will have access to patient population data in the data lake to generate business insights. Dashboards may be created using Amazon QuickSight.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/patient-matching-with-aws-healthlake-and-aws-entity-resolution)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Use Step Functions to orchestrate your entire workflow as a state machine. Step Functions coordinates the processing of multiple Lambda functions, allowing you to perform operations as code for automated processing. You can also limit human error and enable consistent responses to events. EventBridge can schedule the Step Functions state machine to run automatically, reducing operational overhead and ensuring regular processing of your entity resolution process. Additionally, you can automate your extract, transfer, and load (ETL) process by using AWS Glue to crawl your patient dataset and populate the Glue Data Catalog. Finally, monitor the metrics and logs using Amazon CloudWatch, gaining operational visibility and simplifying troubleshooting. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) enforces least-privilege access and can integrate with Lake Formation to create and grant appropriate permissions to stakeholders. This allows your stakeholders to securely query your HealthLake data store using Athena. HealthLake has default encryption at rest and in transit to safeguard your data. You can further enhance your security posture by using Amazon S3 with encryption, access controls, and versioning. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3 offers durable data storage with automatic replication across multiple Availability Zones (AZs). You can use Athena for reliable and highly available access to your data in Amazon S3. In addition, orchestrate your workflows using Step Functions, which provide built-in error handling and retry mechanisms. And by running your services on the global infrastructure of AWS, which is designed for fault tolerance and high availability, you help ensure that issues in one Region do not impact services in other Regions. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

By using serverless technologies like EventBridge, Lambda, AWS Glue, Athena, and Amazon S3, this Guidance scales your configured resources based on your workload demands. Furthermore, with AWS Glue crawlers, you can automate your ETL process by streamlining data preparation and minimizing manual effort. Also, use the advanced matching capabilities of AWS Entity Resolution to accurately identify and link disparate patient records, optimizing resource utilization and reducing the need for manual intervention. You can then monitor the performance of your resources using CloudWatch, so you can identify and address potential bottlenecks or inefficiencies. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Athena, Amazon S3, Lambda, AWS Glue, and EventBridge scale on demand and only charge you for the resources you use. With Athena, you can analyze data in your HealthLake data store without provisioning or managing any infrastructure, eliminating idle resource costs. AWS Entity Resolution follows a pay-per-use model, where you only pay for the number of source records processed by your workflows. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

EventBridge and Step Functions orchestrate workflows in a resilient, efficient manner with minimal resources. And by using Amazon S3, Lambda, Athena, and other serverless services that utilize the renewable energy infrastructure of AWS, your architecture is equipped to scale efficiently, optimizing energy usage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
