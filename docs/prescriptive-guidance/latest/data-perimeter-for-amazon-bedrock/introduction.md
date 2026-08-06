---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/introduction.html
---

# Data perimeter for Amazon Bedrock: Securing generative AI workloads
<a name="introduction"></a>

*Prashanth Sivarajan and Manigandan Shri, Amazon Web Services*

[Data Perimeter on AWS](https://aws.amazon.com/identity/data-perimeters-on-aws/) is a security strategy and set of controls designed to help ensure that only trusted identities can access trusted resources from expected networks within your AWS  environment. It acts as a robust, coarse-grained boundary around your data, complementing fine-grained access controls and helping remediate unauthorized data access and exfiltration.

This article provides a comprehensive guide to address the AI-specific requirements by establishing perimeter controls around foundation models, custom models, knowledge bases, and the data that flows between them. It provides a structured implementation approach using Amazon Bedrock-specific policies and monitoring to ensure your AI applications operate within defined organizational boundaries.

This guidance is intended for Cloud architects and security engineers building a secure-by-default AI solution with Amazon Bedrock on AWS .

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/images/guide-img/4f7d8782-326c-45ca-95dd-0c4e97e42271/images/9344ca1b-063b-4fed-925f-a3804c891a94.png)

## Overview
<a name="overview"></a>

Amazon Bedrock workloads have unique characteristics that benefit from specialized data perimeter approaches. When you invoke foundation models, your prompts may contain business data, custom models store training datasets, and knowledge bases aggregate organizational documents. These AI-specific assets have different access patterns and data flows compared to traditional AWSresources.

Amazon Bedrock workloads often involve distributed architectures spanning multiple accounts for model sharing, automated pipelines for data processing, and real-time inference endpoints.

This distributed nature creates additional considerations for implementing effective perimeter controls.

A data perimeter for Amazon Bedrock addresses these challenges through three AI-focused objectives:

### Data perimeter objectives for Amazon Bedrock
<a name="data-perimeter-objectives-for-9999999999999999brlong-.bd071608-def8-5abd-aebf-fbd18a56ce88"></a>

|
|
| Objective | Definition | Applied on | Using | Implementation Examples |
| --- |--- |--- |--- |--- |
| **Identity Perimeter** | Only trusted identities can access my resources | Resources | Resource-based policy | + Organizational boundary enforcement<br />+ Training data Amazon S3 bucket protection<br />+ Amazon CloudWatch logs access control<br />+ AWS KMS key policies for encryption<br />+ AWS Lambda function invocation restricted to Amazon Bedrock Agents |
| Only trusted identities are allowed from my network | Network | + Amazon VPC endpoint policy | + Amazon VPC endpoint policy restricts access to protected resources only for trusted entities.<br />+  Knowledge base data isolation (Amazon OpenSearch/Amazon S3) |
| **Resource Perimeter** | My identities can access only trusted resources | Identities | Service control policies (SCP) | + Model-specific access controls (foundation and custom models)<br />+ IAM Path-based environment separation<br />+ Service principal restrictions with confused deputy protection<br />+ Cross-service integration controls (AWS Lambda, Amazon DynamoDB, Amazon S3)<br />+ Tag-based resource access (ABAC) |
| Only trusted resources can be accessed from my network | Network | + Amazon VPC endpoint policy | + Amazon VPC endpoint policy restricts access to protected resources only for trusted entities. |
| **Network Perimeter** | My identities can access resources only from expected networks | Identities | Service control policies (SCP) | + Amazon VPC endpoint enforcement for Amazon Bedrock API calls<br />+ Deny public internet access to models |
| My resources can only be accessed from expected networks | Resources | Resource-based policy | + Knowledge base network controls (Amazon OpenSearch domain and Amazon S3vector store VPC endpoint enforcement)<br />+ Amazon VPC endpoint network access controls for Amazon Bedrock resources |

These preventive guardrails are critical for Amazon Bedrock deployments where sensitive prompts, training datasets, and model artifacts require protection from unauthorized access and data exfiltration.

For example, a healthcare organization using Amazon Bedrock to analyze patient records needs to ensure:
+ Their custom medical models are only accessible by authorized clinical applications
+ Their AI systems never send data to external models
+ All patient prompts travel through HIPAA-compliant network paths

## Business Outcome
<a name="business-outcome"></a>

Implementing these controls provides clear visibility into data access patterns, streamlines compliance reporting, and establishes consistent security policies across AI workloads. This creates a foundation for scaling AI initiatives while maintaining operational control and meeting regulatory requirements. The approach enables teams to innovate confidently while maintaining security baseline.
