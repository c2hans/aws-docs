---
source_url: https://docs.aws.amazon.com/solutions/generating-a-bill-of-materials-from-blueprints-on-aws/index.html
---

---
title: 'Guidance for Generating a Bill of Materials from Blueprints on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/generating-a-bill-of-materials-from-blueprints-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Generating a Bill of Materials from Blueprints on AWS

## Overview

This Guidance demonstrates how to automate the extraction of material takeoffs, door and window schedules, and wall assemblies from architectural blueprint PDFs using AI-powered vision analysis. Users upload blueprint PDFs through a web application that orchestrates a multi-agent pipeline powered by Claude on Amazon Bedrock. The pipeline splits PDFs into pages, analyzes each page with vision-capable models to extract structured data, then consolidates and validates results across multiple agents to ensure accuracy. You can reduce manual takeoff time from hours to minutes while minimizing human error in quantity estimates and material lists.

## Benefits

### Automate blueprint material extraction at scale

Replace manual blueprint review with a multi-agent AI pipeline that extracts material takeoffs, schedules, and assemblies from your PDFs in minutes instead of hours.

### Ensure accuracy with self-correcting outputs

Rely on built-in audit and remediation agents that cross-reference extracted data and automatically regenerate results when inconsistencies are detected, reducing costly material errors.

### Optimize costs with serverless AI processing

Process blueprints on demand without provisioning infrastructure. Use a dual-model strategy that pairs vision analysis with efficient summarization to balance accuracy and cost.

## How it works

This architecture diagram shows how a multi-agent pipeline powered by Amazon Bedrock automates extraction of quantities, schedules, and assemblies at scale. [Download the architecture diagram.](downloads/generating-a-bill-of-materials-from-blueprints-on-aws.pdf)

![Architecture diagram for Generating a Bill of Materials from Blueprints on AWS](/images/solutions/generating-a-bill-of-materials-from-blueprints-on-aws/images/generating-a-bill-of-materials-from-blueprints-on-aws.png)

1. **Step 1**: Access the web application hosted on AWS Amplify and authenticate through Amazon Cognito, which issues JWT tokens validated by Amazon API Gateway via a Amazon Cognito authorizer.
1. **Step 2**: Request a pre-signed URL through Amazon API Gateway, which invokes AWS Lambda to generate it. Then upload the blueprint PDF directly to Amazon Simple Storage Service using the pre-signed URL.
1. **Step 3**: The web application invokes Amazon Bedrock AgentCore Runtime, a low-latency serverless environment with session isolation that hosts and operates the multi-agent analysis pipeline.
1. **Step 4**: The PDF Splitter agent reads the uploaded blueprint from Amazon S3 and renders pages to images. Page Analyzer agents analyze each page using Anthropic's Claude Opus via Amazon Bedrock for vision-based extraction.
1. **Step 5**: Material Extractor and Summarizer agents consolidate material takeoffs, door/window schedules, and wall assemblies across pages using Anthropic's Claude Sonnet via Amazon Bedrock.
1. **Step 6**: The Auditor agent cross-references results and the Remediator agent regenerates the project summary if critical issues are found, ensuring output accuracy.
1. **Step 7**: Amazon Bedrock AgentCore Runtime stores structured JSON and markdown results in Amazon S3 (encrypted at rest) and writes job metadata to Amazon DynamoDB (encrypted at rest) upon pipeline completion. Amazon CloudWatch provides pipeline metrics and logging.
1. **Step 8**: You view structured results and ask follow-up questions via the Chat Agent, hosted on Amazon Bedrock AgentCore Runtime, which retrieves analysis context from Amazon S3.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-generating-a-bill-of-material-from-blueprints-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
