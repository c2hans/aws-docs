---
source_url: https://docs.aws.amazon.com/solutions/scalable-model-inference-and-agentic-ai-on-amazon-eks/index.html
---

---
title: 'Guidance for Scalable Model Inference and Agentic AI on Amazon EKS'
canonical_url: https://docs.aws.amazon.com/solutions/scalable-model-inference-and-agentic-ai-on-amazon-eks/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Scalable Model Inference and Agentic AI on Amazon EKS

## Overview

This Guidance demonstrates how to build a robust, enterprise-grade AI architecture that maximizes the value of machine learning investments. It helps organizations optimize their ML workload distribution through intelligent resource allocation, while providing a unified model inference API Gateway for streamlined access and management. The guidance shows how to implement agentic AI capabilities that enable seamless model interactions with external APIs, significantly expanding automation possibilities. Additionally, it demonstrates how to enhance LLM performance by combining specialized tools with Retrieval Augmented Generation (RAG), resulting in more contextually aware and capable AI systems that can better understand and respond to complex business scenarios.

## Benefits

### Optimize AI infrastructure costs

Deploy cost-effective AI workloads using AWS Graviton processors and intelligent auto-scaling. Karpenter automatically provisions the right-sized compute resources based on actual workload demands, reducing unnecessary infrastructure expenses while maintaining performance.

### Scale AI inference seamlessly

Implement a production-ready infrastructure that dynamically scales across multiple availability zones. The architecture efficiently handles varying inference workloads by automatically provisioning GPU, Graviton, and Inferentia-based compute resources as needed, ensuring consistent performance during demand spikes.

### Accelerate AI operations deployment

Reduce operational complexity with pre-configured observability and security controls. The guidance provides ready-to-deploy infrastructure with managed services for monitoring, logging, and security, allowing your team to focus on model development rather than infrastructure management.

## How it works

### Deploy EKS cluster with best practices configuration and critical add-ons for AI workloads

This reference architecture demonstrates how to provision an Amazon Elastic Kubernetes Service (EKS) cluster with best practices configuration and critical add-ons for AI workloads.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/scalable-model-inference-and-agentic-ai-on-amazon-eks.pdf)Step 1DevOps engineer defines a per-environment Terraform variable file that control all of the environment-specific configuration. This configuration file is used in all steps of deployment process by all IaC configurations to create different EKS (Amazon Elastic Kubernetes Service) environmentsStep 2DevOps engineer applies the environment configuration using Terraform following the deployment process defined in the guidance.Step 3An Amazon Virtual Private Cloud (VPC) is provisioned and configured based on specified configuration. According to best practices for Reliability, 3 Availability zones (AZs) are configured with corresponding VPC Endpoints to provide access to resources deployed in private VPC.Step 4User facing Identity and Access Management (IAM) roles (Cluster Admin, Admin, Editor and Reader) are created for various access levels to EKS cluster resources, as recommended in Kubernetes security best practicesStep 5EKS cluster is provisioned with Managed Nodes Groups that run critical cluster add-ons (CoreDNS, AWS Load Balancer Controller and Karpenter) on its compute node instances. Karpenter will manage compute capacity for other add-ons, as well as applications that will be deployed by user while prioritizing price-performance efficient AWS Graviton instancesStep 6Other important EKS add-ons (Cert Manager, FluentBit, Grafana Operator) are deployed based on the configurations defined in the environment Terraform configuration file (see Step1 above).Step 7AWS Managed Observability stack is deployed, including Amazon Managed Service for Prometheus (AMP), AWS Managed collector for Amazon EKS, and Amazon Managed Grafana (AMG)Step 8Users can access Amazon EKS cluster(s) with best practice add-ons, optionally configured Observability stack and RBAC based security mapped to IAM roles for workload deployments using Kubernetes API that is exposed via Network Load Balancer### Deploy and run Model Inference and Agentic AI applications on EKS cluster

This reference architecture diagram demonstrates how to deploy ML Models and MCP server and agent on EKS cluster, provide unified model inference API Gateway, and implement Agentic AI capabilities to enable models’ interactions.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/scalable-model-inference-and-agentic-ai-on-amazon-eks.pdf)Step 1Guidance workloads are deployed into an Amazon EKS cluster, configured for application readiness with compute plane managed by Karpenter autoscaler. This setup efficiently auto-scales AWS Graviton, GPU and AWS Inferentia based compute nodes across multiple Availability Zones (AZs), ensuring robust infrastructure distribution and high availability of various Kubernetes services.Step 2User interaction starts with an authentication to the EKS cluster via IAM. Application HTTP(s) requests are directed to an exposed endpoint, managed by Elastic Load Balancing and protected by AWS Web Application Firewall (WAF). This endpoint URL serves as the gateway for all user queries and ensures balanced distribution of incoming traffic with consistent accessibility.Step 3The Orchestrator agent, powered by Strands Agent SDK, serves as the central workflow coordination hub. It processes incoming queries by connecting with reasoning models supported by LiteLLM and vLLM services, analysing the requests, and determining the appropriate workflow and tools needed for response generation. LiteLLM functions as a unified API gateway proxy for model management, providing centralized security controls and standardized access to both embedding and reasoning models.Step 4Orchestrator agent delegates control to RAG agent to verify knowledge base validity to initiate Knowledge validation. When updates are needed, the RAG agent initiates the process of embedding new information into the Amazon OpenSearch cluster, ensuring the Knowledge Base remains current and comprehensive.Step 5KubeRay cluster handles the embedding process where the Ray header dynamically manages cluster worker node scaling based on resource demands. These worker nodes execute the embedding process through the llamacpp framework, while the RAG agent simultaneously embeds user questions and searches for relevant information with the OpenSearch cluster.Step 6Evaluation agent performs Response Quality assurance which leverages models hosted in Amazon Bedrock. This agent implements a feedback-based correction loop using RAGAS metrics to assess response quality and provides relevancy scores to the orchestrator agent for decision-making purposes.Step 7When the RAG agent's responses receive relevancy scores below the configured threshold, the Orchestrator agent initiates a web search process. It retrieves the Tavily web search API tool from the Web search Model context Protocol (MCP) server and performs dynamic queries to obtain supplementary or corrective information.Step 8Models based on vLLM framework running on GPU (or Inferentia) EKS compute nodes generate final responses which are returned via LiteLLM gateway to the Orchestrator agent. The reasoning model processes the aggregated information, including both Knowledge Base data and Web search results when applicable, refining and rephrasing the content to create a coherent and accurate response for the user's prompt.Step 9Throughout this entire process, the Orchestrator agent maintains comprehensive interaction tracking. It automatically traces all agent activities and communications, with the resulting metrics being visualized via the LangFuse service, providing transparency and monitoring of the system's operations. Additional EKS infrastructure level observability is available via previously deployed and configured Prometheus /Grafana monitoring stack.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/compute/scalabale-model-inference-and-agentic-ai-on-amazon-eks.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks)

[Read usage guidelines](/solutions/guidance-disclaimers/)
