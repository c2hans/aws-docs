---
source_url: https://docs.aws.amazon.com/solutions/automating-sap-configuration-health-checks-on-aws/index.html
---

---
title: 'Guidance for Automating SAP Configuration Health Checks on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/automating-sap-configuration-health-checks-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Automating SAP Configuration Health Checks on AWS

## Overview

This Guidance shows how to automate health checks for customers who are running SAP on AWS using the traditional licensing model. Many customers are choosing RISE with SAP, where SAP handles infrastructure and technical services. For customers using the traditional licensing model with SAP on AWS, this Guidance demonstrates how to automate evaluation of the SAP landscape on AWS against 100+ health checks and architecture best practices aligned with the AWS Well-Architected Framework. It shows how to scan SAP systems automatically for configuration compliance, providing a summary view, detailed views for individual systems, and the capability to compare two systems side-by-side through an Amazon QuickSight dashboard. This empowers customers to proactively identify and remediate potential issues, confirming the SAP landscape adheres to AWS architectural best practices.

## How it works

This architecture diagram demonstrates how to automate health checks based on the AWS Well-Architected Pillars to identify configuration drifts and monitor infrastructure health.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automating-sap-configuration-health-checks-on-aws.pdf)

![Architecture diagram](/images/solutions/automating-sap-configuration-health-checks-on-aws/images/automating-sap-configuration-health-checks-on-aws-1.png)

1. **Step 1**: In an AWS account with SAP workloads, enable AWS Systems Manager. Systems Manager allows you to safely automate common and repetitive IT operations and management tasks.
1. **Step 2**: Create an Amazon Simple Storage Service (Amazon S3) bucket. Download the SAP systems inventory template from the GitHub repository and update with your SAP workload inventory.
1. **Step 3**: Launch the AWS CloudFormation template from the GitHub repository with the input as the S3 bucket. CloudFormation will deploy an AWS Lambda function and Amazon DynamoDB table. Upload the SAP inventory template to the S3 bucket.
1. **Step 4**: Run SAP health checks by executing the Lambda function on-demand, or schedule it periodically using Amazon EventBridge.
1. **Step 5**: The Lambda function evaluates AWS for SAP best practices and identifies any drifts or anomalies. Health checks results are written to the S3 bucket for further analysis.
1. **Step 6**: Amazon Simple Email Service (Amazon SES) sends notification emails regarding identified drifts.
1. **Step 7**: Optionally, analyze output using Amazon QuickSight. Use Amazon Q in QuickSight to query system health using natural language.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-automating-sap-configuration-health-checks-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch provides full transparency into execution logs for a comprehensive view of operations. The DynamoDB editor eliminates the need for additional user interfaces and codebase maintenance. These managed services help you focus on core business objectives without the burden of maintaining additional infrastructure. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) aligns with existing organizational permissions policies, minimizing additional effort and helping ensure appropriate user access levels. IAM seamlessly integrates with this solution, providing a secure foundation while adhering to your current security practices. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda automatically scales to meet application needs, so that you don’t have to overprovision for future spikes in demand. This fully managed approach minimizes overhead of infrastructure management. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda helps with optimizing Python code, which is modularized and optimized to run under 200 MB memory for scalability and efficiency. This service-based approach allows the application to scale up and down seamlessly based on the number of health checks for optimal performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda runs code without requiring servers, eliminating the need to provision and manage Amazon Elastic Compute Cloud (Amazon EC2) instances. By optimizing Python code for Lambda, you can keep costs low, typically less than $1 USD per instance (without considering AWS Free Tier). [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Managed services like Amazon S3, Lambda, and DynamoDB improve application sustainability by sharing resources across a broad customer base, maximizing resource utilization and reducing the overall infrastructure required for cloud workloads. This sustainable approach minimizes the energy and resources needed to power the solution, contributing to a more environmentally responsible cloud workload. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
