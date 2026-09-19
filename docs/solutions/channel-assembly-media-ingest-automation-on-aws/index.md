---
source_url: https://docs.aws.amazon.com/solutions/channel-assembly-media-ingest-automation-on-aws/index.html
---

---
title: 'Guidance for Channel Assembly Media Ingest Automation on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/channel-assembly-media-ingest-automation-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Channel Assembly Media Ingest Automation on AWS

## Overview

This Guidance demonstrates how to prepare mezzanine video files and make them available for scheduling using the channel assembly capability of AWS Elemental MediaTailor. It automates the process of transcoding video files using AWS Elemental MediaConvert, packaging the files into various formats using AWS Elemental MediaPackage, and applying personalized ad insertions to the files. Additionally, an Amazon CloudFront distribution is created as a content delivery network (CDN) that orchestrates the delivery of the files and the details about how to track and manage the content for delivery. The CDN hosts the video streams with security and performance best practices at the forefront.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/channel-assembly-media-ingest-automation-on-aws.pdf)

![Architecture diagram](/images/solutions/channel-assembly-media-ingest-automation-on-aws/images/channel-assembly-media-ingest-automation-on-aws-1.png)

1. **Step 1**: Assets uploaded to Amazon Simple Storage Service (Amazon S3) invokes an AWS Elemental MediaConvert job to process multi-bitrate HTTP Live Streaming (HLS) output.
1. **Step 2**: MediaConvert stores processed assets to an Amazon S3 bucket.
1. **Step 3**: AWS Elemental MediaPackage stores HLS asset as HLS, Dynamic Adaptive Streaming over HTTP (DASH), and Common Media Application Format (CMAF) outputs.
1. **Step 4**: AWS Elemental MediaTailor creates a VOD source and a program in your sample channel.
1. **Step 5**: MediaTailor generates monetized livestreams by interacting with an ad decision server (ADS) and channel.
1. **Step 6**: Amazon CloudFront caches media segments.
1. **Step 7**: Viewers request stream from CloudFront.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

All resources created in this Guidance are tagged, which helps you identify and organize your AWS resources, as well as easily track your AWS costs. If you need to integrate and deploy changes in this Guidance, use an AWS Serverless Application Model (AWS SAM). [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All content at rest is protected by AWS Signature Version 4, and can only be viewed through the CloudFront content delivery network (CDN). You can also configure further access controls at the CDN to secure people and machine access. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

All components in this Guidance are serverless and therefore highly available in any given AWS Region, helping to ensure you are implementing a highly available architecture. The workflow processing steps, as outlined in the preceding diagram, are decoupled and use Amazon EventBridge and stateless AWS Lambda, while retry logic is controlled by you. The workflow steps also emit logs to Amazon CloudWatch, in addition to emails sent through Amazon Simple Queue Service (Amazon SQS) for notifications on content state changes. This Guidance scales up and down with demand, limited only by the underlying service limits of MediaConvert, MediaPackage, and MediaTailor. The versions of this Guidance are controlled through GitLab, with any changes run through integration tests first. And by relying on the underlying services Amazon S3, MediaConvert, MediaPackage, and MediaTailor for failure handling, this Guidance helps to ensure you are implementing a solution resilient to failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services selected for this Guidance were purpose-built for this use, and the components are appropriately sized to help meet your performance requirements. If you want to experiment with this Guidance, you can automate the creation of media resources and channels to determine performance limits. This Guidance can be deployed in any Region that has AWS Elemental services, including MediaConvert, MediaPackage, and MediaTailor. And because the workflow processing steps are decoupled, appropriate queuing helps ensure a large influx of demand is appropriately staggered. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

We evaluated cost and each component in this Guidance have been rightsized for the optimal balance between cost and perceptual quality. Also, there are no idle running costs. Cost is only incurred when and if media is processed and a channel is running. Finally, the relationship between viewer load and infrastructure is separated by CloudFront, so there is no increase in resources when load increases. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance scales to continually match the load with only the minimum resources. There is zero idle compute when a channel is not running. And by deploying the minimum set of resources required for a high-quality consumer experience, there are no idle resources running when not in use. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
