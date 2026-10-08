---
source_url: https://docs.aws.amazon.com/solutions/building-saas-applications-on-amazon-eks-using-gitops/index.html
---

---
title: 'Guidance for Building SaaS applications on Amazon EKS using GitOps'
canonical_url: https://docs.aws.amazon.com/solutions/building-saas-applications-on-amazon-eks-using-gitops/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Building SaaS applications on Amazon EKS using GitOps

## Overview

This Guidance demonstrates how to implement GitOps automation for multi-tenant SaaS applications on Amazon EKS, helping organizations streamline their DevOps practices and tenant management. By leveraging tools like Flux, Argo Workflows, Helm, and Terraform, teams can automate deployment workflows, manage versioning challenges, and handle tenant onboarding efficiently. The solution provides practical expertise for maintaining complex SaaS environments, enabling consistent application updates across tenants while reducing operational overhead and improving deployment reliability.

## Benefits

### Accelerate SaaS deployment

Deploy multi-tenant SaaS applications on Amazon EKS with automated GitOps workflows. Reduce time-to-market by leveraging infrastructure as code and declarative configurations that automatically provision environments and tenant resources.

### Streamline tenant management

Automate tenant onboarding and resource provisioning through GitOps-driven workflows. Argo Workflows and Flux controllers work together to manage tenant configurations and deployments, helping ensure consistent environments across your SaaS platform.

### Optimize operational costs

Implement tiered multi-tenancy models that balance resource isolation with cost efficiency. Share infrastructure components for basic tier tenants while maintaining the ability to provision dedicated resources for premium tiers, maximizing your cloud investment.

## How it works

### Provision EKS Cluster and development environment

This reference architecture shows how to provision an Amazon EKS cluster with critical add-ons and development environment for running this guidance.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-saas-applications-on-amazon-eks-using-gitops.pdf)Step 1DevOps engineer defines a per-environment Terraform variable file that controls environment-specific configuration. This configuration file is used in all steps of deployment process by various configurations to provision different Amazon Elastic Kubernetes Service (Amazon EKS) environments.Step 2DevOps engineer applies the environment configuration using Amazon CloudFormation which deploys an Amazon Elastic Compute Cloud (Amazon EC2) Instance with a VSCode IDE used to apply Terraform.Step 3An Amazon Virtual Private Cloud (VPC) is provisioned and configured based on specified configuration. According to best practices for Reliability, three Availability Zones (AZs) are configured with corresponding VPC endpoints to provide access to resources deployed in private VPC and other VPC connected by VPC Peering.Step 4User facing AWS Identity and Access Management (IAM) roles (Cluster Admin, Karpenter Controller, Argo Workflow, Argo Events, LB Controller, TF Controller) are created for various Amazon EKS cluster resources access levels, per Kubernetes security best practices.Step 5Amazon EKS cluster is provisioned with Managed Nodes Group (MNG) that runs critical cluster add-ons (CoreDNS, AWS Load Balancer Controller, and Karpenter) on its compute node instances. Karpenter manages compute capacity to other add-ons, as well as business applications deployed by user while prioritizing provisioning Amazon EC2 Spot instances for the best price-performance.Step 6Other important Amazon EKS add-ons (Flux controller etc.) are deployed based on the configurations defined in the per-environment Terraform configuration file (see Step1 above).Step 7Gitea source code repositories running on Amazon EC2 can be accessed by Developer users to update microservices source code.### GitOps Driven workflow on EKS Cluster

This architecture diagram shows GitOps driven workflow on Amazon EKS cluster using FluxV2 controller for provisioning SaaS tenant resources.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-saas-applications-on-amazon-eks-using-gitops.pdf)Step 1Gitea source code repositories hold the producer and consumer microservices application code, along with GitOps releases and Tenant resource definitions.Step 2Gitea Actions is responsible to build the Producer and Consumer container images and push them to Amazon Elastic Container Registry (ECR).Step 3Amazon ECR stores the Tenant Template Helm chart that references the producer and consumer service images.Step 4Flux watches environment definition in Git and Amazon ECR to deploy changes to the Amazon Elastic Kubernetes Service (Amazon EKS) cluster, so that the cluster deployments match the expected state declared in the Git source repo and the correct version of Helm chart is deployed in the cluster.Step 5The Argo Workflows controller is used for templating and automating variable replacement during onboarding, offboarding, and deployment processes. Argo Workflows automates these steps by committing the changes to the Git repository, which then triggers the rest of the GitOps pipeline.Step 6Basic tier application tenants share AWS resources (Amazon Simple Queue Service (Amazon SQS) and Amazon DynamoDB). Basic tier tenants are served by the same microservice instances and infrastructure resources. This approach optimizes resource usage and reduces costs by sharing the infrastructure among multiple tenants.### Provision AWS managed resources through Terraform with Tofu Controller

This architecture diagram shows how Tofu Controller works with FluxV2 controller on Amazon EKS cluster to provision AWS managed resources through Terraform.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-saas-applications-on-amazon-eks-using-gitops.pdf)Step 1Flux continuously watches Git repositories for changes. In this case, it monitors the repository containing the Terraform Custom Resource Definition (CRD) and the Terraform module.Step 2When a Terraform CRD is created in the cluster (defined in the Git repository), Flux detects this new resource and starts the reconciliation process.Step 3The TF Controller is responsible for monitoring the Terraform CRD within the flux-system namespace. When it detects a new or updated Terraform CRD, it initiates the necessary actions.Step 4The TF Controller launches a tf-runner pod. This pod pulls the specified Terraform module from the Git repository and executes it, managing the infrastructure as defined in the CRD.Step 5The tf-runner pod provisions the required resources, such as Amazon Simple Storage Services (Amazon SQS) queues and Amazon DynamoDB tables, based on the Terraform module's definitions.Step 6The state and plan of the Terraform execution are stored as Kubernetes secrets (e.g., tfstate and tfplan). This ensures that the state is preserved and can be accessed by subsequent Terraform operations.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/compute/building-saas-applications-on-amazon-eks-using-gitops.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/eks-saas-gitops)

[Read usage guidelines](/solutions/guidance-disclaimers/)
