---
source_url: https://docs.aws.amazon.com/solutions/asynchronous-image-generation-with-stable-diffusion-on-aws/index.html
---

---
title: 'Guidance for Asynchronous Image Generation with Stable Diffusion on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/asynchronous-image-generation-with-stable-diffusion-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Asynchronous Image Generation with Stable Diffusion on AWS

Use open source tools and generative AI for asynchronous image generation

## Overview

This Guidance helps you implement a scalable and low-cost Stable Diffusion (SD) web user interface (UI) inference architecture on AWS. SD is a popular open source project for generating images using generative AI. This Guidance shows how to use serverless and container services to build and deploy an end-to-end, low-cost, and asynchronous image generation architecture.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/asynchronous-image-generation-with-stable-diffusion-on-aws.pdf)

![Architecture diagram](/images/solutions/asynchronous-image-generation-with-stable-diffusion-on-aws/images/asynchronous-image-generation-with-stable-diffusion-on-aws-1.png)

1. **Step 1**: User or application sends a prompt to Amazon API Gateway that acts as an endpoint for overall Guidance, including authentication. AWS Lambda validates the requests, publishes the requests to the designated Amazon Simple Notification Service (Amazon SNS) topic, and immediately returns a response.
1. **Step 2**: Amazon SNS publishes the message to Amazon Simple Queue Service (Amazon SQS) queues. Each message contains a Stable Diffusion (SD) runtime name attribute and will be delivered to the queues with matching SD Runtime names.
1. **Step 3**: In the Amazon Elastic Kubernetes Service (Amazon EKS) cluster, the previously deployed open source Kubernetes Event Driven Auto-Scaler (KEDA) scales up new pods to process the incoming messages from Amazon SQS queues (such as queue 1, queue 2).
1. **Step 4**: In the Amazon EKS cluster, the previously deployed open source Kubernetes compute auto-scaler, Karpenter, launches new compute nodes based on Amazon Elastic Compute Cloud (Amazon EC2) GPU instances (such as g4, g5, and p4) to schedule pending pods. The instances use pre-cached SD Runtime images and are based on Bottlerocket OS for faster boot. The instances can be launched using On-Demand or Spot pricing models.
1. **Step 5**: Stable Diffusion Runtimes load machine learning (ML) inference model files from an Amazon Simple Storage Service (Amazon S3) bucket through the Mountpoint for Amazon S3 CSI Driver upon runtime initialization or on-demand.
1. **Step 6**: Queue agents (a software component created for this Guidance) receive messages from SQS processing queues and converts them to inputs for SD Runtime API calls.
1. **Step 7**: Queue agents call SD Runtime APIs, receive and decode responses, and save the generated images to designated Amazon S3 buckets.
1. **Step 8**: Queue agents send notifications to the designated SNS topic. The user receives notifications from the SNS topic and can render images.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment.The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open implementation guide](https://github.com/aws-solutions-library-samples/guidance-for-asynchronous-inference-with-stable-diffusion-webui-on-aws/blob/main/README.md#deployment-documentation)
[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-asynchronous-inference-with-stable-diffusion-webui-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS X-Ray traces a request from API Gateway to Lambda, Amazon SNS, Amazon SQS, Amazon EKS pods, and all the way to Amazon S3. This allows users to quickly troubleshoot requests. Additionally, X-Ray provides a service map that allows the user to identify the current system status with one glance. AWS Distro for OpenTelemetry collects metrics from the EKS cluster and sends them to Amazon CloudWatch. Distro for OpenTelemetry and CloudWatch help you obtain critical metrics and receive automatic alerts when metrics exceed thresholds. CloudWatch Container Insights helps to visualize those metrics. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) provides access control for API Gateway, Lambda, Amazon SNS, Amazon SQS, and Amazon S3. IAM Roles for Service Accounts (IRSA) on EKS clusters provides fine-grained access control for pods running inside the EKS cluster. IAM and IRSA on EKS clusters enforce role-based access control and limit unauthorized access to resources. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

All the services in this Guidance are regional services with built-in high availability and fault tolerance against Availability Zone failure. In addition to the high availability of each individual service, this Guidance uses a loosely-coupled microservices architecture. Additionally, Amazon S3 and Amazon EFS provide highly reliable storage service to support uptime. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon EKS provides flexible container scheduling and scalability. KEDA is an event-driven pod auto-scaler for Kubernetes. Karpenter simplifies Kubernetes infrastructure and automatically launches the right amount of compute resources to handle the cluster's applications. Combined with KEDA and Karpenter, Amazon EKS can scale up a new node in less than one minute. Bottlerocket is a container-optimized operating system and has a shorter start up time than Amazon Linux 2. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Spot instances offer a lower price than on-demand instances. Stable Diffusion Web UI in Amazon EKS requires GPU instances for inference, and using Spot instances could save up to 70% on costs. Because SQS queues store the inference tasks, you won’t lose data in the event of spot interruption. Additionally, Amazon Elastic Container Service (Amazon ECS) on Fargate provides serverless infrastructure for running containerized applications. Amazon EKS provides a cost-efficient way to deploy, run, and manage containers through standard APIs. Amazon ECS on Fargate and Amazon EKS provide container orchestration with configurable infrastructure options to optimize costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda automatically scales based on requests and does not charge for idle infrastructure. This reduces the compute usage for the frontend API. Karpenter has a container workload consolidation feature that periodically checks if the current workloads can be consolidated onto existing EKS compute nodes with a lesser resource footprint, which helps to reduce idle resources. Amazon ECS on Fargate provides a serverless infrastructure option to run containers with a minimal resource footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
