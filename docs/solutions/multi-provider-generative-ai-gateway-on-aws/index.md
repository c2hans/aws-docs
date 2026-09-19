---
source_url: https://docs.aws.amazon.com/solutions/multi-provider-generative-ai-gateway-on-aws/index.html
---

---
title: 'Guidance for Multi-Provider Generative AI Gateway on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/multi-provider-generative-ai-gateway-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Multi-Provider Generative AI Gateway on AWS

## Overview

This Guidance demonstrates how to streamline access to numerous large language models (LLMs) through a unified, industry-standard API gateway based on OpenAI API standards. By deploying this Guidance, you can simplify integration while gaining access to tools that track LLM usage, manage costs, and implement crucial governance features. This allows easy switching between models, efficient management of multiple LLM services within applications, and robust control over security and expenses.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/multi-provider-generative-ai-gateway-on-aws.pdf)

![Architecture diagram](/images/solutions/multi-provider-generative-ai-gateway-on-aws/images/multi-provider-generative-ai-gateway-on-aws-1.png)

1. **Step 1**: Tenants and client applications access the LiteLLM gateway proxy API through the Amazon Route 53 URL endpoint or Amazon CloudFront, which is protected against common web exploits and bots using AWS WAF.
1. **Step 2**: AWS WAF forwards requests to Application Load Balancer (ALB) to automatically distribute incoming application traffic to Amazon Elastic Container Service (Amazon ECS) tasks or Amazon Elastic Kubernetes Service (Amazon EKS) pods running generative AI gateway containers. TLS/SSL encryption secures traffic to the load balancer using a certificate issued by AWS Certificate Manager (ACM).
1. **Step 3**: Container images for API/middleware and LiteLLM applications are built during guidance deployment and pushed to Amazon Elastic Container Registry (Amazon ECR). They are used for deployment to Amazon ECS on AWS Fargate or Amazon EKS clusters that run these applications as containers in ECS tasks or EKS pods, respectively. LiteLLM provides a unified application interface for configuration and interacting with LLM providers. The API/middleware integrates natively with Amazon Bedrock to enable features not supported by the LiteLLM opensource project.
1. **Step 4**: Models hosted on Amazon Bedrock and Amazon Nova provide model access, guardrails, prompt caching, and routing to enhance the AI gateway and additional controls for clients through a unified API. Model access is also available for models deployed on Amazon SageMaker AI. Access to required Amazon Bedrock models must be properly configured.
1. **Step 5**: External model providers (such as OpenAI, Anthropic, or Vertex AI) are configured using the LiteLLM Admin UI to enable additional model access through LiteLLM's unified application interface. Integrate pre-existing configurations of third-party providers into the gateway using LiteLLM APIs.
1. **Step 6**: LiteLLM integrates with Amazon ElastiCache (Redis OSS), Amazon Relational Database Service (Amazon RDS), and AWS Secrets Manager services. Amazon ElastiCache enables multi-tenant distribution of application settings and prompt caching. Amazon RDS enables persistence of virtual API keys and other configuration settings provided by LiteLLM. Secrets Manager stores external model provider credentials and other sensitive settings securely.
1. **Step 7**: LiteLLM and the API/middleware store application sends logs to the dedicated Amazon Simple Storage Service (Amazon S3) storage bucket for troubleshooting and access analysis.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/ai-ml/guidance-for-multi-provider-generative-ai-gateway-on-aws.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-multi-provider-generative-ai-gateway-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

LiteLLM application logs are stored in S3 buckets for audit and analysis purposes. Amazon ECS and Amazon EKS feature built-in tools and plugins to monitor health and performance of their respective clusters, streaming log data to Amazon CloudWatch for event data analysis. These managed services reduce the operational burden of deploying and maintaining application platform infrastructure. CloudWatch Logs provide comprehensive insights into both infrastructure and application levels of Amazon ECS and Amazon EKS clusters, enabling effective troubleshooting and analysis. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

ACM provides managed SSL/TLS certificates for secure communication and automatically manages these certificates to prevent vulnerabilities. AWS WAF protects web applications from common exploits and provides real-time monitoring and custom rule creation capabilities. Additionally, Amazon ECS and Amazon EKS clusters operate with public and private networks for additional security and isolation. AWS Identity and Access Management (IAM) roles and policies follow the least-privilege principle for both deployment of the Guidance and cluster operations, while Secrets Manager stores external model provider credentials and other sensitive settings securely. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon ECS and Amazon EKS provide container orchestration, automatically handling task placement and recovery across multiple Availability Zones for LiteLLM proxy and API/middleware containers. Amazon ElastiCache enables multi-tenant distribution of application settings and prompt caching. Together, these services enable highly available applications that can maintain operational SLAs even if individual components fail, offering auto-recovery capabilities. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

ElastiCache enhances performance by providing sub-millisecond latency for frequently accessed data through in-memory caching. ALB effectively distributes incoming application traffic across multiple targets based on advanced routing rules and health checks. Amazon ECS on Fargate and Amazon EKS provide on-demand efficient infrastructure for running application containers, offering auto-scaling based on workload demands. The native integration of LiteLLM with ElastiCache and Amazon RDS significantly reduces database load and improves application response times by serving cached content and efficiently routing requests. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon RDS offers automated backups, patching, and scaling, reducing operational overhead and cost of operation. These services provide options for reserved instances or savings plans, allowing you to significantly reduce costs for predictable workloads compared to on-demand pricing. Amazon ECS and Amazon EKS allow you to run containers on efficient compute Amazon Elastic Compute Cloud (Amazon EC2) instances, such as AWS Graviton, or in a serverless Fargate infrastructure. This helps optimize compute costs by right-sizing resources and only paying for what you use. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon EKS and Amazon ECS container orchestration engines enable multiple applications to share underlying compute resources (including efficient compute EC2 instances), maximizing resource utilization and reducing idle capacity. As a managed service, Amazon Bedrock eliminates the need for dedicated GPU infrastructure by sharing pre-trained models across multiple users. This shared infrastructure approach reduces the overall hardware resource footprint and energy consumption compared to running separate dedicated environments. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Guidance for Multi-Provider Generative AI Gateway on AWS**: This workshop provides an overview of Guidance for Multi-Provider Generative AI Gateway on AWS, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the Guidance.

[Learn more](https://catalog.us-east-1.prod.workshops.aws/workshops/db0f23ea-2442-4962-9a54-04dcdab7de59/en-US)

[Read usage guidelines](/solutions/guidance-disclaimers/)
