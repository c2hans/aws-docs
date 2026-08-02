---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/implementation-guide.html
---

# Implementation guide
<a name="implementation-guide"></a>

This guide is organized into focused sections that build upon each other to create comprehensive data perimeter protection for your Amazon Bedrock workloads.

## Core Implementation
<a name="core-implementation"></a>

1. **Identity perimeter** - Establish who can access your AI resources

1. **Resource perimeter** - Control who has access to the resource and what actions they can perform on it

1. **Network perimeter** - Ensure traffic flows through expected network paths

Each section provides detailed implementation guidance with code examples, best practices, and specific considerations for AI workloads. Start with the identity perimeter as it provides the broadest protection, then layer on resource and network controls based on your specific requirements.

## Prerequisites
<a name="prerequisites"></a>

Before implementing the controls in this guide, ensure you have:

**Required knowledge:**
+ Understanding of AWS Identity and Access Management (IAM ) policies and service control policies (SCPs)
+ Familiarity with AWS Organizations and organizational units
+ Basic knowledge of Amazon Bedrock services and features
+ Understanding of VPC networking concepts

## AWS environment requirements:
<a name="aws-environment-requirements"></a>
+ AWS Organizations enabled with multiple accounts (recommended)
+ Appropriate IAM permissions to invoke and configure Amazon Bedrock features.
+ Appropriate IAMpermissions to create and modify SCPs, resource policies, and VPC configurations
+ AWS CloudTrail logging enabled for audit and monitoring

## Replace placeholder values
<a name="replace-placeholder-values"></a>

Throughout this guide, policy examples use placeholder values that you must replace with your actual AWS resource identifiers:
+ `o-1234567890` - Replace with your AWS organization ID (find using: `aws organizations describe-organization`)
+ `123456789012 `- Replace with your AWSaccount ID(s)
+ `us-east-1` - Replace with your deployment region(s)
+ `bedrock-training-data-bucket `- Replace with your actual Amazon S3 bucket names
+ `vpc-12345678` - Replace with your VPC IDs
+ `subnet-ai-workloads-1a` - Replace with your subnet IDs
+ `sg-bedrock-ai-workloads` - Replace with your security group IDs

**Regional considerations:**

Most policy examples in this guide reference us-east-1 as the AWS Region. When implementing these policies in your environment:
+ Adapt region references to match your deployment regions
+ Consider multi-region deployments and ensure policies cover all regions where you operate Amazon Bedrock workloads
+ Be aware that someAmazon Bedrock features and models may have different regional availability
+ For data residency requirements, explicitly restrict operations to approved regions using `aws:RequestedRegion` condition keys

## Getting started
<a name="getting-started"></a>

Your Amazon Bedrock data perimeter implementation follows six foundational building blocks. Each step below provides the essential framework, with detailed implementation guidance, code examples, and best practices covered in the subsequent sections:

1. **Assess your AI environment** - Inventory your foundation models, custom models, knowledge bases, and AI applications. Map data flows from training datasets through inference endpoints to understand your current architecture

1. **Control model access** - Implement service control policies (SCPs) with Amazon Bedrock-specific actions (bedrock:InvokeModel, `bedrock:CreateModelCustomizationJob`) and `aws:ResourceOrgID` conditions to ensure access to your custom models and knowledge bases follows organizational policies

1. **Protect AI data sources** - Deploy resource based policies on resources such as Amazon S3 buckets that contain training data, Amazon OpenSearch Service clusters powering knowledge bases, and other AI data stores using` aws:PrincipalOrgID` to ensure only trusted AI applications can access your datasets

1. **Establish private AI connectivity** - Configure VPC endpoints for Amazon Bedrock with policies that route prompts and model responses through your private networks, particularly important for real-time inference workloads

1. **Monitor AI operations** - Set up AWS CloudTrail logging for Amazon Bedrock API calls and create alerts for model invocations, cross-account model access, and network access patterns that fall outside your defined policies

1. **Test with AI workloads** - Validate your controls support legitimate model training pipelines, knowledge base updates, and inference applications while enforcing your organizational policies

The following sections expand on each building block with step-by-step implementation instructions, policy templates, and monitoring configurations to help you establish a comprehensive data perimeter for your AI workloads.

**Note - Implementation considerations**
+ Apply SCP policies at the root organizational unit to ensure coverage across all accounts
+ Test the policies in a non-production environment first to identify any legitimate cross-organization access needs
+ Document any exceptions and implement them through explicit allow policies rather than modifying the organizational boundary
