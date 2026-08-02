---
source_url: https://docs.aws.amazon.com/solutions/automatic-image-matching-for-articles-using-machine-learning-on-aws/index.html
---

# Guidance for Automatic Image Matching for Articles Using Machine Learning on AWS

## Overview

This Guidance shows how you can use AWS machine learning (ML) services to return semantically similar images to an article. It also uses artificial intelligence (AI) services and pre-trained large language models (LLMs) to summarize the article and extract key points, which become a search input parameter for an Amazon OpenSearch Service index. A search of the index will then return the most relevant images along with key points from the article, such as celebrity names, contributing to quicker discoverability of images from the article.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automatic-image-matching-for-articles-using-machine-learning-on-aws.pdf)

![Architecture diagram](/images/solutions/automatic-image-matching-for-articles-using-machine-learning-on-aws/images/automatic-image-matching-for-articles-using-machine-learning-on-aws-1.png)

1. **Step 1**: Preload Amazon OpenSearch Service with searchable metadata by uploading images to Amazon Simple Storage Service (Amazon S3).
1. **Step 2**: Amazon EventBridge listens for the event and initiates an AWS Step Functions workflow.
1. **Step 3**: Amazon Rekognition extracts Label and Celebrity metadata from the image.
1. **Step 4**: AWS Lambda invokes the Amazon Bedrock Amazon Titan Multimodal Embeddings model to generate an embedding of the image itself.
1. **Step 5**: The next Lambda function stores the image extracted metadata and embedding in OpenSearch Service for easy search.
1. **Step 6**: The content management system resembles the journalist environment. Amazon S3 hosts a simple static website for the semantic image search workload, served by an Amazon CloudFront distribution. Amazon Cognito protects the web application from unauthenticated users.
1. **Step 7**: After the editor has written an article, they select the search button to invoke an Amazon API Gateway API to the backend. The backend will extract names, summarize the article, and generate an embedding which is used as part of the search query against OpenSearch Service.
1. **Step 8**: Lambda invokes Amazon Comprehend with the article text to detect Person entities from the article.
1. **Step 9**: Lambda invokes the Amazon Bedrock Amazon Titan Text G1 - Express model to derive and order the Person names by prominence and summarize the article to meet the max prompt token count of the multimodal embeddings model.
1. **Step 10**: Lambda invokes the Amazon Bedrock Amazon Titan Multimodal Embeddings - G1 model to generate an embedding of the summarized article.
1. **Step 11**: Lambda performs a query against OpenSearch Service using the embedding of the summarized article and the name of the most prominent Person, using exact k-nearest neighbors (k-NN) with scoring script. This returns the top semantically related images with a given celebrity (if present for the given article).
1. **Step 12**: Amazon CloudWatch and AWS X-Ray provide observability into the health of the Guidance.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudWatch and X-Ray provide visibility into the health of the application and allow you to identify where there may be issues through correlation IDs provided by X-Ray. X-Ray integrates with many of the AWS services in this Guidance and can surface where in the chain of events the issue occurred. Additionally, CloudWatch offers monitoring dashboards and sets thresholds against metrics to alert you when there are issues. Many of the services can also write logs to CloudWatch for post-analysis of an issue. CloudWatch automatically monitors the infrastructure and enables build automation into the workflows to notify you of operational issues. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

To access the APIs, Amazon Cognito must provide authentication. Without authenticating, an individual cannot access any of the backend services. Amazon Cognito is scalable to set up and has native integration with API Gateway. API Gateway automatically delivers protection from distributed denial-of-service (DDoS) attacks for the backend services. AWS Identity and Access Management (IAM) allows you to provide granular, least privilege access to resources. IAM restricts access across the Guidance by applying policies to Lambda to confirm it can only invoke certain APIs explicitly provided in the IAM policy. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

CloudFront allows you to reduce the latency of page load times, so editors can access the system from multiple geographies. CloudFront serves images back to the editor and allows the editor to cache images closer to their location, reducing latency of larger files. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

CloudFront uses a global network of 450+ Points of Presence, which provides low latency and faster HTTPS connections. Lambda allows the user to optimize how much memory is required to run the function and can scale out to thousands of requests per second within seconds. Amazon OpenSearch Serverless will automatically upgrade as new versions are released, removing overhead of managing indexes as storage and traffic scales. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

With the services in this Guidance, you do not need to plan for capacity as the cost is per request, and the services will automatically scale out to meet demand. For example, OpenSearch Serverless will scale with your demand, so you don’t need to state how many indexes you require upfront. As these services are serverless, there is no infrastructure to manage, which significantly reduces the total cost of ownership. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon S3 scales as data volumes increase, and you can set up S3 Lifecycle policies to automatically archive or delete data you no longer need. Amazon S3 provisions underlying resources as your storage grows and scales back when you delete objects, reducing overall resource consumption. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
