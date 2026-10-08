---
source_url: https://docs.aws.amazon.com/solutions/digital-thread-using-graph-and-generative-ai-on-aws/index.html
---

---
title: 'Guidance for Digital Thread Using Graph and Generative AI on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/digital-thread-using-graph-and-generative-ai-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Digital Thread Using Graph and Generative AI on AWS

## Overview

This Guidance demonstrates how to create an intelligent manufacturing digital thread through a combination of knowledge graph and generative artificial intelligence (AI) technologies. A digital thread offers an integrated approach to combine disparate data sources across enterprise systems, increasing traceability, accessibility, collaboration, and agility. By integrating knowledge graph and generative AI, you can enhance data integration, improve semantic understanding, and enable intelligent and context-aware applications—ultimately leading to a more personalized user experience.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/digital-thread-using-graph-and-generative-ai-on-aws.pdf)

![Architecture diagram](/images/solutions/digital-thread-using-graph-and-generative-ai-on-aws/images/digital-thread-using-graph-and-generative-ai-on-aws-1.png)

1. **Step 1**: Identify key stakeholders in the manufacturing organization, and understand the business needs.
1. **Step 2**: Identify data sources to build a digital thread using graph and generative AI technologies.
1. **Step 3**: Ingest data into AWS using AWS Database Migration Service (AWS DMS) for databases and AWS DataSync for large datasets.
1. **Step 4**: Upload ingested data into Amazon Simple Storage Service (Amazon S3) for processing and analysis.
1. **Step 5**: Use the Amazon Neptune Bulk Loader to ingest the data from Amazon S3 to Neptune graph database.
1. **Step 6**: Select a foundation model (FM) from Amazon Bedrock, a fully managed service that offers a choice of high-performing FMs from leading AI companies and Amazon through a single API, along with a broad set of capabilities for building generative AI applications.
1. **Step 7**: Establish linkage between Amazon Bedrock and Neptune, and orchestrate the integration with AWS Lambda and Langchain. The orchestrator coordinates the process of generating the query from the FM (executing the query against the knowledge graph) and then returns the result in natural language.
1. **Step 8**: Create an application layer using Streamlit, AWS Fargate for hosting serverless containerized applications, Amazon Elastic Container Registry (Amazon ECR) for managing container images, Elastic Load Balancing (ELB) for traffic distribution, Amazon Route 53 for DNS, and Amazon Cognito for authentication.
1. **Step 9**: Use Amazon Virtual Private Cloud (Amazon VPC) to operate the application in a secure, isolated network. AWS Identity and Access Management (IAM) enhances access control. AWS Certificate Manager manages certificates, and AWS WAF supports web application security. Amazon GuardDuty monitors for malicious activity. Data at rest is encrypted with AWS Key Management Service (AWS KMS) and can be integrated with third-party key management systems.
1. **Step 10**: Use AWS CloudTrail to track activities, Amazon CloudWatch to monitor resources, and AWS CloudFormation for automated resource deployment of digital thread application.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-building-a-manufacturing-digital-thread-using-knowledge-graph-and-gen-ai)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

DataSync automates and optimizes data synchronization, reducing manual intervention and helping ensure operational efficiency in managing digital thread data. To help you further improve operational efficiency across workloads, CloudWatch enables monitoring and logging capabilities to provide real-time insights into system performance. Additionally, CloudTrail helps ensure that you have a comprehensive audit trail, promoting governance and compliance. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

To protect data, IAM offers fine-grained permissions and role-based access control to AWS services and resources, enforcing least privilege and enhancing control over user permissions. Additionally, AWS KMS manages keys for encrypting and decrypting Neptune data at rest. AWS WAF acts as a security layer by protecting against web application vulnerabilities and attacks, safeguarding the digital thread application, and protecting it from common vulnerability. GuardDuty provides automatic thread detection by continuously monitoring for malicious activities, using threat intelligence to promptly detect and respond to potential security risks. Amazon VPC and the VPC endpoint establish a secure network environment, isolating resources and establishing private communication with AWS services to reduce exposure to potential threats. Amazon Bedrock helps ensure data protection by refraining from using prompts for AWS model training, avoiding distribution to third parties, and not storing or logging data in service logs. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses multiple serverless services that contribute to reliability. For example, Fargate supports reliability by offering serverless compute for containers, automatically scaling resources based on demand, and optimizing application performance. The Fargate serverless compute model helps ensure optimal resource utilization and automatic scalability to support overall reliability of containerized applications. As a serverless service, Lambda automatically manages compute resources and scales to meet the size of the workload. This reduces the risk of service disruptions due to scaling issues or resource limitations. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Neptune is a fully managed graph database service that automatically optimizes query execution and indexing, allowing you to retrieve complex interconnected data with low latency. Lambda's event-driven architecture supports performance efficiency by executing functions in response to specific events, allowing for rapid and efficient processing without the need for constant resource management. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The services in this Guidance are designed to help you save on costs by paying only for the resources you use. For example, Neptune allows you to pay only for the actual resources consumed during query execution, eliminating the need for constant provisioned capacity and minimizing costs during periods of low activity. Fargate provides serverless compute for containers, so that you pay only for the exact compute resources used during application execution, reducing costs associated with idle times and over-provisioning. Amazon ECR offers a secure and scalable repository for container images, streamlining deployment processes and minimizing storage costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Fargate automatically manages containerized workloads, optimizing compute resources and minimizing energy consumption during idle periods. The Neptune serverless option and the Fargate serverless compute model dynamically scale resources based on demand, reducing the overall energy consumption associated with constant provisioned capacity. Additionally, Amazon S3 offers efficient storage options like frequent, infrequent, archival, and intelligent tiering for optimized storage, minimizing resource usage and energy consumption. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
