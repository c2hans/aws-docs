---
source_url: https://docs.aws.amazon.com/solutions/ivr-migration-to-amazon-connect-using-generative-ai-on-aws/index.html
---

---
title: 'Guidance for IVR Migration to Amazon Connect Customer Customer Using Generative AI on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/ivr-migration-to-amazon-connect-using-generative-ai-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for IVR Migration to Amazon Connect Customer Customer Using Generative AI on AWS

## Overview

This Guidance demonstrates a streamlined approach to modernizing contact centers by migrating legacy interactive voice response (IVR) and chatbot systems to Amazon Lex and Amazon Connect Customer Customer. Through innovative generative AI tools and automated conversion utilities, the Guidance significantly reduces migration timeframes from months to weeks. The Guidance preserves existing business logic and customer experience while providing comprehensive testing capabilities. Specifically designed to support migrations from solutions like Nuance, this standardized methodology addresses common transition challenges. Organizations can achieve faster implementation, minimize migration risks, and seamlessly integrate with AWS services to transform their contact center operations.

## Benefits

### Accelerate contact center modernization

Transform legacy IVR systems into intelligent conversational experiences using generative AI-powered automation. Reduce migration time and costs while maintaining business continuity.

### Streamline migration validation workflows

Leverage automated schema validation and testing workflows to help ensure accuracy and reliability. Gain near real-time visibility into migration progress while minimizing operational risks.

### Scale customer service on demand

Deploy a scalable, cloud-native contact center solution that integrates seamlessly with Amazon Connect Customer Customer. Enhance customer experiences while reducing infrastructure management overhead.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/ivr-migration-to-amazon-connect-using-generative-ai-on-aws.pdf)

![Architecture diagram](/images/solutions/ivr-migration-to-amazon-connect-using-generative-ai-on-aws/images/ivr-migration-to-amazon-connect-using-generative-ai-on-aws-1.png)

1. **Step 1**: Access the migration tool's React web application through Amazon CloudFront, secured by Amazon Cognito and AWS WAF.
1. **Step 2**: Initiate bot creation by uploading source specification files through the web application, which triggers Amazon API Gateway and AWS Lambda.
1. **Step 3**: Store migration metadata and configuration settings in Amazon DynamoDB. Store migration files and generated bot definitions in Amazon S3.
1. **Step 4**: The migration API creates the bot and bot locale in Amazon Lex.
1. **Step 5**: AWS Lambda sends a message to Amazon EventBridge, triggering AWS Step Functions workflows.
1. **Step 6**: The schema generation workflow generates the Amazon Lex resource definition from the source specification file using Amazon Bedrock.
1. **Step 7**: The test set generation workflow generates the test set from the source specification file using Amazon Bedrock and uploads it to Amazon Lex.
1. **Step 8**: The schema validation workflow uses generated schema definitions to validate Amazon Lex resource creation. It implements a continuous improvement cycle by incorporating validation error messages and tests execution results to iteratively refine the schema specifications.
1. **Step 9**: Live status updates are streamed using AWS AppSync Events real-time WebSocket connections, providing immediate visibility into each stage of the workflow's progression.
1. **Step 10**: Access the migrated chatbot and IVR functionality through Amazon Connect Customer.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-ivr-migration-to-amazon-connect-using-generative-ai-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
