---
source_url: https://docs.aws.amazon.com/solutions/video-summarization-using-amazon-sagemaker-and-ai-services/index.html
---

---
title: 'Guidance for Video Summarization using Amazon SageMaker and AI Services'
canonical_url: https://docs.aws.amazon.com/solutions/video-summarization-using-amazon-sagemaker-and-ai-services/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Video Summarization using Amazon SageMaker and AI Services

Generate video summaries with voice narration, powered by computer vision technology

## Overview

This Guidance demonstrates how Amazon Sagemaker and Large Language Models (LLMs) can be used to create short-form video summaries compiled from a longer, original video file. The summary is used to identify the most relevant video segments, which are compiled into a final video output with voice narration. It helps media organizations automate the process of generating video summaries to enhance the viability, scalability, and efficiency of content production throughout the supply chain process. It also helps media organizations improve their audiences' experiences through personalized content.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/video-summarization-using-amazon-sagemaker-and-ai-services.pdf)

![Architecture diagram](/images/solutions/video-summarization-using-amazon-sagemaker-and-ai-services/images/video-summarization-using-amazon-sagemaker-and-ai-services-1.png)

1. **Step 1**: Amazon Simple Storage Service (Amazon S3) hosts a static website for the video summarization workload, served by an Amazon CloudFront distribution. Amazon Cognito provides customer identity and sign-in functionality to the web application.
1. **Step 2**: Amazon S3 stores the source videos, which are uploaded through pre-signed URLs.
1. **Step 3**: To perform a video summarization, make an API call to Amazon API Gateway that invokes an AWS Lambda function to put the request into an Amazon Simple Queue Service (Amazon SQS) queue. New messages added to the queue are processed by a Lambda function that processes a new AWS Step Functions workflow.
1. **Step 4**: Amazon Transcribe converts the speech in the source video into text, generating an output subtitle file containing the transcript and timestamps.
1. **Step 5**: Amazon SageMaker foundation model endpoint summarizes the text, retaining the story from the original video but in shorter form.
1. **Step 6**: Amazon Polly generates a voice narration. The SageMaker text embedding model endpoint pairs each sentence in the summarized text with its corresponding sentences in the original subtitle file. The output is the most relevant video segments and their timestamps.
1. **Step 7**: AWS Elemental MediaConvert transcodes the final video output using the original video input clipping timestamps. It inserts the voice narration, generated from Amazon Polly, with optional background music of your preference.
1. **Step 8**: Amazon S3 stores the output video that offers durable, highly available, and scalable data storage at low cost.
1. **Step 9**: Amazon DynamoDB tables store profiling and task metadata. This helps you keep track of the tasks' status and other relevant information.
1. **Step 10**: Amazon CloudWatch and Amazon EventBridge monitor in near real-time every component, and can be used to integrate this workflow into other systems.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudWatch, EventBridge, Lambda, API Gateway, and Step Functions are AWS services purpose-built to enhance your operational excellence when operating this Guidance. CloudWatch monitors and collects metrics, logs, and events from Lambda, API Gateway and Step Functions. In addition, using CloudWatch helps you gain insights into the workload performance and identify issues quickly through the proactive monitoring, automated anomaly detection, and near real-time visualization of data. With EventBridge, routing and processing events from Lambda, API Gateway, Step Functions and other sources are supported to make responsive actions during the workflow. EventBridge also reduces tight coupling and enables asynchronous interactions between workflow components, providing an event-driven architecture that can respond effectively to changes while being easily extended. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito, Amazon CloudFront and AWS Shield Standard are deployed in this Guidance to enhance your security. Amazon Cognito enables you to manage user identities and authentication for the application. CloudFront improves website security with secure data transmission and access control, limiting unauthorized access to AWS resources by using origin access control (OAC). Shield Standard is automatically enabled when you use AWS services, such as CloudFront, and defends against the most common, frequently occurring network and transport layer distributed denial of service (DDoS) attacks. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3, CloudWatch, EventBridge, and Lambda are used throughout this Guidance to enhance the reliability of your workloads. Amazon S3 does this by storing objects, including videos and other media file formats, in a highly scalable, highly available manner. Amazon S3 also supports versioning, which enables you to retain and manage historical data versions, contributing to data integrity and availability. EventBridge and CloudWatch monitor and respond to events, such as changes in states in CloudWatch alarms or in Step Functions, to process Lambda functions with remediation logic for the workload. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda, DynamoDB, Amazon S3, and CloudFront help enhance your performance efficiency. With Lambda, you can run code with zero administration, as it will manage everything required to run and scale the code. It also offers event-driven scaling, improving application performance and resource efficiency. Furthermore, DynamoDB provides a fully managed NoSQL database with single-digit millisecond latency at any scale, where all the profiling and video summarization task metadata is stored. Moreover, using Amazon S3 to host static web applications and store media files reduces latency and increases throughput in data access. Additionally, CloudFront includes a caching capability and this service, coupled with Amazon S3, brings content closer to the users with a global network of 550+ Points of Presence, further improving performance and reducing latency. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3, DynamoDB, and Lambda enhance your cost optimization framework in a number of ways. For one, Amazon S3 Lifecycle Management manages your videos and media objects so that they are stored cost effectively throughout their lifecycle. Second, DynamoDB Time to Live (TTL) allows you to define a timestamp by item to determine when an item in the table is no longer needed. And third, with Lambda, you're only charged for the actual compute time used during the processing of your code. There are no charges for idle resources, as Lambda automatically scales resources up or down based on the demand. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda, Amazon S3, DynamoDB, and CloudFront are all used in this Guidance to enhance the sustainability of your workloads. The Lambda serverless architecture dynamically allocates resources based on demand, ensuring efficient utilization and reducing energy consumption. It also provides content filtering options for Amazon SQS, so that the Lambda function is only invoked by Amazon SQS under the filtering criteria you specify, which reduces Lambda function processing. Amazon S3 Intelligent-Tiering storage class and Lifecycle features help automatically move data to appropriate storage tiers based on access patterns, reducing the need for higher-cost storage and deletes unnecessary data. DynamoDB automatically scales read and write capacity based on usage, eliminating over-provisioning and minimizing energy consumption associated with excessive resources. Finally, CloudFront, with global edge locations, reduces the need to repeatedly access origin servers, conserving resources and reducing energy consumption by serving cached content closer to end users. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Video summarization with AWS artificial intelligence (AI) and machine learning (ML) services**: This blog post demonstrates how to build an end-to-end workload to allow users to upload, process, and summarize videos into short form with voice narration by leveraging AWS AI/ML services.

[Learn more](https://aws.amazon.com/blogs/media/video-summarization-with-aws-artificial-intelligence-ai-and-machine-learning-ml-services/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
