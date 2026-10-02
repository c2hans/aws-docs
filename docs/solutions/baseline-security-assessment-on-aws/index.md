---
source_url: https://docs.aws.amazon.com/solutions/baseline-security-assessment-on-aws/index.html
---

---
title: 'Guidance for Baseline Security Assessment on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/baseline-security-assessment-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Baseline Security Assessment on AWS

## Overview

This Guidance helps customers assess their foundational security setup in their AWS account. Use the provided AWS CloudFormation template to automate the assessment of your AWS accounts for security vulnerabilities and deliver an assessment report that includes steps on how to resolve the issues.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/baseline-security-assessment-on-aws.pdf)

![Architecture diagram](/images/solutions/baseline-security-assessment-on-aws/images/baseline-security-assessment-on-aws-1.png)

1. **Step 1**: The AWS user installs the AWS CloudFormation template created for this Guidance. The template deploys an AWS Lambda function along with the necessary AWS Identity and Access Management (IAM) role for the Lambda function.
1. **Step 2**: The Lambda function deploys an AWS Well-Architected custom lens.
1. **Step 3**: The Lambda function assesses resources in the account and checks if: - AWS Secrets Manager is used to store and manage lifecycle of secrets - AWS Systems Manager Patch Manager is used for patch management - Amazon CloudFront is used to deliver static content - Amazon Virtual Private Cloud (Amazon VPC) is configured correctly to setup a secure, isolated network - AWS CloudTrail is setup for audit purposes - AWS Cost Explorer billing alarms are configured - AWS Cost Anomaly Detection is setup - Amazon Simple Storage Service (Amazon S3) is configured correctly to prevent public access
1. **Step 4**: The AWS Well-Architected custom lens questions are answered by the Lambda function to complete the automated assessment.
1. **Step 5**: The AWS user navigates to the console in the AWS Well-Architected Tool to view and download the assessment report.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-baseline-security-assessment-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Security

For secure authentication and authorization, Lambda is granted access to AWS services on the least privilege basis with read-only permissions. Single Lambda functions are deployed in this guidance and are inaccessible from the internet. The customer can view and download an assessment report within the AWS Well-Architected portal, which can only be accessed by logging into the customer's account. No additional data is stored anywhere else in the customer’s account. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda utilizes logs and metrics which are sent to Amazon CloudWatch where the data is analyzed for risks. Using a single CloudFormation template allows customers to easily install and uninstall resources. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda is purpose built for this Guidance, allowing the customer to change the custom lens and modify the Lambda function to meet their security needs. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Using only the minimum resources required, this Guidance scales to meet demand by using serverless services to deliver the security assessment. Costs are incurred only for the resources consumed. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses fully managed serverless services that scale with demand, and allow customers to continually match their loads using only the minimum resources required. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
