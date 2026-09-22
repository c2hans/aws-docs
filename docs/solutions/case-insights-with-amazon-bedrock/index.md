---
source_url: https://docs.aws.amazon.com/solutions/case-insights-with-amazon-bedrock/index.html
---

---
title: 'Guidance for Case Insights with Amazon Bedrock'
canonical_url: https://docs.aws.amazon.com/solutions/case-insights-with-amazon-bedrock/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Case Insights with Amazon Bedrock

## Overview

This Guidance demonstrates how to transform manual AWS cost analysis into an AI-assisted conversational experience using a GenAI-powered Model Context Protocol (MCP) server. Built on Amazon Bedrock and serverless AWS services, it delivers 50+ specialized tools across 10 cost optimization playbooks covering EC2, RDS, S3, Lambda, CloudWatch, and more. By integrating with Kiro CLI and MCP-compatible clients, it enables technical and business users to identify cost-saving opportunities through natural language queries, reducing the complexity of cost optimization while accelerating time-to-insight across AWS environments.

## Benefits

### Accelerate support case resolution

Automatically generate AI-powered summaries, root cause analyses, and resilience classifications for every support case.

### Gain organization-wide case visibility

Consolidate and query support case insights across all AWS accounts through a single, continuously refreshed data layer.

### Integrate insights into existing workflows

Expose processed case data through a standard API for direct access from existing tools and agents.

## How it works

This architecture diagram illustrates how to effectively support Case Insights with Amazon Bedrock on AWS. It shows the key components and their interactions, providing an overview of the architecture's structure and functionality. [Download the architecture diagram](downloads/case-insights-with-amazon-bedrock.pdf)

![Architecture diagram for Case Insights with Amazon Bedrock](/images/solutions/case-insights-with-amazon-bedrock/images/case-insights-with-amazon-bedrock-1.png)

1. **Step 1**: Amazon EventBridge triggers Lambda every 24 hrs.
1. **Step 2**: AWS Lambda connects to AWS Organizations API and retrieves the list of AWS accounts. Creates Amazon Simple Queue Service for each AWS account.
1. **Step 3**: Lambda saves a file with all AWS accounts to an Amazon Simple Storage Service bucket.
1. **Step 4**: For each Amazon SQS message, AWS Lambda processes each case, retrieving metadata and annotation.
1. **Step 5**: For each case, an AWS Step Functions is triggered. Support case annotation is passed into the function.
1. **Step 6**: Amazon Bedrock is called three times, once to produce a summary, then this summary is passed onto two more Amazon Bedrock calls for RCA and Resilience Lifecycle classifications.
1. **Step 7**: When the step function completes it writes a data.json file with all case details to Amazon S3. This completes case analysis.
1. **Step 8**: Customers can call the MCP from their agent of choice via Amazon API Gateway which calls a Lambda.
1. **Step 9**: Lambda retrieves the case details from Amazon Athena.
1. **Step 10**: AWS Glue runs every 24 hrs to refresh the table within Amazon Athena with any new cases processed.
[Read usage guidelines](/solutions/guidance-disclaimers/)
