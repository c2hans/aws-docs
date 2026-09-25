---
source_url: https://docs.aws.amazon.com/solutions/building-custom-chatbots-for-order-recommendations-using-agents-for-amazon-bedrock/index.html
---

---
title: 'Guidance for Building Custom Chatbots for Order Recommendations Using Agents for Amazon Bedrock'
canonical_url: https://docs.aws.amazon.com/solutions/building-custom-chatbots-for-order-recommendations-using-agents-for-amazon-bedrock/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Building Custom Chatbots for Order Recommendations Using Agents for Amazon Bedrock

Build chatbots tailored to your customer

## Overview

This Guidance shows how to build an AI-generated chatbot using the Amazon Bedrock suite of services. The chatbot employs a Retrieval-Augmented Generation (RAG) process, which optimizes the output of a large language model by referencing an authoritative knowledge base, thereby providing more contextual and informed responses. And by integrating with the user's existing internal systems and data sources, the chatbot enables the generation of context-specific responses, such as recommendations based on order history, order placement, order status, and order tracking information. After configuring this Guidance, users can quickly build a highly personalized and efficient conversational AI application that integrates with their business operations.

## How it works

This architecture diagram shows how to build a serverless, scalable generative AI chatbot using both Agents for Amazon Bedrock and Knowledge Bases for Amazon Bedrock. The chatbot can integrate with internal systems to provide personalized recommendations, order placement, and order status.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-custom-chatbots-for-order-recommendations-using-agents-for-amazon-bedrock.pdf?target=_blank)

![Architecture diagram](/images/solutions/building-custom-chatbots-for-order-recommendations-using-agents-for-amazon-bedrock/images/building-custom-chatbots-for-order-recommendations-using-agents-for-amazon-bedrock-1.png)

1. **Step 1**: Users access the webpage, which is served by Amazon CloudFront and backed by Amazon Simple Storage Service (Amazon S3) for website and configuration file storage. Customers can request recommendations or place orders directly from the webpage.
1. **Step 2**: The user authenticates with Amazon Cognito.
1. **Step 3**: AWS Lambda uses Amazon API Gateway to handle user requests for recommendations and order placement.
1. **Step 4**: Lambda uses the InvokeAgent API to initiate calls to Agents for Amazon Bedrock. Agents automate prompt engineering, invoke large language models (LLMs), and orchestrate the user-requested task by dynamically invoking APIs. Amazon Bedrock offers access to foundation models to build generative AI applications.
1. **Step 5**: Agents for Amazon Bedrock query the Knowledge Bases for Amazon Bedrock Retrieve APIs to retrieve relevant text, such as the product catalog from Amazon OpenSearch Service, and augment prompts during inference. The Knowledge Bases for Amazon Bedrock are set up with Amazon S3 and OpenSearch Service to automate the end-to-end Retrieval Augmented Generation (RAG) workflow.
1. **Step 6**: Agents for Amazon Bedrock invoke the Lambda function from their action group, along with function detail parameters or Open API schema configuration, to execute actions such as placing orders, searching for nearest locations, and retrieving customer order history.
1. **Step 7**: Lambda integrates with the user's internal systems and Amazon DynamoDB to provide the Agents with the appropriate data.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Lambda, API Gateway, and Amazon Cognito are serverless services that help users achieve operational excellence by reducing the operational overhead of managing infrastructure. With Lambda, users can run code without provisioning or managing servers, enabling them to focus on their application logic rather than infrastructure management. API Gateway provides a fully managed service for creating, publishing, and securing APIs, eliminating the need to manage API infrastructure. Amazon Cognito simplifies user authentication and authorization, allowing users to offload the complexities of identity management to a managed service. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

CloudFront increases the security of the web application with data encryption, geographic restriction, and integration with AWS WAF to protect against common exploits and AWS Shield Standard for distributed denial of service (DDoS) attacks. AWS Identity and Access Management (IAM) supplies the least privileges to users and services and integrates into Amazon Cognito to manage roles and policies. Furthermore, API Gateway is able to throttle requests and integrates with Amazon Cognito to provide authorization to the endpoint. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

API Gateway and Lambda provide reliability to an application by decoupling the backend logic from the frontend, allowing for a scalable and fault-tolerant infrastructure. Specifically, API Gateway handles incoming requests and routes them to the appropriate Lambda functions, which can automatically scale up or down based on demand for high availability and resiliency of the application. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda automatically scales compute resources to handle fluctuating workloads. It supports efficient resource utilization and provides improved computational performance through the use of AWS Graviton Processors in comparison to the more traditional Intel 8086 microprocessor and its successors. In addition, Amazon Bedrock offers pre-optimized large language models and GPU-backed inference capabilities to accelerate AI-powered applications. Lastly, Amazon OpenSearch Serverless automatically scales compute and storage resources to meet the demands of search and analytics workloads. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

CloudFront optimizes costs by caching content at edge locations, thereby reducing the need to serve data directly from the origin server. API Gateway offers a pay-as-you-go pricing model and caching capabilities to minimize backend service calls. Lambda also provides cost optimization by enabling users to execute code without the need for provisioning or managing servers, charging only for the consumed compute time. Lastly, Amazon S3 offers flexible storage classes, allowing users to align storage costs with their specific data access patterns. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

API Gateway, Lambda, OpenSearch Serverless, Amazon S3, and Amazon Bedrock all contribute to sustainability through their serverless and cloud-native architectures. These services minimize the need for physical hardware and infrastructure, reducing the overall energy and resource consumption required to run applications. By abstracting away the underlying infrastructure, these services enable developers to focus on building and deploying their applications without the burden of managing servers, networks, and other low-level resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Bedrock Agents Chatbot - Recommend & Order**: This workshop demonstrates how a fullstack Chatbot app is able to help a customer find a new drink based on preferences such as calories, allergens, flavors, or seasonal trends.

[Visit the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/f5a3879d-086a-4873-b16f-bd4caf5c1623/en-US?target=_blank)

[Read usage guidelines](/solutions/guidance-disclaimers/)
