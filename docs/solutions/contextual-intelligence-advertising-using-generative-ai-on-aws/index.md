---
source_url: https://docs.aws.amazon.com/solutions/contextual-intelligence-advertising-using-generative-ai-on-aws/index.html
---

---
title: 'Guidance for Contextual Intelligence Advertising Using Generative AI on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/contextual-intelligence-advertising-using-generative-ai-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Contextual Intelligence Advertising Using Generative AI on AWS

## Overview

This Guidance shows how to use generative AI to derive contextual insights from multimedia assets and identify relevant audience segments for targeted advertising placements. By analyzing video, audio, and text, you can identify the most relevant audience segments and deliver personalized advertising experiences. Moreover, the use of multimodal large language models (LLMs) facilitates the extraction of insights from both visual and transcript components so you can align your media with the right advertising opportunities and monetize content more effectively.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/contextual-intelligence-advertising-using-generative-ai-on-aws.pdf)

![Architecture diagram](/images/solutions/contextual-intelligence-advertising-using-generative-ai-on-aws/images/contextual-intelligence-advertising-using-generative-ai-on-aws-1.png)

1. **Step 1**: Upload the latest version of the IAB Content Taxonomy to Amazon Simple Storage Service (Amazon S3).
1. **Step 2**: Create a knowledge base in Amazon Bedrock, a fully managed service that offers a choice of high-performing foundation models (FMs). Select Amazon OpenSearch Serverless as the vector database and Amazon Titan Text Embeddings v2 model as the embeddings model.
1. **Step 3**: Upload media content to an Amazon S3 bucket.
1. **Step 4**: Amazon EventBridge receives object creation notifications from Amazon S3. This triggers an orchestration workflow that executes AWS Step Functions for media preparation and analysis, as well as AWS Lambda functions to invoke Amazon Bedrock for contextual insights extraction.
1. **Step 5**: The Step Functions workflow executes media preparation and analysis tasks, invoking Lambda functions that use open-source tools like ffmpeg and perceptual hashing, generating transcriptions using Amazon Transcribe. The workflow metadata is stored in Amazon DynamoDB, and the processed media files are persisted in Amazon S3.
1. **Step 6**: The Lambda function invokes the multimodal large language models (LLMs) in Amazon Bedrock to extract contextual insights. It uses the Knowledge Bases for Bedrock to map the content to the IAB content taxonomy, utilizing a managed Retrieval Augmented Generation (RAG) search pattern.
1. **Step 7**: The Lambda function persists the contextual insights extracted from Amazon Bedrock into a DynamoDB table, storing the contextual metadata.
1. **Step 8**: When an ad request is received, the ad server invokes a Lambda function to fetch the IAB categories and other relevant contextual metadata from the DynamoDB store. The ad server then uses the retrieved contextual data to select the most relevant advertisement.
1. **Step 9**: AWS Elemental MediaTailor retrieves the relevant advertisement from the ad server, performs ad stitching, and serves a digital Video Ad Serving Template (VAST) manifest file containing the video content and the associated advertisement.
1. **Step 10**: Amazon CloudFront delivers the content, including the contextually relevant advertisements, to the end-user devices.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The Amazon CloudWatch logging service provides valuable insights into API calls across various AWS services, enabling the identification of errors and the subsequent troubleshooting of issues. Furthermore, the integration of EventBridge and Step Functions streamlines the discovery and processing of events, negating the need to maintain a dedicated event bus infrastructure. Additionally, the Step Functions console facilitates the visualization of workflow executions, including the input and output of each step, allowing you to troubleshoot challenges and pinpoint performance gaps. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

CloudFront, the content delivery network service, helps ensure the protection of served content against Distributed Denial of Service (DDoS) attacks while also providing encryption for the transmitted traffic. Notably, CloudFront offers built-in DDoS protection at no additional cost to users. Furthermore, by creating least privilege access policies, you can authorize access to specific Amazon S3 buckets and control which systems have access to the contextual metadata. Complementing these measures, AWS Identity and Access Management (IAM) enforces the principle of least privilege, restricting access to the required resources based on the specific roles assigned to users and applications. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The services outlined in this Guidance are all Regional AWS offerings, inherently providing built-in resilience against Availability Zone failures. The architecture's design uses the loosely coupled nature of EventBridge and Lambda, enabling the parallel execution of multiple contextual insights jobs without mutual impact. Furthermore, Lambda employs provisioned concurrency to support rate limiting, thereby managing service quotas and transactions per second for downstream systems. Complementing these measures, Step Functions facilitate retries and throttling of requests for the extraction of contextual insights and the execution of media preparation workflows. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda, Step Functions, and EventBridge are designed to accommodate the performance requirements for a diverse range of use cases pertaining to the extraction of contextual insights. These services can be used to execute batch jobs for processing large volumes of media assets stored in Amazon S3 buckets as well as to process individual media assets. These services support consistent performance, provided the transactions per second remain within the established AWS service quotas. Complementing these capabilities, CloudFront delivers low-latency content distribution to end-user devices. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda, the serverless compute service, is responsible for processing events triggered by the availability of new Amazon S3 objects or the execution of workflows. Furthermore, the Amazon DynamoDB Standard Infrequent Access (DynamoDB Standard-IA) storage tier enables cost reductions of up to 60% for the contextual metadata associated with media assets that are infrequently accessed by end-users. Additionally, the Amazon S3 Intelligent Tiering storage class automatically migrates Amazon S3 objects to less frequently accessed tiers based on observed access patterns. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda, Amazon Bedrock, and DynamoDB are designed to optimize resource utilization and dynamically scale to accommodate fluctuations in the volume of media assets and advertising requests. This inherent scalability and efficient resource management help minimize the environmental impact by reducing unnecessary resource consumption and energy usage. The serverless nature of these services also eliminates the need for dedicated infrastructure management, further enhancing the overall sustainability of this Guidance. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
