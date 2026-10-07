---
source_url: https://docs.aws.amazon.com/solutions/integrating-amazon-monitron-with-treon-connect-on-aws/index.html
---

---
title: 'Guidance for Integrating Amazon Monitron with Treon Connect on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/integrating-amazon-monitron-with-treon-connect-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Integrating Amazon Monitron with Treon Connect on AWS

## Overview

This Guidance demonstrates how to extend Amazon Monitron sensor investments by integrating them with Treon Connect on AWS to create a comprehensive predictive maintenance solution. By consolidating data from existing Monitron devices, Treon sensors, and third-party systems into a unified interface with a single dashboard and API layer, you can automate work order generation through CMMS/EAM integration and leverage advanced analytics to shift from reactive maintenance to proactive, data-driven strategies that reduce unplanned downtime, optimize maintenance schedules, and improve equipment reliability across industrial operations.

## Benefits

### Consolidate all condition monitoring data

Unify sensor data from multiple sources into a single dashboard and API layer. Eliminate data silos and gain comprehensive asset health visibility across your entire industrial operation.

### Automate maintenance workflow generation

Transform anomaly detection into immediate action by automatically creating work orders in your CMMS or EAM systems. Reduce response time and eliminate manual intervention when equipment issues arise.

### Build custom predictive models

Leverage your industrial data lake to train machine learning models specific to your equipment and operations. Move beyond generic algorithms to achieve maintenance predictions tailored to your unique asset profiles.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/integrating-amazon-monitron-with-treon-connect-on-aws.pdf)

![Architecture diagram](/images/solutions/integrating-amazon-monitron-with-treon-connect-on-aws/images/integrating-amazon-monitron-with-treon-connect-on-aws-1.png)

1. **Step 1**: Install Treon Industrial Node C (based on Amazon Monitron technology) or Treon Industrial Node X on rotating equipment. The sensors connect to the Treon Gateway via Bluetooth Low Energy (Industrial Node C) or Wirepas Mesh (Industrial Node X).
1. **Step 2**: The gateway connects securely to the Treon Connect platform via AWS IoT Core using Wi-Fi, LAN, or cellular network through its preconfigured settings.
1. **Step 3**: Integrate data from other sensors or systems by exposing them in an MQTT broker.
1. **Step 4**: Treon Connect MQTT Client connects to the external MQTT broker and captures this data to make it available for analysis.
1. **Step 5**: Enable Amazon Monitron data export to start a live data export to a new or existing Amazon Kinesis Data Streams stream to expose measurement data and inference results once an hour.
1. **Step 6**: Add a resource-based policy on the Kinesis stream to grant cross-account read access to the Treon Connect AWS Identity and Access Management (AWS IAM) role provided. When the Amazon Monitron data is available in the Kinesis stream, Treon Connect captures it for further analysis.
1. **Step 7**: Maintenance and reliability teams use the Treon Connect application to perform deeper diagnosis and get a unified snapshot of asset health from both Treon sensors and Amazon Monitron.
1. **Step 8**: Treon Connect sends measurements and inference results (insights) with its MQTT Client to AWS IoT Core via MQTT v5.
1. **Step 9**: AWS IoT rules routes predicted anomaly events to Amazon EventBridge, which applies retry logic and invokes an AWS Lambda function.
1. **Step 10**: The Lambda function transforms the anomaly data and creates work orders using the REST API of the target enterprise asset management (EAM) or computerized maintenance management system (CMMS).
1. **Step 11**: An AWS IoT rule routes device MQTT messages to Amazon Data Firehose, which buffers and batches the data before delivering it to Amazon Simple Storage Service (Amazon S3), which serves as the storage foundation for an industrial data lake.
1. **Step 12**: AWS Glue crawler catalogs the industrial data in Amazon S3 and populates the AWS Glue Data Catalog with schema metadata. Amazon Athena queries the cataloged data using standard SQL for ad-hoc analysis and reporting, while Amazon SageMaker accesses the same cataloged data to train custom machine learning models.
[Read usage guidelines](/solutions/guidance-disclaimers/)
