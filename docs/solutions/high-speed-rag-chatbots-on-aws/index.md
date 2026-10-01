---
source_url: https://docs.aws.amazon.com/solutions/high-speed-rag-chatbots-on-aws/index.html
---

---
title: 'Guidance for High-Speed RAG Chatbots on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/high-speed-rag-chatbots-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for High-Speed RAG Chatbots on AWS

## Overview

**Important:** This Guidance requires the use of [AWS Cloud9](https://aws.amazon.com/free/) which is no longer available to new customers. Existing customers of AWS Cloud9 can continue using and deploying this Guidance as normal. This Guidance demonstrates how to build a high-performance Retrieval-Augmented Generation (RAG) chatbot using Amazon Aurora PostgreSQL and the pgvector open-source extension, using AWS artificial intelligence (AI) services and open-source frameworks. Pgvector is configured as a vector database, allowing efficient vector search with the Hierarchical Navigable Small World (HNSW) indexing algorithm. The chatbot allows users to upload PDF files, ask questions in natural language, and receive answers based on the file content. With the scalability, availability, and cost-effectiveness of Aurora, you can operate your natural language processing chatbot globally.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/high-speed-rag-chatbots-on-aws.pdf)

![Architecture diagram](/images/solutions/high-speed-rag-chatbots-on-aws/images/high-speed-rag-chatbots-on-aws-1.png)

1. **Step 1**: Download the AWS CloudFormation template from the GitHub repository and deploy the CloudFormation stack.
1. **Step 2**: The CloudFormation stack deploys an AWS Cloud9 instance, an Amazon Aurora PostgreSQL cluster, a Streamlit custom chatbot application, and other pre-requisites required for this Guidance.
1. **Step 3**: Set up the environment variables to connect to the Aurora PostgreSQL instance, create the pgvector extension, and start the Streamlit application.
1. **Step 4**: Once the Streamlit application starts, upload the PDF document for processing. This will segment the document into chunks and convert them into vectors using an Amazon Titan model from Amazon Bedrock. Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs).
1. **Step 5**: Load the vector embeddings into an Aurora PostgreSQL cluster.
1. **Step 6**: The user asks a question in natural language in the chatbot application.
1. **Step 7**: The question from the Streamlit application is converted into embeddings using the Amazon Titan model. The vectors are then compared with the Aurora PostgreSQL vector store to identify the most semantically similar vectors.
1. **Step 8**: Pass the user question and the context from the vector database to the large language model (LLM). In this example, the Claude 3 model from Anthropic on Amazon Bedrock is used.
1. **Step 9**: The LLM generates a response based on the relevant content and displays the response in the chatbot application.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-high-speed-rag-chatbots-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon Bedrock provides easy access to multiple FMs. In this Guidance, we use an Amazon Titan embeddings model through Amazon Bedrock to generate vector embeddings for the text chunks. For the conversational chatbot, we use the Anthropic Claude 3 LLM. Also, a CloudFormation script is provided to create all the necessary prerequisites for this Guidance to be deployed with a single click. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Secrets Manager securely stores the database user credentials, preventing unauthorized access and password tampering issues. Secrets Manager also offers additional security features like automatic secret rotation and easy secret replication across AWS Regions, as well as auditing and monitoring of secret usage. Additionally, the Aurora storage cluster is encrypted using an AWS Key Management Service (AWS KMS) key. Together, these services reduce the risk of security breaches. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Aurora, with the pgvector extension, provides vector storage and search capabilities, along with the resilient features of a relational database. The Aurora cluster stores six copies of data across three Availability Zones (AZs), providing high availability for the data. Aurora will automatically failover to a replica in another AZ, if an Availability Zone (AZ) or instance encounters a failure. Aurora also continuously backups the data to Amazon Simple Storage Service (Amazon S3). [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Titan Text Embeddings v2 is optimized for high accuracy and well suited for semantic search use. When reducing from 1,024 to 512 dimensions, Titan Text Embeddings V2 retains approximately 99% retrieval accuracy. Vectors with 256 dimensions maintain 97 percent accuracy. This means that you can save 75 percent in vector storage (from 1024 down to 256 dimensions) and keep approximately 97 percent of the accuracy provided by larger vectors. With the Amazon Titan text embeddings model available on Amazon Bedrock, it's easy to use and switch models based on the use case. Finally, the Amazon Titan text model helps to ensure the RAG process retires the most relevant information for the LLM, leading to more accurate answers. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon Bedrock provides a choice of two pricing plans: on-demand and provisioned throughput. The on-demand model allows you to use FMs on a pay-as-you-go basis, which is cost-efficient and gives you the agility to experiment with different models based on your needs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

In this Guidance, we use temporary resources, like an AWS Cloud9 instance for the integrated development environment (IDE), instead of dedicated Amazon Elastic Compute Cloud (Amazon EC2) instances to reduce cost. Also, we are using AWS Graviton Processor instance types for the Aurora database cluster, which uses 60 percent less energy than comparable Amazon EC2 instances with the same performance. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Leverage pgvector and Amazon Aurora PostgreSQL for Natural Language Processing, Chatbots and Sentiment Analysis**: This blog post demonstrates how to build an interactive chatbot app for question answering using LangChain and Streamlit and leveraged pgvector and its native integration with Aurora Machine Learning for sentiment analysis.

[Go to blog](https://aws.amazon.com/blogs/database/leverage-pgvector-and-amazon-aurora-postgresql-for-natural-language-processing-chatbots-and-sentiment-analysis/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
