---
source_url: https://docs.aws.amazon.com/solutions/building-agentic-ai-powered-engineering-knowledge-assistants-on-aws/index.html
---

---
title: 'Guidance for Building Agentic AI powered Engineering Knowledge Assistants on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-agentic-ai-powered-engineering-knowledge-assistants-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Building Agentic AI powered Engineering Knowledge Assistants on AWS

## Overview

This Guidance demonstrates how to implement intelligent AI assistants that revolutionize enterprise knowledge management and accessibility. It helps organizations break down information silos and accelerate data access by creating a unified knowledge ecosystem that combines industry expertise with company-specific insights. The solution shows how to enable multi-modal interactions for instant knowledge retrieval and contextual recommendations, serving diverse stakeholders from design to manufacturing teams. Furthermore, it demonstrates how continuous learning capabilities can enhance cross-team collaboration, streamline decision-making processes, and drive engineering innovation, ultimately reducing cycle time to value across the organization.

## Benefits

### Accelerate engineering decision-making

Transform complex R&D workflows by connecting specialized AI agents to your engineering data sources. Reduce time-to-insight from days to minutes while maintaining technical accuracy through grounded responses.

### Unify fragmented engineering knowledge

Break down information silos by integrating disparate data sources into a unified AI assistant. Enable cross-functional teams to access critical engineering insights regardless of their technical expertise.

### Scale engineering expertise autonomously

Deploy specialized AI agents that handle routine engineering tasks independently. Free your experts to focus on innovation while maintaining compliance and quality standards.

## How it works

### Diagram 1

This diagram illustrates a flexible agentic AI framework on AWS that dynamically assigns specialized agents based on user identity and needs. The system authenticates users and provisions appropriate agent capabilities, maintaining security boundaries while enabling modular addition of new agents and tools for specific engineering domains.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/Agentic%20AI%20powered%20Engineering%20Knowledge%20Assistants.pdf)Step 1Each persona has a set of agents to help perform their respective tasks.Step 2Users engage with the system through a web application that processes initial requests.Step 3Verify identity and permissions through the system's authentication process. Based on the verified role, the system determines which specialized AI agent capabilities to activate for the session.Step 4Coordinate specialized AI functions through the agent management layer, which initializes agents, caches information, streams responses, and adapts to the persona and task requirements.Step 5Access relevant information sources including Retrieval Augmented Generation (RAG) for document retrieval, GraphRAG for relationship analysis, and specialized knowledge bases like Digital Thread and Compliance Standards documentation. These sources provide context-aware responses tailored to the engineering domain.Step 6Execute custom engineering workflows through intelligent agents that access third-party Application Programming Interfaces (APIs), query data stores, and perform specialized logic based on requirements.Step 7Store and organize engineering data across multiple systems including databases, data lakes, and product lifecycle management systems for continuous access and analysis.### Diagram 2

This architecture diagram implements key components from the previous framework: Authentication (Section 2) with Keycloak, Agent Management (Section 3) via the Session Agent Manager, specialized agent routing (Section 4) using AWS Strands Agents SDK, and Custom Tool integration (Section 6) including RAG operations with Bedrock Knowledge Bases and RFQ processing - all hosted on Amazon Elastic Kubernetes Service to provide a secure, flexible framework for engineering R&D.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/Agentic%20AI%20powered%20Engineering%20Knowledge%20Assistants.pdf)Step 1Submit engineering queries through the chat interface hosted on Amazon Elastic Kubernetes Service (Amazon EKS).Step 2Authenticate via Keycloak. The system routes requests to the session agent manager for orchestration.Step 3Session agent manager defines role-based access to agents. The manager initializes and caches each agent for the session.Step 4Route requests to agents built using AWS Strands Agents SDK. The SDK enables developers to create custom agents (such as RFQ agents or Digital Thread agents) that can be specialized for different engineering workflows. The SDK provides the building blocks and primitives needed for multi-agent implementations.Step 5Agents leverage tools that define code-based functionality. Available tools include Knowledge Base Tool for information retrieval, Send Email Tool for Amazon Simple Email Service (Amazon SES) communication, and customizable implementations supporting multiple agents.Step 6Tools perform retrieval augmented generation (RAG) with Amazon Bedrock Knowledge Bases, send RFQ emails via SES, and execute custom functions to complete queries.### Diagram 3

