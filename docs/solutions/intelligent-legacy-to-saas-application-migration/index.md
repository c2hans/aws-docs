---
source_url: https://docs.aws.amazon.com/solutions/intelligent-legacy-to-saas-application-migration/index.html
---

---
title: 'Guidance for Intelligent Legacy to SaaS Application Migration'
canonical_url: https://docs.aws.amazon.com/solutions/intelligent-legacy-to-saas-application-migration/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Intelligent Legacy to SaaS Application Migration

## Overview

This Guidance demonstrates how organizations can leverage AI-powered tools to streamline and optimize their migration assessment workflows while maintaining decision-making transparency. It helps teams accelerate the often complex and time-consuming assessment process by automating analysis, pattern recognition, and recommendation generation. The solution shows how AI can systematically evaluate migration readiness, identify potential challenges, and provide data-driven justification for strategic decisions. By combining artificial intelligence with established migration best practices, organizations can achieve faster, more accurate assessments while ensuring stakeholders understand the rationale behind each recommendation.

## Benefits

### Accelerate migration assessments

Streamline your application migration assessment process with AI-powered tools built on AWS services. Reduce manual analysis time while gaining deeper insights into your legacy applications' migration requirements.

### Enhance decision transparency

Provide clear justification for migration decisions through structured assessment workflows and comprehensive documentation. The solution leverages Amazon Bedrock Knowledge Bases to incorporate relevant context and best practices into your migration recommendations.

### Simplify complex migrations

Deploy a customizable assessment framework that adapts to your specific migration challenges and requirements. The serverless architecture with AWS Fargate and managed services minimizes operational overhead, allowing your team to focus on migration strategy rather than infrastructure management.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/intelligent-legacy-to-saas-application-migration.pdf)

![Architecture diagram](/images/solutions/intelligent-legacy-to-saas-application-migration/images/intelligent-legacy-to-saas-application-migration-1.png)

1. **Step 1**: Users access a user interface hosted on AWS Amplify, authenticate via Amazon Cognito, and configure the S3 URI path for the migration assessment target location.
1. **Step 2**: Using AWS AppSync, users inspect the workflow code through the Workflow Builder interface, reviewing the logic that will be executed by Strands Agents in an AWS Fargate container. Once validated, users initiate a Docker build process.
1. **Step 3**: AWS CodeBuild executes the Docker container build job and, upon successful completion, pushes the image to Amazon ECR.
1. **Step 4**: Throughout the process, configuration details, build image locations, and related metadata are stored in a DynamoDB table. Downstream systems, including the Strands Agents, reference this data during assessments.
1. **Step 5**: With all assets in place, users trigger an assessment job from the UI, which launches an AWS Fargate task to run the Strands Agents.
1. **Step 6**: The Strands Agents execute the code built from the Workflow Builder, querying Amazon Bedrock Knowledge Bases to retrieve relevant documentation and contextual information as needed.
1. **Step 7**: The assessment completes when AWS Fargate writes reports and results to JSON files, saving them to the Amazon Simple Storage Service (Amazon S3) bucket accessible to the frontend. Users can then review the assessment results through the UI.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-intelligent-legacy-to-saas-application-migration)

[Read usage guidelines](/solutions/guidance-disclaimers/)
