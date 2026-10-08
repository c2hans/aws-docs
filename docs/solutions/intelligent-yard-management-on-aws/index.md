---
source_url: https://docs.aws.amazon.com/solutions/intelligent-yard-management-on-aws/index.html
---

---
title: 'Guidance for Intelligent Yard Management on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/intelligent-yard-management-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Intelligent Yard Management on AWS

## Overview

This Guidance demonstrates how to use annotated data to train machine learning (ML) models that help with transportation and logistics yard management. Transportation and logistics yards are complex environments that involve time-consuming manual tracking and monitoring activities. This architecture uses data from these environments to generate ML-powered insights to improve yard management.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/intelligent-yard-management-on-aws.pdf)

![Architecture diagram](/images/solutions/intelligent-yard-management-on-aws/images/intelligent-yard-management-on-aws-1.png)

1. **Step 1**: Recorded videos are used as input to create annotated data. The data is stored in a file system for later use.
1. **Step 2**: A computer vision (CV) model is trained in the ML training module using annotated data.
1. **Step 3**: In the ML training module, Amazon SageMaker infrastructure is critical for training custom CV models. The models are trained to detect physical assets using optical recognition.
1. **Step 4**: The trained model and business logic application is deployed to the AWS Panorama Appliance. Live internet protocol (IP) cameras send a feed to this appliance. Feeds are used for inference at the edge and are not recorded.
1. **Step 5**: The output from the AWS Panorama Appliance is used to create a web application hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance.
1. **Step 6**: End users access this web application through Amazon CloudFront. The web application presents a view of assets in the facility and a dashboard interface powered by Amazon QuickSight.
1. **Step 7**: Optional: Amazon Virtual Private Cloud (Amazon VPC) peering connects data to other external yard systems for enhanced functionality of asset tracking and monitoring.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This architecture displays information on working statistics through services that allow for quick feedback, recovery, and refactoring. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Data is encrypted in transit and at rest. The architecture uses the principle of least privilege and enforced login to protect access to data. Each layer of the application is secured and monitored for traceability. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The architecture distributes workloads to avoid a single point of failure. It uses tracking key performance indicators (KPIs) to monitor reliability for production workloads. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The architecture uses serverless functions (such as AWS Lambda ) where possible in addition to a data driven approach. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Customers pay only for resources used. Monitoring services check that applications are using resources efficiently so that customers do not pay for more resources than they actually need. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Serverless and managed services match instance size and usage to avoid wasted compute power. This architecture maximizes energy efficiency by adopting and aligning to a mature deployment approach using key AWS services, such as SageMaker, Amazon EC2, and AWS Glue. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
