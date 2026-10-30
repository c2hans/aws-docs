---
source_url: https://docs.aws.amazon.com/solutions/advertising-sponsorship-measurement-on-aws/index.html
---

---
title: 'Guidance for Advertising Sponsorship Measurement on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/advertising-sponsorship-measurement-on-aws/
source: aws-documentation
generated_on: 2026-10-29
---

# Guidance for Advertising Sponsorship Measurement on AWS

## Overview

This Guidance shows how media and entertainment organizations can measure advertising sponsorship value in live broadcast video using AWS AI services. Media analysts upload footage through a web portal, and an automated pipeline detects sponsor logos, on-screen text, and spoken brand mentions across both in-media and in-venue placements. The solution combines foundation models with speech-to-text analysis to compute brand screen time, Share of Voice, and placement metrics, then presents results through interactive dashboards. By replacing manual review with scalable, serverless processing, you gain consistent, data-driven measurement of sponsorship exposure and free your teams to focus on insights rather than frame-by-frame inspection.

## Benefits

### Automate sponsorship measurement at scale

Replace manual, frame-by-frame review with an automated pipeline that segments broadcast video and detects sponsor brands across full-length footage. Serverless processing scales to handle concurrent video workloads, so your team measures far more content in less time.

### Quantify brand exposure precisely

Generate frame-level brand detections, screen-time totals, and Share of Voice metrics that combine on-screen logo and text recognition with spoken brand mentions. You get consistent, data-driven sponsorship valuations across both in-media and in-venue placements instead of subjective manual estimates.

### Protect content with built-in controls

Safeguard uploaded broadcast footage and analytics with user authentication and encryption at rest applied across every stage of the pipeline. Managed, serverless components reduce operational overhead so you can run sponsorship analysis securely without maintaining dedicated processing infrastructure.

## How it works

This architecture diagram illustrates how to build and operate Advertising Sponsorship Measurement on AWS. It shows the key components and their interactions. [Download the architecture diagram](downloads/advertising-sponsorship-measurement.pdf)

![Architecture diagram for Advertising Sponsorship Measurement](/images/solutions/advertising-sponsorship-measurement-on-aws/images/advertising-sponsorship-measurement.png)

1. **Step 1**: Amazon CloudFront and Amazon Simple Storage Service (Amazon S3) serve the React.js web portal to a media analyst.
1. **Step 2**: Amazon Cognito authenticates users.
1. **Step 3**: Amazon API Gateway exposes the REST APIs backed by AWS Lambda.
1. **Step 4**: Amazon S3 receives uploaded video via the UI or API and encrypts it at rest using AWS Key Management Service (AWS KMS) keys. On upload completion, the API creates a video processing job that triggers an AWS Step Functions per-video processing pipeline.
1. **Step 5**: An Amazon Elastic Container Service (Amazon ECS) task on AWS Fargate splits the video into segments. Fargate provides automatic scaling to handle concurrent video processing workloads.
1. **Step 6**: Amazon Bedrock Data Automation detects logos/OCR text. Amazon Transcribe generates transcripts from audio in parallel.
1. **Step 7**: The “brand filter” AWS Lambda function filters OCR and transcript text for brand names using an Anthropic Claude Sonnet model on Amazon Bedrock.
1. **Step 8**: The “frame analyzer” Amazon ECS task runs video-frame-level brand detection using an Anthropic Claude Sonnet model on Amazon Bedrock.
1. **Step 9**: The “aggregator” AWS Lambda aggregates screen time, Share of Voice, and brand placement information.
1. **Step 10**: Amazon DynamoDB stores job status and metrics. Amazon S3 stores detection summaries, and Amazon S3 Tables (Apache Iceberg) stores analytics data. AWS KMS keys encrypt all data at rest.
1. **Step 11**: AWS Glue catalogs the analytics data. Amazon Athena provides the data lake query interface. The web portal embeds Amazon Quick to deliver a hybrid visual and agentic AI analytics experience.
[Read usage guidelines](/solutions/guidance-disclaimers/)
