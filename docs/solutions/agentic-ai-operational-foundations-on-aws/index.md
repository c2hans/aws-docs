---
source_url: https://docs.aws.amazon.com/solutions/agentic-ai-operational-foundations-on-aws/index.html
---

---
title: 'Guidance for Agentic AI Operational Foundations on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/agentic-ai-operational-foundations-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Agentic AI Operational Foundations on AWS

## Overview

This Guidance demonstrates how to accelerate and de-risk AI agent development through a comprehensive, production-ready solutions approach. It shows organizations how to establish essential service capabilities including multi-model governance, robust observability, and automated guardrails - critical elements that are often overlooked in early AI projects. The solution helps teams avoid common pitfalls and reduce time-to-value by providing pre-integrated components and proven architectural patterns that support the complete AI application lifecycle. By implementing centralized monitoring, evaluation, and safety controls, this guidance enables organizations to scale their AI initiatives reliably while maintaining visibility and control over model behavior and costs. The offerings approach transforms scattered proof-of-concepts into sustainable, production-grade AI solutions that can evolve with business needs.

## Benefits

### Accelerate customer service resolution

Deploy intelligent AI agents that understand context and automate support workflows. Reduce response times while maintaining personalized, high-quality customer interactions through Amazon Bedrock's agentic capabilities.

### Scale support without scaling costs

Handle increasing customer inquiries automatically using serverless AI orchestration. Your agents learn from each interaction while AWS manages the infrastructure, enabling cost-effective growth.

### Unify knowledge and ticketing systems

Connect existing Zendesk workflows with AI-powered knowledge retrieval and web search capabilities. Enable seamless escalation paths while maintaining comprehensive observability across all customer interactions.

## How it works

### Agentic AI Operational Foundations

This architecture diagram illustrates how to effectively support applications using agentic AI on AWS. It shows the key components and their interactions, providing an overview of the architecture's structure and functionality. The architecture enables authenticated users to interact with AI-powered agents through a frontend application, where Amazon Bedrock AgentCore orchestrates LangGraph-based agents that access knowledge bases, perform web searches, and create support tickets. The architecture incorporates comprehensive security, scalable storage, external integrations, and monitoring capabilities to deliver intelligent, contextual customer support experiences. To deploy Generative AI Gateway (Litellm), refer to Diagram 2.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-agentic-ai-foundation-solutions-on-aws.pdf)Step 1An authenticated user interacts with the Frontend Application, which validates their identity through Amazon Cognito.Step 2The frontend application forwards the user's request to the Amazon Bedrock AgentCore runtime.Step 3Amazon Bedrock AgentCore Identity validates user permissions and establishes secure service-to-service authentication, while Amazon Bedrock Guardrails evaluate the incoming request to ensure it meets safety and compliance requirements before proceeding.Step 4Amazon Bedrock AgentCore Runtime initializes the LangGraph Agent, which acts as the central orchestrator that will make decisions about the workflow path and coordinate all subsequent processing steps.Step 5The LangGraph Agent queries Amazon Bedrock AgentCore Memory to retrieve conversation history and contextual information, enabling continuity across sessions and personalized interactions based on previous exchanges.Step 6The LangGraph Agent analyzes request types and context to determine processing paths, then connects to Amazon Bedrock AgentCore Gateway to discover and invoke available tools such as the Web Search API for gathering external information.Step 7The LangGraph Agent retrieves domain-specific information through the Fetch Context tool powered by Amazon Bedrock Knowledge Base, Amazon S3, and Amazon OpenSearch Vector DB, or creates support tickets via Create Ticket API based on request analysis.Step 8The LangGraph Agent orchestrates response generation using Amazon Bedrock Models, via Multi-Provider Generative AI Gateway (Litellm) combining retrieved knowledge from the Amazon Bedrock Knowledge Base, tools outputs from external services, and conversation context to create intelligent, contextually appropriate responses.Step 9Throughout the entire LangGraph workflow execution, Amazon Bedrock AgentCore Observability tracks system performance, logs decision paths, tool usage patterns, and interaction outcomes, while Amazon CloudWatch monitors the overall system health and collects metrics from all AWS services.Step 10The LangGraph Agent updates Amazon Bedrock AgentCore Memory with new conversation state and user interaction data, then coordinates the final response delivery through the Amazon Bedrock AgentCore runtime back to the Frontend application and ultimately to the authenticated user.Step 11The workflow state and observability data flows to Langfuse for comprehensive tracking and analysis of agent interactions, providing detailed insights into conversation quality and system performance for continuous improvement.### Multi-Provider Generative AI Gateway

This architecture diagram demonstrates how to streamline access to numerous large language models (LLMs) through a unified, industry-standard API gateway based on OpenAI API standards. By deploying this architecture, you can simplify integration while gaining access to tools that track LLM usage, manage costs, and implement crucial governance features. This allows easy switching between models, efficient management of multiple LLM services within applications, and robust control over security and expenses.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-agentic-ai-foundation-solutions-on-aws.pdf)Step 1Tenants and client applications access the LiteLLM gateway proxy API through the Amazon Route 53 URL endpoint or Amazon CloudFront, which is protected against common web exploits and bots using AWS WAF.Step 2AWS WAF forwards requests to Application Load Balancer (ALB) to automatically distribute incoming application traffic to Amazon Elastic Container Service (Amazon ECS) tasks or Amazon Elastic Kubernetes Service (Amazon EKS) pods running generative AI gateway containers. TLS/SSL encryption secures traffic to the load balancer using a certificate issued by AWS Certificate Manager (ACM).Step 3Container images for API/middleware and LiteLLM applications are built during guidance deployment and pushed to Amazon Elastic Container Registry (Amazon ECR). They are used for deployment to Amazon ECS on AWS Fargate or Amazon EKS clusters that run these applications as containers in ECS tasks or EKS pods, respectively. LiteLLM provides a unified application interface for configuration and interacting with LLM providers. The API/middleware integrates natively with Amazon Bedrock to enable features not supported by the LiteLLM opensource project.Step 4Models hosted on Amazon Bedrock and Amazon Nova provide model access, guardrails, prompt caching, and routing to enhance the AI gateway and additional controls for clients through a unified API. Model access is also available for models deployed on Amazon SageMaker AI. Access to required Amazon Bedrock models must be properly configured.Step 5External model providers (such as OpenAI, Anthropic, or Vertex AI) are configured using the LiteLLM Admin UI to enable additional model access through LiteLLM's unified application interface. Integrate pre-existing configurations of third-party providers into the gateway using LiteLLM APIs.Step 6LiteLLM integrates with Amazon ElastiCache (Redis OSS), Amazon Relational Database Service (Amazon RDS), and AWS Secrets Manager services. Amazon ElastiCache enables multi-tenant distribution of application settings and prompt caching. Amazon RDS enables persistence of virtual API keys and other configuration settings provided by LiteLLM. Secrets Manager stores external model provider credentials and other sensitive settings securely.Step 7LiteLLM and the API/middleware store application sends logs to the dedicated Amazon Simple Storage Service (Amazon S3) storage bucket for troubleshooting and access analysis.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/sample-agentic-ai-foundation)

[Read usage guidelines](/solutions/guidance-disclaimers/)
