---
source_url: https://docs.aws.amazon.com/solutions/amazon-connect-real-time-analytics-with-amazon-opensearch-service/index.html
---

---
title: 'Guidance for Amazon Connect Real-Time Analytics with Amazon OpenSearch Service'
canonical_url: https://docs.aws.amazon.com/solutions/amazon-connect-real-time-analytics-with-amazon-opensearch-service/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Amazon Connect Real-Time Analytics with Amazon OpenSearch Service

## Overview

This Guidance shows you how to implement a data mesh architecture in the context of building a unified view of an end-customer. Each producer domain will own the data and any third-party applications specific to their domain, exposing them through data catalogs. A person consuming the data can then use the data catalogs to find the data they need about their end-customer. This Guidance uses Amazon Connect Customer Customer and Amazon OpenSearch Service to stream contact center data—such as metrics, segments, events, and cases—for real-time analytics on AWS.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/amazon-connect-real-time-analytics-with-amazon-opensearch-service.pdf)

![Architecture diagram](/images/solutions/amazon-connect-real-time-analytics-with-amazon-opensearch-service/images/amazon-connect-real-time-analytics-with-amazon-opensearch-service-1.png)

1. **Step 1**: Amazon CloudWatch receives Amazon Connect Customer instance metrics and uses a subscription filter to forward the metrics to Amazon Kinesis Data Firehose.
1. **Step 2**: Amazon Connect Customer streams an Amazon Connect Customer agent event stream and Amazon Connect Customer Contact Lens real-time segments through Amazon Kinesis Data Streams.
1. **Step 3**: Amazon Connect Customer streams Amazon Connect Customer contact event streams, Amazon Connect Customer case event streams, and voice ID events through Amazon EventBridge.
1. **Step 4**: EventBridge forwards the events to Kinesis Data Firehose using AWS Lambda.
1. **Step 5**: Kinesis Data Firehose invokes a Lambda function for data normalization and transformation.
1. **Step 6**: Lambda runs on cron schedule to capture third-party data and Amazon Connect Customer reporting API data. It transforms the data as needed, then calls Amazon OpenSearch Service to forward logs to the OpenSearch index specific to the data source.
1. **Step 7**: Kinesis Data Firehose directly ingests data to OpenSearch Service and into the OpenSearch index specific to the data source.
1. **Step 8**: The OpenSearch Dashboard is configured to visualize the Amazon Connect Customer index data present in OpenSearch Service.
[Read usage guidelines](/solutions/guidance-disclaimers/)
