---
source_url: https://docs.aws.amazon.com/solutions/chatbots-with-vector-databases-on-aws/index.html
---

# Guidance for Chatbots with Vector Databases on AWS

## Overview

This Guidance provides a step-by-step guide for creating a retrieval-augmented generation (RAG) application, such as a question-answering bot. By using a combination of AWS services, open-source foundation models, and packages such as LangChain and Streamlit, you can create an enterprise-ready application. The RAG-based approach uses a similarity search to provide context to users' inquiries, thereby enhancing the precision and sufficiency of the responses provided.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/chatbots-with-vector-databases-on-aws.pdf)

![Architecture diagram](/images/solutions/chatbots-with-vector-databases-on-aws/images/chatbots-with-vector-databases-on-aws-1.png)

1. **Prerequisite**: Amazon SageMaker Processing jobs are used for large scale data ingestion into Amazon OpenSearch Service. In this offline data ingestion step, download the dataset locally into the SageMaker notebook, then ingest it into the OpenSearch Service index. Split the documents into segments, which can then be converted into embeddings to be ingested into OpenSearch Service.
1. **Step 1**: The user provides a question using a Streamlit web application.
1. **Step 2**: The web application invokes the Amazon API Gateway endpoint's representational state transfer API.
1. **Step 3**: API Gateway invokes an AWS Lambda function.
1. **Step 4**: The function invokes the SageMaker endpoint to convert the user's question into embeddings.
1. **Step 5**: The function invokes an OpenSearch Service API to find documents similar to the user's question.
1. **Step 6**: The function creates a prompt, with the user's query and the similar documents as context. It then asks the SageMaker endpoint to generate a response.
1. **Step 7**: The Lambda function provides the response to API Gateway.
1. **Step 8**: API Gateway provides the response to the Streamlit application.
1. **Step 9**: The user can view the response on the Streamlit application.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance enhances operational excellence by automating tasks and providing capabilities that reduce manual efforts, enhance system reliability, and bolster security. AWS services like SageMaker, API Gateway, Lambda, and OpenSearch Service are fully managed, removing the need for your development team to handle server provisioning, patching, and routine maintenance. Additionally, they automate aspects like model deployment, code implementation, scaling, and failover, reducing the likelihood of human errors and accelerating response times during operational events. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance prioritizes security, protecting user data and interactions and building trust among users. Services like SageMaker, API Gateway, and OpenSearch Service scramble data, making it unreadable to unauthorized users. API Gateway, Lambda, and AWS Identity and Access Management (IAM) give you precise control over who can access the system and what they can do, and API Gateway and OpenSearch Service provide authentication to prevent unauthorized entry and avoid potential security issues. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses services with high reliability so that your system stays available and trustworthy for users. AWS services like SageMaker, Lambda, and OpenSearch Service are highly available, scale automatically to handle more users without slowing down, and use built-in backup plans to protect your data from loss or damage. Additionally, services like API Gateway and Lambda handle errors smoothly so that your users won’t notice interruptions. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses services that automate tasks, like setting up models, handling requests, and adjusting to changes. This makes your system faster and more efficient without requiring lots of manual work. SageMaker automates machine learning (ML) model deployment, improving overall application responsiveness. API Gateway efficiently manages incoming requests, minimizing response times. Lambda functions automatically scale to handle varying workloads, and OpenSearch Service provides fast and accurate document retrieval, making the process of finding similar documents quick and responsive. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance supports cost optimization by minimizing idle resource usage, adopting efficient pricing models, reducing maintenance overhead, and optimizing data handling, ultimately leading to lower operational costs. For example, SageMaker, API Gateway, and Lambda automatically scale and allocate resources based on demand. Managed services like SageMaker and OpenSearch Service also reduce the operational burden on your development team, lowering the costs of infrastructure management and maintenance. Additionally, Lambda provides a pay-as-you-go pricing model so that you’re only charged when functions are actively processing requests, and API Gateway efficiently handles requests and responses, reducing the amount of data sent over the network. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses services that support sustainability through automatic scalability. Serverless services such as Lambda and API Gateway use compute resources only when invoked, and OpenSearch Service and SageMaker automatically scale to match your workload’s demands. By promoting efficient resource usage, this Guidance helps you avoid unnecessary energy consumption and reduce your carbon footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Large Language Model (LLM) and Retrieval Augmented Generation (RAG)**: This sample code demonstrates a RAG based LLM powered question answer bot.

[Go to sample code](https://github.com/aws-samples/llm-apps-workshop/tree/main/blogs/rag)

[Read usage guidelines](/solutions/guidance-disclaimers/)
