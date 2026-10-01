---
source_url: https://docs.aws.amazon.com/solutions/customizing-aws-config-resources-in-aws-control-tower/index.html
---

---
title: 'Guidance for Customizing AWS Config Resources in AWS Control Tower'
canonical_url: https://docs.aws.amazon.com/solutions/customizing-aws-config-resources-in-aws-control-tower/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Customizing AWS Config Resources in AWS Control Tower

## Overview

This Guidance demonstrates how to manage the activity that AWS Config records in your AWS Control Tower environment so you can lower overall costs. When governing and securing multi-account AWS environments, AWS Control Tower implements security best practices, such as enabling AWS Config to monitor all supported AWS resources. However, you may wish to filter out unneeded recorded resources to reduce AWS Config costs. This Guidance helps you make changes to AWS Config within your AWS environment while avoiding impacts, such as a reset of filters to AWS Config service, during account creation and account updates.

## How it works

The architecture diagram helps you to turn off recording in AWS Config for non-critical resources to keep AWS Config costs under control. Following the steps in this Guidance, you can make changes to AWS Config within the AWS Control Tower environment, without causing any drift in the landing zone.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/customizing-aws-config-resources-in-aws-control-tower.pdf)

![Architecture diagram](/images/solutions/customizing-aws-config-resources-in-aws-control-tower/images/customizing-aws-config-resources-in-aws-control-tower-1.png)

1. **Step 1**: An Amazon EventBridge rule invokes a producer AWS Lambda function when an AWS Control Tower account lifecycle event occurs.
1. **Step 2**: The producer Lambda function queries the AWS CloudFormation StackSet responsible for deploying AWS Config recorder to collect all AWS Region and child account details.
1. **Step 3**: The producer Lambda function identifies the list of accounts and Regions where the AWS Config recorder is enabled and generates individual messages for each account and Region in an Amazon Simple Queue Service (Amazon SQS) queue.
1. **Step 4**: Every message in the Amazon SQS queue invokes a consumer Lambda function.
1. **Step 5**: The consumer Lambda function assumes the AWSControlTowerExecution role in the member account and updates the AWS Config recorder with the resource list, specified as an input parameter, while deploying the Guidance.
1. **Step 6**: You can continue to use AWS Control Tower to manage the AWS accounts without having to make any changes to the AWS Config resource tracking.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS Control Tower allows you to set up and operate your multi-account AWS environment with prescriptive controls designed for scalable governance and security. This Guidance helps optimize services used for governing resources that are considered non-critical, such as isolated sandboxes or test environments. Additionally, AWS CloudWatch metrics and logs are an important part of observability. They help with troubleshooting failures and continual improvement of the Guidance. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance creates a cross-account execution role in AWS Identity and Access Management (IAM) to grant specific, limited permissions to Lambda functions that make changes to account configurations. AWS Security Token Service (AWS STS) generates short-lived tokens to securely assume roles across accounts. This Guidance follows the least privilege model to perform a required task, authorizing only the necessary permissions for a limited time. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

As fully-managed services, Lambda, EventBridge and Amazon SQS scale horizontally to match customer demand without user intervention, enhancing reliability. Multiple Lambda invocations are based on the number of AWS Config recorder changes needed for each account and Region. This distributes the workflow by parallel execution, helping to avoid a single point of failure. EventBridge provides specific events that trigger the workflow and keep the configuration of the environment in the desired state. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda and Amazon SQS are fully managed services that scale automatically to meet demand. These services allow the system to quickly scale and make configuration changes to several accounts and Regions concurrently. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

EventBridge, Lambda and Amazon SQS follow a pay-as-you-go pricing model, meaning you pay only for the resources you use. This Guidance will be invoked on specific AWS Control Tower events that are typically infrequent. Using a serverless architecture with pay-as-you-go pricing helps ensure that costs are minimized. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Managed services in this Guidance remove the need to identify periods of low or no utilization in your resources. Additionally, this Guidance uses serverless services, which are invoked when a specific AWS Control Tower event is detected. There are no idle resources configured to handle the requests. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