This architecture diagram shows a knowledge base for retrieval augmented generation (RAG) and GraphRAG pipeline.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/Agentic%20AI%20powered%20Engineering%20Knowledge%20Assistants.pdf)Step 1Ingest data from identified sources using AWS Database Migration Service (AWS DMS), AWS DataSync for large datasets, and AWS Glue for ETL jobs into Amazon Simple Storage Service (Amazon S3).Step 2Structure your Amazon S3 data with a purpose-driven organization strategy. Create distinct buckets that align with specific business functions and user needs. This thoughtful organization improves retrieval accuracy and maintains appropriate context for different user groups' queries.Step 3Configure Amazon Bedrock Knowledge Bases with Amazon OpenSearch Serverless to ingest data from Amazon S3. While Amazon Bedrock provides access to various foundation models through a unified API, we've used Amazon Titan Embeddings for creating vector embeddings, enabling efficient similarity search ideal for unstructured data like compliance documents and manuals.Step 4Configure Amazon Bedrock Knowledge Bases with Amazon Neptune Analytics to ingest relational data from Amazon S3. This setup excels at handling complex, interconnected datasets like supply chain networks, enabling queries that understand relationships between suppliers, materials, and distribution channels.Step 5Query the Amazon Bedrock Knowledge Base through API calls to ground LLM responses with your organizational data for factually accurate results.### Diagram 4

This architecture diagram shows continuous integration and continuous deployment diagram of the end-to-end solution.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/Agentic%20AI%20powered%20Engineering%20Knowledge%20Assistants.pdf)Step 1Access the application through the Network Load Balancer (NLB) created by Ingress NGINX for traffic distribution.Step 2Ingress NGINX routes incoming traffic to the correct ingress using path-based routing rules.Step 3Knowledge Assistant Ingress directs traffic to the appropriate endpoint within the Knowledge Assistant application.Step 4Argo CD syncs Knowledge Assistant application manifests from the GitHub repository, serving as the source-of-truth for GitOps deployment.Step 5Argo CD deploys the synchronized manifests from the source-of-truth onto the Amazon Elastic Kubernetes Service (Amazon EKS) cluster.Step 6GitHub Actions builds the Knowledge Assistant Docker image and pushes it to Amazon Elastic Container Registry (Amazon ECR) upon each release.Step 7Knowledge Assistant deployment pulls the latest image from Amazon ECR for container orchestration.### Diagram 5

This architecture diagram shows alternative agent hosting on Amazon Bedrock AgentCore. Deploy secure, scalable AI agents on AWS with AgentCore's comprehensive set of enterprise-grade services, enabling complex workflows across tools and data sources while eliminating infrastructure management overhead.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/Agentic%20AI%20powered%20Engineering%20Knowledge%20Assistants.pdf)Step 1Submit engineering queries through the chat interface hosted on Amazon Elastic Kubernetes Service (Amazon EKS).Step 2Execute agent code, tools, and instructions in Amazon Bedrock AgentCore Runtime's serverless environment, supporting multiple frameworks and 8-hour sessions.Step 3Secure agent operations with Amazon Bedrock AgentCore Identity, managing authentication and access controls across all interactions.Step 4Build context-aware agents with Amazon Bedrock AgentCore Memory, maintaining both short-term and long-term knowledge across interactions.Step 5Access Amazon Bedrock for foundation models, enabling flexible use of various LLMs through a unified API.Step 6Transform REST APIs into Model Context Protocol (MCP) servers through Amazon Bedrock AgentCore Gateway, enabling reusable tool sharing across agents.Step 7Connect to third-party tools like Amazon Bedrock Knowledge Bases to enrich context and perform tasks.Step 8Monitor agent performance through Amazon Bedrock AgentCore Observability, tracking key metrics and ensuring operational excellence.[Read usage guidelines](/solutions/guidance-disclaimers/)
