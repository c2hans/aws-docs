---
source_url: https://docs.aws.amazon.com/solutions/composable-web-analytics-on-aws/index.html
---

---
title: 'Guidance for Composable Web Analytics on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/composable-web-analytics-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Composable Web Analytics on AWS

## Overview

This Guidance demonstrates how to build a comprehensive web analytics platform by combining AWS services with partner solutions like Snowplow and Databricks. It helps organizations transition from traditional analytics tools to a customizable, privacy-focused architecture that leverages existing data infrastructure. The solution enables rapid deployment while maintaining full control over data storage and analysis. Through integration with AWS QuickSight Q's generative BI capabilities, organizations can derive deeper customer journey insights, enabling enhanced personalization and improved customer satisfaction through data-driven decision making.

## Benefits

### Own your web analytics data

Store web interaction data securely in your existing data lake environment. Reduce dependency on third-party analytics providers for customer journey insights.

### Unlock AI-powered analytics insights

Ask questions about your web analytics data using natural language and get instant answers. Create interactive dashboards to visualize customer journeys and identify growth opportunities.

### Enable secure marketing collaboration

Share web analytics data with publisher partners in privacy-enhanced environments for conversion analysis. Measure marketing effectiveness without implementing additional third-party trackers.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/composable-web-analytics-on-aws.pdf)

![Architecture diagram](/images/solutions/composable-web-analytics-on-aws/images/composable-web-analytics-on-aws-1.png)

1. **Step 1**: Snowplow's Collect application automatically captures user interactions from websites and mobile apps through embedded code snippets. The application runs on Amazon Elastic Compute Cloud (Amazon EC2) via Amazon Elastic Kubernetes Service (Amazon EKS). The Validate application validates this event data against the predefined schema stored in the schema registry. The Information is stored in Amazon Relational Database Service (Amazon RDS PostgreSQL). The optional Enrich application uses integrations built with first-party and third-party data sources through APIs to enrich the events for better insights.
1. **Step 2**: Post enrichment, the event data is sent to Amazon Kinesis Data Streams in near real-time. Amazon Kinesis Data Streams delivers enriched events to a custom Databricks loader application in Amazon EKS.
1. **Step 3**: The Databricks loader stores raw data to the existing Databricks volume (bronze layer) which is backed by Amazon Simple Storage Service (Amazon S3), ensuring privacy and ownership.
1. **Step 4**: Databricks Lakehouse processes the raw data using Snowplow's Data models (dbt models) on Databricks compute to create structured, analysis-ready datasets (sliver/gold layers) for better insights.
1. **Step 5**: The Analytics Stack supports Generative BI capabilities for customers to unlock additional use cases using AWS Services. Use Amazon QuickSight for User Journey visualization. QuickSight provides unified Business Intelligence (BI) capabilities for Analytics and dashboarding to support various personas within the organization and externally. Use Amazon Q in QuickSight to create reports and dashboards, and to interact with web analytics data using natural language to analyze user journeys and identify customer segments. Use web interaction data in AWS Clean Rooms and collaborate with publisher partners to perform marketing conversion analysis and measurements in a privacy enhanced manner. This reduces the need for third-party trackers on the web and mobile apps required for marketing measurements.
[Read usage guidelines](/solutions/guidance-disclaimers/)
