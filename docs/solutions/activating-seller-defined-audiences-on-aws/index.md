---
source_url: https://docs.aws.amazon.com/solutions/activating-seller-defined-audiences-on-aws/index.html
---

---
title: 'Guidance for Activating Seller Defined Audiences on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/activating-seller-defined-audiences-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Activating Seller Defined Audiences on AWS

## Overview

This Guidance shows how to activate publisher first-party data from Software as a Service (SaaS) environments that support Seller Defined Audiences (SDA). It uses page content without Personally Identifiable Information (PII) to automatically map to industry standard taxonomies, returning the associated SDA identifications for activation through Real-Time Bidding (RTB).

## How it works

This diagram shows how to activate publisher first-party data from Software as a Service (SaaS) environments that support Seller Defined Audiences (SDA). It uses page content without Personally Identifiable Information (PII) to automatically map proprietary taxonomies, returning the associated SDA IDs for activation through Real-Time Bidding (RTB).

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/activating-seller-defined-audiences-on-aws.pdf)

![Architecture diagram](/images/solutions/activating-seller-defined-audiences-on-aws/images/activating-seller-defined-audiences-on-aws-1.png)

1. **Step 1**: A visitor's browser, mobile client, or Connected TV (CTV) device accesses publisher content containing ad impressions. The OpenRTB header bidding platform, such as prebid.js, is loaded with the page invoking the on-page data assembler. The data assembler forwards a Seller Defined Audiences (SDA) data request to an Amazon CloudFront distribution. The publisher's content and endpoints are protected by AWS WAF and CloudFront. CloudFront forwards the request to the Application Load Balancer (ALB) public endpoint on the publisher's Virtual Private Cloud (VPC) over the AWS network.
1. **Step 2**: The publisher's web tier routes the SDA data request to the internal ALB private endpoint.
1. **Step 3**: The internal ALB routes the SDA data request to the SDA service fleet on Amazon Elastic Kubernetes Service (Amazon EKS) for processing.
1. **Step 4**: Available attributes (such as the page context classification) and user data (such as audience demographics, interest, and purchase intent) are fetched from the NoSQL database such as Aerospike or Amazon DynamoDB. Aerospike will run within the VPC and does not require a VPC endpoint. Configure the rack-aware feature on Aerospike for better performance.
1. **Step 5**: The SDA data containing page context and audience taxonomy segment data is returned to the caller through CloudFront. The returned SDA data does not contain a unique ID of the user nor does it reveal a user's identity.
1. **Step 6**: The on-page data assembler sets the fetched page context classification attributes in the 'site.content' top-level object. The audience related data is set within the 'user.data' top-level object. Both of these objects are configured on Prebid.js. The new segtax identifier extension, that is introduced within these objects for SDA support, determines the provided segments. In the case of site content, this identifier can be custom or the standardized IAB Tech Lab Content Taxonomy. Custom taxonomy types must be registered with IAB Tech Lab to be assigned a number. Prebid.js submits the bid request to the Supply-Side Platform (SSP).
1. **Step 7**: The SSP parses the incoming request, resolves the data from the Prebid ortb2 object, transmits the data into the bid stream after applying the same ortb2 fields, and submits the bid request to its demand sources.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses a microservices-based approach so that components operate independently of one another, allowing you to easily integrate and deploy changes. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM and AWS KMS are AWS services that you can deploy with this Guidance to protect your resources and data. IAM policies grant least privilege access to data, so that users only have the permissions required to perform a specific task. AWS KMS encrypts data at rest and in transit as an additional layer of protection against unauthorized use. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Scalable services and features included in this Guidance, such as autoscaling for Amazon EKS, help you adapt to changes inherent in dynamic workloads. And the deployment pipeline implements and logs configuration changes, allowing you to roll back to a previous state in the case of a disaster. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance allows you to deploy, update, and scale components individually to meet demand for specific functions, allowing you to experiment with this Guidance and optimize it based on your data. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon EC2 Spot Instances offer scale and cost savings for up to a 90% discount when compared to Amazon EC2 On-Demand Instances. And, Amazon EKS and DynamoDB scale based on demand, so you only pay for the resources actually used. "> We recommend using AWS pricing models to help reduce cost. For example, Amazon EC2 Spot Instances offer scale and cost savings for up to a 90% discount when compared to Amazon EC2 On-Demand Instances. And, Amazon EKS and DynamoDB scale based on demand, so you only pay for the resources actually used. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By extensively using serverless services, you maximize overall resource usage because compute is used only as needed. This also reduces the overall energy required to operate your workloads. And to minimize the amount of hardware needed to provision this Guidance, AWS Graviton processors  maximize performance for workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
