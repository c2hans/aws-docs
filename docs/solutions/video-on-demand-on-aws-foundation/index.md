---
source_url: https://docs.aws.amazon.com/solutions/video-on-demand-on-aws-foundation/index.html
---

---
title: 'Guidance for Video on Demand on AWS Foundation'
canonical_url: https://docs.aws.amazon.com/solutions/video-on-demand-on-aws-foundation/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Video on Demand on AWS Foundation

## Overview

This Guidance demonstrates how to address the challenge of delivering video content at scale by automatically provisioning services that ingest, process, and distribute video files globally. The process begins when video files are uploaded to storage, triggering automatic transcoding into multiple formats optimized for different devices and connection speeds, while CloudWatch monitors the encoding progress and notifications keep teams informed of job completion status. You can deliver high-quality video content to viewers worldwide with reduced latency and improved streaming performance.

## Benefits

### Accelerate video content delivery globally

Deploy serverless transcoding workflows that automatically convert videos to adaptive bitrate formats and distribute them worldwide through CloudFront. Reduce time-to-market while AWS manages the underlying infrastructure.

### Scale video processing effortlessly

Handle variable workloads with automated, event-driven transcoding that scales on demand. Pay only for the video processing you use without managing servers or capacity planning.

### Ensure reliable streaming experiences

Deliver high-quality adaptive bitrate video that automatically adjusts to viewer bandwidth conditions. Monitor encoding jobs in near real-time and receive notifications when processing completes.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/video-on-demand-on-aws-foundation.pdf)

![Architecture diagram](/images/solutions/video-on-demand-on-aws-foundation/images/video-on-demand-on-aws-foundation-1.png)

1. **Step 1**: Store source video files and transcode job settings in an Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 2**: Upload a video file to trigger an AWS Lambda function to submit a transcode job to AWS Elemental MediaConvert.
1. **Step 3**: AWS Elemental MediaConvert transcodes the video into HLS adaptive bitrate files.
1. **Step 4**: Amazon CloudWatch tracks encoding jobs in MediaConvert and invokes the Lambda complete function.
1. **Step 5**: An AWS Lambda function processes the output status of each encoding job. Amazon Simple Notification Service (Amazon SNS) publishes notifications of completed jobs.
1. **Step 6**: A destination Amazon S3 bucket stores the transcoded video outputs from AWS Elemental MediaConvert.
1. **Step 7**: Amazon CloudFront is configured with the destination Amazon S3 bucket as the origin for global distribution of the transcoded video content.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/media-entertainment/video-on-demand-on-aws-foundation.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/video-on-demand-on-aws-foundation)

[Read usage guidelines](/solutions/guidance-disclaimers/)
