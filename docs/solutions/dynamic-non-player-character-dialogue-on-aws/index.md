---
source_url: https://docs.aws.amazon.com/solutions/dynamic-non-player-character-dialogue-on-aws/index.html
---

---
title: 'Guidance for Dynamic Non-Player Character (NPC) Dialogue on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/dynamic-non-player-character-dialogue-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Dynamic Non-Player Character (NPC) Dialogue on AWS

## Overview

This Guidance helps game developers automate the creation of non-player characters (NPCs) that dynamically respond to player questions based on custom in-game knowledge and personality. This deployable template sets up API access to large language models (LLMs) in Amazon Bedrock, enabling a game client to connect and prompt the models with player input. Any of the available models in Amazon Bedrock, such as Amazon Nova, Claude, and Llama, can be used to generate dynamic responses from the NPC, enhancing scripted dialogue and creating unique player interactions. At the same time, it ensures that the NPC has secure access to a comprehensive knowledge base of game lore. This Guidance includes architecture sample code and engine integration example for quick and effective deployment.

## How it works

### Overview

This architecture diagram shows an overview workflow for hosting a generative AI NPC on AWS.

[Download architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/dynamic-non-player-character-dialogue-on-aws.pdf)Step 1Game clients interact with the NPC running on Unreal Engine.Step 2Requests for generated text responses from the NPC are sent to a Text API Amazon API Gateway endpoint. Requests that require game-specific context from the NPC are sent to a retrieval-augmented generation (RAG) API Gateway endpoint.Step 3AWS Lambda handles the NPC text requests and sends them to LLMs hosted on Amazon Bedrock.Step 4Base LLMs and LLMs customized through fine-tuning provide a generated text response.Step 5The generated text response is sent to Amazon Polly, which in turn returns an audio stream of the response. The audio format is returned to the NPC and delivered as NPC synthesized speech.Step 6For RAG NPC requests, Lambda submits the request to Amazon Bedrock to generate a vectorized representation from the embeddings model. Lambda then searches for relevant information from an Amazon OpenSearch Service vector index.Step 7OpenSearch Service provides a similarity search capability to provide relevant context that augments the generated text request based on the vectorized representation of the request from Amazon Bedrock.Step 8The relevant context and original text request are sent to LLMs hosted on Amazon Bedrock to provide a generated text response. Amazon Polly then delivers the response as synthesized speech to the NPC.Step 9Game narrative writers add game-specific training data to create custom models using the FMOps process or add game lore data to hydrate the vector database.Step 10Infrastructure and DevOps engineers manage the architecture as code using the AWS Cloud Development Kit (AWS CDK) and monitor the Guidance using Amazon CloudWatch.### LLMOps Pipeline

This architecture diagram shows the processes of deploying an LLMOps pipeline on AWS.

