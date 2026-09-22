---
source_url: https://docs.aws.amazon.com//solutions/using-amazon-eks-capabilities-for-workload-orchestration-and-cloud-resource-management-on-aws//index.html
---

---
title: 'Guidance for Using Amazon Elastic Kubernetes Service Capabilities for Workload Orchestration and Cloud Resource Management on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/using-amazon-eks-capabilities-for-workload-orchestration-and-cloud-resource-management-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Using Amazon Elastic Kubernetes Service Capabilities for Workload Orchestration and Cloud Resource Management on AWS

## Overview

This Guidance demonstrates how to simplify Kubernetes workload orchestration and cloud resource management using three newly announced Amazon EKS capabilities: Argo CD, AWS Controllers for Kubernetes (ACK), and Kube Resource Orchestrator (KRO). Platform engineers create reusable Resource Graph Definitions that encapsulate infrastructure requirements and organizational best practices into custom APIs. Developers can then deploy multi-tier applications using these simplified APIs without directly managing underlying infrastructure complexities, while Argo CD automates deployment across multiple environments and clusters based on Git repository configurations. You gain increased productivity through streamlined workflows that separate platform and workload concerns, enabling your development teams to focus on application delivery rather than infrastructure management.

## Benefits

### Accelerate deployments across environments

Automate application delivery across multiple Amazon EKS clusters using GitOps principles, reducing manual intervention and enabling your teams to ship updates to dev and production environments consistently and reliably.

### Simplify cloud resource management

Empower your developers to provision Kubernetes and AWS resources — including databases and caching layers — through unified abstractions, eliminating the need to manage complex infrastructure configurations directly.

### Strengthen governance at scale

Enforce deployment guardrails and separate platform from workload concerns across your clusters, giving your platform teams centralized control while preserving developer agility.

## How it works

[Download the architecture diagram.](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/using-amazon-eks-capabilities-for-workload-orchestration-and-cloud-resource-management-on-aws.pdf)

### EKS Cluster Architecture for GitOps and ArgoCD

This diagram shows Hub and Spoke Amazon EKS clusters architecture for GitOps with ArgoCD provided by Amazon EKS Capabilities.

Step 1Amazon Elastic Kubernetes Service clusters are deployed within Amazon Virtual Private Cloud.

Step 2Amazon EKS capabilities are enabled and configured in the cluster for Argo CD operations.

Step 3DevOps and platform engineers create ArgoCD resources to separate concerns between platform and workload resources, while maintaining control over the Git repositories that store platform configurations and deployment manifests.

Step 4Secrets are created for multiple spoke clusters and Git repository credentials are configured. Argo CD projects are created with guardrails that define allowed destinations and Git repositories for each project's applications.

Step 5Argo CD Application is configured for platform resources from the Git repository containing infrastructure definitions. These deploy cluster-wide Kubernetes Custom Resource Definitions (CRDs) via Kubernetes Resource Orchestrator (KRO) Resource Graph Definitions (RGDs).

Step 6ArgoCD ApplicationSets iterate over environments and clusters to generate Argo CD Applications based on templates, enabling dynamic per-environment configuration.

Step 7ArgoCD Applications associated with workloads can only deploy resources from designated workload Git repositories. Each application deploys workload instances to separate namespaces representing different environments.

### Application Deployment using EKS Capabilities

This diagram shows application deployment architecture using AWS Controllers for Kubernetes (ACK) and Kube Resource Orchestrator (KRO).

Step 1Amazon Elastic Kubernetes Service cluster is deployed within Amazon Virtual Private Cloud.

Step 2Amazon EKS capabilities are enabled and configured in the cluster for AWS Controllers for Kubernetes (ACK) and KRO.

Step 3DevOps and platform engineers create component ResourceGraphDefinitions (RGD) that encapsulate the necessary resources, along with any additional logic, abstractions, and organizational best practices. When RGDs are applied to the Amazon EKS cluster, new custom APIs are created and available for developers to interact with. They can be used as universal foundation blocks.

Step 4DevOps and platform engineers create a unified RGD for the multi-tier voting application. Developers no longer need to directly manage the underlying infrastructure complexities, as the custom API handles the deployment and configuration of the required resources.

Step 5Developers apply Instance YAML spec to the Amazon EKS cluster using the custom API to deploy the application.

Step 6The API creates a set of resources within the cluster. These resources include both native Kubernetes resources and Custom Resource Definitions (CRDs) installed in the cluster. Some of these resources create additional AWS resources outside of the cluster, including Amazon Relational Database Service for PostgreSQL and Porting Assistant for .NET for Redis.

## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-using-amazon-eks-capabilities-for-workload-orchestration-and-cloud-resource-management)

## Related content

- **Deep dive: Simplifying resource orchestration with Amazon EKS Capabilities**: This blog post demonstrates how to use ACK and kro capabilities on Amazon EKS for declarative AWS resource management, multi-cluster operations, and building reusable infrastructure abstractions with ResourceGraphDefinitions.

[Read the blog](https://aws.amazon.com/blogs/containers/deep-dive-simplifying-resource-orchestration-with-amazon-eks-capabilities/)

- **Deep dive: Streamlining GitOps with Amazon EKS capability for Argo CD**: This blog post demonstrates advanced scenarios with Argo CD including hub-and-spoke multi-cluster deployments, native AWS service integrations, multi-tenancy implementation, and scaling with advanced Argo CD configurations.

[Read the blog](https://aws.amazon.com/blogs/containers/deep-dive-streamlining-gitops-with-amazon-eks-capability-for-argo-cd/)

- **Simplify Kubernetes cluster management using ACK, kro and Amazon EKS**: This blog post demonstrates how to create and manage a fleet of Amazon EKS clusters using kro, ACK, and Argo CD with a GitOps-based approach to increase productivity and improve consistency across your Kubernetes operations.

[Read the blog](https://aws.amazon.com/blogs/containers/simplify-kubernetes-cluster-management-using-ack-kro-and-amazon-eks/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
