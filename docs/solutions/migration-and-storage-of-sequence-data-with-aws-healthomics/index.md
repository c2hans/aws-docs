---
source_url: https://docs.aws.amazon.com/solutions/migration-and-storage-of-sequence-data-with-aws-healthomics/index.html
---

# Guidance for Migration & Storage of Sequence Data with AWS HealthOmics

## Overview

This Guidance demonstrates how to import omics sequence data from Amazon Simple Storage Service (Amazon S3) into AWS HealthOmics Storage. HealthOmics Storage can help you efficiently store and share genomics data, allowing you to realize cost savings when managing your growing volume of genomics data. Because it integrates with other AWS services, not only can you safely and securely store your genomics data, but this Guidance can also you help you protect patient privacy and automate workflows, streamlining data processing and analysis.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/migration-and-storage-of-sequence-data-with-aws-healthomics.pdf)

![Architecture diagram](/images/solutions/migration-and-storage-of-sequence-data-with-aws-healthomics/images/migration-and-storage-of-sequence-data-with-aws-healthomics-1.png)

1. **Step 1**: If you have already followed the directions in How to move and store your genomics sequencing data with AWS DataSync, you will have a pre-existing Amazon Simple Storage Service (Amazon S3) bucket. If you do not have an Amazon S3 bucket, you can create one using either the AWS Management Console or AWS Command Line Interface (AWS CLI).
1. **Step 2**: The Amazon S3 Object Created Event invokes an AWS Lambda function to create a record in the Amazon DynamoDB table.
1. **Step 3**: Creation of a record in the Auto Load Omics Table creates an item in a DynamoDB stream.
1. **Step 4**: The DynamoDB stream event invokes Lambda, which starts the sequence import workflow.
1. **Step 5**: AWS Step Functions workflow using multiple Lambda functions and native Step Functions tasks is initiated to import data. Detailed workflow is located in the code repository.
1. **Step 6**: The original sequence is loaded into AWS HealthOmics Storage.
1. **Consideration A**: Custom Resource: The sequence import requires a reference genome in the HealthOmics Reference store. This Guidance uses an additional AWS Cloud Development Kit (AWS CDK) construct that creates a reference and adds the acquirer reference number (ARN) for that reference as a parameter in AWS Systems Manager Parameter Store.
1. **Consideration B**: Custom Metric: Success or failure of the HealthOmics import job is recorded as a custom metric in Amazon CloudWatch. This allows detailed monitoring of imported statistics.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance is implemented using AWS CDK where the business logic, infrastructure, and configuration are defined as code. This allows changes and integration to perform as code within a version control system. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon S3 is protected by the AWS secure global network infrastructure. Security and Compliance are a shared responsibility between AWS and the customer. And this shared model helps relieve the operational burden from the customer because AWS operates, manages, and controls the components of the operating system. Amazon S3 secures data from unauthorized access with encryption features and access management tools. HealthOmics provides encryption by default to protect sensitive customer data at rest by using a service-owned AWS Key Management Service (AWS KMS) key. Customer-managed KMS keys are also supported. For more on protection with HealthOmics, follow Data protection in AWS HealthOmics. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

By building this Guidance using AWS serverless and managed services, AWS is responsible for the efficient operation of its services and enables the applications to scale with demand. This ensures that the workload performs its intended function correctly and consistently when it's expected to. It also allows customers to operate and test the workload through its total lifecycle. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The backbones of this Guidance are AWS serverless and managed services that minimize operational overhead, such as server management. HealthOmics Storage is purpose built for omics sequence data, allowing customers to store, discover, and share raw sequence data efficiently, securely, and at low cost. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance includes the functionality to move data into HealthOmics Storage. HealthOmics provides a cost-effective, omics-aware storage option for reference and sequence data that can reduce the Total Cost of Ownership (TCO) for storing raw sequence data. Such data can include BAMs, CRAMs, and FASTQ file formats. HealthOmics automatically moves data to the less expensive storage class if the data are not regularly accessed (such as data that has not been accessed for more than 30 days). This is similar to the Amazon S3 Intelligent-Tiering storage class that automates storage cost savings by moving data when access patterns change, resulting in cost savings for customers. This Guidance is built with the AWS serverless service, Lambda, for event-driven computing. Step Functions is used for orchestration, sequencing the data import workflow. AWS serverless services and products allow applications to scale quickly with demand, while ensuring that only the minimum resources are required. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

When building cloud workloads, the practice of sustainability is knowing the impacts of the services used and applying design principles to reduce those impacts. In the case of this Guidance, because it relies extensively on serverless and managed services, the services scale to continually match the load, but with just the minimum resources needed, reducing the risk of over-provisioning resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
