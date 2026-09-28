---
source_url: https://docs.aws.amazon.com/solutions/live-streaming-amazon-s3/index.html
---

---
title: 'Guidance for Live Streaming Amazon S3'
canonical_url: https://docs.aws.amazon.com/solutions/live-streaming-amazon-s3/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Live Streaming Amazon S3

## Overview

This Guidance shows how to address the challenge of delivering live video content reliably to global audiences by creating resilient streaming infrastructure that automatically scales with viewer demand. The system ingests live video feeds and transcodes them into optimized streaming formats, while storing encoded content in highly available storage that ensures uninterrupted playback, and global content delivery networks distribute streams with minimal buffering while providing detailed analytics through comprehensive logging capabilities. You can broadcast live events to worldwide audiences with consistent quality and performance, regardless of geographic location or concurrent viewer volume.

## Benefits

### Simplify live streaming infrastructure

Ingest and transcode live feeds directly to Amazon S3 using AWS Elemental MediaLive. Eliminate complex origin servers while leveraging S3's scalability and high availability for hosting video segments.

### Deliver global streams efficiently

Distribute adaptive bitrate HLS content through CloudFront's content delivery network with low latency and high transfer speeds. Reach viewers worldwide with consistent streaming quality regardless of location.

### Monitor streaming performance continuously

Capture CloudFront access logs automatically in Amazon S3 for comprehensive analysis. Gain insights into viewer behavior and troubleshoot delivery issues to optimize your streaming operations.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/live-streaming-amazon-s3.pdf)

![Architecture diagram](/images/solutions/live-streaming-amazon-s3/images/live-streaming-amazon-s3-1.png)

1. **Step 1**: AWS Elemental MediaLive ingests an input feed and transcodes your content into one adaptive bitrate (ABR) HTTP Live Streaming (HLS) stream as output.
1. **Step 2**: Amazon Simple Storage Service (Amazon S3) provides a scalable highly-available storage bucket to host the encoded segments.
1. **Step 3**: An Amazon CloudFront distribution is configured to use the Amazon S3 custom endpoints as its origin. The Amazon CloudFront distribution delivers your live stream to viewers with low latency and high transfer speeds.
1. **Step 4**: Store Amazon CloudFront Logs in Amazon S3.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/media-entertainment/live-streaming-on-aws-with-amazon-s3.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/live-streaming-on-aws-with-amazon-s3)

[Read usage guidelines](/solutions/guidance-disclaimers/)
