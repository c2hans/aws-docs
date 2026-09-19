---
source_url: https://docs.aws.amazon.com/solutions/connecting-data-products-with-amazon-datazone/index.html
---

---
title: 'Guidance for Connecting Data Products with Amazon DataZone'
canonical_url: https://docs.aws.amazon.com/solutions/connecting-data-products-with-amazon-datazone/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Connecting Data Products with Amazon DataZone

## Overview

This Guidance demonstrates how you can extend the data governance capabilities of Amazon DataZone to other Java Database Connectivity (JDBC) sources, such as MySQL, PostgreSQL, Oracle, and SQL Server. Extending governance to other JDBC data sources, self-managed databases, or third-party offerings is a unified solution to govern all of your data assets. It can be set up as an add-on for Amazon DataZone with the AWS Cloud Development Kit (AWS CDK), making it easy to automatically deploy and customize to fit your needs. You can discover and collaborate with databases, regardless of where the data assets are hosted.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/connecting-data-products-with-amazon-datazone.pdf)

![Architecture diagram](/images/solutions/connecting-data-products-with-amazon-datazone/images/connecting-data-products-with-amazon-datazone-1.png)

1. **Step 1**: A producer provisions a tool from the producer toolkit on AWS Service Catalog in the producer account. The tool will map data assets from the data source into the AWS Glue catalog.
1. **Step 2**: The producer approves a subscription request for one of the mapped data assets in the Amazon DataZone portal. An event is sent to Amazon EventBridge and invokes an AWS Step Functions primary state machine in the governance account.
1. **Step 3**: The primary state machine in the governance account invokes a Step Functions secondary state machine in the producer account.
1. **Step 3a**: The secondary state machine in the producer account uses AWS Lambda to retrieve details for connecting to the data source hosting the subscription's data asset from AWS Glue.
1. **Step 3b**: The secondary state machine in the producer account uses Lambda to connect to the data source, create credentials for the subscription's Amazon DataZone environment (if non-existent), and grant read access to the subscription's data asset.
1. **Step 3c**: The secondary state machine in the producer account uses Lambda that persists the new data source credentials in an AWS Secrets Manager producer secret (if non-existent) with a resource policy allowing read and cross-account access to the Amazon DataZone environment's associated consumer account.
1. **Step 3d**: The secondary state machine in the producer account uses Lambda to update tracking records on Amazon DynamoDB tables of the governance account.
1. **Step 4**: The primary state machine in the governance account invokes a Step Functions secondary state machine in the consumer account.
1. **Step 4a**: The secondary state machine in the consumer account uses Lambda to retrieve connection credentials from the producer secret in the producer account through cross-account access. Then it copies the credentials into a new consumer secret (if non-existent) in Secrets Manager local to the consumer account.
1. **Step 4b**: The secondary state machine in the consumer account uses Lambda to update tracking records on DynamoDB tables in the governance account.
1. **Step 5**: A consumer provisions a tool from the consumer toolkit in the consumer account on Service Catalog. The tool allows the consumer to query the subscription's data asset from its hosting data source through Amazon Athena by using the credentials stored in the consumer secret.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment. The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open implementation guide](https://aws-solutions-library-samples.github.io/databases/connecting-data-products-with-amazon-datazone.html)
[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-connecting-data-products-with-amazon-datazone)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS Cloud Development Kit (AWS CDK), Service Catalog, Lambda, Step Functions, Amazon CloudWatch, and DynamoDB are services that work in tandem to support your operational excellence. First, AWS CDK automates and simplifies the configuration of this Guidance at scale, allowing it to be deployed from within any continuous integration and continuous delivery (CI/CD) tooling that you use. Second, Service Catalog automates and simplifies the deployment of user-targeted tools so that you can deploy these tools in a way that supports your tasks, with the assurance that all deployed resources are aligned with your governance standards. Third, Lambda and Step Functions are serverless, meaning no infrastructure needs to be managed, thereby reducing your operational complexity. Fourth, DynamoDB is used as a storage layer to track all outputs for each component of this Guidance, providing governance teams visibility to support management activities. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM), Secrets Manager, and AWS Key Management Service (AWS KMS) are services that protect both your information and systems. To start, all inter-service communications use IAM roles, whereas the multi-account option leverages IAM roles with cross-account access. And, all roles follow least-privileged access, that is, they only contain the minimum permissions required so that the service can function properly. Some resources do include tag-based policies to restrict cross-project access to unauthorized resources. In addition, Secrets Manager is used to manage credentials to data sources that are created through the components of this solution, and stored as secrets with highly restrictive access. Finally, AWS KMS is used to leverage customer-managed keys for encrypting secrets in Secrets Manager. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Step Functions, Lambda, EventBridge, and DynamoDB are serverless AWS services, meaning that they ensure high availability at a Region level by default. These services also offer recovery from service failure aligned to service-specific service level agreements (SLAs) to help your workloads perform their intended functions correctly and consistently. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

When configuring this Guidance, Lambda functions are deployed as close as possible to the data source for improved performance. Additionally, execution logic inside every Lambda function is designed to eliminate redundant operations and to reuse previously created resources, like secrets, when applicable. Lambda supports the core functionality when connecting to data sources for this Guidance, as it is optimized to be lightweight and high performing. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Step Functions, Lambda, EventBridge, DynamoDB, Secrets Manager, and AWS KMS are all serverless AWS services, so you are only charged for what you use. With AWS Glue, you pay only for the time that your extract, transform, and load (ETL) takes to run. There are no resources to manage or upfront costs, nor are you charged for startup or shutdown time. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

With Step Functions, Lambda, EventBridge, DynamoDB, Secrets Manager, and AWS KMS being serverless AWS services, they can scale up or down as needed, minimizing the environmental impact of the backend services. For example, EventBridge is an event-driven application that provides near real-time access to data in AWS services, your own applications, or other software as a service (SaaS) applications. With this visibility, you can gain a better understanding of the environmental impacts of the services you are using, quantify those impacts through the entire workload lifecycle, and then apply appropriate design principles to reduce those impacts. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Connecting Data Products with Amazon DataZone Workshop**: This workshop demonstrates how to extend Amazon DataZone and govern JDBC backed data sources like MySQL, PostgreSQL, Oracle and SQL Server databases.

[Learn more](https://catalog.us-east-1.prod.workshops.aws/workshops/7cc9e767-10a4-46cc-a432-9b38bde2b9e5/en-US)

- **Governing data in relational databases using Amazon DataZone**: This blog post explains how you can extend the governance capabilities of Amazon DataZone to data assets hosted in relational databases based on MySQL, PostgreSQL, Oracle or SQL Server engines.

[Learn more](https://aws.amazon.com/blogs/big-data/governing-data-in-relational-databases-using-amazon-datazone/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
