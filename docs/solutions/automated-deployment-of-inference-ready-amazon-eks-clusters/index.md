---
source_url: https://docs.aws.amazon.com/solutions/automated-deployment-of-inference-ready-amazon-eks-clusters/index.html
---

---
title: 'Guidance for Automated Deployment of Inference ready Amazon EKS Clusters'
canonical_url: https://docs.aws.amazon.com/solutions/automated-deployment-of-inference-ready-amazon-eks-clusters/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Automated Deployment of Inference ready Amazon EKS Clusters

## Overview

This Guidance demonstrates how to rapidly establish production-ready ML inference environments on Amazon EKS, delivering significant operational and cost benefits. It shows how to leverage optimized compute resources and GPUs for optimal inference performance while implementing industry best practices for auto-scaling and cluster management. The solution helps organizations accelerate their AI initiatives by providing a battle-tested architecture that seamlessly supports both experimental and large-scale production deployments of LLMs and generative AI models. By automating complex infrastructure setup and incorporating comprehensive observability, this guidance enables teams to focus on model deployment and business value rather than infrastructure management.

## Benefits

### Accelerate AI model deployment

Deploy AI inference workloads faster with pre-configured Amazon EKS clusters optimized for machine learning. This guidance provides ready-to-use Terraform templates and Helm charts that streamline the deployment process from cluster creation to model serving.

### Optimize AI infrastructure costs

Balance performance and cost efficiency with topology-aware scheduling that keeps AI/ML workloads in the same Availability Zone. Karpenter's intelligent auto-scaling provisions the right compute resources on demand, helping you avoid over-provisioning while maintaining performance for inference workloads.

### Enhance operational visibility

Gain comprehensive insights into your AI inference infrastructure with the pre-configured observability stack. The integrated FluentBit, Prometheus, and Grafana deployment automatically collects metrics and logs from AI/ML workloads, enabling faster troubleshooting and performance optimization.

## How it works

### Provision EKS

This architecture diagram shows how to provision an Amazon Elastic Kubernetes Service (EKS) Inference ready cluster with best practices configuration for AI workloads.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/automated-deployment-of-inference-ready-amazon-eks-clusters.pdf)Step 1DevOps engineer defines a cluster Terraform variable file that contains the environment-specific configuration.Step 2DevOps engineer applies the environment configuration using Terraform following the deployment process defined in the guidance to the target AWS account.Step 3Provision and configure an Amazon Virtual Private Network (VPC). According to Reliability best practices, configure four Availability zones (AZs) to optimize node acquisition and high availability. Topology awareness defaults to keeping AI/ML workloads in the same AZ for performance/cost but is configurable for availability.Step 4Provision Amazon Elastic Kubernetes Service (Amazon EKS) cluster with Managed Nodes Group (MNG) that run critical cluster add-ons (CoreDNS, AWS Load Balancer Controller - ALB and Karpenter) on its compute nodes. Karpenter will manage compute capacity for other add-ons, as well as deployed ML inference applications. Amazon Elastic Network Interface (ENIs) managed by Amazon EKS are provisioned in respective subnetsStep 5Deploy other important Amazon EKS add-ons (LWS, KubeRay etc.) based on the configurations defined in the cluster Terraform configuration file (see Step 1).Step 6Deploy an observability stack including FluentBit, Prometheus and Grafana to collect metrics and logs from the environment. Deploy Service and Pod Monitors to watch for AI/ML workloads and collect metrics. Configure Grafana dashboards to automatically visualize related metrics and logs.Step 7Users access Amazon EKS K8s API with AWS Network Load Balancer (NLB) endpoint and may deploy containerized AI/ML inference workloads via Kubernetes CLI using the AI on Amazon EKS project inference Helm charts or other repositories.### Deploying AI Models

This architecture diagram shows highlights of deploying AI Models on the Inference-Ready Amazon EKS Cluster using Helm templates.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/automated-deployment-of-inference-ready-amazon-eks-clusters.pdf)Step 1ML Engineers use a Helm chart `values` template file to set values for Helm chart for model deployment.Step 2ML Engineers use `kubectl/helm` CLI tools to deploy the templated Helm chart to the Amazon EKS environment.Step 3Model Helm Templates are applied to Amazon Elastic Kubernetes Service (EKS) API of Inference Ready Amazon EKS cluster to start deployment of desired model.Step 4Amazon EKS API creates a Kubernetes pod and a service for the single model container deployment.Step 5Karpenter auto-scaler provisions Amazon Elastic Compute Cloud (EC2) instances to fulfill the compute node resource request to schedule model pods.Step 6Docker container image requested by the deployed model for the container is pulled from Amazon Elastic Container Registry (ECR).Step 7The weights for the deployed model are pulled from Hugging Face repository into Amazon S3 for faster loading and loaded into the model server.Step 8External Model consumer users can now port-forward the Kubernetes service port to their local machines for accessing the model.Step 9User/application requests to deployed models in the Inference Ready AWS EKS cluster are routed through the Kubernetes service to the model pods, responses are returned the same way.[Read usage guidelines](/solutions/guidance-disclaimers/)
