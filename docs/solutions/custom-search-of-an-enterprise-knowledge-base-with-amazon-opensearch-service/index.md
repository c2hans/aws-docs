---
source_url: https://docs.aws.amazon.com/solutions/custom-search-of-an-enterprise-knowledge-base-with-amazon-opensearch-service/index.html
---

---
title: 'Guidance for Custom Search of an Enterprise Knowledge Base with Amazon OpenSearch Service'
canonical_url: https://docs.aws.amazon.com/solutions/custom-search-of-an-enterprise-knowledge-base-with-amazon-opensearch-service/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Custom Search of an Enterprise Knowledge Base with Amazon OpenSearch Service

## Overview

This Guidance demonstrates how to build an application for search based on the information in an enterprise knowledge base through the deployment of interface nodes, including large language models (LLMs). You can combine services to give answers to questions based on your enterprise knowledge base with a search engine that provides word segmentation search, fuzzy queries, and artificial intelligence (AI) assisted capabilities. This Guidance also includes methods such as manual labeling, unsupervised clustering, supervised classification, and an LLM to extract guide words. Deploying this Guidance can help you automatically split documents into paragraphs with embedded vectors to further establish a structured enterprise knowledge base.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/custom-search-of-an-enterprise-knowledge-base-with-amazon-opensearch-service.pdf?target=_blank)

![Architecture diagram](/images/solutions/custom-search-of-an-enterprise-knowledge-base-with-amazon-opensearch-service/images/custom-search-of-an-enterprise-knowledge-base-with-amazon-opensearch-service-1.png)

1. **Step 1**: The user enters the search query or feedback on the website, which is hosted on AWS Amplify.
1. **Step 2**: The website passes the input query or feedback to Amazon API Gateway and receives the response from API Gateway.
1. **Step 3**: API Gateway passes the input query to the search, question, and answer component. This component has AWS Lambda integrated with Langchain, an opensource framework. The model library is served by Amazon Bedrock or Amazon SageMaker. A search engine component can have Amazon OpenSearch Service or Amazon Kendra. The Lambda function will first get the search results from the search engine (either from OpenSearch Service or Amazon Kendra). The Lambda function then inputs the prompt, which combines the query and search results returned from the search engine. It uses the Retrieval-Augmented Generation (RAG) process to optimize the output of the large language model (LLM) and returns the suggested answer from the LLM to API Gateway.
1. **Step 4**: If the user uses a mobile client, the user can ask a question and get an answer from the artificial intelligence (AI) robot component that has Amazon Connect Customer and Amazon Lex.
1. **Step 5**: Amazon Connect Customer transfers the voice into a text query and sends it to Amazon Lex. Amazon Lex passes the query to the search, question, and answer component to get the suggested answer in the same way as Step 3.
1. **Step 6**: API Gateway passes the feedback to the search optimize component, which has Lambda, Amazon DynamoDB, and Amazon EventBridge. The Lambda function writes the feedback into DynamoDB to help with adjusting the model in the next step.
1. **Step 7**: EventBridge invokes Lambda to train an Extreme Gradient Boosting (XGBoost) model using the feedback stored in DynamoDB. Then the model, described by text through decision trees, is deployed to the search engine.
1. **Step 8**: The Lambda function reads the original file from Amazon Simple Storage Service (Amazon S3) or the customer file system. Then it chunks, embeds, and ingests the data into the search engine. The embedding model is hosted on Amazon Bedrock or a SageMaker endpoint. This serves as the knowledge base for the search engine.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-custom-search-of-an-enterprise-knowledge-base-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

All the services used in this Guidance, such as Lambda and API Gateway, provide Amazon CloudWatch metrics that can be used to monitor individual components of the Guidance. API Gateway and Lambda allow for publishing of new versions through an automated pipeline. CloudWatch is available for Amazon Connect Customer, Amazon Lex, and Amazon Kendra, enabling monitoring, metric collection, and performance analysis for these services. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) is used in this Guidance to control access to resources and data. API Gateway helps with security by providing a protection layer for invoking category services through an outbound API. It acts as a gateway, or a proxy, between the client and the backend services, allowing you to control access and implement security measures. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The services used in this Guidance are Lambda, DynamoDB, Amazon S3, and SageMaker. These services provide high availability within a Region, and allow deployment of highly available SageMaker endpoints. We use these services to implement a reliable application-level architecture by ensuring loosely coupled dependencies, handling throttling and retry limits, and maintaining stateless compute capabilities. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance requires near real-time inference and high concurrency. Lambda, DynamoDB, and API Gateway are designed to meet this criteria. Also, we use SageMaker to host the LLM as an endpoint. Amazon Kendra and OpenSearch are ideal services for the concept of RAG. RAG combines retrieval-based models and language generation to improve generated text. Amazon Kendra and OpenSearch are utilized for efficient knowledge retrieval. This architecture enables the system to leverage retrieved information for more accurate and contextually relevant text generation. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses Lambda to design all compute components of search and question and answer, keeping billing to pay per millisecond. The data store is designed using DynamoDB and Amazon S3, providing a low total cost of ownership for storing and retrieving data. The Guidance also uses API Gateway, which reduces API development time and helps you make sure you only pay when an API is invoked. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses the scaling behaviors of Lambda, a SageMaker inference endpoint, and API Gateway to reduce over-provisioning resources. The serverless services, such as Lambda and API Gateway, are invoked only when there is a user query. It uses AWS Managed Services (AMS) to maximize resource utilization, and to reduce the amount of energy needed to run a given workload. Amplify, Amazon Connect Customer, and Amazon Lex leverage auto-scaling capabilities to continually match the load and allocate resources accordingly. By dynamically adjusting resource levels based on demand, these services ensure that only the minimum necessary resources are utilized, optimizing efficiency and cost-effectiveness. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
