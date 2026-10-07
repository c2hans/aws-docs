---
source_url: https://docs.aws.amazon.com/solutions/integrating-external-single-sign-on-providers-with-amazon-eks/index.html
---

---
title: 'Guidance for Integrating External Single Sign-On Providers with Amazon EKS'
canonical_url: https://docs.aws.amazon.com/solutions/integrating-external-single-sign-on-providers-with-amazon-eks/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Integrating External Single Sign-On Providers with Amazon EKS

## Overview

This Guidance demonstrates how to automate the deployment of an Amazon Elastic Kubernetes Service (Amazon EKS) cluster for external single sign-on authentication. Using [Amazon EKS Blueprints for Terraform,](https://aws-ia.github.io/terraform-aws-eks-blueprints/) an open-source infrastructure-as-code (IaC) tool, you can integrate your cluster’s control plane with an external identity provider like Okta. This Guidance lets you automatically provision resources, create roles and keys, and perform the integration, all through Terraform blueprints, simplifying single sign-on setup.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/integrating-external-single-sign-on-providers-with-amazon-eks.pdf)

![Architecture diagram](/images/solutions/integrating-external-single-sign-on-providers-with-amazon-eks/images/integrating-external-single-sign-on-providers-with-amazon-eks-1.png)

1. **Step 1**: Your platform engineer commits and pushes Terraform IaC changes to the project's Git repository.
1. **Step 2**: A Terraform infrastructure provisioning workflow is invoked by the code push to the Git repository or is initiated manually by your platform engineer.
1. **Step 3**: The Terraform infrastructure provisioning workflow starts resource deployment processes, targeting AWS and Okta environments.
1. **Step 4**: Required AWS Identity and Access Management (IAM) roles and polices and AWS Key Management Service (AWS KMS) keys are created.
1. **Step 5**: Amazon Virtual Private Cloud (Amazon VPC) environments for Amazon Elastic Kubernetes Service (Amazon EKS) control plane and related networking components are deployed.
1. **Step 6**: An Amazon EKS cluster control plane is deployed into the Amazon EKS virtual private cloud (VPC). The cluster control plane is provisioned across multiple Availability Zones (AZs) and is fronted by a Network Load Balancer.
1. **Step 7**: Your VPC is deployed with public and private subnets and other networking components across multiple AZs.
1. **Step 8**: An Amazon EKS compute plane, with managed node groups containing Amazon Elastic Compute Cloud (Amazon EC2) compute nodes, is deployed into your VPC.
1. **Step 9**: Okta resources, an OAuth server, users, groups, and role assignments are created in the specified Okta organization.
1. **Step 10**: An integration between Amazon EKS and Okta is created, along with required Kubernetes roles and role bindings.
1. **Step 11**: The Amazon EKS cluster is available for applications and end users. The Kubernetes API is accessible using a Network Load Balancer with Okta single sign-on user authentication.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-integrating-external-single-sign-on-providers-with-amazon-eks)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch provides focused log event management that helps you quickly identify the root causes of issues and simplifies troubleshooting. Providing comprehensive insights into the infrastructure and application levels of Amazon EKS clusters, it lets you monitor utilization trends and make metrics-driven decisions for optimizing operations. Additionally, as a managed Kubernetes application platform, Amazon EKS is optimized for efficiency in operational management. Finally, Amazon VPC provides network layer isolation for cluster resources, thus increasing operational efficiency. Together, these services reduce the operational burden of deploying and maintaining a security integration with external single sign-on providers. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Amazon EKS integration provides consistent enterprise-grade security through single sign-on providers like Okta. When you use Okta, you can be sure that only properly authenticated users mapped to the Okta organization structure can access your platform and application. This Guidance also natively integrates with AWS Secrets Manager to store Kubernetes secrets, and it enables a private or isolated networking layer through Amazon VPC. This configuration prevents applications deployed to Amazon EKS from being directly accessed through the internet. You can also opt for a completely isolated VPC (one with no internet access) and use VPC endpoints to connect the cluster to required services. Additionally, IAM provides fine-grained access policies to manage instance federation to the cluster, and AWS KMS encrypts all data at rest. Finally, Bottlerocket, an operating system built to run containers, adds security layers like Read Only, Security-Enhanced Linux, and no Secure Shell access. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon EKS runs a secure, scalable, and highly-available Kubernetes control plane across multiple AZs to maintain cluster infrastructure health. Managed node groups for Amazon EKS make sure that Amazon Elastic Compute Cloud (Amazon EC2) node instances are running the latest Amazon Machine Image (AMI). This supports high availability and fault toleration. Additionally, CloudWatch event management efficiently detects events that can negatively impact reliability so that you can proactively address them. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon EKS is a highly available orchestration service optimized for the scalability and performance of containerized applications. It effectively manages its infrastructure to accommodate the total resources requested by the applications running in the cluster. This Guidance balances workloads across the cluster’s compute nodes, and it scales Amazon EC2 instances based on application workload requirements. You can also increase performance efficiency by using compute-efficient compute nodes, such as instances based on AWS Graviton Processors. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The Amazon EKS control plane lets you run applications without provisioning your own infrastructure, enabling you to avoid associated overhead costs. Additionally, because Amazon EKS is a managed service, its cluster costs are significantly lower than self-maintaining clusters. The control plane has a fixed cost and uses managed node groups to provision and allocate compute resources according to application requirements. By rightsizing Amazon EC2 instances and using compute-efficient nodes based on AWS Gravitonprocessors, you can utilize resources more efficiently to optimize costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon EKS and Amazon Elastic Container Registry (Amazon ECR) reduce the environmental impact of your workloads. Because they are managed services, you don’t need to provision your own physical infrastructure for the control plane and image registry. Additionally, this Guidance uses managed node groups to scale Amazon EKS compute nodes up and down based on demand, minimizing energy waste. Finally, it provides the option to use compute-efficient Amazon EC2 instances based on AWS Graviton processors, helping you reduce the carbon footprint of your workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
