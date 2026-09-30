---
source_url: https://docs.aws.amazon.com/solutions/shoppable-video-on-aws/index.html
---

---
title: 'Guidance for Shoppable Video on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/shoppable-video-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Shoppable Video on AWS

Provide viewers with a seamless shopping experience merged with your digital content

## Overview

This Guidance helps digital video streaming companies provide their audience with the opportunity to shop for products while watching digital media. These companies can use data and contextual analysis to create this seamless shopping experience. Content owners can generate increased revenue and enhance engagement with their audience while minimizing disruption in their viewing experience.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/shoppable-video-on-aws.pdf)

![Architecture diagram](/images/solutions/shoppable-video-on-aws/images/shoppable-video-on-aws-1.png)

1. **Step 1**: In the Product Catalog Creation stage, upload product images and product IDs from the ecommerce website to Amazon Simple Storage Service (Amazon S3), invoking the product catalog creation process through AWS Step Functions.
1. **Step 2**: Step Functions orchestrates the product catalog creation process by processing images uploaded in Step 1. AWS Lambda runs a multimodal apparel machine learning (ML) model that identifies products with bounding boxes and generates image embeddings.
1. **Step 3**: Amazon OpenSearch Service cluster with K-nearest neighbors (K-NN) plugins store the product image embeddings with the product identifier and enable the search for similar products.
1. **Step 4**: In the Video and Image Analysis and Processing stage, upload video files to an Amazon Simple Storage Service (Amazon S3) bucket invoking content processing through Step Functions.
1. **Step 5**: Step Functions orchestrates the processing of the video content, apparel identifications, and search for similar items.
1. **Step 6**: AWS Elemental MediaConvert processes video and audio files, extracts frame images from the video files, and stores files in Amazon S3. Amazon Rekognition is used for segment detection in videos. Lambda runs object detection and image embedding models that identify product information from the images obtained through MediaConvert and searches for similar items in the product catalog using OpenSearch Service. The Amazon DynamoDB tables are used for indexing artifacts such as video files and images by MediaConvert.
1. **Step 7**: The output of the Video and Image Analysis and Processing pipeline stage is a shoppable metadata file (stored as JSON), which is used by the user experience (UX) Presentation stage. Lambda and Amazon API Gateway form the API connector to the ecommerce website.
1. **Step 8**: The API connector retrieves detailed information about the products per product ID, such as product images, prices, ratings, and availability, enabling viewers to interact with and shop for desired products.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Step Functions orchestrates Lambda, MediaConvert, and Amazon S3 workflows. The Step Functions console graph view provides a graphical representation of your state machine with visual indications of which steps have succeeded, are in progress, have failed, have caught error, or were cancelled. Visualizing the status of Step Functions states helps the operator understand workflow health. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All user data stored in DynamoDB is fully encrypted at rest. DynamoDB encrypts your data at rest using encryption keys stored in AWS Key Management Service (AWS KMS), which helps reduce the operational burden and complexity involved in protecting sensitive data. All AWS Identity and Access Management (IAM) policies have been scoped down to the minimum permissions required for the service to function properly. Minimum permissions set by IAM help you avoid unauthorized access. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda supports automatic scaling to handle increased workloads and runs in multiple Availability Zones to help ensure that it is available to process events in case of a service interruption in a single Availability Zone. Lambda supports automatic scaling, retries, and high availability, adding resiliency and reliability to the workflow. DynamoDB automatically replicates data across multiple Availability Zones, offering high data durability and integrated availability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Serverless architectures that use serverless managed services like Lambda remove the need to run and maintain physical servers for video or image processing workflows. As a managed service that hosts code, Lambda can also lower transactional costs because managed services operate at scale in the cloud. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The Amazon S3 Intelligent-Tiering storage class optimizes storage costs by automatically moving data to the most cost-effective access tier when access patterns change. This reduces storage cost of the content that is not regularly accessed. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Step Functions is a managed service that scales based on demand, so you do not have to manage underlying infrastructure. This reduces carbon emissions as Step Functions has inherited compute efficiencies and only runs when needed. Additionally, Step Functions provide an event-driven architecture for the Product Catalog Creation and Video and Image Analysis and Processing pipelines, which, in combination with Lambda only consume computational resources when actually processing data. These pipelines scale on demand to avoid over-provisioned server capacity. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
