---
source_url: https://docs.aws.amazon.com/solutions/hyperpersonalized-marketing-with-amazon-personalize-and-amazon-bedrock/index.html
---

---
title: 'Guidance for Hyperpersonalized Marketing with Amazon Personalize and Amazon Bedrock'
canonical_url: https://docs.aws.amazon.com/solutions/hyperpersonalized-marketing-with-amazon-personalize-and-amazon-bedrock/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Hyperpersonalized Marketing with Amazon Personalize and Amazon Bedrock

## Overview

This Guidance shows how to implement a comprehensive travel and hospitality (T&H) customer engagement system to enhance your marketing strategy. Using [Unified Profiles for Travelers and Guests on AWS](/solutions/), you can create unified customer profiles and deliver personalized experiences. For example, you can tailor recommendations for each customer and generate hyperpersonalized marketing content driven by AI. By using this Guidance to implement effective, targeted marketing strategies, you can significantly enhance customer satisfaction, improve engagement across channels, and drive sustainable business growth.

## How it works

This architecture diagram shows how to implement a comprehensive travel and hospitality (T&H) customer engagement platform that uses Unified Profiles for Travelers and Guests on AWS to generate hyperpersonalized marketing content.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/hyperpersonalized-marketing-with-amazon-personalize-and-amazon-bedrock.pdf)

![Architecture diagram](/images/solutions/hyperpersonalized-marketing-with-amazon-personalize-and-amazon-bedrock/images/hyperpersonalized-marketing-with-amazon-personalize-and-amazon-bedrock-1.png)

1. **Step 1**: Using connectors, Unified Profiles for Travelers and Guests on AWS ingests booking, stay, and loyalty data from industry systems and creates unified profiles of travelers or guests.
1. **Step 2**: Catalog traveler/guest metadata using AWS Glue Data Catalog. Use AWS Glue to transform this data from JSON to comma-separated values (CSV) and store it in an Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 3**: Your marketing team indexes the promotion and offers data in Knowledge Bases for Amazon Bedrock stored on Amazon OpenSearch Service.
1. **Step 4**: Amazon Personalize creates a segmentation model from traveler/guest booking, stay, and loyalty data stored on Amazon S3.
1. **Step 5**: Use AWS Lambda to call an Amazon Bedrock foundation model (FM) API and generate hyperpersonalized marketing content using traveler/guest preferences. Store user/content mapping in an Amazon DynamoDB table.
1. **Step 6**: Activate campaigns on AWS End User Messaging to send tailored promotions and offers to travelers/guests using SMS, WhatsApp, email, and push notifications.
1. **Step 7**: A Lambda function acts as the Amazon API Gateway backend, retrieving and batch processing messages from the Amazon Simple Queue Service (Amazon SQS) queue. Amazon SQS decouples the API Gateway endpoint from Lambda, providing a request buffer and preventing throttling. Batch processing improves efficiency and reduces overhead.
1. **Step 8**: The web application, utilizing a REST API hosted on API Gateway with Lambda as the backend, enables your marketers or content strategists to access traveler/guest profiles, segmentation, and content generation services. Requests are queued in Amazon SQS for reliable messaging.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch collects logs, metrics, and events in a unified view of operational health. By providing data and actionable insights, it enables you to monitor applications, respond to system-wide performance changes, and optimize resource utilization. CloudWatch also lets you set alarms, invoke automated actions, and receive notifications when predefined thresholds are breached. By enabling you to identify and resolve issues promptly, these proactive monitoring and automated response capabilities help you keep your systems running smoothly. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

API Gateway helps secure your APIs by providing mechanisms such as API keys for client authentication, authorization, access control, and traffic encryption. For example, it supports encryption in transit using SSL/TLS certificates. Additionally, you can define fine-grained access controls for your APIs so that you can control what actions users can perform. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

OpenSearch Service simplifies running and scaling OpenSearch by automating software patching, failure detection, and failover procedures. It automatically detects and replaces failed nodes, reducing the overhead associated with self-managed clusters. It also replicates data across multiple Availability Zones (AZs) to support data durability and availability in case of node or AZ failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

DynamoDB is designed to handle massive workloads while delivering single-digit millisecond latency at any scale. It uses a distributed, fault-tolerant architecture that automatically spreads data and traffic across multiple servers and data centers, supporting high availability and consistent performance. It also offers global tables, which replicate data across AWS Regions, facilitating worldwide low-latency access to data. Additionally, Amazon DynamoDB Accelerator (DAX) provides an in-memory cache that can significantly reduce response times for read-heavy workloads. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon Bedrock provides the fully managed generative AI foundation models for your application using an API. This service scales to avoid under- or overprovisioning resources, and you only pay for the number of tokens you use during inference. Additionally, Amazon Bedrock is a fully managed service, so you can avoid the cost of maintaining and managing the infrastructure needed to host generative AI foundation models. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda enables you to run code without provisioning or managing servers, and its functions automatically scale to meet demand, including volume spikes. It also reuses implementation environments, improving your application’s resource utilization and minimizing the energy consumption of your workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
