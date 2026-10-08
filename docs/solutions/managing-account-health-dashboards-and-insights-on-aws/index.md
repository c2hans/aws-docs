---
source_url: https://docs.aws.amazon.com/solutions/managing-account-health-dashboards-and-insights-on-aws/index.html
---

---
title: 'Guidance for Managing Account Health Dashboards and Insights on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/managing-account-health-dashboards-and-insights-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Managing Account Health Dashboards and Insights on AWS

## Overview

This Guidance demonstrates how to analyze AWS Health events across multiple AWS accounts using natural language queries and generative business intelligence. Organizations managing thousands of AWS resources can transform operations and security monitoring at scale, transitioning from manual processing to automated analysis. This Guidance enables site reliability engineering (SRE) teams and leadership to gain quick, comprehensive insights into the health of their AWS environment through intuitive queries. This approach streamlines monitoring of service health, planned changes, and other critical AWS notifications, making it easier to maintain optimal performance and respond to potential issues proactively.

## Benefits

### Centralize health monitoring across your organization

Deploy a unified health monitoring system that automatically collects and consolidates AWS Health events from multiple accounts into an interactive, customizable dashboard. Gain comprehensive visibility into service health across your entire AWS environment.

### Accelerate incident response with natural language queries

Transform complex health data into actionable insights using Amazon Q's natural language capabilities. Quickly identify impacted resources by asking simple questions like "Show me impacted Lambda resources," enabling faster problem diagnosis and resolution.

### Reduce operational overhead through automation

Eliminate manual health event processing with a serverless pipeline that automatically collects, transforms, and visualizes AWS Health data in real time. Enable your technical teams to focus on innovation rather than monitoring.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/managing-account-health-dashboards-and-insights-on-aws.pdf)

![Architecture diagram](/images/solutions/managing-account-health-dashboards-and-insights-on-aws/images/managing-account-health-dashboards-and-insights-on-aws-1.png)

1. **Step 1**: AWS Health generates events, which are sent to the default event bus in a member or linked account. There can be multiple member accounts.
1. **Step 2**: A corresponding Amazon EventBridge default event bus directs events to a centralized bus upon pattern matching.
1. **Step 3**: The EventBridge custom event bus then routes the events to Amazon Data Firehose.
1. **Step 4**: Firehose processes and stores the events in an Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 5**: The Amazon S3 bucket is used as a data source for the health insights dataset.
1. **Step 6**: Amazon Athena queries the events data stored in the Amazon S3 bucket.
1. **Step 7**: An AWS Health insights dashboard is created in Amazon QuickSight. The health insight dashboard is a consolidated view of your AWS accounts and AWS Health insights.
1. **Step 8**: Amazon Q is enabled on the analysis through an Amazon Q topic. The Amazon Q topic enables QuickSight to interpret natural language queries to facilitate the development of visuals in the health insights dashboard. Authenticated users can access Amazon Q in QuickSight.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/aws-health-events-insight)

[Read usage guidelines](/solutions/guidance-disclaimers/)
