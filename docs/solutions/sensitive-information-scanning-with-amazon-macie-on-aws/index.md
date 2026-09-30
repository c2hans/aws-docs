---
source_url: https://docs.aws.amazon.com/solutions/sensitive-information-scanning-with-amazon-macie-on-aws/index.html
---

---
title: 'Guidance for Sensitive Information Scanning with Amazon Macie on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/sensitive-information-scanning-with-amazon-macie-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Sensitive Information Scanning with Amazon Macie on AWS

## Overview

This Guidance demonstrates how organizations can leverage Amazon Macie to enhance their data security posture by systematically scanning artifacts for sensitive information. It shows a flexible, prescriptive architecture that can be seamlessly integrated into existing applications or deployed as a standalone microservice. The guidance helps businesses protect valuable data assets by identifying and securing PII, financial information, and credentials. By showcasing the interaction between Macie and other AWS services, this architecture empowers companies to implement robust data discovery and protection measures, ultimately reducing the risk of data breaches and ensuring compliance with data privacy regulations.

## Benefits

### Enhance data protection workflows

Deploy automated scanning that streamlines sensitive information discovery with instant alerts. Reduce compliance overhead through continuous monitoring and detailed audit trails.

### Streamline security workflows

Focus on core business value with a ready-to-implement scanning architecture. Eliminate infrastructure management while maintaining enterprise-grade security controls.

### Simplify security operations

Reduce operational complexity through centralized monitoring and automated response workflows. Free up security teams to focus on high-value activities rather than infrastructure management.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/sensitive-information-scanning-with-amazon-macie-on-aws.pdf)

![Architecture diagram](/images/solutions/sensitive-information-scanning-with-amazon-macie-on-aws/images/sensitive-information-scanning-with-amazon-macie-on-aws-1.png)

1. **Step 1**: The application initiates an Amazon Macie scan request and subscribes to Amazon Macie job completion events by providing a pre-created Amazon EventBridge Event bus ARN. The application calls Amazon API Gateway using Temporary security credentials. AWS Web Application Firewall (AWS WAF) protects calls to API Gateway.
1. **Step 2**: An AWS Lambda function creates a sensitive data discovery job by invoking the Macie API.
1. **Step 3**: Macie scans all objects in the specified Amazon S3 documents to scan bucket to look for sensitive information. Macie uses the customer managed AWS Key Management Service (AWS KMS) key(s) to decrypt the Amazon S3 objects.
1. **Step 4**: Macie stores the scan results and findings in the Amazon S3 results/findings bucket and encrypts the results/findings using a customer managed AWS KMS key.
1. **Step 5**: An Amazon CloudWatch subscription filter invokes an Lambda job status notifications function.
1. **Step 6**: The job status notifications Lambda function sends an event on the EventBridge Event bus.
1. **Step 7**: The EventBridge Rule triggers the application.
1. **Step 8**: The application makes an API call to get the results/findings.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-sensitive-information-scanning-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
