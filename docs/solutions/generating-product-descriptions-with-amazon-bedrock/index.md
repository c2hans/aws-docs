---
source_url: https://docs.aws.amazon.com/solutions/generating-product-descriptions-with-amazon-bedrock/index.html
---

---
title: 'Guidance for Generating Product Descriptions with Amazon Bedrock'
canonical_url: https://docs.aws.amazon.com/solutions/generating-product-descriptions-with-amazon-bedrock/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Generating Product Descriptions with Amazon Bedrock

Reach your target audience with artificial intelligence (AI)-generated product descriptions

## Overview

This Guidance demonstrates how generative AI technology can automate your product review and approval process for an e-commerce marketplace or retail website. It uses Amazon Bedrock, a fully managed service that offers a range of high-performing foundation models (FMs) with a broad set of capabilities you need to build generative AI applications. Here, it leverages computer vision and natural language processing to analyze product images, extract relevant attributes, and generate detailed product descriptions. Using the style guidelines of your website or marketplace, this Guidance can also be configured to develop descriptions from supplier-provided specifications and images, driving operational efficiency and improving your shopper's experience.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/generating-product-descriptions-with-amazon-bedrock.pdf)

![Architecture diagram](/images/solutions/generating-product-descriptions-with-amazon-bedrock/images/generating-product-descriptions-with-amazon-bedrock-1.png)

1. **Step 1**: The client sends a request including input data (either a product image or a basic product description to enhance) to the Amazon API Gateway REST API.
1. **Step 2**: API Gateway passes the request to AWS Lambda through a proxy integration.
1. **Step 3**: When operating on product image inputs, Lambda calls Amazon Rekognition, which uses machine learning to detect objects in the image. Descriptions of the objects detected can then be fed into subsequent steps to create a product description.
1. **Step 4**: Lambda calls large language models (LLMs) hosted by Amazon Bedrock, such as the Amazon Titan language models, to produce product descriptions. The LLMs can either enhance existing basic text descriptions or generate new descriptions based on the objects detected by Amazon Rekognition.
1. **Step 5**: Lambda passes the response to API Gateway.
1. **Step 6**: Finally, API Gateway returns the HTTP response to the client.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-generating-product-descriptions-with-amazon-bedrock)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon Bedrock, AWS Cloud Development Kit (AWS CDK), Lambda, API Gateway, andAmazon CloudWatch work in conjunction to help you run your workloads efficiently while gaining insights into your operations effectively. Take for instance AWS CDK, which codifies all cloud resources through an infrastructure-as-code (IaC) approach. Using an IaC approach helps ensure that all changes to the environment are controlled and logged, preventing untested changes from making it into production and ensuring that any operator can readily determine the current state of the production system. Moreover, Amazon Bedrock and Lambda both provide serverless compute, without any requirement to upgrade or patch virtual machine images or operating system versions. In addition, the Lambda integration with CloudWatch logs ensures that application logs are stored and searchable without any additional infrastructure required. Metrics from CloudWatch can be used to set appropriate rate limits for clients during normal operation and to prevent abuse and anomalous operations. Finally, API Gateway provides many capabilities to facilitate hosting a production-grade API, such as granular rate-limiting controls to ensure a consistent quality of service for all users. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

In this Guidance, configuring AWS Identity and Access Management (IAM) and Amazon Cognito can protect your data, systems, and assets in a number of ways that improves your security posture. Specifically, IAM integrates with Lambda, allowing application code running in Lambda to authenticate with other services, like Amazon Rekognition and Amazon Bedrock,without requiring long-lived credentials to be stored anywhere. Furthermore, API Gateway provides a robust outer authentication boundary, without requiring any custom authentication logic. API Gateway also supports multiple authentication mechanisms, including AWS Signature Version 4 or Cognito, allowing you to select the best authentication mechanism for your environment and access patterns. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Serverless offerings, like Amazon Rekognition, Amazon Bedrock, Lambda, and API Gateway are all deployed across multiple Availability Zones by default. They also do not involve any long-running compute resources that require maintenance, meaning there are fewer failure modes for you to worry about. Using an AWS Region-redundant, fully managed services without any single-points-of-failure provides you with a high degree of redundancy, without requiring any extra work to configure auto-scaling or recovery processes. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Bedrock is a fully managed service that offers your choice of foundation models. Amazon Rekognition is also a fully managed service that helps you add pre-trained computer vision APIs to your applications. These artificial intelligence and machine learning (AI/ML) workloads make it easy to get great performance with AI/ML models without investing heavily in specialized hardware. Especially for AI and ML workloads, using fully managed services provides excellent performance for inference without needing to test many hardware configurations and optimize models to take advantage of certain chip architectures. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

When compared to compute infrastructure that must be provisioned in advance, serverless options like Amazon Bedrock, Amazon Rekognition, and Lambda can be invoked completely on-demand, without any dedicated hosts running when not needed. In addition, when the total cost of ownership is considered, managed services like Amazon Bedrock and Amazon Rekognition allow you to spend less development time on undifferentiated infrastructure work. This drives substantial savings in labor throughout the software development lifecycle. Also, using completely serverless options allows the workload to scale up and down completely dynamically, without any charges accruing during periods of disuse, while also being able to scale to handle spikes in traffic. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

In the same way that serverless options help reduce cost by eliminating wasteful overprovisioning of compute resources, they reduce the power consumed and environmental impact of the workload as well. In addition, Amazon is committed to renewable energy, and using managed services running on AWS, like Amazon Bedrock, Amazon Rekognition, and Lambda, makes it easier for you to drive down your carbon footprints. Using fully managed, serverless services—particularly managed by a provider like AWS who is deeply invested in renewable energy—helps minimize wasted compute resources and thus unnecessary carbon emissions as well. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
