---
source_url: https://docs.aws.amazon.com/solutions/intelligent-identification-of-2d-3d-assets-on-aws/index.html
---

---
title: 'Guidance for Intelligent Identification of 2D/3D Assets on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/intelligent-identification-of-2d-3d-assets-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Intelligent Identification of 2D/3D Assets on AWS

## Overview

This Guidance helps you programmatically identify and manage 2D and 3D assets involved in the production of video games. Powered by artificial intelligence and machine learning (AI/ML), intelligent asset identification and management can save time that would otherwise be spent on manually processing digital assets. When a user uploads an asset, the described system will automatically analyze, identify, and produce labels with assigned confidence, and then store the labels along with other asset metadata. Once stored, you can use the asset labels, data, and metadata for fast querying.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/intelligent-identification-of-2d-3d-assets-on-aws.pdf)

![Architecture diagram](/images/solutions/intelligent-identification-of-2d-3d-assets-on-aws/images/intelligent-identification-of-2d-3d-assets-on-aws-1.png)

1. **Step 1**: Upload the 3D object file and an image(s) of the object to Amazon Simple Storage Service (Amazon S3).
1. **Step 2**: The S3 bucket is configured with an S3 event notification to trigger the processImage AWS Lambda function when an image is uploaded, sending the image files to Amazon Rekognition to be analyzed.
1. **Step 3**: The processImage Lambda function uses Amazon Rekognition to return labels about the image. The function then adds the labels to the image in an S3 bucket as user-defined metadata and tags.
1. **Step 4**: Putting tags on the image triggers the handleLabels Lambda function, which populates an Amazon DynamoDB table with the tags.
1. **Step 5**: When the object file is finished uploading, the processObject Lambda function is triggered. If the object resides in a folder along with image files, the top 5 tags from the image files are applied to the object.
1. **Step 6**: The handleLabels Lambda function populates the LabelMetadata table with the tags and metadata attached to files stored in the S3 bucket.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-intelligent-identification-of-2d-3d-assets-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS CloudFormation enables efficient, reliable, and consistent environment management. By using CloudFormation, you can automate and standardize the deployment of your AWS resources, reducing the risk of human error or environment inconsistencies. You can also modify resources as needed and apply version-controls for each deployment of the Guidance. Amazon CloudWatch provides detailed logging for the asset across the workflow, from the time the asset is uploaded to the time Amazon Rekognition processes it. CloudWatch can provide insights into where the deployment may not be working as intended and prompt appropriate actions for remediation. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

You can control who has the ability to upload, copy, or modify assets by using S3 bucket policies and pre-signed URLs. Bucket policies allow you to manage who can interact with objects in your S3 bucket. Pre-signed URLs allow you to grant temporary access to assets in the S3 bucket without exposing them to unintended users. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

CloudWatch provides insights into failure points and metrics, which is critical for monitoring reliability of your workloads. These metrics allow you to set up your own alerts and track errors, so you can prepare automated actions in response to incidents or events. Automated response minimizes downtime and helps ensure that assets successfully complete processing. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda is event-driven, helping ensure that resources are only used when needed (such as a user uploading an item or altering a tag). Invoking different Lambda functions for different file formats helps you tailor actions across the workflow to your specific needs. Additionally, as a serverless service, Lambda helps offset the need to provision dedicated, idle compute resources. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Games that operate on a live service model or that rely on older assets that have already been commissioned require long-term archive of game assets that do not rely on on-premises storage. Amazon S3 offers multiple storage classes, including cost-optimized archival storage that are ideal for assets from older games that may still be needed at a later date. DynamoDB offers reserve capacity, which allows you to reserve database capacity for a one- or three-year term at a significant discount compared to provisioned capacity pricing. Reserve capacity can be cost-effective, especially if you anticipate a reduction in asset changes or uploads. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

You can choose the appropriate Amazon S3 storage tier to reduce the carbon impact of your workloads. For example, you can select an energy-efficient archival-class storage for infrequently access images or objects. Additionally, Lambda only consumes resources when invoked, helping you to not overprovision or waste compute power. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
