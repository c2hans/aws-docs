---
source_url: https://docs.aws.amazon.com/solutions/capability-insights-for-aws/index.html
---

---
title: 'Guidance for Capability Insights for AWS'
canonical_url: https://docs.aws.amazon.com/solutions/capability-insights-for-aws/
source: aws-documentation
generated_on: 2026-10-22
---

# Guidance for Capability Insights for AWS

## Overview

This Guidance demonstrates how to deploy a private, self-hosted dashboard that provides real-time AWS service, feature, API, and AWS CloudFormation resource availability across all Regions. It helps enterprises accelerate global expansion by eliminating manual regional capability research, auto-generating Region-scoped AWS Identity and Access Management policies and SCPs for proactive governance, and personalizing the view to services your account actually uses via AWS CloudTrail and AWS CloudFormation analysis. The solution includes a conversational AI assistant for natural-language queries, runs entirely within your Amazon Virtual Private Cloud, and integrates directly into CI/CD pipelines—reducing deployment failures and cutting security research time by enabling teams to validate regional readiness before migration.

## Benefits

### Accelerate AWS capability planning

Automatically aggregate and visualize AWS service availability across Regions on a private dashboard, refreshed every 24 hours. Help your teams make faster, more informed decisions about where to deploy workloads without manual research.

### Protect sensitive planning data

Keep capability insights within your own Amazon Virtual Private Cloud using private endpoints, so data never traverses the public internet. Reduce exposure risk while giving authorized users secure, reliable access to the dashboard.

### Reduce operational overhead

Deploy a serverless, event-driven architecture that automatically fetches and merges capability data without manual intervention. Free your teams to focus on strategic planning rather than maintaining data collection processes.

## How it works

This architecture diagram illustrates how to deploy Capability Insights on AWS to collect, merge, and visualize AWS Capability by Region data on a private, VPC-hosted dashboard. [Download the architecture diagram](downloads/capability-insights-for-aws.pdf)

![Architecture diagram for Capability Insights for AWS](/images/solutions/capability-insights-for-aws/images/capability-insights-for-aws-1.png)

1. **Step 1**: A user connects to their User Client (Amazon Elastic Compute Cloud or AWS Client VPN) in the Amazon Virtual Private Cloud over SSH.
1. **Step 2**: The client reaches Amazon API Gateway through the API Gateway VPC Endpoint, and the website through the Amazon S3 Gateway Endpoint.
1. **Step 3**: Amazon API Gateway invokes the API AWS Lambda function to serve requests.
1. **Step 4**: The API AWS Lambda function calls the DataFetch AWS Lambda function via the Lambda Invoke VPC Endpoint.
1. **Step 5**: An Amazon EventBridge scheduled rule triggers the DataFetch AWS Lambda function every 24 hours.
1. **Step 6**: The DataFetch AWS Lambda function pulls capability data from the source Amazon S3 bucket in AWS Capability by Region.
1. **Step 7**: The DataFetch AWS Lambda function writes merged data to the website Amazon S3 bucket.
1. **Step 8**: At deployment, source code is delivered from the capabilities-insights-assets bucket.
1. **Step 9**: Users browse the merged capability data on the dashboard served from the website bucket.
## Related content

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws/capability-insights-for-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
