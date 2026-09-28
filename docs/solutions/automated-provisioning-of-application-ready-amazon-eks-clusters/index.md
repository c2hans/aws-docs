---
source_url: https://docs.aws.amazon.com/solutions/automated-provisioning-of-application-ready-amazon-eks-clusters/index.html
---

---
title: 'Guidance for Automated Provisioning of Application-Ready Amazon EKS Clusters'
canonical_url: https://docs.aws.amazon.com/solutions/automated-provisioning-of-application-ready-amazon-eks-clusters/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Automated Provisioning of Application-Ready Amazon EKS Clusters

## Overview

This Guidance demonstrates how to set up a workload accelerator for Amazon Elastic Kubernetes Service (Amazon EKS) using Terraform blueprints. This collection of sample deployments and configurations addresses the challenges often associated with building your first application-ready Amazon EKS cluster. It incorporates a set of pre-configured and integrated tools, add-ons, and best practices to support core capabilities, including automatic scalability, observability, networking, and security. By using this Guidance and the Terraform blueprints, you can accelerate the process of establishing a fully configured, production-ready Amazon EKS cluster to support your workloads, without having to build and maintain the underlying infrastructure.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automated-provisioning-of-application-ready-amazon-eks-clusters.pdf)

![Architecture diagram](/images/solutions/automated-provisioning-of-application-ready-amazon-eks-clusters/images/automated-provisioning-of-application-ready-amazon-eks-clusters-1.png)

1. **Step 1**: Define a per-environment Terraform variable file that controls all environment-specific configurations. This configuration file is used in all steps of the deployment process by all infrastructure as code (IaC) configurations to create different Amazon Elastic Kubernetes Service (Amazon EKS) environments.
1. **Step 2**: Apply the environment configuration using Terraform.
1. **Step 3**: An Amazon Virtual Private Cloud (Amazon VPC) is provisioned based on the specified configuration. According to best practices for reliability, three Availability Zones (AZs) are configured with corresponding virtual private cloud (VPC) endpoints to provide access to resources deployed in your VPC. These resources might include Amazon Elastic Container Registry (Amazon ECR), Amazon EKS, Amazon Elastic Compute Cloud (Amazon EC2), and Amazon Elastic Block Store (Amazon EBS).
1. **Step 4**: User-facing AWS Identity and Access Management (IAM) roles (cluster admin, admin, editor, and reader) are created for various access levels to Amazon EKS cluster resources, as recommended in Kubernetes security best practices.
1. **Step 5**: The Amazon EKS cluster is provisioned with a managed nodes group (MNG) that runs critical cluster add-ons (such as CoreDNS, Karpenter, and AWS Load Balancer Controller through Elastic Load Balancing) on its compute node instances. Karpenter will manage the compute capacity to other add-ons (as well as business applications that your users deploy) while prioritizing instances powered by AWS Graviton processors for better price performance. Amazon EKS managed elastic network interfaces (ENIs) are deployed in isolated subnets.
1. **Step 6**: Other relevant Amazon EKS add-ons (such as cert-manager or External Secrets Operator (ESO)) are deployed based on their configurations defined in the corresponding Terraform configuration files (step 1).
1. **Step 7**: An AWS managed observability stack is deployed (if configured), including Amazon Managed Service for Prometheus (with an AWS managed collector for Amazon EKS) and Amazon Managed Grafana. In addition, a Grafana operator add-on is deployed with a set of predefined Grafana dashboards to get you started.
1. **Step 8**: One or more Amazon EKS clusters with important add-ons (optionally configured with a managed observability stack and IAM role-based access control) are available for your production workload deployment. These clusters' Kubernetes APIs are exposed using Network Load Balancers.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/compute/automated-provisioning-of-application-ready-amazon-eks-clusters.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-automated-provisioning-of-application-ready-amazon-eks-clusters)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance provisions observability tooling either through an open source software (OSS) or AWS, helping you follow best practices for cross-service configuration. For AWS observability tooling (using Amazon Managed Service for Prometheus and Amazon Managed Grafana), this Guidance creates Grafana dashboards based on the AWS Observability Accelerator project. Additionally, Amazon CloudWatch provides focused log event management. You can use these dashboards and logs to easily monitor utilization trends, quickly identify issues and their root causes, and make data-driven decisions for optimizing operations. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance configures a secured VPC with public, private, and isolated subnets, so when applications are being deployed to Amazon EKS, they cannot be directly accessed externally. You can also request a completely isolated VPC (no internet access). For that use, this Guidance provisions VPC endpoints for the relevant services that are needed for the cluster operations, such as Amazon EC2, Amazon ECR, Amazon EKS, or Amazon EBS. Additionally, you can use IAM to create fine-grained user-facing roles to control access to Amazon EKS clusters. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon EKS scales automatically, and the Kubernetes control plane deploys across multiple AZs to maintain consistent infrastructure health and availability. Additionally, by deploying Amazon Managed Service for Prometheus and Amazon Managed Grafana according to best practices, you can make sure they support high availability and fault tolerance. Finally, the Karpenter automatic scaler for Amazon EKS compute nodes manages the application infrastructure and helps make sure compute node instances are running on the latest Amazon Machine Image (AMI) for the cluster version. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Karpenter helps right-size instances and automatically scales Amazon EKS cluster compute nodes up and down as needed to match the total resources requested by applications running in the cluster. Additionally, it provisions instances powered by AWS Graviton processors to enhance price performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The cost for the Amazon EKS cluster is fixed, regardless of size, and is significantly lower than the cost of self-maintaining a secured, highly available, and scalable infrastructure. For compute, Karpenter provisions and allocates resources strictly according to the needs of the application workload so that you don’t have to pay for overprovisioned resources. Additionally, AWS Graviton processors deliver enhanced price performance for the compute nodes. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon EKS (with Amazon EC2 compute node instances) and Amazon ECR run on AWS, so you do not need to provision your own physical infrastructure. Karpenter automatically scales the cluster’s compute nodes based on demand, and AWS Graviton processors provide up to 40 percent energy efficiency compared to other processors for Amazon EC2 instances, helping you minimize your compute resource footprint and its environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
