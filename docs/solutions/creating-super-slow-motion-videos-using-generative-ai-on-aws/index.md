---
source_url: https://docs.aws.amazon.com/solutions/creating-super-slow-motion-videos-using-generative-ai-on-aws/index.html
---

---
title: 'Guidance for Creating Super Slow-Motion Videos Using Generative AI on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/creating-super-slow-motion-videos-using-generative-ai-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Creating Super Slow-Motion Videos Using Generative AI on AWS

## Overview

This Guidance shows how to create super slow-motion videos by interpolating synthetic frames between real video frames. It uses generative artificial intelligence (AI) to generate new frames between two existing video frames, effectively slowing down the action while maintaining sharpness and detail. This approach can handle large motions between frames, making it well-suited for creating sports highlights or cinematic sequences. By combining the power of generative AI with the scalability and reliability of AWS services, this Guidance delivers a seamless and cost-effective way to unlock new creative possibilities and elevate your visual storytelling.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/creating-super-slow-motion-videos-using-generative-ai-on-aws.pdf)

![Architecture diagram](/images/solutions/creating-super-slow-motion-videos-using-generative-ai-on-aws/images/creating-super-slow-motion-videos-using-generative-ai-on-aws-1.png)

1. **Step 1**: A DevOps engineer calls an Amazon API Gateway endpoint to create a model endpoint.
1. **Step 2**: API Gateway invokes an AWS Lambda function to process the request.
1. **Step 3**: The Lambda function uploads model artifacts. In this case, the Frame Interpolation for Large Motion (FILM) model and the endpoint configuration are uploaded to an Amazon Simple Storage Service (Amazon S3) bucket, creating an endpoint.
1. **Step 4**: On endpoint creation, Amazon SageMaker creates an asynchronous inference endpoint with an autoscaling feature.
1. **Step 5**: The operator uploads a short video to an Amazon S3 bucket for processing.
1. **Step 6**: An Amazon S3 event invokes an AWS Step Functions state machine through Amazon EventBridge to process the request.
1. **Step 7**: A Lambda function extracts frames from the video and stores them in an Amazon S3 bucket.
1. **Step 8**: A Lambda function creates an inference job by invoking the SageMaker Asynchronous Inference endpoint, where the FILM model interpolates new frames. The state machine processing is paused and waits for a job completion status.
1. **Step 9**: The SageMaker Asynchronous Inference endpoint sends the job status to Amazon Simple Notification Service (Amazon SNS).
1. **Step 10**: The state machine processing job resumes, where a Lambda function encodes all new frames to create a slow motion video, storing the frames in an Amazon S3 bucket.
1. **Step 11**: An Amazon S3 event sends the status to Amazon SNS to notify the operator that the slow-motion video is complete.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses SageMaker Asynchronous Inference and Amazon CloudWatch to reduce operational overhead while also making it easier to maintain and troubleshoot the video processing pipeline. Specifically, SageMaker Asynchronous Inference allows users to process multiple requests in parallel, providing a scalable and fault-tolerant architecture with its built-in queuing mechanism. This ensures the efficient and reliable handling of large volumes of video processing requests. CloudWatch, on the other hand, collects metrics and logs from AWS services like Lambda, Step Functions, and SageMaker Asynchronous Inference endpoints, enabling visibility into performance, health, and utilization. This proactive monitoring and alerting capability facilitates timely identification and resolution of issues, optimizes resource utilization, and enables data-driven decision-making for improved operations and cost efficiency. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

API Gateway adds an essential security layer that supports robust authentication, authorization, and protection against common threats for secure and controlled access to the video processing pipeline. It provides built-in mechanisms for authenticating and authorizing API requests, allowing users to control access to their APIs using Amazon Cognito user pools, OAuth 2.0, or AWS Identity and Access Management (IAM) roles. From a data protection perspective, API Gateway ensures that data coming to the endpoint is SSL/TLS encrypted, safeguarding the confidentiality and integrity of the data in transit. Additionally, API Gateway supports API throttling, helping to protect the backend resources from excessive traffic or abuse, and mitigating the risk of distributed denial-of-service (DDoS) attacks. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

By combining the capabilities of API Gateway, Lambda, SageMaker Asynchronous Inference, and Step Functions, this Guidance is capable of handling varying workloads to support reliable video processing, even in the face of traffic spikes or other potential disruptions. API Gateway provides built-in fault tolerance and automatic scaling capabilities, enabling it to handle traffic spikes seamlessly. Its integration with Lambda and SageMaker simplifies the process of building highly scalable and reliable serverless APIs. Lambda offers automatic scaling and high availability, allowing code processing without concerns about the underlying infrastructure management, so video processing workloads can be processed reliably, even during periods of high demand. SageMaker and its managed features are designed to deliver high reliability and availability for running machine learning workloads, so that the generative AI models used for creating slow-motion videos are consistently available and reliable. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

SageMaker offers a high-performance, low-latency inference feature specifically designed for hosting and serving machine learning models efficiently. It also has the capability to fine-tune the deployment configuration based on specific workload characteristics, helping to achieve optimal performance efficiency without over-provisioning resources. Users can easily configure the instance type, count, and other deployment configurations to right-size their inference workloads. This flexibility allows for optimizing the video processing performance based on factors such as latency requirements, desired throughput, and cost considerations. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses serverless services that offer auto-scaling capabilities, allowing users to optimize their costs by paying only for the resources they consume. For example, SageMaker Asynchronous Inference supports auto-scaling down to zero instances when not in use, effectively eliminating compute costs during idle periods. Similarly, Lambda and Step Functions follow a serverless compute model, where users are charged only for the compute time consumed while their code is running. This pay-per-use pricing model eliminates the need for provisioning and maintaining compute resources that run continually, leading to significant cost savings, especially during periods of low or intermittent workloads. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The SageMaker Asynchronous Inference auto-scaling capability eliminates unnecessary compute resource consumption during idle periods. Additionally, Lambda and Step Functions follow a serverless compute model where resources are dynamically allocated based on demand, so no resources are wasted when not actively processing workloads. By using the auto-scaling and serverless nature of these services, this Guidance promotes resource sharing and reuse, reducing the overall compute workload required to run the slow-motion video processing workload. This efficient utilization of resources helps minimize the environmental impact associated with running compute workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
