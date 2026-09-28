---
source_url: https://docs.aws.amazon.com/solutions/capturing-retail-video-analytics-on-aws/index.html
---

---
title: 'Guidance for Capturing Retail Video Analytics on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/capturing-retail-video-analytics-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Capturing Retail Video Analytics on AWS

## Overview

This Guidance shows how retailers can harness in-store cameras and AI/ML capabilities to gain deeper customer insights and enhance in-store experiences. With this Guidance, retailers can automatically collect valuable analytics like heatmaps, dwell-time, and traffic flow. This approach empowers brick-and-mortar retailers to better understand customer behavior, optimize layouts, and improve the shopping experience. By analyzing customers' in-store journeys, retailers can make data-driven decisions to enhance customer satisfaction, increase conversions, and boost overall sales performance.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/capturing-retail-video-analytics-on-aws.pdf)

![Architecture diagram](/images/solutions/capturing-retail-video-analytics-on-aws/images/capturing-retail-video-analytics-on-aws-1.png)

1. **Step 1**: Users upload historical videos to Amazon Simple Storage Service (Amazon S3).
1. **Step 2**: Amazon S3 event notifications of a new object insert a new message in Amazon Simple Queue Service (Amazon SQS).
1. **Step 3**: A video processing application listens to the Amazon SQS queue for new object uploads. It downloads and extracts people-pathing information. Amazon EC2 Auto Scaling helps ensure there is always an Amazon Elastic Compute Cloud (Amazon EC2) worker for processing and scales down if there are no videos to process.
1. **Step 4**: After processing, people-tracking data is uploaded to an output folder in Amazon S3.
1. **Step 5**: New JSON output files trigger another Amazon SQS queue message.
1. **Step 6**: A visualization app captures new messages from Amazon SQS to render and display heat map information.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-capturning-retail-video-analytics-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Integrating Amazon EC2 with Amazon CloudWatch logs allows you to seamlessly store and search your application logs, without additional infrastructure. Automatically scale your EC2 instances based on service events, such as new Amazon S3 objects or Amazon SQS messages. CloudWatch allows you to visualize and analyze these components so you can identify performance bottlenecks and troubleshoot requests. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Use AWS Identity and Access Management (IAM) roles with minimum privileges to provide secure access to different components within your architecture. This approach ensures the best authorization mechanism to protect your system. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon EC2 Auto Scaling groups provide resiliency in processing video files, while Amazon SQS helps ensure that files are processed by your frontend application running on Amazon EC2. As managed services, Amazon S3 and Amazon SQS offer inherent reliability, with Amazon SQS monitoring queue length to spin up additional EC2 instances and Amazon EC2 Auto Scaling health checks confirming that new instances are provisioned to maintain desired capacity. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Use Amazon EC2 GPU instances to satisfy the performance requirements of your video processing use case. Yolo9 deep learning models and GPU-based EC2 instances can help achieve optimal performance in your object detection algorithms. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The serverless nature of Amazon S3 and Amazon SQS eliminate the need for dedicated hosts when not in use. Amazon EC2 Auto Scaling groups and GPU-based instances optimize costs, as faster processing means less total compute time required compared to CPU-based instances. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Serverless services and Amazon EC2 Auto Scaling groups in this Guidance help reduce power consumption and environmental impact by eliminating wasteful overprovisioning of compute resources. Services like Amazon SQS, Amazon S3, and Amazon EC2 Auto Scaling are managed by AWS and help minimize wasted compute resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
