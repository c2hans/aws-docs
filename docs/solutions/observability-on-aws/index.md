---
source_url: https://docs.aws.amazon.com/solutions/observability-on-aws/index.html
---

---
title: 'Guidance for Observability on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/observability-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Observability on AWS

## Overview

This Guidance helps you implement the observability capability in your cloud environment. Observability enables you to gather and analyze operational data about system and application activities. This includes the analysis of data to identify anomalies, indicators of compromise, performance, and configuration changes. Building observability into your cloud foundation will help you establish a reliable, secure, and scalable environment to deploy, operate, and govern your cloud workloads.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram PDF](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/observability-on-aws.pdf)

![Architecture diagram](/images/solutions/observability-on-aws/images/observability-on-aws-1.png)

1. **Step 1**: Deploy and configure log analysis tools and filters to identify key events within your AWS Organization using sources from an AWS CloudTrail organization trail and events in Amazon EventBridge.
1. **Step 2**: Centralize log visibility across your AWS Organization using Amazon CloudWatch cross-account observability.
1. **Step 3**: Build CloudWatch metrics to filter and alert based on key performance indicators and operational events.
1. **Step 4**: Build and share dashboards and visualizations using CloudWatch, and set up CloudWatch alarms that notify you when resources reach a pre-defined threshold.
1. **Step 5**: Centralize persistent long-term log storage for CloudWatch logs, CloudTrail logs, and AWS Config logs to manage lifecycle and cost optimization.
1. **Step 6**: Implement automated log archival by exporting CloudWatch logs to a centralized Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 7**: Centralize operational and security events across your AWS Organization by using EventBridge and EventBridge rules.
1. **Step 8**: Define EventBridge rules to send notifications to actionable team members using Amazon Simple Notification Service (Amazon SNS) topics.
[Read usage guidelines](/solutions/guidance-disclaimers/)
