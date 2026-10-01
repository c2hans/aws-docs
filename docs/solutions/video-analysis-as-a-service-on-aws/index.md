---
source_url: https://docs.aws.amazon.com/solutions/video-analysis-as-a-service-on-aws/index.html
---

---
title: 'Guidance for Video Analysis as a Service on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/video-analysis-as-a-service-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Video Analysis as a Service on AWS

Implement intelligent video analytics for optimized insights from video assets

## Overview

This Guidance demonstrates how to implement a scalable video analysis as a service solution on AWS, providing you with powerful tools to manage and analyze video data from large IoT device fleets. It enables real-time event processing and intelligent video analysis, allowing you to derive actionable insights from video data quickly. The user-friendly interface provides administrators with a centralized dashboard for monitoring events, accessing video footage, and performing advanced searches across their entire fleet. With this Guidance, you can enhance security, improve operational visibility, and make data-driven decisions based on their video assets.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/video-analysis-as-a-service-on-aws.pdf)

![Architecture diagram](/images/solutions/video-analysis-as-a-service-on-aws/images/video-analysis-as-a-service-on-aws-1.png)

1. **Step 1**: The admin user registers a new IoT thing through Amazon API Gateway. A state machine controls different states of device registration, allowing for asynchronous registration. Additional device configurations and preferences are stored as an IoT shadow. The IoT thing is registered on AWS IoT Core.
1. **Step 2**: The IoT thing connects to AWS IoT Core using MQTT. The device finishes provisioning and downloads configurations and forwarding rules.
1. **Step 3**: The IoT thing applies configurations—forwarding rules based on AI events—and creates MQTT subscriptions for updates and actions.
1. **Step 4**: When an event occurs, the IoT thing sends the event's metadata and thumbnail to AWS IoT Core and video streams to Amazon Kinesis Video Streams.
1. **Step 5**: An AWS Step Functions workflow processes, indexes, and organizes events and video streams. The workflow invokes an AWS Lambda function and persists the information on Amazon OpenSearch Service.
1. **Step 6**: The ops user accesses event timelines, video footage, and advanced event search across multiple devices in a fleet using an AWS Amplify UI and API Gateway.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/ai-ml/video-analysis-as-a-service-on-aws/index.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-video-analysis-as-a-service-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

API Gateway, Lambda, and Step Functions work together to provide comprehensive tracing and visualization of asynchronous API components, allowing you to analyze requests as they travel through the system. This integration helps in troubleshooting errors and monitoring latency issues effectively. By utilizing these services, you can gain valuable insights into your operations, automate changes, respond to events efficiently, and continuously improve processes and procedures. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) policies are scoped down to minimal required permissions, enhancing access control. The edge process uses AWS IoT Core Credential Provider to obtain new temporary credentials every six hours, improving credential management. These services help you protect data confidentiality and integrity, manage user permissions effectively, and establish controls to detect security events. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda enhances system reliability through a robust serverless architecture, automatic scaling capabilities, built-in fault-tolerance mechanisms, and multi-Availability Zone redundancy for consistent system performance. The serverless architecture of Lambda eliminates traditional infrastructure management concerns, helping ensure reliable performance across diverse workloads. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda provides dynamic scaling capabilities to eliminate idle capacity and optimize resource allocation. DynamoDB tables and Kinesis Data Streams operate in on-demand mode, automatically scaling to accommodate workloads without capacity planning. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Data retention policies are set to 90 days for Kinesis Video Streams, 7 days for Kinesis Data Streams, and 30 days for OpenSearch Service (with data moving from hot to warm state after 30 minutes). This helps you avoid unnecessary costs associated with storing irrelevant data. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The serverless architecture of Lambda optimizes resource usage and reduces energy consumption through automatic scaling, while Kinesis Video Data Streams, OpenSearch Service, and Amazon S3 data retention policies reduce storage requirements. By optimizing infrastructure sharing, automating resource management, and enforcing data lifecycle policies, you can minimize overall resources required for your workload. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
