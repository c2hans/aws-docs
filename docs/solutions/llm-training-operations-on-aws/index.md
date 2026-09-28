---
source_url: https://docs.aws.amazon.com/solutions/llm-training-operations-on-aws/index.html
---

---
title: 'Guidance for LLM Training Operations on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/llm-training-operations-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for LLM Training Operations on AWS

## Overview

This Guidance demonstrates how to establish a robust pre-flight testing and monitoring system for enterprise LLM training operations. It helps organizations overcome common challenges in large-scale machine learning deployments by implementing comprehensive validation across hardware, network, and monitoring layers. By systematically verifying GPU health, memory systems, and network interconnects, the solution ensures optimal resource utilization and minimizes costly training interruptions. This structured approach is particularly valuable for global enterprises seeking to enhance operational reliability and efficiency in their distributed computing environments.

## Benefits

### Prevent costly ML training interruptions

Automate comprehensive pre-flight validation of GPU health, drivers, and infrastructure configurations before initiating expensive LLM training workloads. Reduce the risk of mid-training failures and resource waste.

### Optimize ML infrastructure performance

Monitor critical metrics across CPU, memory, GPU, and network resources in real-time. Receive instant notifications when performance thresholds are exceeded, enabling rapid response to training issues.

### Streamline LLM operations management

Deploy a ready-to-use monitoring framework with customizable thresholds using infrastructure as code. Focus on model development while automated checks ensure infrastructure reliability.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/llm-training-operations-on-aws.pdf)

![Architecture diagram](/images/solutions/llm-training-operations-on-aws/images/llm-training-operations-on-aws-1.png)

1. **Step 1**: Administrator deploys AWS CloudFormation template with custom settings for CPU, memory, and disk thresholds, along with email address for Amazon Simple Notification Services (SNS) Topics notifications
1. **Step 2**: AWS CloudFormation template creates Amazon EC2 instances and executes pre-flight checks validating GPU health, CUDA drivers, NCCL testing, EFA connectivity, and CPU/memory/disk performance, while configuring security groups, permissions, CloudWatch agent, and notification channels
1. **Step 3**: Amazon SNS topic sends a notifications for any failed pre-flight checks to administrator with specific failure details
1. **Step 4**: User Initiates the LLM training job by invoking the Amazon Lambda Input function for fetching the training data stored in Amazon S3
1. **Step 5**: Amazon EC2 instances loads data from Amazon S3 bucket and runs the LLM training process
1. **Step 6**: Monitor system health continuously through Amazon CloudWatch by tracking real-time CPU usage against defined thresholds, memory consumption, disk space utilization and I/O performance, network throughput and connectivity status, plus GPU utilization and temperature for ML workloads
1. **Step 7**: Send runtime monitoring alerts through Amazon SNS when operational thresholds are exceeded during training, including specific triggering metrics and current system status in each notification
1. **Step 8**: Amazon Lambda Storage Function stores the queryable training metadata in the Amazon DynamoDB
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-llm-training-operations-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
