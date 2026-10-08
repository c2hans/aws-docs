---
source_url: https://docs.aws.amazon.com/solutions/connected-airports-using-internet-of-things-on-aws/index.html
---

---
title: 'Guidance for Connected Airports Using Internet of Things on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/connected-airports-using-internet-of-things-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Connected Airports Using Internet of Things on AWS

## Overview

This Guidance demonstrates how you can enhance your airport’s operational efficiency and improve the passenger experience using the Internet of Things (IoT). Connect critical airport assets—like heating, ventilating, and air-conditioning (HVAC) systems; baggage handling, security, and access control systems; runways, taxiways, and passenger boarding bridges; and equipment and aircraft. Then, you can build an asset-monitoring system that provides insights and helps you streamline operations. You’ll be able to enact predictive maintenance, respond rapidly to downtime and disruptions, manage employee badges and tags, reduce passenger wait times, and make more-informed decisions.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/connected-airports-using-internet-of-things-on-aws.pdf)

![Architecture diagram](/images/solutions/connected-airports-using-internet-of-things-on-aws/images/connected-airports-using-internet-of-things-on-aws-1.png)

1. **Step 1**: Use AWS IoT Greengrass core device to connect to, publish to, and subscribe to data from airport assets on the edge using the open standard Message Queuing Telemetry Transport (MQTT) protocol.
1. **Step 2**: Use AWS IoT Core to maintain shadows of airport assets, connect to AWS, and manage messages from Internet of Things (IoT) sensors for further processing.
1. **Step 3**: Create a detector model in AWS IoT Events with AWS IoT Core as the input source. Configure Amazon Simple Notification Service (Amazon SNS) in the detector model to send notifications by SMS or email when an unusual event occurs or when a sensor reaches your set thresholds.
1. **Step 4**: Use AWS IoT Analytics to aggregate, transform, and analyze IoT messages from AWS IoT Core. Build an IoT analysis dashboard and visualize on Amazon QuickSight.
1. **Step 5**: Configure an IoT rule to send messages from AWS IoT Core to Amazon Kinesis Data Streams for downstream processing.
1. **Step 6**: Use an AWS Lambda function to process messages from Kinesis Data Streams, and store them on Amazon DynamoDB.
1. **Step 7**: Amazon Kinesis Data Firehose reads data from Kinesis Data Streams and stores it in an Amazon Simple Storage Service (Amazon S3) data lake. Use AWS Glue to transform data and store it back on Amazon S3.
1. **Step 8**: Use Amazon SageMaker to build, train, and validate machine learning (ML) models for predictive maintenance and anomaly detection of airport assets. Optionally, use this ML model inference with an AWS IoT Greengrass core device on the edge.
1. **Step 9**: Use a Lambda function to process all IoT data stored on a DynamoDB table and fetch the ML model inference endpoint for predictions. Create a REST API with a Lambda function as a backend on Amazon API Gateway.
1. **Step 10**: Develop an airport operations web application to centralize asset monitoring and predictive maintenance capabilities. Also, integrate a QuickSight dashboard using QuickSight embeddings.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch provides near real-time visibility into infrastructure and application performance through detailed metrics and logs. For example, it gives you insights into the performance of Lambda functions, enabling you to identify and resolve issues quickly. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) lets you grant granular and least-privilege permissions so that users only have access to the specific resources they need. API Gateway enhances security for backend services and data by providing authentication and access control through API keys, helping you restrict access to your APIs and limit API rates using throttling. It also provides access logs and implementation logs to give you visibility into API usage and help you identify security issues. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS IoT Core enables reliable bidirectional communication between IoT-connected airport assets and AWS services. It can handle a high volume of messages from many assets and reliably route those messages to AWS for downstream processing and connecting. It also helps you reliably collect and process telemetry IoT data from your airport assets. AWS IoT Core scales to support any number of devices without compromising on reliability, and the built-in retries facilitate reliable communication at scale. Additionally, AWS IoT Greengrass core devices can continue to operate locally if disconnected from the AWS Cloud. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

DynamoDB provides fast, predictable performance by spreading data across multiple Availability Zones. It offers single-digit latency at scale, so you can build highly responsive applications with predictable performance at any scale, and provision the throughput capacity you need without having to overprovision for peak usage. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 provides cost-effective storage for any amount of data at scale. Its object life-cycle management and storage tiering reduce costs by automatically transitioning less frequently accessed data to more affordable tiers, such as Amazon S3 Standard-Infrequent Access (S3 Standard-IA) or Amazon S3 Glacier storage classes. This minimizes the overall storage expenses of your architecture at scale. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS IoT Greengrass enables local compute, messaging, device shadow, and ML inference capabilities on edge devices. Performing compute and inference locally is more energy efficient than sending large amounts of data back and forth between local devices and the AWS Cloud. By reducing the need to transmit data to AWS for analysis, you can save network bandwidth and energy consumption and reduce the overall carbon footprint of your workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
