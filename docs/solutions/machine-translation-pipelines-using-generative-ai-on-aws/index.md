---
source_url: https://docs.aws.amazon.com/solutions/machine-translation-pipelines-using-generative-ai-on-aws/index.html
---

---
title: 'Guidance for Machine Translation Pipelines Using Generative AI on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/machine-translation-pipelines-using-generative-ai-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Machine Translation Pipelines Using Generative AI on AWS

## Overview

This Guidance shows how to improve your content localization processes using foundation models. It provides a blueprint for building modern localization capabilities, addressing both real-time and batch translation needs. The Guidance combines established localization practices, such as translation memory management, with newer approaches, such as automated quality prediction and evaluation. Implementing these techniques can help you reduce costs and speed up your time-to-market for localized content. As a result, you'll be able to enhance your global communication efforts and maintain quality content that resonates across different markets and languages.

## Benefits

### Accelerate multilingual content delivery

Deploy an automated translation pipeline that combines foundation models with quality assessment, reducing manual review cycles. Enable faster time-to-market while maintaining translation quality standards.

### Optimize translation quality and costs

Leverage AI-powered quality scoring and assessment to identify which content needs human review. Reduce costly manual reviews while ensuring consistent translation quality across all content.

### Enhance operational efficiency securely

Implement a fully managed translation workflow with built-in security controls and automated orchestration. Focus on content strategy while AWS handles infrastructure management and security.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/machine-translation-pipelines-using-generative-ai-on-aws.pdf)

![Architecture diagram](/images/solutions/machine-translation-pipelines-using-generative-ai-on-aws/images/machine-translation-pipelines-using-generative-ai-on-aws-1.png)

1. **Step 1**: The user uploads source text to the Amazon Simple Storage Service (Amazon S3) input bucket to initiate the translation process.
1. **Step 2**: Amazon EventBridge invokes AWS Step Functions to start the translation workflow.
1. **Step 3**: An AWS Lambda function begins the Step Functions execution, receiving configuration parameters from Parameter Store, a capability of AWS Systems Manager, for secure management.
1. **Step 4**: Lambda fetches the translation memory from Amazon Relational Database Service (Amazon RDS) Aurora PostgreSQL and generates translation prompts.
1. **Step 5**: Lambda stores translation prompts in the S3 input bucket.
1. **Step 6**: Lambda invokes foundation models hosted on Amazon Bedrock to perform machine translation.
1. **Step 7**: The translated outputs from Amazon Bedrock are stored in the S3 model output bucket.
1. **Step 8**: Lambda invokes Amazon Bedrock for LLM-driven qualitative assessment.
1. **Step 9**: Quality assessment results from Amazon Bedrock are stored in the S3 consolidated results bucket.
1. **Step 10**: Lambda invokes the Amazon SageMaker AI endpoint for COMET ML score estimation.
1. **Step 11**: SageMaker AI evaluation results are consolidated with the output and stored in the S3 consolidated results bucket.
1. **Step 12**: AWS Glue prepares the consolidated results for end-user consumption and analysis.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-machine-translation-pipelines-using-generative-ai-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
