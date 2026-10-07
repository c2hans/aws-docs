---
source_url: https://docs.aws.amazon.com/solutions/product-carbon-footprinting-on-aws/index.html
---

---
title: 'Guidance for Product Carbon Footprinting on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/product-carbon-footprinting-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Product Carbon Footprinting on AWS

## Overview

This Guidance helps customers scale product carbon footprint (PCF) tracking, reduce the manual effort involved with data collection and calculation, and provide transparent and auditable PCFs for reporting. The architecture pairs Internet of Things (IoT) sensor data from a manufacturing facility with product information and emission factors. An interactive dashboard uses this data to track product-level energy and carbon footprint in addition to benchmarking environmental performance across equipment and sites. With this Guidance, customers can identify hotspots and best practices to lower their PCF and manufacturing costs. Please note: This solution by itself will not make a customer compliant with any product carbon footprint frameworks, standards, or regulations. It provides the foundational infrastructure from which additional complementary solutions can be integrated.

## How it works

### Overview

Please note: This is an overview architecture. For diagrams highlighting different aspects of this architecture, open the other tabs.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/product-carbon-footprinting-on-aws.pdf#page=1)Step 1Telemetry data, such as utility consumption and production metrics, are collected from sensors deployed at the industrial equipment.Step 2Telemetry data is ingested to the cloud and processed.Step 3Sustainability subject matter experts (SMEs) generate static files for bill of materials, reference data, emission factors, and supplier information.Step 4The files are ingested and processed into mapped emission factors and combined with telemetry data for PCF calculations. An audit trail of the PCF calculation is stored in an audit log.Step 5An interactive dashboard or a web application can combine and visualize the processed data to provide stakeholders with valuable insights.### Data sources and ingestion

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/product-carbon-footprinting-on-aws.pdf#page=2)Step 1Sensors collect measurements of electricity and natural gas usage for the PCF analysis.Step 2AWS IoT Greengrass collects, aggregates, and filters sensor readings. AWS IoT Greengrass Stream Manager exports the telemetry data to Amazon Kinesis Data Streams.Step 3Kinesis Data Streams allows for high-throughput ingestion of telemetry data. An AWS Lambda function consumes the stream and loads telemetry data into Amazon Timestream. Amazon Kinesis Data Firehose loads the telemetry data into Amazon Simple Storage Service (Amazon S3).Step 4Sustainability SMEs collect static files for bill of materials, reference data, emission factors, and supplier information.Step 5These static files are ingested to Amazon S3 through a REST API endpoint exposed by Amazon API Gateway and backed by Lambda.### Storage and processing

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/product-carbon-footprinting-on-aws.pdf#page=3)Step 1Timestream stores raw telemetry data as hot storage.Step 2A Timestream scheduled query aggregates the telemetry data to the maximum granularity required by downstream consumers and stores it in a new table.Step 3Raw static files are stored in an Amazon S3 bucket.Step 4Lambda functions and AWS Glue read the static files from the raw S3 bucket and transform them into structured data within the processed storage tier. This processing step includes a set of precomputations, such as the mapped emission factors for emission sources and raw materials and electricity for a specific factory based on the grid mix.Step 5The processed static data is loaded into Amazon Relational Database Service (Amazon RDS) and the data lake powered by Amazon S3. This provides long-term storage and fast query access for downstream calculations.Step 6A Lambda function reads emission factors and bill of materials data from Amazon RDS and electricity consumption data from Timestream. It performs carbon footprint calculations and stores the results and audit logs in the curated data tier.Step 7The processed and curated storage tiers store the PCFs in Amazon RDS and Amazon S3 for flexible access and long-term storage. Amazon CloudWatch stores audit logs.### Consumption and dashboard

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/product-carbon-footprinting-on-aws.pdf#page=4)Step 1Timestream, Amazon RDS, and Amazon S3 store data available for consumption.Step 2Amazon QuickSight builds interactive dashboards to help executives, sustainability SMEs, and operations personnel analyze the PCF data, including on-the-fly PCF calculations. It can also pull precomputed PCF values for known queries ahead of time.Step 3Based on the consumption patterns and type of business insights, executives, sustainability SMEs, and operations personnel may need a custom web application. This web application can pull precomputed PCF values from Amazon RDS or perform ad-hoc calculations as the user requests them.Step 4Amazon Route 53, the domain name system (DNS), enables front-end clients to resolve the website hostname to the AWS content delivery network, Amazon CloudFront.Step 5CloudFront routes the web requests to origin servers and caches the static content and assets served from Amazon S3 and origin servers. It secures the application traffic using AWS WAF, a web application firewall that helps to protect the application against common exploits and bots.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudWatch provides centralized logging with metrics and alarms across all deployed services. These metrics and alarms can raise alerts for operational anomalies. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Resources are protected using AWS Identity and Access Management (IAM) policies and principles. Use least privilege access and role-based access to grant permissions to operators. AWS Key Management Service (KMS) encrypts data at rest. HTTPS endpoints with transport layer security (TLS) provide encryption for in-transit data, including service endpoints and API Gateway endpoints. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses serverless services whenever possible, such as API Gateway, Lambda, and Timestream, enabling auto-scaling to respond to fluctuating demands. This Guidance also uses AWS services such as Amazon S3, Amazon RDS, and Timestream to provide built-in functionality for data backup and recovery. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses serverless managed services, such as Lambda, that automatically scale in response to changing demand, reducing resource overhead. Additionally, customers can apply different analytics tools to their data stored in Amazon S3, depending on their needs. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance relies on serverless and fully managed services, such as Lambda, Amazon S3, and Timestream, which automatically scale according to workload demand. As a result, you only pay for the resources you use. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon S3 lifecycle policies can automatically move data to more energy-efficient storage classes, enforce deletion timelines, and minimize overall storage requirements. Timestream allows for data to automatically be moved from the memory tier to the magnetic tier to minimize cost. This Guidance also uses managed, serverless technologies such as AWS Glue, Lambda, and Timestream to help ensure hardware is minimally provisioned to meet demand. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
