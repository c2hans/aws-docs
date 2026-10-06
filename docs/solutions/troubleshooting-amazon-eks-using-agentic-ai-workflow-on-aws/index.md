---
source_url: https://docs.aws.amazon.com/solutions/troubleshooting-amazon-eks-using-agentic-ai-workflow-on-aws/index.html
---

---
title: 'Guidance for Troubleshooting Amazon EKS using Agentic AI workflow on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/troubleshooting-amazon-eks-using-agentic-ai-workflow-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Troubleshooting Amazon EKS using Agentic AI workflow on AWS

## Overview

This Guidance demonstrates how to address the complexity of troubleshooting Amazon EKS environments with multiple metrics and logs by implementing an agentic AI workflow that uses generative AI with RAG-enabled knowledge bases and chat interfaces to accelerate problem diagnosis. The implementation deploys a comprehensive EKS environment using Terraform with managed node groups, observability stack including Amazon Managed Prometheus and Grafana, and RBAC-based security mapped to IAM roles. A Slack-integrated AI agent system runs on the EKS cluster, where an orchestrator agent receives troubleshooting requests and delegates tasks to specialized agents that connect to Amazon S3 vector-based knowledge bases for semantic similarity matching against historical troubleshooting cases. You can significantly reduce your mean time to triage EKS issues while improving the accuracy of root cause analysis and remediation initiation across various infrastructure and application problems.

## Benefits

### Accelerate Kubernetes troubleshooting with AI

Deploy intelligent agents that analyze cluster data and historical cases to deliver actionable recommendations. Reduce mean time to resolution by automating diagnostic workflows through natural language interactions in Slack.

### Provision production-ready EKS clusters efficiently

Implement infrastructure as code with Terraform to deploy secure, multi-AZ Amazon EKS environments with essential add-ons and observability. Ensure consistent configurations across development, staging, and production environments.

### Enable collaborative platform engineering practices

Empower DevOps teams, SREs, and developers to troubleshoot Kubernetes issues directly from Slack using ChatOps patterns. Leverage real-time cluster insights and semantic search of past incidents to resolve problems faster.

## How it works

### Provision EKS Cluster

This diagram shows how to provision an Amazon Elastic Kubernetes Service (EKS) cluster with best practices configuration and critical add-ons.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/troubleshooting-amazon-eks-using-agentic-ai-workflow-on-aws.pdf)Step 1DevOps engineer defines a per-environment Terraform variable file that controls all environment-specific configuration. This configuration file is used in all steps of deployment process by all IaC configurations to provision Amazon Elastic Kubernetes Service (Amazon EKS) environmentsStep 2DevOps engineer applies the environment configuration using Terraform following the deployment process defined in the guidance.Step 3An Amazon Virtual Private Network (VPC) is provisioned and configured based on specified configuration. According to best practices for Reliability, 3 Availability zones (AZs) are configured with corresponding VPC Endpoints to provide access to resources deployed in private VPC.Step 4User facing Identity and Access Management (IAM) roles (Cluster Admin, Admin, Editor etc.) are created for various access levels to Amazon EKS cluster resources, as recommended in Kubernetes security best practicesStep 5Amazon EKS cluster is provisioned with Managed Nodes Groups that run critical cluster add-ons (CoreDNS, AWS Load Balancer Controller and Karpenter auto-scaler) on its compute node instances. Karpenter will manage compute capacity for other add-ons, as well as applications that will be deployed by userStep 6Other important Amazon EKS add-ons (Cert Manager, FluentBit, Grafana Operator etc.) are deployed based on the configurations defined in the environment Terraform configuration file (Step1 above).Step 7AWS Managed Observability stack is deployed (), including Amazon Managed Service for Prometheus (AMP), AWS Managed collector for Amazon EKS, and Amazon Managed Service for Grafana (AMG)Step 8Users can access Amazon EKS cluster(s) with best practice add-ons, optionally configured Observability stack and RBAC based security mapped to IAM roles for workload deployments using Kubernetes API that is exposed via AWS Network Load Balancer### Agentic AI Workflow

This architecture diagram shows  Agentic AI troubleshooting workflow working with real-time EKS cluster data and integrated with AWS AI services for analysis and Slack for ChatOps.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/troubleshooting-amazon-eks-using-agentic-ai-workflow-on-aws.pdf)Step 1Guidance workloads are deployed into an Amazon EKS cluster, configured for application readiness with compute plane managed by Karpenter auto-scaler, as shown in Diagram 1Step 2Users (DevOps engineers, SREs, developers) who encounter Kubernetes (K8s) issues send troubleshooting requests through designated Slack channel integrated with K8s Troubleshooting AI Agent. Its components are running as containers on the Amazon EKS cluster deployed from previously built images and hosted in Elastic Container registry (ECR) via Helm charts.Step 3Designated Slack receives user messages via AWS Elastic Load Balancer and establishes a WebSocket connection (Socket Mode) to the Orchestrator agent running on the Amazon EKS clusterStep 4Orchestrator agent receives users' message and calls Amazon Nova Micro via Amazon Bedrock, a fully managed service for foundation models, to determine whether the message requires K8s troubleshooting. If an issue is classified as K8s-related, the Orchestrator agent initiates a workflow by delegating tasks to specialized agents while maintaining overall user session context.Step 5Orchestrator agent invokes the Memory agent, which connects to Amazon S3 Vectors based knowledge base to search for similar troubleshooting cases for precise classificationStep 6The Memory agent invokes Amazon Titan Text Embeddings via Amazon Bedrock to generate semantic embeddings and perform vector similarity matching against the shared Amazon Simple Storage Service (Amazon S3) Vectors knowledge baseStep 7Orchestrator agent invokes the K8s Specialist agent, which utilizes the fully managed Amazon EKS Model Context Protocol (MCP) Server to execute read-only commands against the Amazon EKS API Server. The MCP Server authenticates with the Kubernetes API using IAM credentials, then gathers real-time cluster state (including pod status, deployments, services), retrieves relevant pod logs, collects recent events, and captures resource metrics (CPU, memory, network). This comprehensive data is structured and normalized by the MCP Server and returned to the K8s Specialist agent to provide context for the current problem analysis.Step 8K8s Specialist agent sends the collected cluster data to Anthropic Claude model via Amazon Bedrock for intelligent issue analysis and resolution generationStep 9Orchestrator agent synthesizes the historical context received from Memory agent and current cluster state from K8s Specialist, then uses Anthropic Claude model via Amazon Bedrock to generate comprehensive troubleshooting recommendations, which are stored in Amazon S3 Vectors for future reference.Step 10Orchestrator agent generates troubleshooting recommendations and sends them back to Users via integrated dedicated Slack channel. This illustrates troubleshooting using an increasingly popular "ChatOps" Platform Engineering pattern.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](https://aws-solutions-library-samples.github.io/compute/troubleshooting-amazon-eks-using-agentic-ai-workflow-on-aws.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs

[Go to sample code](https://github.com/aws-solutions-library-samples/eks-troubleshooting-agentic-ai-chatops)

## Related content

- **Architecting conversational observability for cloud applications**: This blog post walks through building a generative AI–powered troubleshooting assistant for Kubernetes.

[Learn more](https://aws.amazon.com/blogs/architecture/architecting-conversational-observability-for-cloud-applications/)

- **Streamline Amazon EKS operations with Agentic AI**: This video explains how to build agentic AI systems that automate Amazon EKS cluster management, from real-time issue diagnosis to guided remediation.

[Learn more](https://www.youtube.com/watch?v=4s-a0jY4kSE)

[Read usage guidelines](/solutions/guidance-disclaimers/)
