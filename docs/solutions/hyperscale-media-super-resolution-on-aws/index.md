---
source_url: https://docs.aws.amazon.com/solutions/hyperscale-media-super-resolution-on-aws/index.html
---

---
title: 'Guidance for Media Super Resolution on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/hyperscale-media-super-resolution-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Media Super Resolution on AWS

Machine learning powers video resolution upscaling

## Overview

This Guidance demonstrates how to use a type of artificial intelligence (AI) called "generative AI" to convert videos from low-resolution into high-definition. Many media companies have extensive archives of older video content originally encoded in now outdated lower resolutions, like standard definition. Modern display technology can now support sharper ultra-high-definition formats like 4K resolution. However, manually remastering expansive archives is extremely labor-intensive. You can configure this Guidance to solve that challenge; it uses generative AI that can magnify and extrapolate missing details in low-quality videos to increase the resolution. This prepares even grainy, dated footage for today's high-resolution screens and 4K television standards that consumers now expect when watching content.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/hyperscale-media-super-resolution-on-aws.pdf)

![Architecture diagram](/images/solutions/hyperscale-media-super-resolution-on-aws/images/hyperscale-media-super-resolution-on-aws-1.png)

1. **Step 1**: The user accesses the application, hosted on AWS Fargate, through an Amazon CloudFront distribution that is in front of an Application Load Balancer (ALB). ALB redirects the user to Amazon Cognito for authentication for a new user session.
1. **Step 2**: A task is registered in the task tracker table in Amazon DynamoDB for the user. This task tracking helps secure access to upscaled videos by associating pipeline tasks with the user who owns them.
1. **Step 3**: App containers use the AWS Systems Manager Run Command to run scripts on the head node to allocate new tasks and get the status of tasks.
1. **Step 4**: The user uploads or views upscaled video directly from Amazon Simple Storage Service (Amazon S3). This is done by requesting presigned URLs for uploading and downloading from the Fargate container that is hosting the app.
1. **Step 5**: An AWS Lambda function is invoked upon a successful Amazon S3 upload. This initiates a video upscaling workflow, which invokes a Systems Manager Run Command. A video upscaling pipeline is run by submitting the task into the Slurm job queue in AWS ParallelCluster.
1. **Step 6**: A scheduled task in ParallelCluster extracts video frames and writes images. It also extracts audio and media metadata, such as bitrate and frames per second (fps), into the shared Amazon FSx for Lustre file system for artificial intelligence (AI) super resolution tasks. The file system is encrypted with a key provided by AWS Key Management System (AWS KMS). The cluster automatically scales the central processing unit (CPU) compute fleet for video frame processing tasks.
1. **Step 7**: ParallelCluster performs AI upscaling on each frame. It does this by invoking a generative AI model (RealESRGan and SwinIR2) through an Amazon SageMaker endpoint hosted in the Graphics Processing Unit (GPU) compute fleet. The output is written to the FSx for Lustre file system. The cluster automatically scales the GPU compute fleet for video upscaling tasks.
1. **Step 8**: A ParallelCluster batch job encodes image frames to create new video content and uploads it to a given Amazon S3 location. An Amazon S3 presigned URL is created on-demand if an authorized user requests it.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance complements your operational needs through end-to-end visibility and scalable automation across the video upscaling pipeline. For example, Amazon CloudWatch metrics and DynamoDB task tracking provide process oversight to monitor performance, help you identify issues, and troubleshoot root causes. Lambda facilitates automated, zero-downtime deployments, so infrastructure updates happen seamlessly without manual overhead. Additionally, ParallelCluster automates consistent infrastructure provisioning across environments using infrastructure as code (IaC) for simplified change control. And lastly, Amazon Elastic Container Registry (Amazon ECR) centralizes machine learning (ML) model containers for easy large-scale inference deployments using a unified script. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Robust security protections span the entire workflow while simplifying access control. Input and output Amazon S3 buckets use presigned URLs or AWS Identity and Access Management (IAM) roles to grant temporary access, keeping data locked down. Authenticated users connect through Amazon Cognito to the private ALB. ParallelCluster seals ML inferencing within an isolated VPC, reachable only through Systems Manager. Also, administrators can restrict access to the FSx for Lustre file system with VPC security groups, and the data can be encrypted through AWS KMS. Lastly, AWS CloudTrail centralizes activity logging for audit visibility. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The serverless frontend architecture provided by Elastic Load Balancing (ELB), Fargate, and DynamoDB provides high availability within a Region. In addition, you can deploy the transcoding and ML compute nodes across multiple Availability Zones (AZs) in a highly available manner. You can also deploy the Slurm controllers in a primary or secondary model across multiple AZs for resilience against failures. The FSx for Lustre file system stores data in cost-optimized storage for short-term, process-heavy workloads, such as transcoding. However, the source and final material are stored in Amazon S3 for high durability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance achieves scalable performance efficiency by using ParallelCluster, which auto-scales GPU resources to match dynamic batch processing needs, avoiding overprovisioning costs. Just-in-time job placement further optimizes infrastructure utility by intelligently assigning video workflows across the heterogeneous cluster. Lambda functions scale the invocation count for video frame extractions, while provisioned concurrency guarantees low-latency responses. Finally, using a shared FSx for Lustre file system across the cluster provides low-latency with read and/or write access for individual video frames. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The event-driven architecture behind this Guidance means that compute and network resources are consumed only when needed. Additionally, Lambda only bills by the millisecond of processing time, while ParallerCluster compute nodes can be configured to reduce capacity to zero when there are no jobs in the queue, saving you compute costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Achieving sustainability requires optimizing resources and infrastructure. The ParallelCluster Slurm scheduler enables intelligent job placement matching specific workload needs. Video extraction and transcoding tasks are efficiently assigned to cost-effective CPU nodes, while GPU fleets are reserved just for compute-intensive upscaling. This minimizes over-provisioned resources, speeds time to output, and lowers energy demands. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
