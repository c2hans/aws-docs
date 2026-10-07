---
source_url: https://docs.aws.amazon.com/solutions/implementing-near-real-time-analytics-with-spark-streaming-on-aws/index.html
---

---
title: 'Guidance for Implementing Near Real-Time Analytics with Spark Streaming on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/implementing-near-real-time-analytics-with-spark-streaming-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Implementing Near Real-Time Analytics with Spark Streaming on AWS

## Overview

This Guidance demonstrates how to configure a self-service data analytics environment that is simple to launch and access for data engineers and data scientists. The integrated development environment (IDE) is based on Jupyter Notebooks, providing an interactive interface for easy data exploration, and includes all the necessary tools to debug, build, and schedule near real-time data pipelines. The environment supports secure team collaboration with workload isolation, and allows administrators to self-provision, scale, and de-provision resources from a single interface without exposing the complexities of the underlying infrastructure or compromising security, governance, and costs. Administrators can independently manage cluster configurations and continuously optimize for cost, security, reliability, and performance.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/implementing-near-real-time-analytics-with-spark-streaming-on-aws.pdf)

![Architecture diagram](/images/solutions/implementing-near-real-time-analytics-with-spark-streaming-on-aws/images/implementing-near-real-time-analytics-with-spark-streaming-on-aws-1.png)

1. **Step 1**: Cloud operations teams develop Amazon EMR cluster templates in AWS CloudFormation according to their desired specifications (such as instance types and network configurations) and publish the templates as products in the AWS Service Catalog for self-service provisioning.
1. **Step 2**: Bid events or pixels on web ads capture user impressions and sends the data to an Amazon Kinesis Data Streams endpoint.
1. **Step 3**: Data engineering teams log in to their workspaces in Amazon EMR Studio. Here, they self-provision Amazon EMR clusters. Alternatively, they attach existing clusters to develop Spark streaming applications, like bid validation or impression measurement, using interactive notebooks.
1. **Step 4**: A Spark streaming application runs on an Amazon EMR cluster. It continuously ingests raw bid or impression event data from Kinesis Data Streams. The application transforms the data. It then stores the transformed data in an Amazon Simple Storage Service (Amazon S3) data lake. This process enables near real-time operational reporting. You can choose provisioned Amazon EMR clusters for the most flexibility in cost optimization or serverless Amazon EMR clusters to simplify deployment and cluster management.
1. **Step 5**: Amazon S3 stores data in partitioned folders. The data can be compressed and in columnar format or in other open table formats like Apache Iceberg.
1. **Step 6**: All database and table metadata is registered within an AWS Glue Data Catalog, so data can be queried by multiple AWS services like Amazon Athena or Amazon SageMaker.
1. **Step 7**: (Optional) Data lake administrators can register the Data Catalog with AWS Lake Formation to provide more granular access controls and centralize user management.
1. **Step 8**: Users can run SQL queries against curated clickstream or impression data in Amazon S3 in near real-time with Athena and visualize dashboards with Amazon QuickSight.
1. **Step 9**: In addition to the Amazon S3 data lake, Amazon EMR workloads can write data to NoSQL databases like Amazon DynamoDB or in-memory databases like Aerospike. This supports read workloads requiring fast performance on a large scale, such as bid filtering or operational reporting.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/real-time-analytics-spark-streaming)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon EMR Studio provides a fully managed, web-based integrated development environment (IDE) with Jupyter Notebooks, allowing data engineering or data science teams to develop, visualize, and debug Spark streaming applications interactively without managing additional servers. Teams can self-provision Amazon EMR clusters that have been predefined using infrastructure as code (IaC) templates in the Service Catalog. This reduces the dependency on cloud operations teams, improves development agility, and helps organizations follow security and governance best practices with minimal overhead. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon EMR Studio supports authentication and authorization with AWS Identity and Access Management (IAM), or AWS Identity Center, removing the need to connect with SSH (Secure Shell) directly into Spark clusters. Lake Formation allows for granular and centralized access control to the data in your data lakes, centralizing user access management and augmenting a strong security and governance posture on your data pipelines. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Kinesis Data Streams and Amazon EMR provide autoscaling capabilities to meet the throughput demand of your real-time data streaming workflow. Amazon EMR uses the Apache Spark framework, which automatically distributes and retries jobs in the event of application or network failures. Kinesis Data Streams also scales capacity automatically and synchronously replicates data across three Availability Zones, providing high availability and data durability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Kinesis Data Streams automatically scales capacity in response to varying data traffic, allowing your real-time processing workflow to meet throughput demands. Amazon EMR provides multiple performance optimization features for Spark, allowing users to run 3.5 times faster without any changes to their applications. In addition, Athena automatically processes queries in parallel and provisions the necessary resources. Also, data can be stored in Amazon S3 partition keys and columnar formats to increase query performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance provides a sample Amazon EMR cluster template that uses instance fleets with Amazon EC2 Spot Instance capacity and specifies Amazon EC2 Graviton3 instance types. This can provide up to 20 percent in cost savings over comparable x86-based Amazon Elastic Compute Cloud (Amazon EC2) instances. Further, the use of idle timeouts and Amazon S3 storage tiers allows for better utilization of compute and storage resources with optimized costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon EC2 Graviton3 instance types use up to 60 percent less energy for the same performance as comparable Amazon EC2 instances, helping to reduce the carbon footprint. The use of Amazon EC2 Spot Instances and Amazon EMR idle timeout settings helps ensure better utilization of resources and minimizes the environmental impact of the workload. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
