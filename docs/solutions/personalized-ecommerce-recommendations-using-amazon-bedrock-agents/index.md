---
source_url: https://docs.aws.amazon.com/solutions/personalized-ecommerce-recommendations-using-amazon-bedrock-agents/index.html
---

---
title: 'Guidance for Personalized Ecommerce Recommendations Using Amazon Bedrock Agents'
canonical_url: https://docs.aws.amazon.com/solutions/personalized-ecommerce-recommendations-using-amazon-bedrock-agents/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Personalized Ecommerce Recommendations Using Amazon Bedrock Agents

## Overview

This Guidance demonstrates how to implement personalized ecommerce recommendations using Amazon Bedrock Agents. The Guidance leverages advanced natural language processing to analyze customer preferences and behavior, providing tailored product suggestions that enhance the shopping experience. Integrating Amazon Bedrock Agents into ecommerce systems can help you boost customer engagement, increase conversion rates, and optimize recommendation strategies. Built on a robust foundation of cloud services, this Guidance illustrates how to create scalable, efficient recommendation agents while maintaining security and cost optimization.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/personalized-ecommerce-recommendations-using-amazon-bedrock-agents.pdf)

![Architecture diagram](/images/solutions/personalized-ecommerce-recommendations-using-amazon-bedrock-agents/images/personalized-ecommerce-recommendations-using-amazon-bedrock-agents-1.png)

1. **Step 1**: Amazon Simple Storage Service (Amazon S3) stores sales pitch data for the knowledge base to reference.
1. **Step 2**: Amazon Bedrock Knowledge Bases contains historical sales scripts that Amazon Bedrock Agents uses to guide interactions.
1. **Step 3**: Amazon Titan Embeddings models on Amazon Bedrock generates embeddings for vector search to find relevant products.
1. **Step 4**: The user interacts with the chatbot, triggering product recommendations and sales processes.
1. **Step 5**: Amazon Bedrock Agents acts as the chatbot interface that recommends and sells products to the user based on their inquiries and needs.
1. **Step 6**: The OpenAPI Schema hosted on an S3 bucket contains schema or structured data that helps Amazon Bedrock Agents interpret and process information accurately.
1. **Step 7**: AWS Lambda executes backend logic in response to triggers from Amazon Bedrock Agents, enabling real-time operations and responses.
1. **Step 8**: Amazon OpenSearch Service supports vector search to quickly retrieve relevant products or content for the user.
1. **Step 9**: Amazon Personalize generates personalized product recommendations based on user IDs.
1. **Step 10**: Amazon DynamoDB manages user and item data to provide personalized recommendations based on user behavior and preferences.
1. **Step 11**: Anthropic Claude 3 in Amazon Bedrock generates content using AI, crafting personalized responses or product descriptions to effectively engage users.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-personalized-ecommerce-recommendations-using-amazon-bedrock-agents/tree/main#)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

DynamoDB and Lambda streamline data management and backend processing tasks. DynamoDB delivers high availability and low-latency access with automated backups, monitoring, and security features that minimize manual intervention. Lambda executes code in response to events without infrastructure management, automatically scaling to match demand. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) and Amazon OpenSearch Serverless establish robust security controls for data access and user management. OpenSearch Serverless implements fine-grained access control for precise user permissions over search and analytics data. Through seamless integration with IAM, authentication and authorization mechanisms help ensure data remains protected while maintaining stringent access controls. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda and DynamoDB create a foundation for consistent, uninterrupted operations. Lambda distributes workloads across multiple Availability Zones, providing built-in fault tolerance and automatic scaling for varying demands. DynamoDB enhances this reliability through multi-Region replication, automatic scaling, and comprehensive backup capabilities so that data remains accessible and protected even during system failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda and DynamoDB deliver optimal performance through intelligent resource utilization. Lambda executes backend logic only when triggered, eliminating idle resource consumption. DynamoDB provides fast data access through built-in caching and indexing, enabling rapid retrieval of information while automatically scaling to match user demand patterns. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

OpenSearch Serverless eliminates unnecessary spending through dynamic resource allocation. By automatically scaling OpenSearch Compute Units based on actual usage patterns, resources are provisioned only when needed. This approach prevents overprovisioning while maintaining responsiveness during peak traffic periods. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon S3 Intelligent-Tiering reduces environmental impact through smart data storage management. The automated movement of data between storage tiers based on access patterns optimizes energy consumption without compromising accessibility. When data becomes less frequently accessed, it automatically transitions to lower-energy tiers, minimizing the carbon footprint of long-term data storage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
