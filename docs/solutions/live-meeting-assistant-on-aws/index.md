---
source_url: https://docs.aws.amazon.com/solutions/live-meeting-assistant-on-aws/index.html
---

---
title: 'Guidance for Live Meeting Assistant on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/live-meeting-assistant-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Live Meeting Assistant on AWS

Automated meeting notes, translation, and transcription with generative AI

## Overview

This Guidance shows how you can add generative artificial intelligence (generative AI) to your virtual meetings to translate languages, summarize conversations, and capture live insights. As virtual meetings become more prevalent, retaining all the information presented can be challenging for participants. The Live Meeting Assistant (LMA) on AWS collects speaker audio and metadata from a browser-based meeting app, softphone app, or audio source. It then uses large language models (LLMs) to generate customizable transcriptions, insights, and summaries, helping participants derive more value from every meeting.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/live-meeting-assistant-on-aws.pdf)

![Architecture diagram](/images/solutions/live-meeting-assistant-on-aws/images/live-meeting-assistant-on-aws-1.png)

1. **Step 1**: Your Live Meeting Assistant (LMA) administrator installs the LMA browser extension as a plugin to their browser. Meeting participants join the meeting app.
1. **Step 2**: The LMA bowser extension registers the meeting in the LMA web app. Amazon CloudFront serves the web app from an Amazon Simple Storage Service (Amazon S3) source. LMA users are authenticated through Amazon Cognito.
1. **Step 3**: The LMA web app communicates with an API hosted by AWS AppSync and stores meeting information in Amazon DynamoDB.
1. **Step 4**: The API is backed by AWS Lambda, which uses functions to process call events. Transcriptions are processed from a stream in Amazon Kinesis Data Streams.
1. **Step 5**: The LMA browser extension sends audio to a CloudFront WebSocket endpoint. WebSocket traffic is load balanced by Application Load Balancer.
1. **Step 6**: Amazon Transcribe transcribes the audio and stores the call recording in Amazon S3. Authorization occurs using Amazon Cognito. AWS Fargate clusters process the audio into a stream in Kinesis Data Streams.
1. **Step 7**: The LMA solution supports retrieval-augmented generation (RAG) by enabling users to create a new (or link to an existing) Knowledge Base in Amazon Bedrock. Additional data sources, like those indexed in Amazon Kendra, can be configured in the open-source QnABot on AWS solution as a fallback RAG index.
1. **Step 8**: Amazon Bedrock provides API access to LLMs to generate call summaries.
1. **Step 9**: The LMA solution deploys open-source QnABot on AWS as a nested AWS CloudFormation stack for answers based on FAQs and as an orchestrator for request routing to the appropriate AI service. LMA admins interact with the chatbot using Amazon Lex through the LMA web app.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudFormation creates a stack in the AWS Management Console, providing an infrastructure as code mechanism that enables updates to the deployed solution. QnABot on AWS, nested within the stack, can quickly create a meeting assistant interface, and you can version it to enable updates as new features become available. Lambda divides functions into smaller, event-driven components so that you can more efficiently track the flow of data and isolate potential issues in call processing. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito is tightly integrated within the AWS services that comprise the LMA outlined in this Guidance. The service provides authentication and authorization capabilities, so that only authorized users can access and interact with the LMA web application and the supporting Lambda functions. Through this Amazon Cognito integration, the system maintains a secure and controlled provisioning of access to its various components, aligned with the principle of least privilege, enhancing the overall confidentiality and reliability of the meeting data processed by the LMA application. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Application Load Balancer routes traffic requests to the call processing functions and prevents the overload of any one container. Fargate scales audio processing as needed during call events, and its default health monitoring functionality quickly alerts you to any failure of the audio processing component. AWS AppSync provides a managed GraphQL service to provide a serverless, automatically scaling API to the frontend. Kinesis Data Streams synchronously replicates data across three Availability Zones, providing high availability and data durability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

CloudFront caches assets that serve the web application on the edge so that they can quickly respond to user requests. It also supports using WebSocket, a TCP-based protocol that is useful when you need long-lived bidirectional connections between clients and servers. As a result, it can support real-time audio processing. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Unlike in monolithic applications, which might require you to run and pay for unnecessary resources, this Guidance breaks call processing into smaller components, using discreet Lambda functions. Additionally, the DynamoDB on-demand throughput mode conserves read and write capacity and provides pay-per-request pricing so that you only pay for what you use. Finally, Fargate scales audio processing functions up and down with demand, conserving resources and optimizing costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By using on-demand services so that you only use the resources you need, this Guidance conserves computational resources and minimizes your workload’s environmental impact. For example, CloudFront caches web assets on the edge, reducing the need to serve requests from the origin. Kinesis Data Streams is fully managed and can stream massive amounts of data on demand. And DynamoDB scales database functions on-demand so that its provisioned capacity matches your application’s needs. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Live Meeting Assistant (LMA) with Amazon Transcribe, Amazon Bedrock, and Knowledge Bases for Amazon Bedrock**: This sample code demonstrates a flexible, feature-rich, and customizable approach to provide live meeting assistance to improve your productivity during and after meetings.

[Learn more](https://github.com/aws-samples/amazon-transcribe-live-meeting-assistant)

- **Live Meeting Assistant with Amazon Transcribe, Amazon Bedrock, and Knowledge Bases for Amazon Bedrock**: This blog post demonstrates how to use LMA with Amazon Transcribe, Amazon Bedrock, and Knowledge Bases for Amazon Bedrock.

[Learn more](https://aws.amazon.com/blogs/machine-learning/live-meeting-assistant-with-amazon-transcribe-amazon-bedrock-and-knowledge-bases-for-amazon-bedrock/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
