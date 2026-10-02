---
source_url: https://docs.aws.amazon.com/solutions/live-streaming-on-aws/index.html
---

---
title: 'Guidance for Live Streaming on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/live-streaming-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Live Streaming on AWS

## Overview

This Guidance demonstrates how to overcome the challenge of delivering consistent, high-quality live video streams globally by building resilient streaming infrastructure that automatically handles redundancy and multiple delivery formats. The system ingests live video feeds and processes them through parallel streams to ensure uninterrupted delivery, while automatically packaging content into multiple streaming formats optimized for different devices and viewing conditions, and includes a built-in demo player that allows teams to test and validate streaming performance before going live with viewers. You can deliver live video content to global audiences with minimal latency and maximum reliability, ensuring viewers receive smooth streaming experiences regardless of their location or device.

## Benefits

### Deliver resilient multi-format live streams

Ingest and transcode live feeds with built-in redundancy into adaptive bitrate HLS, DASH, and CMAF formats. Reach viewers across all devices while AWS manages the underlying media infrastructure.

### Distribute live content globally

Stream live events to worldwide audiences through CloudFront's content delivery network with low latency and high transfer speeds. Scale automatically to handle audience surges without capacity planning.

### Secure live streams with authorization

Protect premium content using CDN authorization that validates requests between MediaPackage and CloudFront with secure identifiers. Control access to ensure only authorized viewers can watch your live broadcasts.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/live-streaming-on-aws.pdf)

![Architecture diagram](/images/solutions/live-streaming-on-aws/images/live-streaming-on-aws-1.png)

1. **Step 1**: AWS Elemental MediaLive ingests the input feed and transcodes your content into two adaptive bitrate (ABR) HTTP Live Streaming (HLS) streams as output. Two feeds are ingested and processed in parallel by MediaLive redundancy.
1. **Step 2**: AWS Elemental MediaPackage ingests MediaLive ABR output and packages the live stream into HTTP Live Streaming (HLS), Dynamic Adaptive Streaming over HTTP (DASH) and Common Media Application Format (CMAF) formats that are delivered to three MediaPackage custom endpoints.
1. **Step 3**: An Amazon CloudFront distribution is configured to use the MediaPackage custom endpoints as its origin and includes a CDN Identifier custom HTTP header to authenticate requests. MediaPackage only fulfills playback requests that are authorized between MediaPackage and CloudFront using the CDN Identifier. This CDN Identifier is created as part of the CloudFormation deployment and securely stored in AWS Secrets Manager. For details, refer to the CDN Authorization in AWS Elemental MediaPackage guide.
1. **Step 4**: The CloudFront distribution delivers your live stream to viewers with low latency and high transfer speeds.
1. **Step 5**: A demo HTML preview player is available to help you test the solution. The player is a static website hosted in an Amazon Simple Storage Service (Amazon S3) bucket. Amazon CloudFront is used to restrict access to the solution's website bucket.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/media-entertainment/live-streaming-on-aws.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/live-streaming-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
