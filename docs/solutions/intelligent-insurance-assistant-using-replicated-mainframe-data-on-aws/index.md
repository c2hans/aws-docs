---
source_url: https://docs.aws.amazon.com/solutions/intelligent-insurance-assistant-using-replicated-mainframe-data-on-aws/index.html
---

---
title: 'Guidance for Intelligent Insurance Assistant Using Replicated Mainframe Data on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/intelligent-insurance-assistant-using-replicated-mainframe-data-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Intelligent Insurance Assistant Using Replicated Mainframe Data on AWS

## Overview

This Guidance demonstrates how to implement an intelligent conversational AI chatbot that uses insurance policy, billing, and claims data from mainframe applications to receive and deliver responses using natural language. With change data capture (CDC) technology, the data is replicated from the mainframe application to AWS using low-latency, high-throughput data pipelines. The conversational AI application then reads the replicated data from the AWS data stores and provides responses to customer inquiries, such as claim status, policy status, and next premium due dates, in natural language. This Guidance can enhance your customer’s experience, reduce call center volume, and optimize your operational costs. While tailored for the insurance industry, the underlying technology used throughout this Guidance can be adopted for other industries requiring mainframe data integration on AWS.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/intelligent-insurance-assistant-using-replicated-mainframe-data-on-aws.pdf)

![Architecture diagram](/images/solutions/intelligent-insurance-assistant-using-replicated-mainframe-data-on-aws/images/intelligent-insurance-assistant-using-replicated-mainframe-data-on-aws-1.png)

1. **Step 1**: For the Amazon Bedrock Agent to report the correct claim status, it needs to have access to near real-time data in the mainframe. AWS Mainframe Modernization Data Replication with Precisely makes this data available in Amazon Relational Database Service (Amazon RDS). The Precisely Capture component gets mainframe data from Change Data Capture (CDC) logs and maintains this data within its internal transient storage, referred to as DB Logs. The mainframe data sources that can be replicated include Db2, a Virtual Storage Access Method (VSAM), and an Information Management System (IMS).
1. **Step 2**: The Precisely Publisher component monitors the internal data storage for any changes and subsequently transmits the corresponding CDC records to the Precisely Dispatcher component through a TCP/IP network connection.
1. **Step 3**: The Precisely Apply Engine component ingests the CDC records and transforms the data as necessary, such as by filtering or mapping the information, in order to align with the requirements of the target database. The Precisely Apply Engine then processes each CDC record and distributes the transformed data to Amazon MSK.
1. **Step 4**: Customized Java application-based database connectors ingest the CDC records from Amazon MSK and stores the data in the designated target database. The target database can be any supported system, such as Amazon DynamoDB, Amazon RDS, Amazon Redshift, or Amazon Simple Storage Service (Amazon S3). Amazon RDS is used here.
1. **Step 5**: The product specification and policy documentation files are uploaded to Amazon S3 for the Amazon Bedrock knowledge base. This stored content will be used by the Amazon Bedrock Agent to deliver more relevant, accurate, and customized responses to customer inquiries.
1. **Step 6**: Both customers and customer service representatives (CSRs) interact with the conversational AI-powered Amazon Bedrock Agent to make inquiries regarding the status of insurance claims.
1. **Step 7**: The Amazon Bedrock Agent invokes an AWS Lambda function, which in turn invokes the Claim Status API. This API then retrieves the current status of an insurance claim from Amazon RDS.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch logging capabilities facilitate the tracing and monitoring of the CDC and publishing processes. Additionally, CloudWatch logs will capture relevant information pertaining to the invocation of the Amazon Bedrock Agent and the Claim Status API, which is implemented using Lambda. CloudWatch can also assist in the troubleshooting of any issues related to the invocation of the Claim Status API through the Lambda function. Furthermore, the AWS CloudTrail service enables comprehensive operational and risk auditing, as well as governance and compliance monitoring, for your AWS accounts. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The AWS Identity and Access Management (IAM) policies governing this Guidance are scoped down to the minimum required permissions for Amazon Bedrock, Lambda, and the AWS Mainframe Modernization services. By restricting the IAM policies to the least privileged access levels, unauthorized access to resources by any user, role, or AWS service is limited. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses fully managed AWS services, including Amazon Bedrock for the conversational AI agent, Lambda for API invocation, DynamoDB for the claims data store, and Amazon MSK for publishing the CDC records from the mainframe application. By utilizing these fully managed services, the reliability of the conversational AI agent, the Claim Status API function, the data store, and the CDC queueing process is inherently managed and maintained by AWS. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

With this Guidance using fully managed AWS services, the conversational AI agent, Claim Status API, data store, and CDC publishing queue will automatically scale based on the number of users accessing the system to check their claim status. In addition, the CloudWatch logging and alarm features will enable the monitoring of performance and the identification of any potential bottlenecks, not only for the Precisely Apply Engine agent, but also for other AWS services used in this architecture, such as Amazon Bedrock, Lambda, DynamoDB, and Amazon MSK. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The Amazon Bedrock and Lambda services used within this Guidance will automatically scale, both in and out, in response to the user load on the conversational AI agent. Similarly, the DynamoDB data store and Amazon MSK service will scale automatically based on the CDC data being applied from the mainframe by the Precisely Apply Engine agent. The automated scaling of the AWS services used in this architecture helps to optimize costs by dynamically adjusting resource consumption to match actual usage patterns. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS continuously innovates to counterbalance its operational carbon footprint through energy-efficient data center design, reduced reliance on fossil fuels, renewable energy procurement, and carbon offset initiatives. By utilizing fully managed AWS services which automatically scale in and out based on usage, the energy consumption can be effectively controlled. Additionally, the right-sizing of Amazon Elastic Compute Cloud (Amazon EC2) instances further contributes to the mitigation of your carbon footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
