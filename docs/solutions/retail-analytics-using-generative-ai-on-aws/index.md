---
source_url: https://docs.aws.amazon.com/solutions/retail-analytics-using-generative-ai-on-aws/index.html
---

---
title: 'Guidance for Retail Analytics using Generative AI on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/retail-analytics-using-generative-ai-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Retail Analytics using Generative AI on AWS

## Overview

This Guidance shows how to use large language models (LLMs) to generate SQL queries and perform data analytics, enhancing the value of your data. It leverages Amazon Bedrock and Amazon SageMaker to build a SQL generator that uses natural language processing (NLP). To improve accuracy for SQL generation, this Guidance also uses retrieval augmented generation (RAG) to retrieve historical data as few-shot samples in the prompt. With this Guidance, you can optimize costs for data analysis and operations teams by automating routine tasks, reducing working hours, and minimizing labor costs.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/retail-analytics-using-generative-ai-on-aws.pdf)

![Architecture diagram](/images/solutions/retail-analytics-using-generative-ai-on-aws/images/retail-analytics-using-generative-ai-on-aws-1.png)

1. **Step 1**: The user interacts with the system through Elastic Load Balancing (ELB), which directs traffic to the appropriate service within the AWS Cloud.
1. **Step 2**: The configurator uses ELB to access configuration-related services.
1. **Step 3**: Amazon Cognito handles user authentication and authorization, ensuring secure access to the services.
1. **Step 4**: The authenticated user accesses the frontend (Service 2) and API (Service 3) hosted on Amazon Elastic Container Service (Amazon ECS), which manages the deployment and scaling of these services.
1. **Step 5**: AWS Secrets Manager securely stores and retrieves sensitive information, such as database credentials, used by the services.
1. **Step 6**: Amazon DynamoDB stores user profiles and related data, providing a scalable and high-performance NoSQL database.
1. **Step 7**: The embedding module leverages Amazon OpenSearch Service and embedding models from Amazon Bedrock (Titan) or Amazon SageMaker (for example, BGE) to process and index data for efficient querying.
1. **Step 8**: LLMs hosted on Amazon Bedrock (Claude) or SageMaker (for example, Llama 3) converts natural language text into SQL queries, enabling users to interact with databases using plain language.
1. **Step 9**: The system pulls data definition language (DDL) information and queries customer data sources such as Amazon Aurora, Amazon Relational Database Service (Amazon RDS), Amazon Athena, and other third-party integrations to fetch data as required by the user queries.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-retail-analytics-using-generative-ai-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS managed services like Amazon ECS, Amazon Bedrock, and SageMaker offload operational burden, allowing developers to focus on application logic rather than undifferentiated heavy lifting tasks. These services handle provisioning, scaling, patching, and infrastructure maintenance, so applications can handle varying user traffic without compromising performance or availability through automatic scaling capabilities. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) manages access to AWS resources by creating and managing users and groups, controlling their permissions to perform specific actions on specific resources. Implementing the principle of least privilege minimizes the risk of unauthorized access, enhancing application security. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon ECS relieves the responsibility of managing and scaling underlying infrastructure, reducing operational overhead and enabling automatic scaling and recovery from failures. OpenSearch Service provides high availability and resilience against node failures or data loss, helping ensure critical functionalities remain uninterrupted. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

OpenSearch Service is a distributed search and analytics engine leveraging Apache Lucene for high-performance text search and data retrieval. It enables efficient storage and fast retrieval of large volumes of data, such as our historical question and SQL datasets. By using OpenSearch Service in this Guidance, you can rapidly access relevant information and assemble prompts for our text-to-SQL functionality, benefiting from its caching mechanisms and distributed architecture for enhanced performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

OpenSearch Service is a managed service that relieves you from managing search infrastructure. AWS handles the underlying resources, patching, and scaling, allowing you to focus on application functionality. Its ability to scale resources based on usage help optimize costs by avoiding overprovisioning or under-utilization of resources. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS Cloud infrastructure is designed for sustainability, leveraging energy-efficient data centers, renewable energy sources, and optimized resource utilization. You can offload infrastructure management to AWS, reducing environmental impact while leveraging sustainable practices for search and analytics needs. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
