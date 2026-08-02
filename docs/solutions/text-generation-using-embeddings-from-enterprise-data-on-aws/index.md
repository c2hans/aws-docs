---
source_url: https://docs.aws.amazon.com/solutions/text-generation-using-embeddings-from-enterprise-data-on-aws/index.html
---

# Guidance for Text Generation using Embeddings from Enterprise Data on AWS

## Overview

This Guidance demonstrates question answering using Retrieval Augmented Generation (RAG) with foundation models in Amazon SageMaker JumpStart. Generative AI is powered by large language models (LLMs), commonly referred to as foundation models, that are pre-trained on vast amounts of data. This Guidance shows how to solve a question answering task with Amazon SageMaker LLMs and embedding endpoints so you can build models that generate text based on specific, enterprise data rather than generic data. This can help you automate tasks, enhance your applications, and improve information retrieval.

## How it works

This architecture diagram shows a secure, generative AI-based application that generates text from enterprise data.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/text-generation-using-embeddings-from-enterprise-data-on-aws.pdf?target=_blank)

![Architecture diagram](/images/solutions/text-generation-using-embeddings-from-enterprise-data-on-aws/images/text-generation-using-embeddings-from-enterprise-data-on-aws-1.png)

1. **Step 1**: Users access a React app with three pages: one for image prompts, one for text prompts, and one for questions that provide context-based answers from a Text-to-Text model.
1. **Step 2**: The React app, built with AWS Amplify libraries, is hosted and served from an Amplify URL. The Amplify command line interface (CLI) is used to set up and deploy the app's hosting environment.
1. **Step 3**: If a user has not been authenticated, the user will be authenticated against Amazon Cognito using the Amplify React user interface (UI) library.
1. **Step 4**: When a user provides an input and submits the form, Amazon API Gateway processes the request.
1. **Step 5**: Depending on the chosen application (Text-to-Text, Text-to-Image, or LLM RAG Search), API Gateway invokes the appropriate Lambda function. The Lambda function sanitizes user input and invokes the corresponding SageMaker endpoint, formatting prompts as needed for the language models. It also reformats the model output and returns it to the user.
1. **Step 6**: Three distinct endpoints are deployed for Text-to-Text (Flan T5 XXL), Text-to-Embeddings (GPTJ-6B), and Text-to-Image models (Stability AI). Depending on the specific use case, these endpoints produce responses, and Lambda functions format the generated output.
1. **Step 7**: AWS Fargate receives documents, breaks them into smaller sections, uses the Text-to-Embeddings LLM to generate embeddings, and then indexes these embeddings into Amazon OpenSearch Service for context-based searching.
1. **Step 8**: The Text-to-Embeddings model creates document embeddings, which OpenSearch Service indexes. An index with k-Nearest Neighbor (k-NN) capability is activated, enabling efficient searching of these embeddings within OpenSearch Service.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-text-generation-using-embeddings-from-enterprise-data-on-aws/)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The services in this Guidance collectively support operational excellence by automating tasks, improving security, enhancing scalability, and streamlining management and operations of the generative AI application. For example, SageMaker JumpStart simplifies machine learning (ML) model deployment, API Gateway provides secure and scalable API access, Lambda automates processing and response formatting, OpenSearch Service improves data retrieval, and Fargate automates resource provisioning for indexing jobs. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito helps ensure that only authenticated and authorized users can access the application. It manages user identities through multi-factor authentication (MFA) options. Amazon Virtual Private Cloud (Amazon VPC) isolates resources, such as SageMaker endpoints and Lambda functions, within a private network. This isolation protects communication between components of the application, enhancing data privacy and security. Amazon VPC also allows for the implementation of network security measures, such as security groups and network access control lists (NACLs). These services help you safeguard sensitive data and maintain the confidentiality, integrity, and availability of the application. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

SageMaker JumpStart simplifies the deployment and management of ML models, including model versioning and monitoring. This simplification reduces the risk of model deployment errors and helps ensure that models are consistently available and reliable for inference. Additionally, Lambda functions process user input and invoke SageMaker endpoints. Lambda is serverless and automatically handles scaling and availability so that the application can reliably process user requests without the need for manual scaling or managing servers. Fargate initiates indexing jobs for embeddings and automates resource provisioning and container management, so that indexing jobs are completed reliably and at scale. This automation reduces the risk of resource limitations or failures during indexing processes. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

In a generative AI application where tasks may involve complex ML inference, data processing, and retrieval, efficiency is crucial to delivering a responsive and high-performing user experience. By using SageMaker JumpStart, Lambda, OpenSearch Service, and Fargate, this Guidance efficiently manages workloads, enables quick response times, and scales to meet performance demands, ultimately enhancing the user's experience with improved application responsiveness and efficiency. SageMaker JumpStart optimizes model deployment and monitoring so that ML inferences are initiated efficiently, leading to faster response times and better performance for users. Lambda functions automatically scale to handle concurrent requests so the application can maintain performance efficiency, even during periods of high user demand. OpenSearch Service indexes and searches embeddings, enhancing the application's information retrieval capabilities and enabling users to quickly access the information they need. Fargate invokes indexing jobs for embeddings. It automates resource provisioning, allowing the application to efficiently process and index large amounts of data without manual intervention. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

SageMaker JumpStart provides pre-built ML models and workflows, reducing the time and resources required to develop and train models from scratch. This can lead to cost savings by accelerating the development cycle. Lambda follows a pay-as-you-go pricing model, meaning you only pay for the compute time used when your function is invoked. OpenSearch Service allows you to easily scale your cluster based on your search and analytics workloads. You can optimize costs by adjusting the resources to match your actual usage. Fargate automatically manages the underlying infrastructure, which means you don't need to provision or manage servers. This eliminates the need to pay for unused server capacity, resulting in cost savings. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Services such as Lambda, SageMaker, and Fargate contribute to sustainability by optimizing resource usage. They automatically scale resources based on workload demand, reducing unnecessary energy consumption during periods of low activity. For example, as a serverless compute infrastructure, Fargate runs containerized application workloads and minimizes your overall resource footprint. Similarly, SageMaker JumpStart helps in preventing idle overprovisioned resources by automatically adjusting computing resources to match workload needs. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Question answering using Retrieval Augmented Generation with foundation models in Amazon SageMaker JumpStart**: This blog post describes RAG and its advantages, and demonstrates how to quickly get started by using a sample notebook to solve a question answering task using RAG implementation with LLMs in Jumpstart.

[Learn more](https://aws.amazon.com/blogs/machine-learning/question-answering-using-retrieval-augmented-generation-with-foundation-models-in-amazon-sagemaker-jumpstart/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
