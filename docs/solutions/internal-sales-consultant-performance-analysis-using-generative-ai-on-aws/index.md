---
source_url: https://docs.aws.amazon.com/solutions/internal-sales-consultant-performance-analysis-using-generative-ai-on-aws/index.html
---

---
title: 'Guidance for Internal Sales Consultant Performance Analysis using Generative AI on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/internal-sales-consultant-performance-analysis-using-generative-ai-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Internal Sales Consultant Performance Analysis using Generative AI on AWS

## Overview

This Guidance demonstrates how to transform sales team performance through AI-powered near real-time coaching that analyzes Internet Sales Consultant (ISC) and Inside Sales Representative (ISR) interactions with potential customers. By providing immediate, actionable feedback at the end of each call—including performance scoring, conversation summaries, and constructive recommendations—sales professionals can continuously improve their techniques and customer engagement skills. The solution integrates seamlessly with CRM systems to streamline sales processes, enhance customer experiences, and drive higher conversion rates and revenue growth through data-driven performance insights.

## Benefits

### Accelerate sales rep skill development

Receive immediate, actionable feedback within seconds of each customer call. Enable continuous improvement through AI-powered performance insights that identify strengths and opportunities, helping your team refine techniques and close more deals faster.

### Scale coaching without increasing overhead

Deliver consistent, objective performance evaluation across your entire sales organization without expanding management resources. Provide every representative with personalized coaching insights that would be impossible to achieve through manual review alone.

### Integrate seamlessly with existing workflows

Deploy AI-powered coaching that works within your current CRM system, requiring minimal operational changes. Maintain your established sales processes while enhancing them with intelligent feedback that appears exactly when and where your team needs it.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/internal-sales-consultant-performance-analysis-using-generative-ai-on-aws.pdf)

![Architecture diagram](/images/solutions/internal-sales-consultant-performance-analysis-using-generative-ai-on-aws/images/internal-sales-consultant-performance-analysis-using-generative-ai-on-aws-1.png)

1. **Step 1**: Salesforce triggers the API hosted on Amazon API Gateway to initiate the performance review flow when a customer call ends.
1. **Step 2**: Amazon API Gateway receives initial triggers/requests from Salesforce. An AWS Lambda function validates the Salesforce outbound message object and acknowledges the call with 200 OK.
1. **Step 3**: The ReceiveTriggerFunction AWS Lambda function initiates the workflow when it receives new interaction data.
1. **Step 4**: AWS Step Functions orchestrates the workflow. The CallSalesforce AWS Lambda function retrieves transcript data, customer notes, and past context from Salesforce via an API.
1. **Step 5**: A "Check Transcript" decision point determines if the transcript is ready for analysis.
1. **Step 6**: The system enters a WAIT STATE if the transcript is not ready.
1. **Step 7**: When ready, the CallBedrock AWS Lambda function leverages the fully managed Amazon Bedrock service for generative AI-powered analysis of ISC interactions leveraging prompt engineering patterns. The foundation model will consider the customer context, history, and conversation, adhering to data privacy requirements to generate performance score, explanation, and constructive feedback while maintaining customer data.
1. **Step 8**: The WriteFeedback AWS Lambda function processes the analysis results and generates structured feedback. It sends this feedback back to Salesforce via an API, which displays it as a banner or pop-up for the ISR within seconds.
1. **Step 9**: Amazon DynamoDB maintains status tracking throughout the entire process for debugging and auditing purposes. AWS Secrets Manager stores credentials for Amazon DynamoDB and Salesforce access.
[Read usage guidelines](/solutions/guidance-disclaimers/)
