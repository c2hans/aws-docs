---
source_url: https://docs.aws.amazon.com/solutions/multi-agent-employee-virtual-assistant-on-aws/index.html
---

# Guidance for Multi-Agent Employee Virtual Assistant on AWS

## Overview

This Guidance demonstrates how TeamLink AI, an employee virtual assistant, centralizes access to cross-functional knowledge through a unified, intelligent chat interface. Leveraging advanced language models hosted on Amazon Bedrock, this virtual assistant helps break down departmental information silos by providing employees with instant access to critical organizational knowledge. This Guidance streamlines workplace efficiency by helping employees quickly find and retrieve the information they need, when they need it, eliminating the traditional barriers between different departmental knowledge bases.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/multi-agent-employee-virtual-assistant-on-aws.pdf)

![Architecture diagram](/images/solutions/multi-agent-employee-virtual-assistant-on-aws/images/multi-agent-employee-virtual-assistant-on-aws-1.png)

1. **Step 1**: The user accesses TeamLink AI, an Amazon Bedrock-powered virtual assistant, through their web browser to submit queries and receive instant cross-departmental information.
1. **Step 2**: When the user accesses the application, Amazon CloudFront delivers the web interface content, helping ensure a smooth experience regardless of the user's location.
1. **Step 3**: Behind the scenes, Amazon Simple Storage Service (Amazon S3) serves the static website content, while Amazon Cognito verifies the user's identity and permissions to access the system.
1. **Step 4**: After the user submits their query, the client application triggers an AWS Lambda function that acts as the orchestrator for the AI processing workflow.
1. **Step 5**: The Lambda function forwards the user's request to the Amazon Bedrock Supervisor Agent, which acts as the primary coordinator for processing the query.
1. **Step 6**: The Supervisor Agent within Amazon Bedrock analyzes the query and directs it to the appropriate Domain-Specific Agent for specialized processing.
1. **Step 7**: To locate relevant information, the Domain Agent queries Amazon Bedrock Knowledge Bases, the system's central information repository.
1. **Step 8**: The system then uses Amazon OpenSearch Serverless to search through indexed documents for query-related matches.
1. **Step 9**: During this process, Amazon S3 provides access to domain-specific datasets that have been previously indexed in the OpenSearch system.
1. **Step 10**: If the query requires external information, the system activates a Lambda Web Search function to expand the search beyond internal resources.
1. **Step 11**: Lambda web search queries the internet for additional data if needed, using Tavily API.
1. **Step 12**: Throughout the interaction, Amazon DynamoDB maintains a record of the entire conversation between the user and system.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-employee-virtual-assistant-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Lambda orchestrates interactions between services, while DynamoDB tracks conversation history. Amazon Bedrock manages AI capabilities, andAmazon OpenSearch Serviceefficiently indexes and searches large datasets. Amazon S3 provides scalable storage for AI/ML data. This comprehensive suite enables automated operations, consistent deployments, and data-driven insights for both traditional and AI/ML components. Teams can automate deployments, monitor system health, and analyze application performance across all components. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito provides secure user authentication and authorization for the virtual assistant interface, handling complex authentication workflows and supporting enterprise identity federation. CloudFront delivers encrypted content with edge security. Amazon Bedrock helps ensure secure AI model access and execution with built-in security controls, eliminating the need for custom AI infrastructure security. AWS Identity and Access Management (IAM) implements fine-grained permissions for service-to-service communication, following a least-privilege access model. Both OpenSearch Service and DynamoDB encrypt data at rest and maintain secure access patterns for knowledge base queries and conversation history. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

CloudFront distributes content across global edge locations, helping ensure low-latency access to the web UI and preventing single point of failure for content delivery. Amazon S3 provides highly durable storage for static assets and knowledge base content with 99.999999999% durability to protect critical data. DynamoDB offers multi-AZ replication for conversation history, protecting against regional failures. Lambda functions provide distributed processing with automatic scaling and fault isolation. Amazon Bedrock supports reliable AI processing through multiple domain-specific agents. This comprehensive approach creates a highly available and fault-tolerant system, so that teams can maintain workplace productivity without interruption. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

CloudFront delivers low-latency content globally, minimizing latency for users worldwide through its global edge network. Amazon S3 offers fast access to static assets and datasets, while DynamoDB provides low-latency access to conversation history data. Lambda enables serverless processing for AI orchestration and web searches, allowing for quick scaling based on demand and cost-efficiency. Amazon Bedrock provides efficient AI processing capabilities without managing complex infrastructure. OpenSearch Service enables rapid retrieval of indexed documents. Together, these services create a highly performant and scalable approach that adapts to varying workload requirements and traffic patterns. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 offers low-cost storage with different tiers for cost-effective data management. CloudFront uses edge caching to reduce data transfer costs and improve performance. Together, these services helpminimize data transfer charges and storage costs. Additionally, Lambda provides a serverless compute model where you only pay for consumed compute time, eliminating the need for maintaining and scaling infrastructure. DynamoDB offers an on-demand capacity mode that allows for cost-effective handling of variable workloads without overprovisioning. Amazon Bedrock enables AI processing without maintaining expensive ML infrastructure. This suite of services allows this Guidance to scale efficiently, matching resources to actual usage, while providing the performance and capabilities needed for a sophisticated employee virtual assistant. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda enables serverless computing, spinning up resources only when needed and scaling automatically based on demand. This helps ensure compute resources are used efficiently, minimizing idle time and energy waste. Amazon Bedrock provides optimized AI models, reducing the need for custom infrastructure and maximizing AI processing efficiency. DynamoDB auto-scaling capabilities adjust capacity units based on actual usage patterns, maintaining high utilization of deployed resources. CloudFront provides a global content delivery network that reduces redundant data transfers, lowering network traffic and associated energy consumption. By leveraging serverless and managed services, this Guidance minimizes the need for provisioning and maintaining physical hardware, reducing overall environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
