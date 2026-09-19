---
source_url: https://docs.aws.amazon.com/solutions/enhancing-smart-products-through-device-telemetry-and-amazon-connect/index.html
---

---
title: 'Guidance on Enhancing Smart Products through Device Telemetry and Amazon Connect Customer Customer'
canonical_url: https://docs.aws.amazon.com/solutions/enhancing-smart-products-through-device-telemetry-and-amazon-connect/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance on Enhancing Smart Products through Device Telemetry and Amazon Connect Customer Customer

## Overview

This Guidance helps manufacturers overcome the challenge of reactive product support by enabling real-time device monitoring that feeds directly into customer service workflows. Devices send telemetry data to AWS IoT Core at regular intervals, where threshold-based checks automatically flag anomalies and route alerts to support teams. Operators can trigger on-demand high frequency diagnostics through a mobile control app, capturing detailed device behavior that combines with historical data archives to create comprehensive reports. When support sessions begin, agents receive enriched context including current alerts, telemetry trends, and diagnostic findings—directly within their Connect Customer chat interface, while specialists run AI-guided analytics through QuickSight dashboards. By seamlessly integrating device telemetry, anomaly detection, and Connect Customer, this solution empowers manufacturers to transform their product support operations, delivering faster issue resolution and driving ongoing product enhancements. Support agents see complete device health at a glance, reducing mean time to resolution, while product teams use fleet-wide analytics to drive continuous improvement and prevent recurring issues.

## Benefits

### Accelerate proactive device support

Empower support teams with real-time device context combining telemetry, alerts, and diagnostics. Resolve customer issues faster by eliminating manual data gathering and laying the foundation for future AI-guided troubleshooting through integrated analytics.

### Reduce operational monitoring costs

Automate device monitoring and alerting across your smart product fleet. Scale efficiently with serverless architecture that processes telemetry data and triggers notifications without managing infrastructure.

### Enable data-driven product insights

Build comprehensive analytics from device telemetry stored in time-series data lakes. Identify usage patterns and failure trends to improve product design and predict maintenance needs before devices fail.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/enhancing-smart-products-through-device-telemetry-and-amazon-connect.pdf)

![Architecture diagram](/images/solutions/enhancing-smart-products-through-device-telemetry-and-amazon-connect/images/enhancing-smart-products-through-device-telemetry-and-amazon-connect-1.png)

1. **Step 1**: Device Telemetry payload is sent at medium frequency to an AWS IoT Core topic. Optionally send Amazon Cloudwatch EMF formatted payload directly with Basic Ingest. Device firmware uses AWS IoT SDK or builds on top of MQTT stack.
1. **Step 2**: An AWS IoT Rule redirects telemetry data to an AWS Lambda function, (or optionally to an Amazon Cloudwatch LogGroup) that performs a first threshold-based sanity check of data and alerts to an Amazon DynamoDB table and an Amazon SNS topic based on the severance of threshold violations. When using CloudWatch, Telemetry Metrics are automatically generated for each IoT Device in Amazon Cloudwatch Metrics, that allow for further fine-grained actuation.
1. **Step 3**: The latest Telemetry Record is stored in a dedicated Amazon DynamoDB table, using again an AWS IoT Rule. Note: AWS IoT Device Shadows would allow to do the same.
1. **Step 4**: Another AWS IoT Rule sends all Telemetry to an Amazon Data Firehose Stream, that stores all Telemetry as an Amazon S3 Timeseries Datalake using parquet file format. That S3 Datalake can act as a rolling Telemetry Archive and evict data after e.g., 30 days based on S3 Lifecycle rules.
1. **Step 5**: Now, the devices also features a Control UI App, that runs on mobiles (Smartphones) or e.g., next to the Devices (like 3D Printers) on-prem at the shopfloor. That UI allows to consume all collected Telemetry Data via a HTTP API, exposed by Amazon API Gateway, that routes API requests to dedicated AWS Lambda functions.
1. **Step 6**: Alerts, Amazon CloudWatch Metrics or Telemetry Data are queried by an AWS Lambda function and returned as response payload to the UI.
1. **Step 7**: Device-Specific Control commands, Simulation Scenario Setpoints, or specialized Data Capture Campaigns triggers can be sent back to the Device. AWS Lambda sends dedicated command payloads to the Command Topic. Note: AWS IoT Jobs might also come into focus here, as it allows sophisticated control over IoT Devices.
1. **Step 8**: The Device IoT firmware control loop is subscribed to the Commands Topic and can act based on incoming command payloads.
1. **Step 9**: In Case of a Diagnostics Data Capture Activation through Command Topic, the device produces high frequent (e.g. 2/sec) Diagnostics payload, that contains lots of low-level details of the device. Data is stored in an Amazon DynamoDB table for further consumption.
1. **Step 10**: A dedicated Deep-Dive API Resource builds out a Data Report with Data from the Telemetry Datalake, combined with data from the latest Diagnostics data. Reports are stored in Amazon S3 and referenced in an Amazon DynamoDB table.
1. **Step 11**: Users of the Control UI App can Start an Amazon Connect Customer Support Session within the Device Details page.
1. **Step 12**: A dedicated AWS Lambda function collects the latest Telemetry report, alerts and Deep Dive Info and adds it as context to the built-up Amazon Connect Customer Session.
1. **Step 13**: A Call Center 1st Line Agent (human or AI based) has all high-level Device details at hand within the Amazon Connect Customer Chat Interface. Specialist Persona, working next to 1st line agents, can work with a statistical Deep Dive Analysis.
1. **Step 14**: Support SMEs and Support Specialists might use Amazon Quick Suite, to conduct AI guided Analytics on the Telemetry and Diagnostics Datasets.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-smart-products-and-telemetry-driven-x-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
