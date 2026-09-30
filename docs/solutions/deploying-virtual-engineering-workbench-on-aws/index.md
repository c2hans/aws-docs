---
source_url: https://docs.aws.amazon.com/solutions/deploying-virtual-engineering-workbench-on-aws/index.html
---

---
title: 'Guidance for Deploying Virtual Engineering Workbench on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-virtual-engineering-workbench-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Deploying Virtual Engineering Workbench on AWS

## Overview

This Guidance demonstrates how the Virtual Engineering Workbench (VEW) framework accelerates software development lifecycles and supports software-defined vehicles. VEW automates, virtualizes, and orchestrates processes to support the software development lifecycle, enabling original equipment manufacturers (OEMs) to reduce feedback cycle times. Using VEW, this Guidance implements automated testing, validation, and development processes, significantly reducing feature cycle time and increasing new feature throughput while maintaining consistent development environments.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-virtual-engineering-workbench-on-aws.pdf)

![Architecture diagram](/images/solutions/deploying-virtual-engineering-workbench-on-aws/images/deploying-virtual-engineering-workbench-on-aws-1.png)

1. **Step 1**: Connect to the VEW frontend through Amazon CloudFront backed by Amazon Simple Storage Service (Amazon S3), and select the workbench and virtual targets with which you'll work. Manage user authentication with Amazon Cognito and secure access with AWS WAF.
1. **Step 2**: Amazon API Gateway and AWS Lambda handle frontend requests and trigger workbench and virtual target provisioning through Amazon EventBridge and AWS Step Functions. Store product metadata in Amazon DynamoDB.
1. **Step 3**: VEW manages its products (digital toolchains and virtual targets) in AWS Service Catalog. Store product dependencies like binaries or libraries in Amazon S3, and handle events using EventBridge, Amazon Simple Notification Service (Amazon SNS), and Lambda.
1. **Step 4**: VEW deploys workbenches and virtual targets as Amazon Elastic Compute Cloud (Amazon EC2) instances into product accounts using Service Catalog, from which they can be accessed by the user through Amazon DCV, remote desktop protocol (RDP), or SSH.
1. **Step 5**: Deploy a fully automated VEW product lifecycle pipeline using Amazon EC2 ImageBuilder, creating Amazon EC2 AMIs and storing assets on Amazon S3.
1. **Step 6**: With AWS Direct Connect, VEW can be integrated with customers' corporate resources like identity providers, license servers, or code repositories.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

With Lambda, you can focus on building business logic while AWS manages the underlying infrastructure. Integrate API Gateway and EventBridge to create loosely coupled, event-driven architectures that are highly reliable. Amazon CloudWatch monitors, observes, and gains insights into your applications and services. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito enhances security through robust user authentication, authorization, and identity management. AWS WAF protects your applications from common web exploits and malicious traffic. Amazon CloudWatch monitors and logs security-related events, enabling threat detection and analysis. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Achieve fault tolerance, automatic scaling, and robust event processing with Amazon EC2, EventBridge, and API Gateway. EC2 instances can be distributed across multiple Availability Zones and Regions, helping ensure high availability through failover strategies. EventBridge offers improved failure recovery with dead-letter queues and custom retry policies, while API Gateway minimizes infrastructure failure risks. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

CloudFront accelerates content delivery through its global edge network. Amazon EC2 offers scalable compute resources on-demand. Direct Connect provides dedicated, low-latency connectivity to AWS. Lambda@Edge enables real-time processing at the edge, reducing latency. These services address key aspects of application delivery and processing, including content caching, compute scaling, reliable connectivity, and dynamic edge processing, creating a robust infrastructure for delivering high-performance applications and content globally. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Analyze monthly spending, define budgets, and identify cost outliers with AWS Cost Explorer. Cost Explorer provides right-sizing recommendations to optimize your compute instances and improve cost transparency. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS Graviton instances use energy-efficient ARM-based processors, which help you increase your energy-to-compute power ratio. Provision EC2 instances on-demand to replace underutilized infrastructure and improve resource utilization. Implement serverless architectures with Lambda to minimize idle resources and reduce your environmental footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
