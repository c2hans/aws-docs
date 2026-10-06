---
source_url: https://docs.aws.amazon.com/solutions/video-on-demand-on-aws/index.html
---

---
title: 'Guidance for Video on Demand on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/video-on-demand-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Video on Demand on AWS

## Overview

This Guidance demonstrates how to address the challenge of managing complex video processing workflows at scale by providing orchestrated automation that handles everything from ingestion to delivery with customizable options for different business needs. The system automatically manages the entire video lifecycle through coordinated workflows that transcode content into multiple formats optimized for different devices, while storing all processing metadata for easy tracking and downstream integration, and includes optional features such as automated archiving to reduce storage costs and advanced packaging capabilities that enable digital rights management and multi-format streaming. You can streamline video operations from upload to viewer delivery while maintaining full control over processing options, storage costs, and content protection requirements.

## Benefits

### Orchestrate scalable video workflows

Automate ingest, transcoding, and publishing with Step Functions coordinating Lambda functions and MediaConvert. Process video content efficiently while maintaining workflow metadata and error handling throughout the pipeline.

### Optimize storage costs automatically

Store source media in Amazon S3 with lifecycle policies that transition content to S3 Glacier for long-term archival. Reduce storage expenses while maintaining access to your complete video library.

### Deliver multi-device video experiences

Transcode videos into HLS and DASH formats for playback across all devices and platforms. Distribute content globally through CloudFront to ensure consistent viewing quality for your audiences.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/video-on-demand-on-aws.pdf)

![Architecture diagram](/images/solutions/video-on-demand-on-aws/images/video-on-demand-on-aws-1.png)

1. **Step 1**: Store source media files in an Amazon Simple Storage Service (Amazon S3) bucket. Content is eventually transitioned to Amazon S3 Glacier following an Amazon S3 lifecycle policy.
1. **Step 2**: AWS Step Functions state machines orchestrate ingest, processing, and publishing workflows.
1. **Step 3**: AWS Elemental MediaConvert transcodes media files from their source format into popular distribution formats such as HLS and DASH.
1. **Step 4**: A collection of AWS Lambda functions perform the work of each step, and process error messages.
1. **Step 5**: Store metadata captured through the workflow in Amazon DynamoDB.
1. **Step 6**: Amazon CloudWatch is used for logging and Amazon CloudWatch Events rules for AWS Elemental MediaConvert notifications.
1. **Step 7**: Amazon Simple Notification Service (Amazon SNS) topics publish encoding, publishing, and error notifications.
1. **Step 8**: AWS Elemental MediaPackage (optional) creates video streams formatted to play on several devices from a single video input.
1. **Step 9**: Amazon S3 bucket stores distribution media files.
1. **Step 10**: Amazon CloudFront distribution delivers video content to end users.
1. **Step 11**: An Amazon Simple Queue Service (Amazon SQS) queue captures the workflow outputs.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/media-entertainment/video-on-demand-on-aws.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/video-on-demand-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
