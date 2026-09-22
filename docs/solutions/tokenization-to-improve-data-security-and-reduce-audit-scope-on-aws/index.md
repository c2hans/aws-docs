---
source_url: https://docs.aws.amazon.com/solutions/tokenization-to-improve-data-security-and-reduce-audit-scope-on-aws/index.html
---

---
title: 'Guidance for Tokenization to Improve Data Security and Reduce Audit Scope on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/tokenization-to-improve-data-security-and-reduce-audit-scope-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Tokenization to Improve Data Security and Reduce Audit Scope on AWS

## Overview

This Guidance shows how to build a serverless tokenization framework that replaces sensitive data with unique, formatted identifiers known as "tokens." These tokens can be used in place of the original data in frontend or backend applications, allowing for the generation of tokens, storage of client-side encrypted sensitive data in a token vault, and retrieval of original sensitive data when necessary. The framework incorporates multi-layered security measures to protect tokenization and de-tokenization APIs. By adopting this serverless approach, organizations can enhance data security while reducing the costs and overhead associated with managing and scaling resources for tokenizing customers' sensitive data. Additionally, it lowers the cost of meeting compliance requirements, such as those set by the Payment Card Industry Data Security Standard (PCI DSS), while effectively safeguarding personally identifiable information (PII).

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/tokenization-to-improve-data-security-and-reduce-audit-scope-on-aws.pdf)

![Architecture diagram](/images/solutions/tokenization-to-improve-data-security-and-reduce-audit-scope-on-aws/images/tokenization-to-improve-data-security-and-reduce-audit-scope-on-aws-1.png)

1. **Step 1**: The customer-facing application authenticates with Amazon Cognito and obtains an authorization token to access the tokenization APIs.
1. **Step 2**: The customer-facing application invokes tokenization APIs using Amazon API Gateway with mutual TLS and API keys. The APIs are routed through AWS WAF to enforce the intended access.
1. **Step 3**: API Gateway validates the authorization token and then forwards the requests to the tokenization AWS Lambda function.
1. **Step 4**: The tokenization Lambda function assumes an AWS Identity and Access Management (IAM) role to access the Lambda layer, the AWS Key Management Service (AWS KMS) encryption key, and the Amazon DynamoDB databases.
1. **Step 5**: The tokenization Lambda function uses a verified and version-controlled Lambda layer to generate unique tokens for sensitive data.
1. **Step 6**: The tokenization Lambda layer encrypts the sensitive plaintext using the encryption keys from AWS KMS. The connection uses an Amazon Virtual Private Cloud (Amazon VPC) endpoint with an endpoint policy to provide additional protection. AWS KMS uses a resource policy to validate the permissions for accessing the encryption key.
1. **Step 7**: The encrypt and tokenize Lambda layer sends the tokenized data to the application database and stores the encrypted text in a cipher database for future retrieval. The connection uses an Amazon VPC endpoint with an endpoint policy to provide additional protection. The application database and the cipher database reside in different AWS accounts.
1. **Step 8**: The tokenization Lambda function returns the tokenized data back to the customer-facing application upon request.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS X-Ray and Amazon CloudWatch Logs enable visualization and logging of tokenization transactions across API Gateway, Lambda functions, and Lambda layers. By visualizing traces and collecting logs, users can more easily troubleshoot performance bottlenecks or identify failures. Moreover, the AWS Database Encryption software development kit (SDK) for DynamoDB provides APIs for encryption, decryption, and key management, reducing overhead compared to manual service integrations and cryptographic implementations. Lastly, the included AWS CloudFormation template automates provisioning of required resources, streamlining deployment to support users with quick experimentation, and reducing the overhead of manually configuring services. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The services selected for this Guidance work in tandem to secure API access, protect the sensitive data network, enable fine-grained access control, manage encryption keys to reduce risk, and enforce mutual TLS. Specifically, AWS WAF filters incoming traffic to allow only legitimate access to tokenization APIs, preventing distributed denial of service (DDoS) attacks. Amazon VPC endpoints and AWS PrivateLink control network-level access to DynamoDB tables storing sensitive data and keys. The AWS IAM Access Analyzer provides insights to fine-tune access permissions. AWS KMS manages the encryption keys used by the tokenization Lambda function. Amazon Cognito handles user authentication and authorization for the tokenization APIs. And lastly, the Database Encryption SDK for DynamoDB generates secure data encryption keys from AWS KMS and stores encrypted data in DynamoDB. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The API Gateway API keys help to rate limit APIs for different API clients and set burst rate limits for managing transactions per second. AWS KMS has a request per second quota on cryptographic operations, and API throttling prevents requests from exceeding the current quota limit. Lambda makes the tokenization APIs highly scalable to meet the fluctuating demands of tokenizing sensitive data, while the AWS Serverless Application Model (AWS SAM) simplifies the deployment of new code versions and automation templates. Furthermore, the use of private subnets deployed across multiple Availability Zones (AZs), Regional services with built-in resilience and high availability, multi-AZ Amazon VPC endpoints, and Amazon DynamoDB global tables provide enhanced reliability and availability. AWS SAM also provides a higher-level abstraction on top of CloudFormation to define Lambda functions and enable local unit testing. Collectively, these services provide the framework to help ensure workloads perform their intended functions correctly and consistently, while also enabling quick recovery from failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

API Gateway and Lambda enable near real-time, synchronous, event-driven communication between the client (UI) and server. The Lambda function can also handle thousands of tokenization requests per second in real-time. Similarly, API Gateway can handle thousands of API requests per second in real-time to tokenize sensitive data when a user submits information on a web page. Furthermore, DynamoDB allows for the storage of unstructured information at scale with a latency of less than a few milliseconds. Moreover, DynamoDB provides a low-latency database layer for storing encrypted sensitive information and generated tokens. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The Lambda function allows memory and CPU requirements to be optimized for price and performance using the AWS Lambda Power Tuning tool. Users can also select the Amazon DynamoDB Standard-Infrequent Access (Standard-IA) storage class for workloads that require long-term storage of infrequently accessed data, thereby optimizing storage costs. Both Lambda and DynamoDB provide on-demand and provisioned capacity options to cater to various price and performance scenarios. Lastly, PrivateLink optimizes the data transfer costs by keeping the network traffic within the AWS network and avoiding charges for NAT gateway, a Network Address Translation (NAT) service. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda, API Gateway, and DynamoDB are designed to scale dynamically to meet the demand for optimized resource utilization, thereby reducing the energy usage required to run the servers. These are serverless services that optimize resource utilization and dynamically scale to match the demands of the tokenization and de-tokenization APIs. The storage and compute layers scale dynamically to accommodate the incoming traffic demands, which in turn reduces the overall energy usage and environmental impacts. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Building a serverless tokenization solution to mask sensitive data**: This blog post demonstrates how data obfuscation can be used to reduce the risk of unauthorized access.

[Learn more](https://aws.amazon.com/blogs/compute/building-a-serverless-tokenization-solution-to-mask-sensitive-data/)

- **How to use tokenization to improve data security and reduce audit scope**: This blog post demonstrates how to determine your requirements for tokenization, with an emphasis on the compliance lens given our experience as PCI Qualified Security Assessors (PCI QSA).

[Learn more](https://aws.amazon.com/blogs/security/how-to-use-tokenization-to-improve-data-security-and-reduce-audit-scope/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
