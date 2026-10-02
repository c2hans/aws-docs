---
source_url: https://docs.aws.amazon.com/solutions/patient-360-on-aws/index.html
---

---
title: 'Guidance for Patient 360 on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/patient-360-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Patient 360 on AWS

## Overview

This Guidance helps payors offer a centralized medical records system to patients, allowing patients to manage their healthcare information in a consolidated repository. Patients control access to their medical records (including diagnostic activities, such as lab tests and procedures) and can choose which providers are authorized to view their data and the duration that they will have access. Providers will gain a 360-view of the patient’s health and medical history, leading to improved diagnoses and a reduced need for redundant tests or lab procedures. This results in lowered costs for both payors and patients. With the patient’s authorization, the payor can access patient population data to generate personalized wellness tips and business insights for the patient.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/patient-360-on-aws.pdf)

![Architecture diagram](/images/solutions/patient-360-on-aws/images/patient-360-on-aws-1.png)

1. **Step 1**: Patients will use mobile devices to manage their healthcare data. Patients will input data manually by uploading photos of medical records and through future wearables. All data interactions will occur through Amazon API Gateway and AWS Lambda.
1. **Step 2**: Health data from multiple sources will be added to Amazon Neptune.
1. **Step 3**: When patients upload pictures of medical records, such as a lab report or diagnosis, the text will be extracted from the image using Amazon Artificial Intelligence (AI) services, and data will be sent to Neptune.
1. **Step 4**: Patients will authorize providers with view access for a duration of time (such as 90 days) to their medical records. A token will be managed in Amazon DynamoDB to represent provider authorization and expiry.
1. **Step 5**: The payor will enrich the patient data from other sources. The data may come from the payor's source systems or from Amazon HealthLake if the payor has one set up.
1. **Step 6**: The provider will have access to a secure portal for accessing the patient's authorized 360 medical records.
1. **Step 7**: Providers will also have the ability to add medical episode and other relevant information to the patient data.
1. **Step 8**: Data captured in Neptune will be added to the payor's data lake and used for generating personalized medical tips for the patient.
1. **Step 9**: The payor will have access to patient population data in the data lake to generate business insights. Dashboards may be created using Amazon QuickSight.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

All services in this architecture emit Amazon CloudWatch events that can be used to monitor the individual components of the design. Changes to the infrastructure may be managed using AWS CloudFormation, AWS Cloud Development Kit (CDK), or tools like Terraform. Logs captured by various components may be consolidated into existing services, such as Splunk and DataDog. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Neptune can only be created in a virtual private cloud (VPC) and can only be accessed from subnets within the VPC. As a best practice, ensure that the data in Neptune is encrypted at rest. Amazon Cognito supports authentication and authorization for patient and providers. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Neptune offers high durability due to the separation of compute and storage. Six copies of data are stored across three Availability Zones. Compute instances are created across multiple Availability Zones to ensure high availability. The read replicas in the Neptune cluster are a candidate for failover—if the primary compute instance fails, one of the replicas takes over the role of the primary instance. Neptune and DynamoDB backups may be automated using AWS Backup. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Neptune decouples compute and storage, allowing customers to select an appropriately-sized compute instance based on the workload. Customers can create up to 15 read replicas and split the read/write load across the primary and replicas, leading to better performance. Neptune has an auto-scaling feature that can increase the database instances in the cluster under heavy load, helping achieve consistent performance from the cluster. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

With serverless technologies, you provision the exact amount of resources you use. Neptune automatically scales storage, so customers pay only for the storage they use and do not need to maintain excess storage for future growth. We recommend that customers adjust the size of the compute instances for the databases to meet their workload's service level agreement (SLA) and avoid paying for excess capacity. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Serverless services in this architecture lead to an optimal use of resources. The managed services in the architecture support on-demand scaling, which maximizes resource utilization and reduces the energy needed to run workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
