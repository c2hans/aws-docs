---
source_url: https://docs.aws.amazon.com/solutions/ultra-low-latency-machine-learning-feature-stores-on-aws/index.html
---

---
title: 'Guidance for Ultra-Low Latency, Machine Learning Feature Stores on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/ultra-low-latency-machine-learning-feature-stores-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Ultra-Low Latency, Machine Learning Feature Stores on AWS

## Overview

This Guidance shows how you can build an ultra-low latency online feature store using Amazon ElastiCache for Redis, a fully managed Redis service from AWS, and Feast, an open-source store framework. The online store uses machine learning (ML) for real-time data access and sub-millisecond latency. This Guidance covers a sample use case based on a real-time loan approval application that makes online predictions based on a customer’s credit scoring model.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/ultra-low-latency-machine-learning-feature-stores-on-aws.pdf)

![Architecture diagram](/images/solutions/ultra-low-latency-machine-learning-feature-stores-on-aws/images/ultra-low-latency-machine-learning-feature-stores-on-aws-1.png)

1. **Step 1**: Set up data infrastructure to deploy Amazon Redshift, an Amazon Simple Storage Service (Amazon S3) bucket containing zip code and credit history parquet files, and AWS Identity and Access Management (IAM) roles. Additionally, set up policies for Amazon Redshift to access Amazon S3, and create an Amazon Redshift table that can query the parquet files.
1. **Step 2**: Deploy Feast infrastructure.
1. **Step 3**: Create a feature store repository, and configure Amazon ElastiCache as the online feature store and Amazon Redshift as the offline feature store. Create feature definitions.
1. **Step 4**: Register the feature definitions and the underlying infrastructure into a Feast registry using the Feast SDK.
1. **Step 5**: Generate training data using features and labels from the data and features from Feast. The features from Feast enrich the historical data and create a Feature DataFrame.
1. **Step 6**: Train the ML model using the training dataset and a model trainer.
1. **Step 7**: Ingest batch features into the ElastiCache online feature store. These online features are used to make online predictions with our trained model.
1. **Step 8**: Read feature vector from ElastiCache for making predictions.
1. **Step 9**: Use AWS Key Management Service (AWS KMS) to encrypt ElastiCache data at rest.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-ultra-low-latency-features-stores-with-aws-machine-learning-ml)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch enhances operational excellence for ElastiCache by providing comprehensive monitoring, logging, and automation capabilities. It tracks ElastiCache metrics like CPU utilization, memory usage, network traffic, command statistics, and cache hit/miss ratios, enabling proactive performance management. CloudWatch logs integration allows centralized log analysis, simplifying troubleshooting. CloudWatch alarms invoke automated actions, such as scaling ElastiCache clusters for optimal performance during traffic spikes while reducing costs during lulls. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

By scoping IAM policies to the minimum required permissions, unauthorized access to resources is limited. KMS provides control over encryption keys used to protect data, eliminating key management overhead. IAM policies are scoped to grant ElastiCache only the necessary permissions for operation. ElastiCache offers encryption in-transit and at-rest, while KMS allows you to create, manage, and control access to customer-managed encryption keys used for data protection. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

ElastiCache auto scaling groups ensure reliable performance by dynamically adjusting Redis cluster capacity (shards and replicas) based on utilization metrics. CloudWatch continuously monitors key metrics and initiates alarms to proactively detect and mitigate issues. Auto scaling handles traffic spikes by launching additional nodes, preventing overload and maintaining consistent performance. Nodes can be distributed across Availability Zones, enhancing redundancy against outages. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

ElastiCache auto scaling dynamically provisions and right-sizes Redis clusters based on demand for optimal resource utilization. During traffic spikes, auto scaling launches additional nodes to handle increased loads, preventing overloads and maintaining low latency. ElastiCache features such as in-memory architecture, data structures, transactions, scripting, and clustering are optimized for high throughput and low latency operations, making it ideal for performance-critical workloads. Horizontal scaling and read replicas further boost throughput and response times. Redis Cluster Mode shards data across multiple nodes, distributing memory and workload for improved parallelization and linear throughput scaling. Sharding maximizes memory utilization by overcoming single-node limits, while locally executing commands on shards minimizes network hops. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Auto scaling optimizes ElastiCache costs by automatically adjusting cluster capacity based on utilization metrics. During low traffic periods, it scales in by terminating unnecessary nodes, preventing overprovisioning and reducing operational expenses. Conversely, it launches additional nodes during traffic spikes, helping to ensure sufficient capacity without incurring excess costs. This elasticity eliminates the need for manual capacity management and helps ensure clusters are right-sized to workload demands, running only the required resources. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

ElastiCache allows right-sizing caches to match application requirements, improving infrastructure efficiency and preventing resource waste. The availability of multiple AWS Regions enables deploying ElastiCache clusters closer to end users, reducing network latency and data transfer and leading to lower energy consumption and emissions from reduced network usage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Blog**: This blog post demonstrates how customers are building online feature stores on AWS with Amazon ElastiCache for Redis to support mission-critical ML use cases that require ultra-low latency.

[Build an ultra-low latency online feature store for real-time inferencing using Amazon ElastiCache for Redis](https://aws.amazon.com/blogs/database/build-an-ultra-low-latency-online-feature-store-for-real-time-inferencing-using-amazon-elasticache-for-redis/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
