---
source_url: https://docs.aws.amazon.com/solutions/payment-connectivity-gateway-orchestration-and-routing-on-aws/index.html
---

---
title: 'Guidance for Payment Connectivity, Gateway, Orchestration & Routing on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/payment-connectivity-gateway-orchestration-and-routing-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Payment Connectivity, Gateway, Orchestration & Routing on AWS

Transform your global payments network with today's technology

## Overview

This Guidance helps financial institutions implement a quick response (QR) code and payment processing on AWS for their digital customers. With the managed serverless solutions, you do not need to own, run, or manage the compute infrastructure, allowing you to focus on payment processing.

## How it works

This reference architecture displays how a quick response (QR) or wallet payment traverses through various components.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/payment-connectivity-gateway-orchestration-and-routing-on-aws.pdf)

![Architecture diagram](/images/solutions/payment-connectivity-gateway-orchestration-and-routing-on-aws/images/payment-connectivity-gateway-orchestration-and-routing-on-aws-1.png)

1. **Step 1**: To start, customers scan the business QR code displayed at the checkout page on a website or at the point of sale (POS) terminal.
1. **Step 2**: Amazon Route 53 routes traffic to an Amazon API Gateway endpoint where Amazon CloudFront distributes dynamic and static content. AWS security services such as AWS WAF and AWS Shield protect the web applications from common application-layer exploits and against distributed denial-of-service (DDoS) attacks.
1. **Step 3**: CloudFront content delivery network (CDN) is used to return resources found in its cache and static resources from Amazon Simple Storage Service (Amazon S3).
1. **Step 4**: Amazon API Gateway and Amazon CloudFront can be seamlessly integrated with AWS Certificate Manager. These services manage the complexity of creating, storing, and renewing public and private SSL/TLS X.509 certificates and keys that protect your applications.
1. **Step 5**: The request is routed through a Network Load Balancer to distribute incoming traffic across its healthy registered targets.
1. **Step 6**: Payment request is processed at application layer using Amazon Elastic Container Service (Amazon ECS) that deploys tasks on AWS Fargate.
1. **Step 7**: Payment transaction information is stored in Amazon Aurora or Amazon DynamoDB. Amazon ElastiCache is used as a session store to manage session information in payment processing. AWS CloudHSM is a cryptographic service for creating and maintaining hardware security modules (HSMs).
1. **Step 8**: Service logs are collected in Amazon S3 and analyzed and monitored using Amazon OpenSearch Service.
1. **Step 9**: At the security and compliance layer, AWS Config evaluates, assesses, and audits configurations of resources. Amazon GuardDuty monitors for malicious activity and unauthorized behavior, protecting AWS accounts and workloads. AWS Secrets Manager helps protect secrets needed to access applications, services, and IT resources.
1. **Step 10**: Payment request outbound traffic is sent to the payment processor through a NAT Gateway that is connected to card schemes for verification.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

To enable fast iteration and consistent deployment, you can use AWS Cloud Development Kit (AWS CDK) version 2, AWS CloudFormation, and Terraform. The recommended services are built with observability in mind, with process level metrics, logs, and dashboards. Extend these mechanisms to meet your needs and create alarms in Amazon CloudWatch to notify your on-call team of any issues. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The payment backend is protected with API Gateway resource policies to allow your API to be securely invoked from known resources. When you choose managed services, you can be sure that all AWS API calls are done through HTTPS endpoints using TLS communication, which will protect your data in transit. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

All components scale automatically, and the account limits should be clearly defined for the supported product range to avoid affecting reliability. To further increase reliability, consider implementing a disaster recovery plan for your solution by initiating cross-region failover using Route 53 for the whole infrastructure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Managed serverless solutions can help you avoid having to worry about scaling requirements. Fargate removes the need to own, run, and manage a compute infrastructure, allowing you to focus on payment processing. Network Load Balancer distributes incoming traffic across multiple targets, which can handle millions of requests per second. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance is designed to help you build a serverless architecture that keeps costs down. You pay only for the time and resources used to process payments. With managed and serverless services, you can set attributes that ensure sufficient capacity. You must set and monitor these attributes so that you minimize excess capacity and maximize performance. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

To reduce the amount of hardware required for provisioning, consider using managed container services, such as Fargate, instead of implementing your own container infrastructure. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **How Payment Companies are Using Cloud Technology to Advance Quick Response (QR) Transactions**: This post explains how new norms have influenced the rapid adoption of Quick Response codes (QRCs), initially located on restaurant menus in the US at the start of the pandemic and now used as a full-fledged form of payment.

[How Payment Companies are Using Cloud Technology to Advance Quick Response (QR) Transactions](https://aws.amazon.com/blogs/industries/how-payment-companies-are-using-cloud-technology-to-advance-quick-response-qr-transactions/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
