---
source_url: https://docs.aws.amazon.com/solutions/media-extraction-and-dynamic-content-policy-framework-on-aws/index.html
---

---
title: 'Guidance for Media Extraction and Dynamic Content Policy Framework on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/media-extraction-and-dynamic-content-policy-framework-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Media Extraction and Dynamic Content Policy Framework on AWS

## Overview

This Guidance demonstrates how to accelerate your content analysis workflows by automating video metadata extraction, intelligence gathering, and content moderation. It enables you to efficiently process large volumes of video content, extract valuable insights, and make data-driven decisions through customizable policy evaluations. By automating these traditionally manual tasks, you can reduce operational costs, improve accuracy, and scale your content analysis capabilities while maintaining secure and reliable operations.

## How it works

### Extraction of generic metadata

This architecture diagram shows how to use generative AI to extract generic metadata from videos and demonstrates a dynamic policy evaluation analysis.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/media-extraction-and-dynamic-content-policy-framework-on-aws.pdf)Step 1Media analysts access front end static website through Amazon CloudFront distribution. The static content hosted on Amazon Simple Storage Service (Amazon S3).Step 2Users log in to the frontend web application, authenticated by an Amazon Cognito user pool.Step 3Users upload video(s) to Amazon S3 directly from the browser using multi-part, pre-signed Amazon S3 URLs managed by the UI application.Step 4The frontend UI interacts with the extract service (microservice) through a RESTful interface provided by Amazon API Gateway. This interface offers Create, Read, Update, Delete (CRUD) features for video task extraction and management. The extraction service can be deployed and used independently of the other components.Step 5An AWS Step Functions state machine oversees the analysis process. It transcribes audio using Amazon Transcribe, samples image frames from video using moviepy, uses multimodal models on Amazon Bedrock to analyze images, and uses Amazon Rekognition for additional insights. It also generates text and multimodal embeddings on the frame level. Users can customize the logic in this Guidance to integrate their preferred generative AI models.Step 6Amazon DynamoDB stores media processing task metadata and extracted video information in text format. An Amazon OpenSearch Service cluster stores vector embeddings and facilitates search and discovery needs.Step 7Using the solution UI, the user selects and customizes existing template prompts, then initiates the policy evaluation utilizing Amazon Bedrock large language models (LLMs) based on the extracted video metadata.### Restful APIs of the extraction service

This architecture diagram illustrates the key RESTful APIs of the extraction service, served through Amazon API Gateway. The UI uses APIs to retrieve data, allowing users to integrate the extraction service into existing workflows.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/media-extraction-and-dynamic-content-policy-framework-on-aws.pdf)Step 1The /start_task endpoint serves as the core of the extraction service, managing the video metadata extraction process and maintaining the results.Step 2DynamoDB stores the extracted metadata. The raw results from generative AI models are saved as JSON or text files in Amazon S3. Amazon OpenSearch Service indexes store frame-level embeddings to serve search.Step 3The process includes invoking Amazon Transcribe to generate audio transcriptions, sample image frames from the video at a specified interval, and remove similar frames by generating multimodal embeddings and applying similarity comparison. For each image frame, the service applies AI or generative AI features to extract metadata. Additionally, the service generates text and multimodal embeddings for each frame to enable vector search capabilities.Step 4Amazon Simple Notification Service (Amazon SNS) notifies downstream workflows of task completion.Step 5The /get_task endpoint retrieves video task information using a unique task ID. The data is fetched from the DynamoDB tables.Step 6The /delete_task endpoint deletes video tasks using a unique task ID. It will delete all the task-related states from DynamoDB tables, Amazon S3, and Amazon OpenSearch indexes.Step 7The /search_task endpoint searches for tasks matching the provided criteria. It supports keyword searches against the DynamoDB task name and description, as well as semantic and multimodal embedding searches using the Amazon OpenSearch vector index.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-media-extraction-and-dynamic-content-policy-framework-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch provides logging and insights for the services running in AWS Lambda and Step Functions. This Guidance pushes metrics to CloudWatch at various stages to provide observability into the infrastructure, such as Lambda functions, AI/ML services, and S3 buckets. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance implements least-privilege AWS Identity and Access Management policies and encrypts S3 data using AWS Key Management Service (AWS KMS) keys. User authentication is handled through Amazon Cognito using OAuth patterns for both web application login and API Gateway calls. The OpenSearch service cluster is deployed in an Amazon Virtual Private Cloud (Amazon VPC) private subnet, accessible only to authorized Lambda functions. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3 provides robust data management through version control, deletion prevention, and cross-region replication capabilities. Serverless services like API Gateway, Lambda, Step Functions, and Amazon Simple Queue Service (Amazon SQS) offer built-in scalability and high availability. The OpenSearch Service deployment supports high availability through multiple Availability Zones, featuring redundant data nodes with replicated shards, helping ensure data persistence and recovery capabilities. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda and Step Functions enable efficient parallel processing through concurrent execution of functions and workflow steps. This parallel processing capability improves overall throughput and reduces execution time. The serverless architecture automatically handles the complexity of scaling workloads on AWS for optimal performance for media processing tasks. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 storage classes and lifecycle policies optimize video storage costs, while serverless and AI/ML services operate on a pay-as-you-go model, meaning you only pay for services used. The event-driven architecture helps ensure charges apply only for resources actually used, allowing you to configure and tailor your media workflows cost-effectively while using S3 lifecycle policies to to store and archive ingested contents, proxies, and metadata. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS serverless services and AI/ML components allocate compute resources dynamically based on demand, eliminating over-provisioning and reducing resource waste. This approach minimizes energy consumption and compared to traditional on-premises servers, while maximizing the efficiency of AWS AI services to reduce the environmental impact of backend operations. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
