---
source_url: https://docs.aws.amazon.com/solutions/analytics-observability-on-aws/index.html
---

---
title: 'Guidance for Analytics Observability on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/analytics-observability-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Analytics Observability on AWS

## Overview

This Guidance demonstrates how you can improve the observability of your data pipelines running on Apache Spark. While this open-source framework provides tools that collect runtime metrics for visibility into low-level data processing activities, these metrics are relatively raw. By using AWS services for extract, transform, and load (ETL) operations alongside Apache Spark, you can enhance data quality and granularity, enabling better insights into optimization opportunities. Additionally, improved data pipeline observability helps increase efficiency, reduce operational overhead, accelerate troubleshooting, avoid performance bottlenecks, and achieve greater value from your data processing workloads.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/analytics-observability-on-aws.pdf)

![Architecture diagram](/images/solutions/analytics-observability-on-aws/images/analytics-observability-on-aws-1.png)

1. **Step 1**: The observability connector for Amazon OpenSearch Service is packaged into Apache Spark applications running through Amazon EMR or AWS Glue or self-hosted on Amazon Elastic Compute Cloud (Amazon EC2). The connector is a Java Archive (JAR) file to put on the driver and executor classpaths.
1. **Step 2**: The observability connector includes a custom log appender (Log4j AsyncAppender) and a custom SparkListener. They collect logs and metrics from the application and push the data out through the OpenSearch Service client.
1. **Step 3**: The observability connector pushes the data into an Amazon OpenSearch Ingestion pipeline. The pipeline applies data transformation and also acts as an ingestion buffer into OpenSearch Service.
1. **Step 4**: Ingestion-related logs and metrics are stored in OpenSearch Service indexes: one for each data type. The data delivery frequency is defined as part of the OpenSearch Service pipeline configuration. Log and metric data are encrypted using an AWS Key Management Service (AWS KMS) key.
1. **Step 5**: Prebuilt OpenSearch Dashboards is a tool that offers authenticated users insights into their data pipelines using aggregated views of performance metrics and logs at various levels of granularity, such as Spark application, job run, stage, and partition. The dashboard also provides performance scores calculated based on the collected metrics to enable easier analysis.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-analytics-observability-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses an OpenSearch Service observability connector to automate the collection of Apache Spark logs and metrics, then transforms them through OpenSearch Ingestion pipelines, which are highly configurable and can evolve to your needs. OpenSearch Service provides a powerful search capability, and the built-in OpenSearch Dashboards improve observability, providing visuals that shorten time to insights and aid troubleshooting. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) lets you control access to the pipeline as well as to the OpenSearch indexes. You can use IAM policies to make sure that metric and log collection processes happen within the security boundaries of their current Apache Spark application. You can use dedicated management roles, pipeline roles, and ingestion roles to enforce the least privilege principal. Additionally, this Guidance uses Amazon Virtual Private Cloud (Amazon VPC) for communication with OpenSearch to achieve proper network traffic isolation, and it uses AWS KMS to encrypt the data before it is stored in OpenSearch. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The OpenSearch Service observability connector collects and sends logs and metrics to OpenSearch Ingestion pipelines, which automatically scale in and out as new logs and metrics are produced. This limits the impact of unexpected activity spikes on OpenSearch Service cluster performance and stability. Additionally, the observability connector’s buffering and sampling feature helps you further reduce potential ingestion back pressure. To maintain high availability and increase reliability, you can enable multi–Availability Zone (AZ) deployments on the OpenSearch Service cluster, which will then distribute Ingestion OpenSearch Compute Units (Ingestion OCUs) across AZs. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

OpenSearch Service lets you specify minimum and maximum Ingestion OCUs for your OpenSearch Ingestion pipeline, and it will automatically scale up and down based on the pipeline's processing requirements and the load generated by your client application. The observability connector integrates with the native Apache Spark low-level plugin interface to collect the data while limiting performance overhead on Apache Spark jobs. Additionally, the built-in custom Apache Spark metric and log collector implements API consumption best practices, such buffering and exponential backoff, to minimize the impact on the Apache Spark application. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The OpenSearch Service observability connector pre-aggregates certain metrics to reduce postprocessing and ingestion volumes, optimizing the volume of metrics and logs produced. This reduces the risk of Ingestion OCU overconsumption. The OpenSearch Ingestion pipeline then uses dynamic scaling to make sure that you don’t incur charges for periods of inactivity; instead, you only pay for the pipeline’s effective usage. You can also start and stop pipelines on demand. OpenSearch Domains can also use ultrawarm nodes to reduce the cost of infrequently accessed indexes. Additionally, this Guidance reduces the need for custom developed components, which can help further optimize the total cost of ownership. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

OpenSearch Ingestion pipelines are natively serverless and provide elasticity for data ingestion and transformation, minimizing the environmental impact of backend services. This Guidance also supports both provisioned clusters and serverless collections, and you can use OpenSearch Serverless to further optimize sustainability. Additionally, you can use the insights provided by OpenSearch Dashboards to optimize your Apache Spark workloads and reduce your overall environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
