---
source_url: https://docs.aws.amazon.com/solutions/advanced-multimodal-chatbot-with-speech-to-speech-on-aws/index.html
---

# Guidance for Advanced Multimodal Chatbot with Speech-to-Speech on AWS

## Overview

This Guidance demonstrates how to implement an advanced multimodal chatbot that transforms interactions with diverse data sources, including documents, audio, and video content. Extracting meaningful data insights from abundant data has become increasingly challenging, especially when company data includes audio and video files. The advanced multimodal chatbot helps you quickly access specific sections or topics, summarize content, or answer questions about your data. It seamlessly integrates with various file formats, providing a unified interface for knowledge extraction. You can then ask questions about your data, and the chatbot delivers precise answers, complete with source links and exact attribution for fast, efficient reference.

## Benefits

### Transform complex data into actionable insights

Extract meaningful information from diverse data sources including audio and video files through a unified interface. Ask questions in natural language and receive precise answers with source attribution for faster decision-making.

### Deploy enterprise-grade AI with minimal overhead

Leverage serverless architecture with Amazon Bedrock, Lambda, and EventBridge to eliminate infrastructure management. Scale automatically with demand and get visibility into system performance and user interactions through built-in monitoring

### Optimize costs while maximizing performance

Pay only for resources you use with serverless components that scale automatically. Reduce data transfer costs with CloudFront edge caching while S3 Intelligent-Tiering minimizes storage expenses as your data volume grows.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/advanced-multimodal-chatbot-with-speech-to-speech-on-aws.pdf)

![Architecture diagram](/images/solutions/advanced-multimodal-chatbot-with-speech-to-speech-on-aws/images/advanced-multimodal-chatbot-with-speech-to-speech-on-aws-1.png)

1. **Step 1**: Users access the web application UI to authenticate, upload multimedia files, and ask questions about their data.
1. **Step 2**: Amazon CloudFront delivers the web application UI, which is hosted in an Amazon Simple Storage Service (Amazon S3) bucket and authenticates users through Amazon Cognito.
1. **Step 3**: Authenticated users upload multimedia files through the web application UI to the multimedia data S3 bucket.
1. **Step 4**: File uploads to the multimedia data S3 bucket trigger an Amazon EventBridge rule. EventBridge invokes the file handler AWS Lambda function.
1. **Step 5**: The Lambda function invokes an Amazon Bedrock Data Automation project with the file.
1. **Step 6**: The Amazon Bedrock Data Automation project processes the file to extract information in structured JSON format. Text, image descriptions, and table data are extracted from rich documents. Image summary and categories are extracted from images. Audio segments, summary, and timestamps are extracted for both video and audio files. In addition, video frames and video summary are also extracted for video files.
1. **Step 7**: Upon successful Amazon Bedrock Data Automation job completion, the Lambda function (text processor) is invoked by EventBridge and formats the JSON output, tests it, and uploads it to the documents folder in the organized data S3 bucket.
1. **Step 8**: Users trigger the Amazon Bedrock Knowledge Bases retriever from the web application UI with questions about their data. The web application UI invokes the Lambda function (chatbot backend), which calls Amazon Bedrock to search the retrieved content and generate a response. The generated response is then returned to the web application UI.
1. **Step 9**: When users initiate speech-to-speech communication, the web application UI forwards the process through Amazon CloudFront to the speech-to-speech processing pipeline. This pipeline consists of Amazon Elastic Container Service (Amazon ECS) with a running task to establish and maintain connection with Amazon Nova Sonic, and a network load balancer (NLB) to distribute traffic. Amazon Nova Sonic handles speech recognition, natural language processing, and speech synthesis workloads, enabling users to ask questions through voice and receive answers through audio, with relevant context from Amazon Bedrock Knowledge Bases.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-advanced-multi-modal-chatbot-including-speech-to-speech-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
