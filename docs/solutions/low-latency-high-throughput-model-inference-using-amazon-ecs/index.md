---
source_url: https://docs.aws.amazon.com/solutions/low-latency-high-throughput-model-inference-using-amazon-ecs/index.html
---

---
title: 'Guidance for Low-Latency High-Throughput Model Inference Using Amazon ECS'
canonical_url: https://docs.aws.amazon.com/solutions/low-latency-high-throughput-model-inference-using-amazon-ecs/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Low-Latency High-Throughput Model Inference Using Amazon ECS

## Overview

This Guidance demonstrates how to build a real-time machine learning (ML) inferencing solution on AWS that can serve millions of requests per second. By hosting your solution’s ML model on Amazon Elastic Container Service (Amazon ECS) and routing requests to the ML server using Network Load Balancer, you can achieve low latency and support high-throughput inference requirements commonly found in real-time and programmatic advertising. This Guidance provides an example of applying ML for ad request filtering and demonstrates how to build a client application that can simulate high-throughput OpenRTB-based requests to send to the ML inference server.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/low-latency-high-throughput-model-inference-using-amazon-ecs.pdf)

![Architecture diagram](/images/solutions/low-latency-high-throughput-model-inference-using-amazon-ecs/images/low-latency-high-throughput-model-inference-using-amazon-ecs-1.png)

1. **Step A**: Data scientists use Amazon SageMaker to experiment with, build, and train their ML model. Once the model is ready, it is saved in Amazon Simple Storage Service (Amazon S3).
1. **Step B**: The trained model is read and loaded by the Amazon Elastic Container Service (Amazon ECS) model inference task. The model is hosted as a Thrift endpoint. Incoming requests, in OpenRTB format (for real-time bidding), are used for inference.
1. **Step 1**: A publisher issues requests to a supply-side platform (SSP) auction server for an ad placement.
1. **Step 2**: The auction server (a client application) is hosted as an Amazon ECS application within the SSP's virtual private cloud (VPC). The auction request issues a bid request based on the OpenRTB format.
1. **Step 3**: Network Load Balancer distributes the incoming requests to an Amazon Elastic Compute Cloud (Amazon EC2)-based Amazon ECS cluster that hosts the ad-filtering ML server. The purpose of the ad-filtering ML server is to infer the likelihood of a bid for every bid request, filtering the demand partners that need to be sent to the auction request, and optimizing the cost per bid.
1. **Step 4**: The ad-filtering ML server is hosted as a container within an Amazon EC2-based Amazon ECS cluster. An Amazon EC2 Auto Scaling group maintains the desired number of Amazon EC2 instances running across multiple Availability Zones (AZs) to maintain high availability. Amazon ECS deploys and maintains the desired capacity of the Amazon ECS tasks, hosting the ML container. Each task loads the ad-filtering model from an Amazon S3 bucket and hosts it as a Thrift protocol-based endpoint. This helps in low-latency-based communication, and multiple instances of the tasks support a high number of concurrent requests.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch monitors the performance of the Amazon ECS cluster (including CPU and memory) along with the incoming requests sent through Network Load Balancer. Your CloudWatch dashboard—created as part of an AWS CloudFormation script—provides a comprehensive view of the number of incoming requests and their associated latency. By using CloudWatch to visualize and analyze performance and latency, you can better identify any bottlenecks in your application. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

By scoping down all AWS Identity and Access Management (IAM) policies to the minimum permissions required for the services to function properly, you can limit unauthorized access to resources. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The Amazon ECS cluster runs a service definition that maintains a desired capacity of EC2 instances. If one of the instances becomes unavailable, a new instance will automatically launch and be registered with the Amazon ECS cluster as a healthy target to receive incoming requests routed by Network Load Balancer. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Network Load Balancer, which communicates with Amazon ECS, supports low-millisecond latency and high throughput that are apt for this use case. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon EC2 Auto Scaling groups let you run your application at the desired capacity while providing dynamic support for scaling based on the load. Automatic scaling grows or reduces the infrastructure based on load and your scaling policy. This helps you control the costs associated with running your application. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The Amazon EC2 -based Amazon ECS cluster lets you choose appropriate hardware types and configurations for specific workloads so that they run efficiently. As a result, you can maximize utilization and avoid overprovisioning resources. This Guidance is designed for low-latency and high-performance model inference workloads, so appropriate EC2 instance types are powered by AWS Graviton3. This service uses up to 60 percent less energy for the same performance as comparable EC2 instances, helping you reduce your carbon footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