[Download architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/dynamic-non-player-character-dialogue-on-aws.pdf#page=2)Step 1Infrastructure engineers build and test the codified infrastructure using AWS CDK.Step 2Updates to infrastructure code are committed to the Git repository, invoking the continuous integration and continuous deployment (CI/CD) pipeline within the Toolchain AWS account.Step 3Infrastructure assets, such as docker containers and AWS CloudFormation templates, are compiled and stored in Amazon Elastic Container Registry (Amazon ECR) and Amazon Simple Storage Service (Amazon S3).Step 4The infrastructure is deployed to the quality assurance (QA) AWS account as a CloudFormation stack for integration and system testing.Step 5AWS CodeBuild initiates automated testing scripts that verify that the architecture is functional and ready for production deployment.Step 6Upon successful completion of all systems tests, the infrastructure is automatically deployed as a CloudFormation stack into the Production (PROD) AWS account.Step 7The FMOps pipeline resources are also deployed as a CloudFormation stack into the PROD AWS account.### FMOps Pipeline

This architecture diagram shows the process of tuning a generative AI model using FMOps.

[Download architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/dynamic-non-player-character-dialogue-on-aws.pdf#page=3)Step 1Game lore text documents are uploaded to an S3 bucket.Step 2The document object upload event invokes Amazon SageMaker Pipelines.Step 3The preprocessing step runs a SageMaker processing job to pre-process the text documents for model fine-tuning and model evaluation.Step 4The callback step allows SageMaker Pipelines to integrate with other AWS services by sending a message to an Amazon Simple Queue Service (Amazon SQS) queue. After sending the message, SageMaker Pipelines waits for a response from the queue.Step 5Amazon SQS manages the message queue that coordinates tasks between the SageMaker Pipelines and the AWS Step Functions workflow.Step 6The Step Functions workflow orchestrates the process of fine-tuning the LLM. Once a model has been fine-tuned, Amazon SQS sends a success message back to the SageMaker Pipelines callback step.Step 7The model evaluation step runs a SageMaker processing job to evaluate the fine-tuned model's performance. The tuned model is stored in the Amazon SageMaker Model Registry.Step 8Machine learning (ML) practitioners review the tuned model and approve it for production use.Step 9An AWS CodePipeline workflow is invoked to deploy the approved model into production.### Database Hydration

This architecture diagram shows the process for database hydration by vectorizing and storing gamer lore for RAG.

[Download architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/dynamic-non-player-character-dialogue-on-aws.pdf#page=4)Step 1A data scientist uploads game lore text documents to an S3 bucket.Step 2The object upload invokes a Lambda function to launch a SageMaker processing job.Step 3A SageMaker processing job downloads the text document from Amazon S3 and splits the text into multiple chunks.Step 4The SageMaker processing job then submits each chunk of text to an Amazon Titan embeddings model hosted on Amazon Bedrock to create a vectorized representation of the text chunks.Step 5The SageMaker processing job then ingests both the text chunk and the vector representation into OpenSearch Service for RAG.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-dynamic-game-npc-dialogue-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses Lambda, API Gateway, and CloudWatch to track all API requests for generated NPC dialogue between the Unreal Engine client and the Amazon Bedrock foundation model. This provides end-to-end visibility into the status of the Guidance, allowing you to granularly track each request and response from the game client so you can quickly identify issues and react accordingly. Additionally, this Guidance is codified as a CDK application using CodePipeline,sooperations teams and developers can address faults and bugs through appropriate change control methodologies and quickly deploy these updates or fixes using the CI/CD pipeline. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon S3 provides encrypted protection for storing game lore documentation at rest in addition to encrypted access for data in transit, while ingesting game lore documentation into the vector or fine-tuning an Amazon Bedrock foundation model. API Gateway adds an additional layer of security between the Unreal Engine and the Amazon Bedrock foundation model by providing TLS-based encryption of all data between the NPC and the model. Lastly, Amazon Bedrock implements automated abuse detection mechanisms to further identify and mitigate violations of the AWS Acceptable Use Policy and the AWS Responsible AI Policy. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

API Gateway manages the automated scaling and throttling of requests by the NPC to the foundation model. Additionally, since the entire infrastructure is codified using CI/CD pipelines, you can provision resources across multiple AWS accounts and multiple AWS Regions in parallel. This enables multiple simultaneous infrastructure re-deployment scenarios to help you overcome AWS Region-level failures. As serverless infrastructure resources, API Gateway and Lambda allow you to focus on game development instead of manually managing resource allocation and usage patterns for API requests. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Serverless resources, such as Lambda and API Gateway, contribute to the efficiency of the Guidance by providing both elasticity and scalability. This allows the Guidance to dynamically adapt to an increase or decrease in API calls from the NPC client. An elastic and scalable approach helps you right-size resources for optimal performance and to address unforeseen increases or decreases in API requests—without having to manually manage provisioned infrastructure resources. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Codifying the Guidance as a CDK application provides game developers with the ability to quickly prototype and deploy their NPC characters into production. Amazon Bedrock gives developers quick access to foundation models hosted on Amazon Bedrock through an API Gateway REST API without having to engineer, build, and pre-train them. Turning around quick prototypes helps reduce the time and operations costs associated with building foundation models from scratch. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda provides a serverless, scalable, and event-driven approach without having to provision dedicated compute resources. Amazon S3 implements data lifecycle policies along with compression for all data across this Guidance, allowing for energy-efficient storage. Amazon Bedrock hosts foundation models on AWS silicon, offering better performance per watt of standard compute resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
