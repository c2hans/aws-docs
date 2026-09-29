---
source_url: https://docs.aws.amazon.com/solutions/ecommerce-migration-with-hcl-commerce-cloud-on-aws/index.html
---

---
title: 'Guidance for Ecommerce Migration with HCL Commerce Cloud on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/ecommerce-migration-with-hcl-commerce-cloud-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Ecommerce Migration with HCL Commerce Cloud on AWS

Increase scalability, availability, and performance when you migrate your HCL Commerce Cloud operations to AWS

## Overview

This Guidance shows how to migrate HCL Commerce Cloud to AWS and maximize the benefits of cloud-native and managed services. HCL Commerce Cloud, a commerce platform from HCLSoftware, has been developed over many years and tested by some of the largest retailers in the world. It is traditionally hosted on premises or used with hosting partners, but many of its users are now looking to migrate it to AWS to achieve the reliability, cost efficiency, scale, and security of the modern cloud. Using containers, HCL Commerce Cloud customers can use the recommended architecture to meet those demands and migrate their applications to AWS efficiently and at scale.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/ecommerce-migration-with-hcl-commerce-cloud-on-aws.pdf)

![Architecture diagram](/images/solutions/ecommerce-migration-with-hcl-commerce-cloud-on-aws/images/ecommerce-migration-with-hcl-commerce-cloud-on-aws-1.png)

1. **Step 1**: Amazon CloudFront provides a highly secure and programmable content delivery network.
1. **Step 2**: Application Load Balancer automatically distributes the incoming traffic across multiple containers in multiple Availability Zones (AZs) to provide resilience.
1. **Step 3**: Amazon Elastic Kubernetes Service (Amazon EKS) is used to run HCL Commerce Cloud on Kubernetes. Amazon EKS orchestrates and scales containers on demand with resiliency built in.
1. **Step 4**: Amazon Relational Database Service (Amazon RDS) for Oracle provides high performance and availability at a global scale with full HCL Commerce Cloud version 9 compatibility.
1. **Step 5**: You can use infrastructure as code through AWS CloudFormation to deploy a consistent architecture running HCL Commerce Cloud on AWS.
1. **Step 6**: Amazon Route 53 provides DNS configuration.
1. **Step 7**: Amazon Simple Storage Service (Amazon S3) is used to store backups and serve static content.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon EKS is a fully managed service that removes the burden of managing Kubernetes infrastructure. Your teams can easily deploy, manage, and scale the containerized components for your HCL Commerce Cloud deployment. Additionally, Amazon RDS for Oracle automates database administration tasks like hardware provisioning, software patching, maintaining high availability, and performing backups. This reduces the operational load so that teams can redirect their efforts to innovation. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

CloudFront improves website security by providing traffic encryption and access controls. It also works with AWS Shield Standard, which defends against distributed denial-of-service attacks at no additional charge, and AWS WAF, which helps protect against common web exploits. Additionally, Amazon Virtual Private Cloud (Amazon VPC) separates your database and compute networks from the internet and protects them with a closed-down network access control list and security groups. It exposes only Application Load Balancer to the public internet. This Guidance also scopes down all AWS Identity and Access Management (IAM) policies to the minimum permissions required for the service to function properly, helping you limit unauthorized access to resources. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Elastic Load Balancing (ELB) routes user traffic to healthy containers in Amazon EKS, which automatically scales containers across multiple AZs for high availability. Similarly, Amazon RDS for Oracle places database instances in two AZs and provides failover support for high availability. Amazon S3, which provides 99.999999999% (11 nines) durability, stores automated backups. By using ELB, Amazon EKS, and Amazon RDS together, you reduce the chance of application failure, so your users can browse HCL Commerce Cloud with virtually zero downtime, and your operation's teams can meet their recovery time objective and recovery point objective requirements. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance helps you sustain peak traffic for your ecommerce website. Amazon EKS scales your HCL Commerce Cloud containers on demand, so only the necessary compute resources are allocated. Amazon RDS for Oracle can scale out the database using read replicas. Additionally, CloudFront serves requests through the edge location closest to the requester to reduce network latencies. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

CloudFront helps decrease the frequency of data access or microservice invocations through caching where possible. This means that Amazon EKS, through automatic application scaling and efficient compute resource provisioning, will provision the minimum amount of resources, lowering your compute costs. And as a managed service, Amazon EKS enables you to offload the undifferentiated heavy lifting of operating the Kubernetes control plane. Similarly, Amazon RDS for Oracle helps you avoid the costs of maintaining an underlying database infrastructure. You can also buy Amazon RDS Reserved Instances, which provide maximum cost savings for a long-term commitment. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon EKS adapts to demand and scales down during periods of low traffic, making the architecture more sustainable by reducing your carbon footprint. You can also use the latest AWS Graviton Processors for Amazon EKS and Amazon RDS. These processors use up to 60 percent less energy than comparable Amazon Elastic Compute Cloud (Amazon EC2) instances for the same performance. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
