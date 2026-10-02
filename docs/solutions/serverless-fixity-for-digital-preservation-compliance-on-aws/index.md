---
source_url: https://docs.aws.amazon.com/solutions/serverless-fixity-for-digital-preservation-compliance-on-aws/index.html
---

---
title: 'Guidance for Serverless Fixity for Digital Preservation Compliance on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/serverless-fixity-for-digital-preservation-compliance-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Serverless Fixity for Digital Preservation Compliance on AWS

## Overview

This Guidance demonstrates how to validate checksums for compliance and audit requirements with an on-demand fixity check process. You can check the integrity of objects stored in any [Amazon Simple Storage Service](/s3/) (Amazon S3) storage class using either the MD5 or SHA1 checksum algorithm without having to incur the cost and complexity of third-party software.

## How it works

This architecture diagram shows how customers who require an on-demand fixity check process can validate the checksums for compliance and audit requirements.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/serverless-fixity-for-digital-preservation-compliance-on-aws.pdf)

![Architecture diagram](/images/solutions/serverless-fixity-for-digital-preservation-compliance-on-aws/images/serverless-fixity-for-digital-preservation-compliance-on-aws-1.png)

1. **Step 1**: You can start the process for this Guidance by using AWS Management Console, Amazon API Gateway, or AWS Command Line Interface (AWS CLI).
1. **Step 2**: The AWS Step Functions state machine workflow uses AWS Lambda functions for restoration and compute using an MD5, SHA1, or SHA256 checksum algorithm. It validates objects stored in your Amazon Simple Storage Service (Amazon S3) buckets.
1. **Step 3**: This Guidance orchestrates the fixity check process in various states. If necessary, the workflow restores the object from Amazon S3 Glacier or the Amazon S3 Glacier Deep Archive. Then the process incrementally computes the fixity. After the MD5, SHA1, or SHA256 checksum is calculated, it is validated with the original checksum value stored with the object.
1. **Step 4**: The results of the fixity check process are sent to an Amazon Simple Notification Service (Amazon SNS) topic, which is then sent to subscribers by email notification.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/serverless-fixity-for-digital-preservation-compliance)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses AWS CloudFormation templates to prepare and operate. It makes any configuration changes as needed, and all infrastructure can be reprovisioned in the event of a failure. Additionally, it iterates on and implements all feedback and suggestions where possible. By using this Guidance, you can build procedures to support your workloads and their expected behaviors, identify and respond to risks, and adapt accordingly. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance lets you use the RESTful API endpoint to programmatically start a fixity process and start using Management Console and AWS CLI. This Guidance uses AWS Identity and Access Management (IAM) roles and policies and encryption in transit to protect and manage resources and protect data. Step Functions and AWS Lambda functions are granted with the least-privilege permissions. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance is serverless and multi–Availability Zone by default, can be deployed in any AWS Region, and can scale resources. Serverless services support versioning, so you can manage different versions of your deployed code. Step Functions, Lambda, and Amazon SNS provide a reliable and decoupled architecture for this workflow. Step Functions has built-in fault tolerance and maintains service capacity across multiple Availability Zones in each Region. It protects applications against individual machine or data center failures, providing high availability, and it automatically retries any failed computational runs. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses serverless services like API Gateway, Lambda, Step Functions, and Amazon SNS to minimize cost and maintenance and improve performance. By building applications from individual components that each perform a discrete function, you can scale more easily and change applications more quickly. For example, Step Functions helps coordinate the components of distributed applications and microservices using visual workflows, automatically scaling your application’s required operations and underlying compute in response to changing workloads. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance only uses serverless services, which let you run code without provisioning or managing servers and you only pay for what you use. Lambda functions run on processors configured to balance the speed of processing and the cost. All your data enters a virtual private cloud (VPC), and the cost depends on the data transferred and the Region. Amazon S3 data storage rates depend on your objects’ size, how long you store the objects, and the storage class you choose. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance only uses serverless services, so they scale based on load, and you don’t have to provision or manage any hardware. You can check the integrity of objects stored in any Amazon S3 storage class using the MD5, SHA1, or SHA256 checksum algorithm without the complexity of managing third-party software. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
