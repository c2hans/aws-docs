---
source_url: https://docs.aws.amazon.com/solutions/aerospace-technicians-assistant-on-aws/index.html
---

---
title: 'Guidance for Aerospace Technician’s Assistant on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/aerospace-technicians-assistant-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Aerospace Technician’s Assistant on AWS

## Overview

This Guidance demonstrates how aerospace technicians can use a generative artificial intelligence (generative AI)-powered 'assistant' to answer natural language technical questions using custom document libraries for authoritative answers. With airplane assembly and repair manuals often comprising thousands of pages, it is time-consuming for technicians to search these physical documents manually. Using optical character recognition (OCR), scanned documents can be converted into searchable text and then integrated with the AI assistant to enable natural language queries. Technicians can quickly search by keywords or receive answers to spoken questions, enhancing efficiency while maintaining quality and safety in assembly and troubleshooting processes.

## How it works

### Amazon Q

This architecture diagram shows how to use Amazon Q to enable natural language searching of paper documents.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/aerospace-technicians-assistant-on-aws.pdf#page=1?target=_blank)Step 1Create an Amazon Q Business application and an associated retriever. Amazon Q provides retrievers both for Amazon Kendra indexes and for native indexes. You can select an Amazon Q retriever to use with an Amazon Q native index, or you can use an already-configured Amazon Kendra index as a retriever. The retriever pulls data from the index in real-time during a conversation.Step 2Connect your data sources to your retriever. Available data sources will vary based on your choice of retriever. You can use Amazon Simple Storage Service (Amazon S3), Amazon Relational Database Service (Amazon RDS), or other data sources, and you can choose from supported data connectors.Step 3Use AWS Identity and Access Management (IAM) Identity Center as a gateway for managing user access. For applications that use legacy identity management, Amazon Q Business requires that you integrate your web experience with an identity provider (IdP) that's compliant with SAML 2.0. Amazon Q Business can work with any IdP that's compliant with SAML 2.0. Amazon Q uses service-initiated single sign-on to authenticate users.### Amazon Bedrock

This architecture diagram shows how to use Amazon Bedrock to enable natural language searching of paper documents.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/aerospace-technicians-assistant-on-aws.pdf#page=2)Step 1Upload data to Amazon S3.Step 2Use Knowledge Bases for Amazon Bedrock to index your data by generating embeddings and storing them in a supported vector store, such as Amazon OpenSearch Service.Step 3Query the large language model (LLM) and return augmented responses to your applications. Provide access to Amazon Bedrock APIs using AWS Lambda and Amazon API Gateway for external and AWS endpoints. Amazon Bedrock is a service that offers access to foundation models to build generative AI applications.Step 4Use Amazon Bedrock agents to orchestrate and analyze tasks to break them down into the correct logical sequence using the foundation model's reasoning abilities. Amazon Bedrock agents automatically call the necessary APIs to transact with your systems to fulfill the request, determining along the way if they can proceed or if they need to gather more information.Step 5As part of your responsible artificial intelligence (AI) strategy, you can now use Guardrails for Amazon Bedrock to promote safe interactions between users and your applications generated with AI. You can do this by implementing safeguards customized to your use cases and responsible AI policies.### Amazon SageMaker

This architecture diagram shows how to use Amazon SageMaker to enable natural language searching of paper documents.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/aerospace-technicians-assistant-on-aws.pdf#page=3)Step 1Upload data to Amazon S3.Step 2Convert your files to text using Amazon Textract for PDF or image files. Use Amazon Transcribe for multimedia files. Store the converted text in Amazon S3.Step 3If needed, use Amazon Translate to translate your text into a language compatible with your chosen LLMs. Store translated text in Amazon S3.Step 4Store document processing status information and other relevant metadata in Amazon DynamoDB.Step 5Create embeddings from your processed or translated text data using an embedding model on an Amazon SageMaker endpoint. Store the embeddings in an OpenSearch Service index.Step 6Host an LLM on a SageMaker endpoint (the query endpoint) to process user queries.Step 7Use Lambda to make queries to your SageMaker endpoints, your OpenSearch Service index, DynamoDB, and other AWS services.Step 8Use API Gateway to provide access control, authorization, and API access to your Lambda functions.Step 9Use DynamoDB to store chat information to enable a stateful chat interface.Step 10Integrate your Retrieval-Augmented Generation (RAG) framework with other AWS services using AWS service endpoints.### VPC Networking

