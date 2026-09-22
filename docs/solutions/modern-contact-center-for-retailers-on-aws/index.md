---
source_url: https://docs.aws.amazon.com/solutions/modern-contact-center-for-retailers-on-aws/index.html
---

---
title: 'Guidance for a Modern Contact Center for Retailers on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/modern-contact-center-for-retailers-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for a Modern Contact Center for Retailers on AWS

## Overview

This Guidance helps retailers to quickly build a modern, scalable contact center on AWS. A contact center in the cloud offers retailers an omnichannel experience through voice, chat, and tasks, allowing them to help their consumer more efficiently. Call details are securely stored, with personal and credit card details encrypted, then integrated with services that can check inventory, product, consumer, and transaction history. All data can be captured with analytics and reporting tools and used for marketing, helping the retailer automate their systems and processes while improving the quality of their interactions with their consumers.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/modern-contact-center-for-retailers-on-aws.pdf)

![Architecture diagram](/images/solutions/modern-contact-center-for-retailers-on-aws/images/modern-contact-center-for-retailers-on-aws-1.png)

1. **Step 1**: Retail customers contact the retailer's customer service team using their phone or chat feature, initiating a call or chat session on Amazon Connect Customer.
1. **Step 2**: Customer contact center receives or dials customer calls. Multiple agents, supervisors, or administrators can use various devices and channels, such as phones or chat through computers.
1. **Step 3**: The retailer's Amazon Connect Customer instance captures the call details, including contact flow, call recordings, and call metrics.
1. **Step 4**: Call details, including recordings, are stored in Amazon Simple Storage Service (Amazon S3). Amazon Kinesis prepares, redacts, or encrypts any payment card industry (PCI) or personally identifiable information (PII) before storing in Amazon S3.
1. **Step 5**: Call flow integrations use Amazon EventBridge, AWS Lambda, Amazon Lex, and Amazon Polly. These services invoke event related processes and data dips with multiple source systems, or databases, to check the inventory, product, customer, and transaction history.
1. **Step 6**: Amazon Connect Customer Contact Lens provides real-time analytics of customer sentiment and their conversation using machine learning (ML).
1. **Step 7**: Amazon Athena and Amazon Quicksight provide data analytics on the details from the stored calls.
1. **Step 8**: Amazon Pinpoint is used for marketing or customer communication over channels like short message service (SMS), voice, or emails.
1. **Step 9**: Amazon CloudWatch, Amazon Macie, AWS Key Management Service (AWS KMS), and AWS Identity and Access Management (IAM) monitor, scan for PCI or PII information, and secure the customer's data.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses fully managed, serverless services that automatically scale to meet demand. With Amazon Connect Customer, you can build a highly scalable contact center that is tightly integrated with other AWS managed services, including machine learning and analytics. This integration helps you deliver an improved experience for your consumers, while allowing you to depend on the AWS services to operate as expected. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Direct Connect, or a site-to-site virtual private network (VPN), provides secure connections between the contact center and the AWS cloud. In this Guidance, we use IAM, Macie, and AWS KMS to secure and encrypt data. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon Polly, Amazon Lex, Amazon DynamoDB, and EventBridge are highly available and reliable managed services that help your workspaces scale in a stable environment. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

DynamoDB, Amazon S3, and Kinesis are scalable and highly available services. They are core components in this Guidance that help you meet your workload requirements and maintain efficiency as demand changes and technologies evolve. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Serverless services, such as Lambda, Kinesis, and EventBridge, are used extensively throughout this Guidance to reduce cost. These services help you implement a cloud financial management framework where you can build capability through knowledge building, programs, resources, and processes to become a more cost-efficient retailer. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance addresses the long-term environmental, economic, and societal impact of the activities of retailers. That’s why we leveraged serverless components throughout this Guidance. These components automate the process of infrastructure management, scale with demand, and help you maximize the minimum number of resources needed to deploy this Guidance. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
