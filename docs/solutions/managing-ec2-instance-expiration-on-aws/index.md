---
source_url: https://docs.aws.amazon.com/solutions/managing-ec2-instance-expiration-on-aws/index.html
---

---
title: 'Guidance for Managing EC2 Instance Expiration on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/managing-ec2-instance-expiration-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Managing EC2 Instance Expiration on AWS

## Overview

This Guidance shows how to terminate Amazon Elastic Compute Cloud (Amazon EC2) instances based on expiration values defined in their tags. For example, you can stop an instance a specified number of hours after its launch time or at an exact date and time. These settings let you prevent ephemeral instances (such as build agent machines) from existing beyond their expected use. You can also preset development instances to automatically terminate at a future time or terminate an instance that has failed to continuously reset its own watchdog tag. This helps you to avoid running unnecessary compute.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/managing-ec2-instance-expiration-on-aws.pdf)

![Architecture diagram](/images/solutions/managing-ec2-instance-expiration-on-aws/images/managing-ec2-instance-expiration-on-aws-1.png)

1. **Step 1**: Amazon EventBridge rules send Amazon Elastic Compute Cloud (Amazon EC2) start and tag-change events to an Amazon Simple Queue Service (Amazon SQS) queue.
1. **Step 2**: An EventBridge schedule sends an event to the Amazon SQS queue when an Amazon EC2 instance expires.
1. **Step 3**: An AWS Lambda function consumes events from the Amazon SQS queue.
1. **Step 4**: The Lambda function handles Amazon EC2 instance expirations and updates the EventBridge schedule for the next instance to expire.
1. **Step 5**: Upon instance expiration, the Lambda function uses Amazon EC2 to stop or terminate the instance.
1. **Step 6**: The Lambda function optionally emits action events regarding any actions taken on Amazon EC2 instances.
1. **Step 7**: An EventBridge rule contains an event pattern to match action events and propagate them to targets.
1. **Step 8**: An Amazon Simple Notification Service (Amazon SNS) topic can be used as a target of the action rule to generate administrative notifications.
1. **Step 9**: The Lambda function sends metrics and logs to Amazon CloudWatch for observability, including through a CloudWatch dashboard.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-instance-expiration-on-aws/)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The Guidance sends events to an EventBridge event bus and provides a rule that matches those events. You can also add an Amazon SNS topic as a target to the rule. These aspects provide visibility into actions and let you integrate the actions with downstream systems to produce notifications or enable additional automation. Additionally, this Guidance supports decoupled integration with other systems. Finally, CloudWatch monitors the infrastructure and provides logs and metrics that aid troubleshooting of potential issues. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) lets you set up granular permission policies and short-lived access through roles (rather than hard-coded credentials). By using IAM policies to implement the principle of least privilege for the Lambda function used in this Guidance, you can limit unauthorized access. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses an Amazon SQS queue between event sources and the Lambda function that consumes those events. This enables Lambda to perform retries without event loss in the case of failure. Additionally, EventBridge is a fully managed and internally resilient service that helps you avoid any single point of failure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses event-driven services like EventBridge, Amazon SQS, and Lambda. This supports asynchronous, responsive behavior so that the solution can react and implement actions promptly. For example, Amazon EC2 instances stop (or terminate) within low-single-digit seconds of their scheduled expiration. This is more effective than a polling-based design, which would check instances for expiration at set intervals, resulting in imprecise implementation. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

EventBridge, Amazon SQS, and Lambda provide a pay-as-you-go pricing model, meaning you pay only for resources used. Because this solution remains idle for extended periods, these cost-elastic services offer significant savings by eliminating compute costs during times of inactivity. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses services that support event-driven, asynchronous, and intermittent behaviors. For example, Lambda only uses compute resources when necessary. And as a shared service, Amazon SQS does not dedicate compute to this Guidance specifically. These aspects make this solution resource efficient, supporting sustainability. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
