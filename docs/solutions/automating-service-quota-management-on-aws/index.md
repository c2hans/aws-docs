---
source_url: https://docs.aws.amazon.com/solutions/automating-service-quota-management-on-aws/index.html
---

---
title: 'Guidance for Automating Service Quota Management on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/automating-service-quota-management-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Automating Service Quota Management on AWS

## Overview

This Guidance shows how to automatically monitor and receive alerts on service quota usage across single or multiple AWS accounts. Effectively managing your AWS service quotas is crucial for maintaining operational continuity and preventing unexpected disruptions to your business-critical applications. This Guidance provides an automated and comprehensive quota management strategy, helping you reduce the impact of potential service limitations.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automating-service-quota-management-on-aws.pdf)

![Architecture diagram](/images/solutions/automating-service-quota-management-on-aws/images/automating-service-quota-management-on-aws-1.png)

1. **Step 1**: In the spoke account, an Amazon EventBridge rule running on a time schedule invokes an AWS Lambda function.
1. **Step 2**: The Lambda function reads the configuration file from the specified Amazon Simple Storage Service (Amazon S3) bucket to identify the quotas to monitor.
1. **Step 3**: The Lambda function queries the Service Quotas API to fetch current quota values for the specified services and regions.
1. **Step 4**: The Lambda function makes API calls to the AWS services that are being monitored to determine the quota usage data.
1. **Step 5**: The Lambda function stores the quota usage data in an Amazon DynamoDB table for tracking and analysis.
1. **Step 6**: The Lambda function compares the retrieved quota usage against the configured thresholds. If any quota exceeds its threshold, the Lambda function generates a custom event and sends it to the event bus.
1. **Step 7**: EventBridge uses cross-account integration to send the custom event to the event bus in the hub account.
1. **Step 8**: EventBridge sends a message to the Amazon Simple Notification Service (Amazon SNS) topic using an event rule and invokes an email notification.
1. **Step 9**: In a single account deployment, the event bus in the spoke account sends the custom event directly to the Amazon SNS topic in the same account to invoke an email notification.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-managing-aws-quotas-through-automation)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

EventBridge and Lambda provide a serverless model that enables you to build an event-driven architecture and automate workflows for quota management. The EventBridge automation invokes a Lambda function to capture usage data and quota values of various AWS services and resources at regular intervals. It also automates notifications to your cloud administrators so that they can perform remediation if needed. This approach reduces the operational burden of managing infrastructure and maintaining custom integrations. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses AWS Identity and Access Management (IAM) policies that are scoped down to the minimum permissions required for services to function properly. This limits unauthorized access to resources. Additionally, in a multi-account environment, this Guidance uses a cross-account EventBridge integration with scoped-down policies, permitting communication between spoke and management accounts only when needed. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon SNS enables an event-driven architecture, and its built-in retry mechanism supports successful event delivery. Additionally, DynamoDB synchronously replicates data across three facilities in an AWS Region, providing high availability and data durability. As a result of this quota management automation, you can take quick corrective actions to prevent productivity impairments and downtime. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

DynamoDB is a fully managed NoSQL database that provides fast, consistent performance at any scale. Lambda automatically scales resources up and down based on the demand, improving responsiveness. Together, they enable this Guidance to handle high event volume with low latency, without the need for you to manage traffic. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda and DynamoDB are serverless and automatically scale to manage resource utilization, so you only need to pay for the resources consumed in serving requests. The event traffic in this Guidance is not continuous (instead occurring at configurable intervals), so a scalable model keeps idle resources from causing unnecessary costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda and DynamoDB are serverless and support efficient, automatic resource scaling based on demand. By optimizing resource utilization and avoiding resource consumption while idle, these services reduce energy waste, all without requiring you to manage infrastructure. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
