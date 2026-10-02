---
source_url: https://docs.aws.amazon.com/solutions/similarity-search-based-retrieval-augmented-generation-rag-on-aws/index.html
---

---
title: 'Guidance for Similarity Search-Based Retrieval Augmented Generation (RAG) on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/similarity-search-based-retrieval-augmented-generation-rag-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Similarity Search-Based Retrieval Augmented Generation (RAG) on AWS

## Overview

This Guidance shows how to build an advanced question-answering application using the latest AI tools from AWS and its partners. The architecture includes a database service that stores both operational data and vector data embeddings. A fully managed generative AI service creates these embeddings, which are then stored and managed alongside your most relevant documents based on their proximity to the query vector. This technique, known as Retrieval-Augmented Generation (RAG), enhances AI response accuracy and relevance. As a result, you can provide better, faster answers to your customers' questions using your own data. **Note:** See disclaimer below

## How it works

This architecture diagram illustrates how to process user queries and generate accurate, contextually relevant responses. It enhances a foundation model (FM) on Amazon Bedrock using Retrieval Augmented Generation (RAG); the vector search capabilities of Amazon DocumentDB and LlamaIndex enable more accurate and informed answers from a customized knowledge base.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/similarity-search-based-retrieval-augmented-generation-rag-on-aws.pdf?target=_blank)

![Architecture diagram](/images/solutions/similarity-search-based-retrieval-augmented-generation-rag-on-aws/images/similarity-search-based-retrieval-augmented-generation-rag-on-aws-1.png)

1. **Step 1**: The user uploads enterprise or external data, which lies outside of the large language model's (LLM) training data, to augment the trained model. It can come from various sources including APIs, databases, or document repositories.
1. **Step 2**: The application hosted on Amazon Elastic Compute Cloud (Amazon EC2) preprocesses data by removing inconsistencies and errors, splitting large documents into manageable sections, and chunking the text into smaller, coherent pieces for easier processing.
1. **Step 3**: The application generates text embeddings for relevant data using the Titan text embedding models on Amazon Bedrock.
1. **Step 4**: The application fetches credentials from AWS Secrets Manager to connect to Amazon DocumentDB (with MongoDB compatibility).
1. **Step 5**: The application creates a vector search index in Amazon DocumentDB and uses LlamaIndex to load the generated text embeddings along with other relevant information into an Amazon DocumentDB collection.
1. **Step 6**: The user submits a natural language query for finding relevant answers to a web application.
1. **Step 7**: The application fetches credentials from Secrets Manager to connect to Amazon DocumentDB.
1. **Step 8**: The user's question is transformed into a vector embedding in the application using the same embedding model that was used during the data ingestion workflow.
1. **Step 9**: The application passes the query to the LlamaIndex query engine. LlamaIndex is a data orchestration tool that helps with data indexing and querying. LlamaIndex performs a similarity search in the Amazon DocumentDB collection using the query embedding. The search retrieves the most relevant documents based on their proximity to the query vector.
1. **Step 10**: The LlamaIndex query engine augments this retrieved information, along with the user's question, as a prompt to the LLM model on Amazon Bedrock to generate more accurate and informed responses.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-similarity-search-based-retrieval-augmented-generation-on-aws?target=_blank)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as amany Well-Architected best practices as possible.

### Operational Excellence

Amazon Bedrock and Amazon DocumentDB integrate with Amazon CloudWatch and AWS CloudTrail, offering a comprehensive monitoring, logging, and visibility approach. This integration allows you to track API activity, monitor model usage metrics and token consumption, and access other performance-related data in Amazon Bedrock. You gain visibility to over 40 key operational metrics for the Amazon DocumentDB cluster, including compute, memory, storage, query throughput, MongoDB opcounters, and active connections. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon DocumentDB prioritizes security through comprehensive encryption and access control measures. It encrypts data at rest using AWS Key Management Service (AWS KMS) keys and secures data in transit with TLS. As a virtual private cloud (VPC)-only service, Amazon DocumentDB uses Amazon Virtual Private Cloud (Amazon VPC) for network isolation and access control. Role-based access control (RBAC) enables least privilege access, while AWS Identity and Access Management (IAM) policies provide granular control over user actions and resource access. For enhanced protection of sensitive information, you can implement Client-Side Field Level Encryption (CS-FLE), which uses AWS KMS to selectively encrypt data such as personally identifiable information (PII). Additionally, Amazon DocumentDB stores log data in CloudWatch, facilitating comprehensive auditing capabilities. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon DocumentDB offers strategic deployment and robust backup capabilities. By deploying clusters across three Availability Zones (AZs), Amazon DocumentDB ensures continuous operations even in the face of potential failures. The Multi-AZ cluster design offers high availability, with automated failovers to existing replicas completing in under 30 seconds without manual intervention. The built-in backup functionality of Amazon DocumentDB, enabled by default, supports point-in-time recovery for clusters, allowing restoration to any second within the specified retention period. This capability significantly reduces the risk of data loss and minimizes downtime. Additionally, the serverless architecture of Amazon Bedrock eliminates infrastructure management concerns, further contributing to the overall reliability of this Guidance by reducing potential points of failure and simplifying operations. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses the vector search capabilities of Amazon DocumentDB, providing mechanisms for fine-tuning the query parameters. The initial configuration uses the optimized settings for vector search queries, but you can further tune the probes or efSearch parameters based on the workload traffic and query performance requirements. Increasing the probes or efSearch value improves recall but reduces speed, so you can experiment with the recommended starting point setting of sqrt(# of lists) for the probes parameter. To help ensure the cluster can handle workload spikes and meet performance service level agreements (SLAs), this Guidance relies on Amazon CloudWatch Logs and Amazon DocumentDB Performance Insights to monitor and scale the cluster, both horizontally and vertically as needed. Similarly, Amazon Bedrock integrates with CloudWatch, providing comprehensive monitoring, logging, and visibility into API activity, model usage metrics, token consumption, and other performance-related data. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon DocumentDB offers a flexible and scalable architecture, automatically scaling storage and I/O based on workload demands so you only pay for resources you actually use. Amazon DocumentDB provides both Standard and I/O-Optimized storage configurations, allowing you to choose the most cost-effective option for your specific workload requirements. To further optimize costs, you can use CloudWatch to monitor resource consumption and inform scaling decisions or storage configuration choices. Together, these options allow you to balance cost and performance based on your specific needs and usage patterns, avoiding long-term commitments when unnecessary and achieving cost savings for more stable workloads. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This combination of flexible scaling and energy-efficient hardware significantly enhances the sustainability profile of this architecture. For example, the horizontal scaling capabilities of Amazon DocumentDB allow for precise adjustment of resources, scaling in and out as needed. This approach optimizes resource usage, minimizes waste, and reduces unnecessary energy consumption. Furthermore, Amazon DocumentDB offers AWS Graviton instances, which reduce energy consumption while delivering improved performance. Amazon Bedrock complements these efforts with its serverless architecture, eliminating the need for you to manage infrastructure and thereby reducing potential resource waste. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
