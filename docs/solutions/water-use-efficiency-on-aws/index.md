---
source_url: https://docs.aws.amazon.com/solutions/water-use-efficiency-on-aws/index.html
---

# Guidance for Water Use Efficiency on AWS

## Overview

**Important:** This Guidance requires the use of [Amazon Forecast](/forecast/latest/dg/what-is-forecast.html) , which is no longer available to new customers. Existing customers of Amazon Forecast can continue using and deploying this Guidance as normal. This Guidance demonstrates how industrial operations and water utilities can collect and monitor water usage data. It displays how you can improve your water use efficiency through the use of advanced analytics, such as forecasting. By adopting sustainable water management practices and investing in water-efficient technologies, you may reduce your business’s water usage and mitigate some of the operational risks of water scarcity.

## How it works

### Overview

This architecture diagram provides an overview of the data workflow for collecting, monitoring, and optimizing telemetry data for water use efficiency. For more details about the different stages of the data workflow, open the other tabs.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/water-use-efficiency-on-aws.pdf)Step 1Collect water usage telemetry data from industrial operations and water utilities.Step 2Ingest telemetry data and any other relevant enterprise data into the cloud.Step 3Store the raw telemetry for water consumption in a hot data store, and store the other enterprise data in a cold data store, such as a data lake.Step 4Process raw telemetry data and other enterprise data.Step 5Store the processed water usage telemetry data in the hot data store. Store the other processed enterprise data in a data lake or a data warehouse, based on data consumption patterns.Step 6Extract actionable insights on water consumption and efficiency through tools such as a real-time dashboard or a custom web application. Use advanced analytics to optimize and forecast water consumption. You can also set up notifications when anomalies are detected.### Part 1

This architecture diagram provides a more detailed description about data sources and ingestion. Follow the steps in this architecture diagram to deploy Part 1 of the Guidance.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/water-use-efficiency-on-aws.pdf)Step 1To collect water usage telemetry data, use either an open platform communications (OPC) Unified Architecture (UA) server with AWS IoT SiteWise Edge in an industrial operations setting or a purpose-built water meter using FreeRTOS in a water utility setting.Step 2AWS IoT SiteWise or AWS IoT Core ingests the water usage telemetry data and moves it to Amazon Kinesis and Amazon Timestream.Step 3Amazon API Gateway and AWS Glue ingest other static enterprise data, such as site metadata. Amazon Simple Storage Service (Amazon S3) stores this data.### Part 2

This architecture diagram provides a more detailed description about storing and processing data in hot and cold storage. Follow the steps in this architecture diagram to deploy Part 2 of the Guidance.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/water-use-efficiency-on-aws.pdf)Step 1After AWS IoT SiteWise or AWS IoT Core ingests the raw water usage telemetry data, store it in a hot data store like AWS IoT SiteWise or Timestream. Store your other enterprise data in a cold data store, such as a data lake on Amazon S3.Step 2Process the raw water usage telemetry data using AWS Lambda or a Timestream scheduled query, and process the other enterprise data using Lambda and AWS Glue.Step 3Store the processed water usage telemetry data in a hot data store, such as AWS IoT SiteWise or Timestream. Store your other processed enterprise data in a data lake on Amazon S3 or a data warehouse such as Amazon Redshift.### Part 3

This architecture diagram provides a more detailed description about processing and storing data for visualization and analytics. Follow the steps in this architecture diagram to deploy Part 3 of the Guidance.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/water-use-efficiency-on-aws.pdf)Step 1AWS IoT SiteWise or Timestream stores processed water usage telemetry data in a hot data store. A data lake on Amazon S3 or a data warehouse such as Amazon Redshift stores your other processed enterprise data.Step 2Build a real-time dashboard or custom application to visualize and monitor your water usage and efficiency using Amazon Managed Grafana or AWS Amplify. Enable third-party data consumption through RESTful APIs using API Gateway.Step 3Your company's business analysts can also directly query water usage data for custom metrics using Amazon Athena and create business intelligence reporting using Amazon QuickSight.Step 4Predict and optimize water consumption through advanced analytics using Amazon SageMaker.Step 5Set up alerts for anomaly detection using AWS IoT Events and Amazon Simple Notification Service (Amazon SNS).Step 6Using Amazon CloudWatch, you can monitor the overall health and performance of your application. AWS Systems Manager Parameter Store stores and manages configuration data across the application.Step 7Secure your data and application with AWS Key Management Service (AWS KMS) and AWS Identity and Access Management (IAM).## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses AWS IoT Events to continuously monitor Internet of Things (IoT) sensor data for equipment failures. Amazon SNS alerts you when it detects an event. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM policies and roles protect resources, following the least-privilege principle. It encrypts IoT data in transit using Transport Layer Security (TLS), and it encrypts and protects data at rest using AWS KMS. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance follows an event-driven architecture with loosely coupled dependencies, making it easy for you to isolate behaviors and increase resilience and agility. You can also use CloudWatch metrics and alarms to monitor the application and send notifications when thresholds breach. Specify an automation runbook in Systems Manager Incident Manager to enable automated responses to critical issues. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services in this Guidance are purpose-built to perform required functions. For example, AWS IoT SiteWise is built to collect, organize, and analyze data from industrial equipment at scale. It reads data from on-site equipment using industrial protocols, such as OPC UA. Timestream is built to store and manage time-series data from telemetry. Forecast is made for time-series forecasting based on machine learning. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses services that scale automatically according to demand, so you only pay for what you use. Timestream manages the life cycle of timeseries data, keeping recent data in memory and moving historical data to a cost-optimized storage tier based on user-defined policies. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance follows an event-driven architecture and uses fully managed services such as Timestream, AWS Glue, and Amazon S3. These services scale automatically according to workload, helping you avoid overprovisioning resources. Additionally, you can use the Amazon S3 Intelligent-Tiering storage class to automatically move data to the most sustainable access tier in Amazon S3. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
