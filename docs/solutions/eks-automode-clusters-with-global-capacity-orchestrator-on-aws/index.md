---
source_url: https://docs.aws.amazon.com/solutions/eks-automode-clusters-with-global-capacity-orchestrator-on-aws/index.html
---

---
title: 'Guidance for EKS AutoMode Clusters with Global Capacity Orchestrator on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/eks-automode-clusters-with-global-capacity-orchestrator-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for EKS AutoMode Clusters with Global Capacity Orchestrator on AWS

## Overview

This Guidance helps organizations deploy machine learning inference workloads across multiple AWS Regions by automating capacity orchestration and providing a unified API for global Kubernetes cluster management. Platform engineers deploy a single AWS CDK application that provisions identical Amazon EKS Auto Mode clusters across configured regions, connected through AWS Global Accelerator for intelligent traffic routing. Users submit Kubernetes manifests through a REST API or CLI with AWS IAM authentication—no manual cluster configuration required—while the platform automatically provisions GPU, AWS Trainium, AWS Inferentia, or CPU nodes on demand based on workload requirements. You gain simplified multi-region operations with automatic failover, reduced latency through global traffic optimization, and cost efficiency through on-demand node provisioning without pre-scaling infrastructure.

## Benefits

### Eliminate idle GPU capacity costs

Provision GPU, Trainium, and Inferentia nodes on demand with automatic bin-packing and termination. Scale AI/ML infrastructure to zero when workloads complete, eliminating over-provisioned accelerator spend.

### Deploy globally from one command

Manage identical multi-region EKS clusters through a single CDK application and unified API. Submit workloads without per-cluster kubeconfig while automatic failover routes to the nearest healthy region.

### Enforce compliance across every region

Apply a uniform five-layer security model validated against HIPAA, NIST 800-53, and PCI DSS to all clusters. Eliminate static credentials with dynamic pod-level IAM roles and daily-rotating secrets.

## How it works

This architecture diagram shows how to deploy and manage machine learning inference workloads across multiple AWS Regions using EKS Auto Mode clusters with automated global capacity orchestration. [Download the architecture diagram.](downloads/eks-automode-clusters-with-global-capacity-orchestrator-on-aws.pdf)

### Deployment Architecture

Step 1DevOps / Platform Engineers author and deploy one AWS Cloud Development Kit (AWS CDK) app; regions are configured in the cdk.json.

Step 2The command `gco stacks deploy-all` is used to provision identical AWS CloudFormation stacks in every configured AWS Region (auto-bootstrap included).

Step 3Users submit Kubernetes manifests through one REST API or CLI signed with AWS SigV4 (no per-cluster `kubeconfig` configuration is necessary).

Step 4Amazon API Gateway (edge-optimized) validates IAM credentials at Amazon CloudFront edges and routes the request to the AWS Lambda proxy.

Step 5The AWS Lambda proxy injects a rotating secret from AWS Secrets Manager into user request before forwarding it to AWS Global Accelerator.

Step 6AWS Global Accelerator routes each request over the AWS backbone to the nearest healthy AWS Region, with automatic failover.

Step 7Per-region deployed Application Load Balancers accept traffic only from Global Accelerator IP addresses and route into respective Amazon Elastic Kubernetes Service clusters.

Step 8Each AWS Region runs an Amazon Elastic Kubernetes Service Auto Mode cluster that provisions GPU, AWS Trainium, AWS Inferentia, and CPU based nodes on demand via node pools configurations.

### EKS Auto Mode in a multi-AZ VPC

Step 1An internet-facing Application Load Balancer deployed in Amazon VPC public subnets accepts only from Global Accelerator IPs and routes via Kubernetes Ingress.

Step 2Amazon Elastic Kubernetes Service Auto Mode cluster runs a managed control plane and auto-provisions nodes with no pre-scaling.

Step 3Karpenter nodepools include system, general CPU (AMD64+ARM64), NVIDIA GPU, AWS Trainium/AWS Inferentia, inference, and Amazon Elastic Fabric Adapter (EFA) components.

Step 4Platform pods in `gco-system` namespace operate the workloads: Manifest Processor applies manifests, Queue Processor consumes the job queue, Inference Monitor reconciles endpoints, and Health Monitor tracks cluster health.

Step 5Workloads persist data to Amazon EFS (shared RWX access) and optionally FSx for Lustre; inference workloads use Valkey cache, Amazon Aurora PostgreSQL pgvector vector storage, and Amazon S3 model weights.

Step 6A Regional API Gateway with VPC Link fronts an internal Network Load Balancer for private, in-VPC access to AWS services.

Step 7The internal Network Load Balancer forwards private traffic to in-cluster services without any public exposure.

Step 8Regional AWS services: Queue Processor drains Amazon Simple Queue Service, Inference Monitor reconciles Amazon DynamoDB, and Health Monitor publishes to Amazon CloudWatch.

### End-to-end security

Step 1IAM Authentication: Amazon API Gateway validates users' AWS credentials with SigV4 on every request.

Step 2Secret Header: an AWS Lambda proxy injects a rotating token from AWS Secrets Manager, rotated daily.

Step 3IP Restriction: ALB security groups accept traffic only from AWS Global Accelerator IPs.

Step 4Header Validation: backend services reject any request missing the valid secret token.

Step 5IAM Roles for Service Accounts (IRSA): pods assume IAM roles for AWS access, no static credentials are stored in the cluster.

Step 6Compliance is validated with CDK-nag validation utility against AWS Solutions, HIPAA, NIST 800-53, and PCI DSS standards.

Step 7Default-deny Kubernetes network policies plus encryption at rest (AWS KMS) and in transit (TLS 1.2+) protect all service communication.

## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/global-capacity-orchestrator-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
