---
source_url: https://docs.aws.amazon.com/solutions/scaling-geospatial-data-lakes-with-earth-on-aws/index.html
---

---
title: 'Guidance for Scaling Geospatial Data Lakes with Earth on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/scaling-geospatial-data-lakes-with-earth-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Scaling Geospatial Data Lakes with Earth on AWS

## Overview

This Guidance shows how to build scalable geospatial data repositories on AWS, simplifying the design of data pipelines and facilitating faster access to raw data. By integrating [Earth on AWS](https://aws.amazon.com/earth/) datasets from the Registry of Open Data on AWS, it eliminates the need for storing this data in your own data lake, reducing costs and complexity. This Guidance also offers integration with a variety of dissemination mechanisms and supports diverse processing demands, from basic spatial queries to complex analytics. These features allow you to streamline geospatial workflows and enhance data accessibility.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/scaling-geospatial-data-lakes-with-earth-on-aws.pdf)

![Architecture diagram](/images/solutions/scaling-geospatial-data-lakes-with-earth-on-aws/images/scaling-geospatial-data-lakes-with-earth-on-aws-1.png)

1. **Step 1**: Invoke a data ingestion pipeline based on new scene detection. Subscribe to Amazon Simple Notification Service (Amazon SNS) topics for managed datasets with appropriate filters, and configure time-based ingestion rules using Amazon CloudWatch.
1. **Step 2**: AWS Lambda queries the SpatioTemporal Asset Catalog (STAC) API for respective datasets to get product details. Lambda then invokes the data processing pipeline through AWS Step Functions.
1. **Step 3**: Step Functions orchestrates the processing tasks. Parallel or sequential processing can be configured based on task characteristics and requirements.
1. **Step 4**: Amazon Elastic Container Service (Amazon ECS) runs the following containerized tasks: - Downloads the products from datasets hosted on the Registry of Open Data on AWS. - Processes the tiles (through crop and geomosiac operations) to the area of interest and stores them in an Amazon Simple Storage Service (Amazon S3) automated optical inspection (AOI)-processed bucket. - Builds metadata and stores it in Amazon DynamoDB. - Stores vector data in Amazon Aurora PostgreSQL-Compatible Edition with PostGIS extensions.
1. **Step 5**: Step Functions invokes the next processing task with Amazon SageMaker. Machine learning (ML) models on SageMaker perform cloud removal and band math and store the data in an Amazon S3 preprocessed bucket.
1. **Step 6**: QGIS, a geographic information system (GIS) software, is hosted on Amazon WorkSpaces. The QGIS workbench is used for visualizing or further processing.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudWatch provides comprehensive monitoring and observability for your applications. It captures and analyzes events, logs, and metrics to give you real-time insights into your system's health and performance. By using CloudWatch, you can proactively detect issues, troubleshoot problems more efficiently, and respond to incidents faster. This continuous monitoring helps ensure better application reliability while allowing you to maintain optimal performance across your AWS infrastructure. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS provides a comprehensive suite of security services and features to protect your data and resources. AWS Identity and Access Management (IAM) enables fine-grained access control, allowing you to set permission policies that restrict who can access and manage AWS resources. Data protection occurs through various means: Amazon S3 employs server-side encryption and bucket policies for data at rest, while AWS Key Management Service (AWS KMS) offers customer-managed keys for encrypting data in Amazon S3, Amazon Relational Database Service (Amazon RDS), and DynamoDB. This Guidance enhances network security by using security groups attached to container task network interfaces, protecting virtual private cloud (VPC) resources. It also configures network access control lists for subnet-level access restrictions and utilizes VPC endpoints to keep traffic within the AWS environment, safeguarding data in transit. Furthermore, the use of managed services like Amazon ECS, Lambda, and SageMaker reduces your security maintenance burden under the shared responsibility model. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The services selected for this Guidance offer high availability, durability, and scalability for your applications. Lambda enhances reliability by running functions across multiple Availability Zones (AZs) so that event processing continues even if one AZ fails. Aurora PostgreSQL provides robust high-availability options, replicating data six ways across three AZs for improved fault tolerance, even with a single database instance. For controlled scaling and resilience, Step Functions allows you to manage processing rates, preventing overload on downstream services and avoiding rate limits. It also orchestrates stateless components, which are inherently more scalable, robust, and manageable. Data durability is supported by Amazon S3, offering automatic cross-Region replication, while both DynamoDB and Aurora provide flexible backup capabilities for point-in-time recovery. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses AWS managed services that automatically adjust to workload demands. For example, Lambda scales automatically to handle querying and data processing based on incoming event volume. Step Functions manages workflow orchestration, dynamically adjusting to increased loads by parallelizing or queueing tasks. For data storage and access, this Guidance utilizes three key services: Together, these services provide a scalable infrastructure capable of handling varying workloads efficiently so that your application can maintain performance and responsiveness as demand fluctuates without the need for manual intervention or complex capacity planning. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance optimizes costs through several strategies: These approaches minimize expenses across storage, compute, and networking while maintaining performance for geospatial processing workloads. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Through the use of managed, serverless services, this Guidance minimizes the environmental impact of backend resources by scaling them up and down to meet demand. Additionally, you can monitor CloudWatch metrics to make sure that the scaled environment is not overprovisioned, further reducing your environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
