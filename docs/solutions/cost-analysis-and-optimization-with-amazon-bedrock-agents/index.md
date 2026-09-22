---
source_url: https://docs.aws.amazon.com/solutions/cost-analysis-and-optimization-with-amazon-bedrock-agents/index.html
---

---
title: 'Guidance for Cost Analysis and Optimization with Amazon Bedrock Agents'
canonical_url: https://docs.aws.amazon.com/solutions/cost-analysis-and-optimization-with-amazon-bedrock-agents/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Cost Analysis and Optimization with Amazon Bedrock Agents

## Overview

This Guidance shows how to analyze and optimize AWS service costs using Amazon Nova language model and automated workflows. The Guidance combines Amazon Bedrock Agents with AWS Lambda functions to generate cost forecasts and specific savings recommendations, all while keeping implementation costs low. Organizations can deploy this self-managed system to make better decisions about their AWS resource usage and spending without requiring significant upfront investment or ongoing maintenance.

## Benefits

### Streamline FinOps with intelligent agents

Deploy specialized Amazon Bedrock Agents that automatically route cost inquiries to the appropriate analysis or optimization workflows, reducing manual effort while providing consistent, accurate financial insights across your organization.

### Accelerate cost optimization decisions

Enable stakeholders to interact naturally with AI agents that access AWS Cost Explorer and Trusted Advisor recommendations in real-time. Make data-driven cost decisions faster without navigating multiple AWS consoles or dashboards.

### Simplify cloud financial management

Implement a secure, authentication-enabled solution that combines cost analysis and optimization in one conversational interface. Focus on acting on financial insights rather than gathering and interpreting complex AWS billing data.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/cost-analysis-and-optimization-with-amazon-bedrock-agents.pdf)

![Architecture diagram](/images/solutions/cost-analysis-and-optimization-with-amazon-bedrock-agents/images/cost-analysis-and-optimization-with-amazon-bedrock-agents-1.png)

1. **Step 1**: The administrator user deploys the Guidance to an AWS Account and AWS Region using an AWS CloudFormation template. The base CloudFormation stack will deploy and create all the AWS resources needed to host the Guidance. This includes the Amazon Cognito user group and user, Amazon Bedrock Agents, AWS Lambda functions, AWS Identity and Access Management (IAM) roles, and an AWS Security Token Service (AWS STS) token.
1. **Step 2**: The user navigates to the secure chat UI URL.
1. **Step 3**: The secure chat application is hosted on AWS Amplify.
1. **Step 4**: The page is returned with HTML, CSS, and JavaScript. The user can then input the configuration details for Amazon Cognito and Amazon Bedrock Agents.
1. **Step 5**: Upon configuration completion, the user is prompted to authenticate using Amazon Cognito with a username and password configured for them in the user pool.
1. **Step 6**: After successful authentication, Amazon Cognito identity pool will negotiate temporary credentials from AWS STS.
1. **Step 7**: Amazon Cognito identity pool passes temporary AWS credentials to the secure chat UI.
1. **Step 8**: Once authenticated, the user will see the secure chat UI prompt to interact with the Amazon Bedrock Agent that is configured.
1. **Step 9**: The FinOps Supervisor Agent evaluates each user's question and directs it to one of two specialized sub-agents: the Cost Analysis Agent or the Cost Optimization Agent.
1. **Step 10**: Each specialized agent (Cost Analysis or Cost Optimization) reviews its predefined set of actions to identify the correct procedure for answering the user's question.
1. **Step 11**: The action groups execute their respective Lambda functions to fetch data, whether that includes accessing the AWS Cost Explorer API or pulling recommendations from the AWS Trusted Advisor Cost Optimization pillar.
1. **Step 12**: The FinOps Supervisor Agent compiles all the gathered data into a final answer and sends it back to the secure chat UI visible to the user.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/compute/cost-analysis-and-optimization-with-amazon-bedrock-agents.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-cost-analysis-and-optimization-with-amazon-bedrock-agents)

[Read usage guidelines](/solutions/guidance-disclaimers/)
