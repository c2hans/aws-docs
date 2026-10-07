---
source_url: https://docs.aws.amazon.com/solutions/automating-tasks-using-agents-for-amazon-bedrock/index.html
---

---
title: 'Guidance for Automating Tasks Using Agents for Amazon Bedrock'
canonical_url: https://docs.aws.amazon.com/solutions/automating-tasks-using-agents-for-amazon-bedrock/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Automating Tasks Using Agents for Amazon Bedrock

## Overview

This Guidance demonstrates how to build on existing enterprise resources to automate tasks associated with the insurance claim lifecycle using Agents and Knowledge Bases for Amazon Bedrock. Your Amazon Bedrock-powered insurance agent can assist users by creating new claims, sending pending document reminders, gathering claims evidence, and searching across existing claims and knowledge repositories. This Guidance enhances operational efficiency, improves customer service, and enables better decision support through improved knowledge management while efficiently scaling to meet your needs.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automating-tasks-using-agents-for-amazon-bedrock.pdf)

![Architecture diagram](/images/solutions/automating-tasks-using-agents-for-amazon-bedrock/images/automating-tasks-using-agents-for-amazon-bedrock-1.png)

1. **Step 1**: During pre-processing, Knowledge Bases for Amazon Bedrock segments customer source documents into manageable chunks for efficient processing.
1. **Step 2**: These chunks are converted into embeddings using an Amazon Bedrock embedding model, facilitating semantic analysis.
1. **Step 3**: The embeddings power a vector store index, such as Amazon OpenSearch Service or Amazon Aurora, enabling semantic similarity comparisons between user queries and customer data source text.
1. **Step 4**: A user provides natural language queries, which are transformed into vectors using an Amazon Bedrock embedding model.
1. **Step 5**: Agents for Amazon Bedrock uses the preprocessing template to validate, contextualize, and categorize user input. The user input (or task) is interpreted by Agents for Amazon Bedrock using conversation history, agent instructions and configuration, and the underlying Amazon Bedrock foundation model (FM).
1. **Step 6**: Knowledge Bases for Amazon Bedrock offers fully managed retrieval augmented generation (RAG) for Agents for Amazon Bedrock access to customer data. They are configured by specifying usage instructions and linking to a customer Amazon Simple Storage Service (Amazon S3) data source.
1. **Step 7**: Action groups are a set of APIs and corresponding business logic, whose OpenAPI schema is defined as JSON files stored in Amazon S3.
1. **Step 8**: During orchestration, Agents for Amazon Bedrock utilizes ReAct prompting with the orchestration prompt template to run an optimal set of actions to complete the user's task, incorporating action group API invocations and knowledge base queries to generate observations. These observations enhance the base prompt for the Amazon Bedrock FM, guiding the Agents for Amazon Bedrock decision-making process. Optionally, advanced prompts can be configured to boost Agents for Amazon Bedrock precision by employing more detailed configurations and offering manually-selected examples for few-shot prompting.
1. **Step 9**: Using the knowledge base response generation prompt template, Agents for Amazon Bedrock conducts semantic similarity searches on the knowledge base to retrieve text, which is then used to augment the base prompt with additional context.
1. **Step 10**: The Agents for Amazon Bedrock reasoning process continues until Agents for Amazon Bedrock provides a final response or prompts the user for further information, ensuring accurate and contextual interactions.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon Bedrock streamlines operations through natural language understanding, automating tasks and reducing manual effort. Agents for Amazon Bedrock leverages high-performing models to comprehend inquiries and orchestrate multi-step tasks efficiently. Agents for Amazon Bedrock also integrates with existing systems through API calls to automate interactions. Knowledge Bases for Amazon Bedrock provide managed RAG to generate accurate responses. Additionally, automating resource provisioning with AWS CloudFormation ensures consistent deployments, reducing configuration errors. Amazon DynamoDB offers low-latency performance for storing claims data, handling high throughput responsively. AWS Lambda runs business logic using a serverless approach, ensuring scalability and reliability without infrastructure management. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Bedrock helps ensure data confidentiality, integrity, and availability through encryption, access controls, and secure data handling practices like anonymization and masking. DynamoDB provides secure claims data management with access controls, encryption, and automated backups. AWS Identity and Access Management (IAM) enables secure authentication and authorization, managing permissions and access to resources. Lambda minimizes the attack surface by running functions in isolated environments with IAM integration. OpenSearch Service offers encryption, access controls, and authentication mechanisms for data protection, while Amazon Simple Notification Service (Amazon SNS) facilitates secure communication for notifications. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

CloudFormation automates provisioning, enabling reliable and consistent infrastructure creation. DynamoDB offers high availability, durability, and automatic failover for data accessibility. OpenSearch Service provides data replication and fault tolerance for availability. Amazon SNS offers scalable and durable messaging for reliable notifications, and Amazon S3 helps ensure high durability and availability for stored data with redundancy and data protection. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Bedrock provides high-performing FMs accessible through an API, enabling efficient generative AI application development and scaling without manual optimization. CloudFormation enables rapid deployment and scaling of infrastructure components, minimizing deployment time. DynamoDB offers a fully managed NoSQL database service with low-latency data access for efficient claims data handling. OpenSearch Service optimizes search and analytics performance with efficient indexing and processing of large data volumes. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

As a managed service, Amazon Bedrock optimizes costs by eliminating infrastructure provisioning needs. DynamoDB offers on-demand capacity and auto-scaling, eliminating over-provisioning. Amazon OpenSearch Serverless scales based on demand without additional infrastructure costs. Amazon S3 provides cost-effective storage with lifecycle policies for transitioning data to lower-cost tiers. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

CloudFormation automates infrastructure management, reducing resource wastage. DynamoDB scales automatically based on demand, minimizing energy consumption. Lambda dynamically allocates resources, eliminating idle servers and reducing energy usage. Additionally, Amazon SNS facilitates sustainable communication by providing efficient and scalable messaging capabilities, reducing resource overhead and energy consumption associated with traditional messaging systems. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
