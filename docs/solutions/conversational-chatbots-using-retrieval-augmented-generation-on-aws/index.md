---
source_url: https://docs.aws.amazon.com/solutions/conversational-chatbots-using-retrieval-augmented-generation-on-aws/index.html
---

---
title: 'Guidance for Conversational Chatbots Using Retrieval Augmented Generation on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/conversational-chatbots-using-retrieval-augmented-generation-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Conversational Chatbots Using Retrieval Augmented Generation on AWS

## Overview

This Guidance demonstrates how to combine Retrieval Augmented Generation (RAG) with AWS services to build generative AI applications. Large language models (LLMs), a type of generative AI, are typically trained offline, making the models become less relevant as more data is created after the model was trained. With this Guidance, you can use RAG to retrieve data from multiple data sources, including data from outside the LLM. The data can be added to the LLM model to generate more accurate, human-like responses across text and voice interfaces.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/conversational-chatbots-using-retrieval-augmented-generation-on-aws.pdf)

![Architecture diagram](/images/solutions/conversational-chatbots-using-retrieval-augmented-generation-on-aws/images/conversational-chatbots-using-retrieval-augmented-generation-on-aws-1.png)

1. **Step 1**: The user initiates a request. The request ingests content from the web, serving as a data source in Amazon Kendra, and an index ID is created in Amazon Kendra.
1. **Step 2**: The user interacts with the Amazon Lex conversational chatbot using the Amazon Lex chat window or, optionally, through the Amazon Lex web user interface (UI), an open-source project, to submit a query or request. Amazon Lex is responsible for understanding and interpreting users' intent and extracting relevant information from the input.
1. **Step 3**: Amazon Lex invokes the AWS Lambda function. This Lambda function handles user interactions. Lambda receives the request from the user either through the Amazon Lex UI, distributed by Amazon CloudFront, or an Amazon Lex chat window, and returns the responses.
1. **Step 4**: Using Amazon Kendra, relevant passages are identified and extracted when there is a user request sent through the Lambda function. Amazon Kendra identifies and extracts the relevant passages when a request is submitted.
1. **Step 5**: The conversation is also stored in Amazon DynamoDB to serve subsequent user requests, and is used for conversational memory.
1. **Step 6**: A query, along with context from Amazon Kendra, is forwarded to the large language model (LLM) by the Lambda function with the help of a LangChain orchestrator, an open-source framework for developing applications powered by language models. The LLM processes this query and produces a response.
1. **Step 7**: The generated response from the LLM is returned to the Lambda function.
1. **Step 8**: The Lambda function formats and delivers the response back to the user through the Amazon Lex chat UI distributed by CloudFront, or through the Amazon Lex chat window in the console.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-custom-search-using-large-language-models-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon Kendra, Amazon Lex, Lambda, DynamoDB, and Amazon SageMaker are used throughout this Guidance to enhance your operational excellence. Amazon Kendra enhances the efficiency and precision of accessing enterprise content, delivering accurate results swiftly. Paired with Amazon Lex, it offers a fluid conversational interface, making user inquiries and intent processing more streamlined. Lambda offers agile and scalable user interaction management, and the integration of the LangChain orchestrator within Lambda promotes efficient coordination among services, simplifying operations. Also, the capability of DynamoDB to store conversations reliably means no repeated interactions. Finally, the LLM of SageMaker contributes to context-relevant replies, bolstering consistent operations and an improved user experience. These services have been integrated to ensure your operations remain streamlined, efficient, and capable of consistently delivering desired outcomes. From the precise content retrieval using Amazon Kendra, to the structured orchestration managed by LangChain, every component aims to reduce operational overhead, minimize errors, and promote a system that's continuously improving in efficiency and responsiveness. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Kendra, Amazon Lex, Lambda, CloudFront, DynamoDB, and SageMaker offer a comprehensive and integrated approach to secure user interactions and data management. Their inherent security mechanisms, from the controlled access in Lambda to the encrypted storage in DynamoDB and the secure data indexing in Amazon Kendra, support a secure, responsive, and efficient user experience. For example, Amazon Kendra safely collects and organizes content from the internet, guaranteeing the accuracy of the data. Additionally, users have the option to use the Amazon Lex web UI, a protected environment, to communicate with the chatbot. When invoked by Amazon Lex, Lambda serves as a safeguarded bridge for user requests, processing queries from the Amazon Lex UI, delivered by CloudFront, and sending back answers. Lambda also establishes a secure link with Amazon Kendra to extract pertinent details and collaborates with the LLM in SageMaker to generate responses. Moreover, all conversations are securely preserved in DynamoDB, ensuring lasting data protection. Finally, within Lambda, the LangChain orchestrator ensures a safe coordination among Amazon Lex, Amazon Kendra, and the LLM of SageMaker. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS CloudFormation, Amazon Kendra, Amazon Lex, Lambda, CloudFront, DynamoDB, and SageMaker work collectively to enhance the reliability of your workloads. Specifically, using CloudFormation can help you set up the system using best practices, ensuring reliable resource management, while Amazon Kendra offers stable data retrieval through dependable indexing. With Amazon Lex, you get accurately interpreted user intent, coupled with Lambda that helps to ensure scalable and continuous responses. Also, DynamoDB securely stores conversations and the LLM of SageMaker ensures uninterrupted responses to user queries. These services have been selected to ensure a system that is resilient, scalable, and can recover from failures efficiently. From infrastructure as code practices with CloudFormation that allow for quick recovery, to the seamless orchestration between services ensuring consistent performance, each component has been integrated to uphold the highest standards of reliability set by AWS. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services selected for this Guidance help improve your performance in a number of ways. First, Amazon Kendra improves the RAG process to get relevant content. Next, Amazon Lex provides an easy way for users to ask questions and understand their intent. Also, Lambda offers quick responses, while DynamoDB stores and fetches conversations efficiently, reducing delays. Finally, using the right LLM in SageMaker, users get quicker answers, leading to a better experience. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon Kendra, SageMaker, Amazon Lex, CloudFront, and DynamoDB offer a number of cost-saving features. One, Amazon Kendra and SageMaker adjust resources based on actual need, ensuring you only pay for what you use. Also, the pricing for SageMaker is flexible and automatically scales. Two, Amazon Lex lets you create chat interfaces without the hassle of managing an infrastructure. Three, DynamoDB offers flexible payment options for better cost management. These services were selected because they offer efficient mechanisms for resource management and billing. Their dynamic scaling, pay-as-you-go models, and other tailored features, like caching in CloudFront and flexible payment options in DynamoDB, align seamlessly with the goal of cost optimization. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Each service deployed in this Guidance was selected due to its serverless and managed nature, eliminating the need for physical hardware. By using serverless services like Lambda and Amazon Lex, you can automatically adjust to demand without using physical servers, reducing energy use. Services like Amazon Kendra and SageMaker operate efficiently without manual setup or maintenance. DynamoDB saves conversations and prevents repeat computations, saving resources. Altogether, this approach is eco-friendly to help you align with your current sustainability objectives. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