This architecture diagram shows how to enable VPC networking for services used in generative AI solutions.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/aerospace-technicians-assistant-on-aws.pdf#page=4)Step 1Connect Amazon S3 and DynamoDB to your Amazon Virtual Private Cloud (Amazon VPC) environment using gateway endpoints.Step 2Connect Amazon Textract, Amazon Translate, Amazon Transcribe, and API Gateway to your VPC using VPC endpoints.Step 3Use service-managed elastic network interfaces to connect to SageMaker inference endpoints, Lambda functions, and OpenSearch Service domains.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Try out this Guidance

[Explore an interactive demo](https://demos.awsplayer.com/guidance/factory-visibility-and-intelligence/index.html)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Lambda, API Gateway, and DynamoDB generate Amazon CloudWatch log files that track operational steps for ingesting new documents into the knowledge base. CloudWatch also tracks interactions for web-based user chat sessions, constructing prompts, and invoking generative AI models. Logging at every stage of the processing pipeline is essential for identifying errors and maintaining the availability and performance of the chatbot, and you can use these log files (as well as other integrated tools, like AWS X-Ray ) to trace implementation errors to resolve problems. DynamoDB tables also track individual user chat history and the state of document ingestion. You can use these tables (along with point-in-time recovery) to re-create an error state. This Guidance provides a direct mechanism for user feedback on each technical response generated so that it can regularly tune the model and provide strategies for meeting your business objectives. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon VPC provides a virtual network that logically isolates all its resources, and only authorized users and services have access to the resources in this Guidance. This Guidance deploys Lambda, OpenSearch Service, and SageMaker to a VPC and uses VPC endpoints so that these services can securely communicate with functions managed by AWS (like API Gateway ) without traversing the public internet. SageMaker, Amazon Bedrock, and Amazon Q Business store LLM chat history; the associated data stay in your private account and never feed into public LLM repositories. Guardrails for Amazon Bedrock also prevent the LLM from displaying any unauthorized or inappropriate content. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3 lets you store technical knowledge base documents with extremely high durability. DynamoDB provides native backup, restoration, and point-in-time recovery so that you can quickly restore operations in the event of a disruption. All these services are fully managed by AWS for high reliability and availability; for example, DynamoDB automatically creates three replicas of all tables in separate Availability Zones. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Bedrock, Amazon Q, Lambda, and DynamoDB are all fully managed services, so you don’t need to select instance types or manage scaling. Additionally, they are all serverless, so they automatically scale capacity to match demand. These services host the LLM, implement workflows through agents, manage the knowledge base, and store the document metadata and chat history. Additionally, Lambda enables a high degree of concurrency, so the technician’s assistant can support a large number of simultaneous users. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using Amazon S3 Intelligent-Tiering, you can tailor your document storage retention policies. For example, you can automatically move infrequently accessed documents to lower-cost tiers like Amazon S3 Glacier Instant Retrieval. DynamoDB supports a time-to-live (TTL) feature that automatically deletes old entries (such as expired chat histories) from your table so that they don’t consume write bandwidth. By using these services and features, you can minimize the recurring costs of storage for your knowledge base. All the computational services use a pay-as-you-go model, and that cost directly scales with your usage of the technician’s assistant chatbot; as a result, you can save by not overprovisioning capacity. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon S3, DynamoDB, Amazon Q, Amazon Bedrock, and Lambda are fully managed services that automatically scale their allocation of resources based on demand. Additionally, Amazon S3 supports S3 Intelligent-Tiering policies, and DynamoDB supports a TTL feature. You can use these options to automatically delete unused data (such as documents or session histories) to minimize your storage, subsequently lowering your carbon footprint. Additionally, this Guidance scales computational resources based on demand, helping you avoid energy waste. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
