---
source_url: https://docs.aws.amazon.com/solutions/generating-infrastructure-as-code-templates-from-architecture-diagrams-on-aws/index.html
---

---
title: 'Guidance for Generating Infrastructure-as-Code Templates from Architecture Diagrams on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/generating-infrastructure-as-code-templates-from-architecture-diagrams-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Generating Infrastructure-as-Code Templates from Architecture Diagrams on AWS

## Overview

This Guidance demonstrates how to transform architecture diagrams into Infrastructure as Code (IaC) templates using AI, addressing the challenge of time-consuming manual coding for solutions targeted for AWS deployments. The process begins when users upload diagrams through a web interface, where advanced AI models analyze the image and generate a comprehensive summary. A step-by-step workflow then creates AWS CDK code with appropriate IAM permissions, storing the deployable code in S3 and notifying users via email upon completion. You can accelerate your solution builds and deployments by 80-90% while ensuring adherence to your organization’s specific best practices and development guidelines.

## Benefits

### Accelerate cloud architecture deployment with AI-powered automation

Transform architecture diagrams into deployable infrastructure code through an intelligent, serverless workflow. This solution reduces manual coding efforts and accelerates time-to-market by automatically generating AWS CDK stacks from visual representations of your architecture.

### Enhance architecture quality with AI-guided implementation

Leverage advanced AI models to analyze architecture diagrams and generate comprehensive documentation and implementation code that adheres to AWS Well-Architected best practices. This approach ensures consistent quality and reduces the risk of misconfigurations in your cloud deployments.

### Streamline developer workflows with visual-to-code transformation

Enable your teams to design architectures visually and automatically convert them to production-ready code. This visual-first approach bridges the gap between design and implementation, improving collaboration between architects and developers while maintaining governance through standardized CDK deployments.

### Tailor code generation to your organization’s standards

Seamlessly integrate your organization’s specific guidelines and best practices into the AI-driven code generation process. This customizable approach ensures that all generated infrastructure code inherently complies with your unique specifications, maintaining consistency and governance across your cloud deployments while reducing the need for manual adjustments after generation.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/developing-infrastructure-as-code-templates-from-architecture-diagrams-on-aws.pdf)

![Architecture diagram](/images/solutions/generating-infrastructure-as-code-templates-from-architecture-diagrams-on-aws/images/generating-infrastructure-as-code-templates-from-architecture-diagrams-on-aws-1.png)

1. **Step 1**: Users upload an AWS architecture diagram via a React Web UI hosted on AWS Fargate, fronted by Amazon CloudFront using AWS Cognito authentication, supported by an Application Load Balancer.
1. **Step 2**: The uploaded diagram is sent to an AWS Lambda function within the Fargate Target group, that is invoked via the WebUI, using path based routing.
1. **Step 3**: The Web UI responder Lambda invokes Amazon Bedrock API, leverages Claude 3.7 Sonnet, to perform Image analysis. The image is also stored in Amazon Simple Storage Service (Amazon S3).
1. **Step 4**: A comprehensive summary of the architecture describing the use case, workflow and the different AWS services used is generated and returned to the Web UI.
1. **Step 5**: The Web UI Responder invokes an AWS Step Function. The Step Function passes the architecture description to an agentic workflow within the Code Generator Lambda function for AWS CDK Stack generation.
1. **Step 6**: The code generator lambda invokes the Perplexity LLM repeatedly in a sequential manner using pre-engineered, elaborate prompts to understand individual modules from the image analysis, evolve the CDK Stack and associated IAM roles, policies for each module in parallel. The LLM leverages inbuilt tool use capabilities to access a search index and retrieve the most recent CDK constructs and IAM permissions to generate deployable code.
1. **Step 7**: The generated code is stored in an Amazon S3 bucket.
1. **Step 8**: After a successful execution of the workflow, the user receives a Amazon Simple Notification Service (Amazon SNS) notification via E-mail.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-developing-infrastructure-as-code-templates-from-architecture-diagrams-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
