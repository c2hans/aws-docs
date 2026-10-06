---
source_url: https://docs.aws.amazon.com/solutions/airport-data-management-on-aws/index.html
---

---
title: 'Guidance for Airport Data Management on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/airport-data-management-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Airport Data Management on AWS

Enhance the traveler experience and optimize airport operations with a data management solution built on AWS

## Overview

This Guidance helps you build data management systems that can both monitor airport operations and enhance the traveler experience. Data is collected from traditional systems of record, securely stored, managed, and transformed into reportable data sets. Purpose-built databases and AWS services are used to build near real-time operational dashboards and traveler applications that are flexible, agile, easy to deploy, and resilient.

## How it works

### Enhanced traveler experience

This diagram shows how to build a data management system that will generate meaningful insights with information from airlines and vendors to enhance the traveler experience.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/airport-data-management-on-aws.pdf)Step 1Build an operational data management system with systems of record such as schedules, near real-time flight information, traveler check-ins, loyalty transactions, lounge usage, and transactions in the airport.Step 2Collect addresses, demographics, and other public data sets with AWS Data Exchange. Ingest private data sets with AWS Storage Gateway and AWS Transfer Family.Step 3Optionally, enhance the baggage system with a radio-frequency identification (RFID) type of sortation and tracking system. Or, leverage the bar code scanners and baggage sortation events. Combine AWS IoT Greengrass, AWS IoT Core, and Amazon Kinesis to ingest sortation events.Step 4Provide staging for ingesting all batch and near real-time data using cost-effective storage classes in Amazon Simple Storage Service (Amazon S3).Step 5Use Amazon EMR and AWS Glue to transform your data. Use open standards to build the data lake using the same data as the operational data management system. Use a read pattern schema to make the raw data and curated data readily available for all user roles.Step 6Build all reportable data sets in Amazon S3, and leverage Amazon Redshift, Amazon Athena, and Amazon QuickSight for analytics. Optionally, build data marts in Amazon Redshift for heavily used analytics. For miscellaneous requirements, publish the AWS Glue Data Catalog, and use Athena for analysis using the data lake built in Step 5.Step 7Use Amazon SageMaker to provide standard artificial intelligence and machine learning (AI/ML) models for operational analytics. You can also use SageMaker to build your own models on top of the data.Step 8Use purpose-built databases like Amazon DynamoDB, and serverless services like AWS Lambda and Amazon API Gateway, to deliver microservices and events for operational data stores. Build near real-time operational dashboards and customer applications using these microservices.Step 9Leverage Amazon DynamoDB Streams and AWS Step Functions to publish flight and customer events to downstream systems, like baggage reconciliation and ground transportation.### Optimizing operations

This diagram shows how to build a data management system to monitor airport operations in near real-time. It can be used to predict costs, revenue, turnaround times, and potential delays using open data standards, purpose-built databases, and an extensive serverless architecture.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/airport-data-management-on-aws.pdf)Step 1Build the data management system with systems of record such as airline schedules, near real-time flight information, weather forecasts, aircraft position data, airport resources, and billing.Step 2Leverage AWS Data Exchange to create the data collection from public sources such as the weather and aircraft position. Ingest private data sets with Storage Gateway and Transfer Family.Step 3Use AWS Panorama or follow Aircraft Turn Tracking to passively collect and leverage aircraft gate turn events.Step 4Provide staging for ingesting all batch and near real-time data using cost-effective storage classes in Amazon S3.Step 5Transform your data with Amazon EMR and AWS Glue. Use open standards to build a data lake using the same data as the operational data management system. Use a read pattern schema to make the raw data and curated data readily available for all roles.Step 6Build all reportable data sets in Amazon S3. Build data marts in Amazon Redshift for heavy analytics. For miscellaneous requirements, publish the Data Catalog and use Athena and QuickSight for analysis using the data lake.Step 7Use SageMaker to provide standard AI/ML models for operational analytics, or use SageMaker to build your own models on top of the data.Step 8Use purpose-built databases like DynamoDB and serverless services like Lambda and API Gateway to deliver microservices and events for operational data stores. Build a near real-time operational dashboard and customer applications leveraging these microservices.Step 9Leverage DynamoDB Streams and Step Functions to publish flight and aircraft movement events to keep the Airport Operating Database and Airport Display systems current.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

To safely operate this Guidance, use Amazon CloudFormation and deploy in your cloud environment. CloudFormation helps you scale your infrastructure and manage your resources through a single operation. We also recommend you use Amazon CloudWatch to increase your observability with application and service-level metrics, personalized dashboards, and logs. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

For secure authentication and authorization, this Guidance uses AWS Identity and Access Management (IAM) roles that control people and machine access. In addition, file transfers into Amazon S3 are secured through the services' native security features. To protect resources in this Guidance, all data is encrypted both in motion and at rest. You can also use customer-controlled AWS Key Management Service (AWS KMS) for encryption. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The serverless components in this Guidance are highly available and automatically scale based on usage, ensuring you have a reliable application-level architecture. With Amazon S3 Select, you can use structured query language (SQL) to filter the contents of an Amazon S3 object and retrieve only the subset of data that you need. Athena allows you to analyze data wherever it lives, while QuickSight powers you with unified business intelligence. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

To optimize this Guidance, consider adjusting the data input with direct integrations into your own systems through Lambda or AWS Marketplace connectors. A connector is an optional code package that assists with access to data stores that you can subscribe to. You can subscribe to several connectors offered in AWS Marketplace. You can also add more data relevant to your business needs through AWS Data Exchange and adjust the AWS Glue crawler to construct modified data sets to use for forecasting. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

With this Guidance, you benefit from Amazon S3 for inexpensive storage. And with the serverless applications, such as AWS Glue and Lambda, you are charged only for usage. The managed serverless services in this Guidance offer a pay-as-you-go approach where you pay only for the individual services you need, for as long as you need them. The AWS Billing Console and AWS Budgets can help you monitor spending and control costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By default, the resources in this Guidance are only activated when there are changes in Amazon S3 buckets, ensuring that this Guidance scales to continually match the load with only the minimum resources required. And with the managed services and dynamic scaling that this Guidance deploys, you minimize the environmental impact of the backend services. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
