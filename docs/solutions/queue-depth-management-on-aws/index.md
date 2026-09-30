---
source_url: https://docs.aws.amazon.com/solutions/queue-depth-management-on-aws/index.html
---

---
title: 'Guidance for Queue Depth Management on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/queue-depth-management-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Queue Depth Management on AWS

## Overview

<p>This Guidance for queue depth management shows how you can improve customer experience by monitoring queues using cameras, use computer vision to measure queue depth, and provide alerts about bottlenecks and unreasonable queue depths to customer service managers. Travel & Hospitality organizations can apply this solution to improve employee productivity, streamline lobby management, gain customer insights, reduce walkaways and negative perceptions of wait times.</p>

## How it works

Monitor the passenger and guest queues using cameras, use computer vision to measure queue depth, and provide alerts about bottlenecks and unreasonable queue depths to customer service managers, improving the traveler experience.

[Download the architecture diagram](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/guidance-for-queue-depth-management-ra.pdf)

![Architecture diagram](/images/solutions/queue-depth-management-on-aws/images/queue-depth-management-on-aws-1.png)

1. **Step 1**: Cameras are placed in important airport or hotel areas to improve customer waiting times.
1. **Step 2**: A machine learning model for human heads detection is deployed at the edge.
1. **Step 3**: An admin authenticates by using Amazon Cognito into a private dashboard to configure cameras and queues. The dashboard is hosted as a static website using Amazon Simple Storage Service (Amazon S3) and Amazon CloudFront.
1. **Step 4**: The admin can generate asynchronous screenshots from cameras and use the UI to highlight areas of interest and the queue threshold.
1. **Step 5**: The camera configuration is stored in Amazon DynamoDB and thresholds are propagated into an IoT rule.
1. **Step 6**: The edge device runs inference on the live video camera streams and only sends as many aggregated results in the cloud as the number of people in a queue at a specific time.
1. **Step 7**: The inference output is stored in Amazon Timestream for future processing and forecasting.
1. **Step 8**: When the queue threshold limit is met, an alert is sent into an Amazon Simple Notification Service (Amazon SNS) topic. Events are logged in Amazon CloudWatch for future analysis.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance has been written using the AWS Cloud Development Kit (AWS CDK) for infrastructure as code wherever possible. It can be easily redeployed into new environments with minimal setup. It has also been created with examples of how to route data for analysis purposes, in addition to having IoT rules established for the publishing of metrics and notifications. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

By default, all AWS IoT data in transit and at rest is encrypted. Data in transit is encrypted using TLS, and data at rest is encrypted using AWS owned keys. In addition, the frontend uses authentication through Amazon Cognito, which helps you control which users are able to access the system. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

All communications within the system are handled through AWS IoT Core MQTT messaging protocol, which allows for “At Least Once” delivery of messages. The edge device (simulated by an Amazon Elastic Compute Cloud (Amazon EC2) instance) is managed through the AWS Lambda runtime. Updates to those components are continuously version controlled and managed through deployments within AWS IoT Greengrass. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The computer vision model is developed to capitalize the resources available on the host system. Where GPU processing is available, it will use that to speed up processing. Images are automatically downscaled to decrease processing time. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

To ensure that costs are kept low, the Guidance only uses a single EC2 instance to simulate an edge device and illustrate the function of the computer vision model. In addition, only the minimal usage of other AWS services is present within the system. These include a single Amazon S3 bucket for uploading pictures, a single DynamoDB table for storing queue vertices, and a minimal set of examples of using IoT rules to route data to CloudWatch. To further reduce costs, users can remove all of the IoT rules that route incoming data and run the model on their edge device. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance focuses on reducing environmental impact by only ever using the minimal set of resources required to make the system operate. There is very little resource usage throughout the system because it does not need to operate frequently or interact with many other services. For most of the time, the system will be inert until it is manually initiated by the user. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
