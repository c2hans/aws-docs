---
source_url: https://docs.aws.amazon.com/solutions/agentic-ai-research-platform-on-aws/index.html
---

---
title: 'Guidance for Agentic AI Research Platform on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/agentic-ai-research-platform-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Agentic AI Research Platform on AWS

## Overview

This Guidance demonstrates how organizations can eliminate research bottlenecks that cost millions in delayed decisions by deploying an AI-powered platform that transforms weeks of manual data gathering into minutes of conversational queries. The platform uses Amazon Bedrock to power intelligent agents that can think through complex problems, execute analytical code, and pull insights from both proprietary knowledge bases and real-time web sources. These agents operate through a secure containerized environment on Amazon ECS, with all sensitive data remaining within the organization's AWS infrastructure while maintaining enterprise-grade security through AWS WAF and Cognito authentication. You can democratize analytical capabilities across your team regardless of technical skill level, enabling faster time-to-insight for competitive analysis, technical research, and strategic planning through simple conversational interfaces.

## Benefits

### Accelerate research with intelligent agents

Deploy specialized AI agents that automatically route complex queries to the most capable specialist. Reduce research time while maintaining accuracy through multi-agent collaboration powered by Amazon Bedrock.

### Scale research capabilities without infrastructure overhead

Leverage serverless containers on Amazon Fargate to automatically scale your research platform based on demand. Focus on insights while AWS manages the underlying infrastructure and orchestration.

### Secure enterprise research with layered protection

Protect sensitive research data with AWS WAF, Amazon Cognito authentication, and AWS Secrets Manager for credential management. Maintain compliance while enabling seamless access to internal knowledge bases and external sources.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/agentic-ai-research-platform-on-aws.pdf)

![Architecture diagram](/images/solutions/agentic-ai-research-platform-on-aws/images/agentic-ai-research-platform-on-aws-1.png)

1. **Step 1**: The authenticated user accesses the web application through their browser, with requests first passing through AWS WAF for security filtering. Amazon CloudFront then delivers the static web content, while Amazon Cognito handles user authentication and authorization for secure access to the platform.
1. **Step 2**: User requests are routed through the Application Load Balancer to Amazon Fargate, which hosts the containerized application running on Amazon ECS. The container images for the application are stored and managed in Amazon ECR, ensuring secure and reliable deployment of the Amazon Bedrock AgentCore Runtime and associated components.
1. **Step 3**: The application leverages Amazon AgentCore Runtime, built with the Strands Agents SDK, to orchestrate and manage the specialized AI agents that intelligently route research queries to the appropriate handler. When a research query is received, the Amazon Bedrock AgentCore Runtime routes it to either the Base Agent or Custom Agent depending on the task complexity and requirements.
1. **Step 4**: These agents are powered by Amazon Bedrock and have access to a comprehensive toolset including file operations (read_file, create_file, append_to_file), command execution (execute_command), knowledge retrieval (retrieve_kb_data), search capabilities (web_search, news_search), and text manipulation (str_replace).
1. **Step 5**: The agents retrieve contextual information and domain knowledge from Amazon Bedrock Knowledge Base, which is populated with relevant data stored in S3 Vectors for semantic search and S3 Document Bucket for raw document storage.
1. **Step 6**: Sensitive configuration data, API keys, and database credentials required by the agents are securely stored and retrieved from AWS Secrets Manager, which maintains a connection to Amazon RDS for persistent storage of secrets and configuration management. This ensures that all agent operations maintain security best practices while accessing necessary resources to complete research tasks and deliver intelligent, scalable research assistance.
1. **Step 7**: The web_search and news_search tools allow agents to search for websites and news from the public internet.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-agentic-ai-research-platform-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
