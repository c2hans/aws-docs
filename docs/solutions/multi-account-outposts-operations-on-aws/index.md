---
source_url: https://docs.aws.amazon.com/solutions/multi-account-outposts-operations-on-aws/index.html
---

---
title: 'Guidance for Multi Account Outposts Operations on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/multi-account-outposts-operations-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Multi Account Outposts Operations on AWS

## Overview

This Guidance demonstrates how to effectively manage and optimize Multi-Account AWS Outposts environments through an innovative quota management system. It helps organizations implement precise resource control and cost management by enabling dynamic setting and enforcement of both soft and hard utilization limits across member accounts. The solution showcases advanced monitoring capabilities through centralized CloudWatch dashboards, providing granular usage metrics at both an organizational and account levels. This empowers administrators to maintain operational efficiency, ensure fair resource allocation, and provides consumption metrics to support chargeback mechanisms, ultimately maximizing the return on investment in shared Outposts infrastructure.

## Benefits

### Automate Resource Management Controls

Implement automated monitoring and intervention for AWS Outposts resources across member accounts. Real-time event processing ensures compliance with defined resource limits while reducing administrative overhead.

### Enhance Operational Visibility

Gain centralized control and monitoring of Outposts resources through a secure web interface. Proactively identify and address capacity issues before they impact business operations.

### Strengthen Security Controls

Deploy comprehensive authentication and access controls using AWS IAM Identity Center and WAF protection. Ensure only authorized administrators can manage shared Outposts resources across accounts.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/multi-account-outposts-operations-on-aws.pdf)

![Architecture diagram](/images/solutions/multi-account-outposts-operations-on-aws/images/multi-account-outposts-operations-on-aws-1.png)

1. **Step 1**: Admin users authenticate via AWS IAM Identity Center. The AWS Outposts owner account hosts the web UI and the API using Amazon API Gateway. AWS Web Application Firewall (AWS WAF) provides IP-based access control. The AWS Lambda API Handler executes changes in the UI.
1. **Step 2**: AWS Resource Access Manager (AWS RAM) shares the services in the AWS Outposts rack with the Consumer Account. The controlled resources on the Outposts rack can include services like Amazon Elastic Compute Cloud (Amazon EC2), Amazon Elastic Block Store (Amazon EBS), and Amazon Simple Storage Service (Amazon S3).
1. **Step 3**: The Customer Account Amazon CloudWatch reads CloudWatch Alert thresholds from the Consumer Account and writes them to a centralized alert configuration.
1. **Step 4**: Amazon EventBridge powers the event management system, actively routing service notifications such as 'an EC2 instance has started'.
1. **Step 5**: When triggered by an event, the Event Processor Handler Lambda function collects real-time usage data from the consumer account. This Lambda function then evaluates this data against CloudWatch alert thresholds to determine if automated intervention is necessary.
1. **Step 6**: The Event Processor Handler Lambda function sends a message on the Amazon Simple Notification Service (Amazon SNS) Alert Topic to the Intervention Handler Lambda function, which performs remedial actions, as applicable.
1. **Step 7**: CloudWatch triggers an alert when an Outposts resource crosses a set threshold.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/compute/multi-account-outposts-operations-on-aws.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-multi-account-outposts-operations-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
