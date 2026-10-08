---
source_url: https://docs.aws.amazon.com/solutions/sentiment-analysis-on-aws/index.html
---

---
title: 'Guidance for Sentiment Analysis on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/sentiment-analysis-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Sentiment Analysis on AWS

## Overview

This Guidance demonstrates how to use pgvector and Amazon Aurora PostgreSQL for sentiment analysis, a powerful natural language processing (NLP) task. The Guidance shows how to integrate Amazon Aurora PostgreSQL-Compatible Edition with the Amazon Comprehend Sentiment Analysis API, enabling sentiment analysis inferences through SQL commands. By using Amazon Aurora PostgreSQL with the pgvector extension as your vector store, you can accelerate vector similarity search for Retrieval Augmented Generation (RAG), delivering queries up to 20 times faster with pgvector's Hierarchical Navigable Small World (HNSW) indexing. **Important:** This Guidance requires the use of [AWS Cloud9](https://aws.amazon.com/free/) which is no longer available to new customers. Existing customers of AWS Cloud9 can continue using and deploying this Guidance as normal.

## How it works

This architecture diagram shows how to generate sentiment analysis using Amazon Aurora PostgreSQL-Compatible Edition with pgvector enabled as the vector store. It details the process of integrating Amazon Aurora with an Amazon Comprehend Sentiment Analysis API and generating sentiment analysis inferences using SQL commands.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sentiment-analysis-on-aws.pdf)

![Architecture diagram](/images/solutions/sentiment-analysis-on-aws/images/sentiment-analysis-on-aws-1.png)

1. **Step 1**: Download the AWS CloudFormation template from the GitHub repository, and deploy the CloudFormation stack.
1. **Step 2**: The CloudFormation stack deploys an AWS Cloud9 instance, an Amazon SageMaker notebook instance, an Amazon Aurora PostgreSQL cluster, and all the other prerequisites required for this Guidance.
1. **Step 3**: Set up the environment variables to connect to the Aurora PostgreSQL instance and to create pgvector and aws_ml extensions.
1. **Step 4**: Set up the environment to access the Hugging Face Sentence-Transformer model and to generate document embeddings in SageMaker. Store the vector embeddings in Aurora PostgreSQL with pgvector.
1. **Step 5**: Run a similarity search on the vector data with the similarity_search_with_score function from pgvector. Integrate Aurora with an Amazon Comprehend function to retrieve sentiment analysis.
1. **Step 6**: Use PostgreSQL plsql client in AWS Cloud9 IDE to retrieve results with SQL statements.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-sentiment-analysis-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The provided CloudFormation script automates the deployment of key resources, including an Aurora PostgreSQL cluster, a SageMaker notebook instance, an AWS Cloud9 instance, virtual private cloud (VPC), subnets, security groups, and AWS Identity and Access Management (IAM) roles. This automated deployment streamlines operations, reduces manual effort, and mitigates configuration errors, promoting operational excellence. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

An IAM role integrates Aurora with Amazon Comprehend, granting the minimum required permissions. This role is associated with the Aurora cluster and does not have credentials such as passwords or access keys, enhancing security. Database user credentials are securely stored in AWS Secrets Manager, preventing unauthorized access and potential security breaches. IAM roles and policies provide controlled access to Amazon Comprehend's sentiment analysis API from Aurora, limiting permissions to only what's necessary. This principle of least privilege approach to access management strengthens the Guidance’s security posture. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Aurora with pgvector enables storing and searching machine learning (ML)-generated embeddings while leveraging PostgreSQL features like indexing and querying. Aurora provides high availability and reliability by maintaining six copies of data across three Availability Zones, with read replicas and global database replication options. Use Aurora with pgvector as the vector store offers vector capabilities combined with data reliability and durability, eliminating the need to move data across separate vector stores. Aurora's resiliency features and pgvector's capabilities allow you to use an existing relational database as a vector store, seamlessly integrating with artificial intelligence (AI) and ML services like Amazon Comprehend and SageMaker. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Aurora PostgreSQL with pgvector offers optimized storage, compute resources, and vector indexing capabilities within the relational database, helping ensure efficient workload performance. Aurora Optimized Reads can boost vector search performance with pgvector by up to nine times for workloads, exceeding regular instance memory. Aurora with pgvector not only provides vector search, indexing, and sentiment analysis capabilities but also features for optimal query performance, combining the benefits of a relational database with vector capabilities. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

SageMaker offers Savings Plans, reducing costs by up to 64 percent, in addition to flexible on-demand pricing for Studio notebooks, notebook instances, and inference. Using the AWS Cloud9 IDE instead of dedicated Amazon Elastic Compute Cloud (Amazon EC2) instances further decreases costs. Additionally, Amazon Comprehend API's pay-per-use model optimizes expenses. These services provide cost-effective options through on-demand and Savings Plans to help you align with your budget. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Aurora clusters on AWS Graviton instances consume up to 60 percent less energy than comparable EC2 instances while delivering the same performance and better price performance. This Guidance uses temporary resources like AWS Cloud9 and SageMaker notebooks to reduce carbon footprint. AWS Cloud9, a temporary IDE, integrates Aurora with Amazon Comprehend and generates inferences through SQL statements, further minimizing the environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Leverage pgvector and Amazon Aurora PostgreSQL for Natural Language Processing, Chatbots and Sentiment Analysis**: This blog post demonstrates how to build an interactive chatbot app for question answering using LangChain and Streamlit and leveraged pgvector and its native integration with Aurora Machine Learning for sentiment analysis.

[Read the blog](https://aws.amazon.com/blogs/database/leverage-pgvector-and-amazon-aurora-postgresql-for-natural-language-processing-chatbots-and-sentiment-analysis/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
