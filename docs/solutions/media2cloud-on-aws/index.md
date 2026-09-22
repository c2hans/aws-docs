---
source_url: https://docs.aws.amazon.com/solutions/media2cloud-on-aws/index.html
---

---
title: 'Guidance for Media2Cloud on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/media2cloud-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Media2Cloud on AWS

## Overview

This Guidance helps you facilitate the migration of your digital assets to the cloud, allowing you to take full advantage of the latest advancements in asset management and prepare content for distribution to media consumers. It sets up serverless ingestion and analysis workflows to move your video assets and associated metadata to the AWS Cloud. During the migration, this Guidance analyzes and extracts machine learning metadata from your video. It also comes with a web interface so you can immediately start ingesting and analyzing your content.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/media2cloud-on-aws.pdf)

![Architecture diagram](/images/solutions/media2cloud-on-aws/images/media2cloud-on-aws-1.png)

1. **Step 1**: An Amazon Cognito user pool to provide a user directory.
1. **Step 2**: An Amazon API Gateway RESTful API endpoint, which is configured to use AWS Identity and Access Management (IAM) authentication.
1. **Step 3**: An Amazon CloudFront distribution that hosts the web application artifacts, such as minimized JavaScript files and graphics stored in the web bucket.
1. **Step 4**: An AWS Step Functions main state machine which serves as the entry point to the backend ingestion and analysis workflows.
1. **Step 5**: An Step Functions ingestion sub-state machine that orchestrates the ingestion process by media file type and generates proxies for ingested media. It uses AWS Elemental MediaConvert for video and audio files and open-source tools for image files and documents.
1. **Step 6**: A Step Functions analysis sub-state machine that is responsible for the analysis process. It consists of Step Functions that run analysis jobs with Amazon Rekognition, Amazon Transcribe, Amazon Comprehend, and Amazon Textract.
1. **Step 7**: Amazon DynamoDB tables to store artifacts generated during the ingestion and analysis processes, such as overall status, pointers to where intermediate files are stored, and state machine run tokens.
1. **Step 8**: An Amazon OpenSearch Service cluster, which stores ingestion attributes and machine learning metadata, and facilitates your search and discovery needs.
1. **Step 9**: Four Amazon Simple Storage Service (Amazon S3) buckets store: uploaded content, file proxies that the Guidance generates during ingestion, static web application artifacts, and access logs for services used.
1. **Step 10**: Amazon CloudWatch event rules that are logged when specific tasks undergo state changes.
1. **Step 11**: Amazon EventBridge used by an internal queue management system where the backlog system notifies workflows (state machines) when a queued artificial intelligence and machine learning (AI/ML) request has been processed.
1. **Step 12**: An AWS IoT Core topic that allows the ingestion and analysis workflows to communicate with the front-end web application asynchronously through publish or subscribe MQTT messaging.
1. **Step 13**: Amazon Simple Notification Service (Amazon SNS) topics to allow Amazon Rekognition to publish job status in the video analysis workflow, and to support custom integration with your system.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment. The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open implementation guide](https://aws-solutions-library-samples.github.io/media-entertainment/media2cloud-on-aws.html)
[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-media2cloud-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance pushes metrics to CloudWatch at various stages to provide observability into the infrastructure, such as AWS Lambda functions, AI services, and Amazon S3 buckets. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

We highly recommend that you encrypt sensitive data in transit and at rest. This Guidance automatically encrypts media files and metadata at rest with Amazon S3 server-side encryption (SSE-S3). The Guidance's Amazon SNS topics and DynamoDB tables are also encrypted at rest using SSE-S3. Furthermore, documents indexed to the OpenSearch Service cluster are encrypted at rest, and node-to-node communication within the cluster is also encrypted. This Guidance deploys a static website hosted in an Amazon S3 bucket. To help reduce latency and improve security, this Guidance includes a CloudFront distribution with an origin access identity, which is a special CloudFront user that helps restrict access to website bucket contents. For more information, refer to Restricting access to an Amazon S3 origin. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Guidance for Media2Cloud on AWS uses AWS serverless services wherever possible (for example, Lambda, API Gateway, Amazon S3, and DynamoDB) to ensure high availability and quick recovery from service failure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

You can create workflows with the pre-built AWS CloudFormation template. Because this Guidance is an open source project published on GitHub, you can customize this and build from the source code. The README provides a step-by-step guide to build and customize this Guidance, along with a mini-tutorial, and an in-depth explanation of each component and the overall design. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Because this Guidance uses a serverless and event-driven architecture, you are only charged for what you use. Its design allows you to configure and tailor your own media workflows, and use only the AWS services that you need. Furthermore, it allows your assets to be stored cost effectively using Amazon S3 with Lifecycle policies to store and archive ingested contents, proxies, and metadata. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

A critical component for sustainability is maximizing the usage of the AWS AI services so you minimize the environmental impact of the backend services. And, the serverless design of this Guidance is designed to reduce your carbon footprint compared to the footprint of continually operating on-premises servers. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Announcing AWS Media Intelligence Solutions**: This blog post announces AWS Media Intelligence (AWS MI) solutions and covers four important use cases: content search and discovery, captioning and localization, compliance and brand safety, and content monetization.

[Learn more](https://aws.amazon.com/blogs/machine-learning/announcing-aws-media-intelligence-solutions/)

- **Successful innovation for ESSENCE as Starchive and AWS help deliver the 2020 ESSENCE Festival of Culture**: This blog post describes how ESSENCE Magazine, with the help of Starchive.io and AWS, celebrated their landmark anniversary with a major virtual event to mark the occasion.

[Learn more](https://aws.amazon.com/blogs/media/successful-innovation-for-essence-as-starchive-and-aws-help-deliver-the-2020-essence-festival-of-culture/)

- **AWS Solutions Media2Cloud: Architecture for the Formula 1 Legacy**: Learn how AWS created a long-term remedy to F1’s media asset management needs using the Media2Cloud (M2C) reference implementation by AWS Solutions.

[Learn more](https://youtu.be/CANn5FdkNbA)

- **UKTV Enhances Media Workstreams and Functions with an AWS Solution**: Learn how UKTV uses this AWS Solution to achieve their goals of increased observability, better resilience, and greater possibilities for more advanced media functionality.

[Learn more](https://youtu.be/cz03AFD1T-c)

[Read usage guidelines](/solutions/guidance-disclaimers/)
