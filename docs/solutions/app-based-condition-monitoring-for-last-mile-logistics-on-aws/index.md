---
source_url: https://docs.aws.amazon.com/solutions/app-based-condition-monitoring-for-last-mile-logistics-on-aws/index.html
---

---
title: 'Guidance for App-based Condition Monitoring for Last-Mile Logistics on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/app-based-condition-monitoring-for-last-mile-logistics-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for App-based Condition Monitoring for Last-Mile Logistics on AWS

## Overview

This Guidance demonstrates how to implement cost-effective application-based condition monitoring for last-mile logistics using Bluetooth Low Energy (BLE) sensors and AWS services. It helps businesses in agriculture, pharmaceutical, and grocery retail sectors monitor temperature-sensitive goods in small crates with minimal maintenance requirements. The solution shows how to leverage existing Android devices as IoT gateways, integrate with AWS IoT Core for data collection, and utilize Amazon Aurora for auditable record-keeping. Organizations can benefit from the long battery life of sensors, real-time temperature monitoring through web dashboards, and a complete audit trail of order states, all while keeping implementation and operational costs low.

## Benefits

### Enhance supply chain visibility

Deploy a serverless solution that provides real-time temperature monitoring across your entire cold chain. Track environmental conditions continuously with BLE sensors that transmit data every 10 seconds, giving you immediate insights into product quality and compliance.

### Strengthen compliance management

Maintain comprehensive audit trails with automated backups and hash verification in Amazon Aurora PostgreSQL. Every temperature threshold breach and state change is recorded with timestamps, helping you meet regulatory requirements while simplifying compliance reporting.

### Streamline field operations

Empower warehouse and delivery personnel with mobile applications that seamlessly connect physical assets to cloud services. The Android gateway application allows staff to scan and match orders to specific sensors via QR codes, reducing manual processes and improving operational efficiency.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/app-based-condition-monitoring-for-last-mile-logistics-on-aws.pdf)

![Architecture diagram](/images/solutions/app-based-condition-monitoring-for-last-mile-logistics-on-aws/images/app-based-condition-monitoring-for-last-mile-logistics-on-aws-1.png)

1. **Step 1**: BLE sensors attached to small crates continuously collect temperature and environmental data with 5+ year battery life. These sensors communicate via Bluetooth Low Energy, broadcasting temperature data every 10 seconds to nearby Android gateway devices without requiring direct pairing.
1. **Step 2**: Warehouse/delivery personnel utilize Android gateway applications on handheld devices to scan for nearby BLE sensors. The mobile app authenticates users through Amazon Cognito and enables matching orders to specific devices via QR code scanning, serving as the bridge between physical sensors and cloud services.
1. **Step 3**: The authenticated Android gateway devices transmit the collected sensor data to AWS IoT Core, which serves as the primary ingestion point for all environmental data. AWS IoT Core processes and routes this information through IoT Rules for near real-time processing.
1. **Step 4**: IoT Rules trigger AWS Lambda functions that serve as the core processing layer. The GetOrderStatusFunction processes incoming sensor data, evaluating temperature thresholds and initiating appropriate alerts based on predefined conditions.
1. **Step 5**: The Data Merge & Alarm AWS Lambda function handles comprehensive processing, managing IoT data ingestion, order management, device assignment, status updates, and maintaining audit trail operations.
1. **Step 6**: Data flows from the Data Merge & Alarm AWS Lambda function to the Table component and connects with Amazon Aurora, managing structured data storage and state records. When there the order state changes (order creation, warehouse pickup, delivery completion, or temperature threshold violations during delivery), it is permanently recorded in the Amazon Aurora PostgreSQL table. These records serve as the definitive source for audit purposes, independent of time-series data in Amazon Timestream.
1. **Step 7**: Both Amazon Timestream and Amazon Aurora connect to Amazon API Gateway. Amazon Timestream provides time-series data for near real-time temperature monitoring and analysis, while Aurora PostgreSQL maintains the immutable state records with timestamps and hash verification. This integration through Amazon API Gateway enables access to current temperature monitoring data.
1. **Step 8**: The web dashboard interface, hosted Amazon Simple Storage Service (Amazon S3), provides a comprehensive view of near real-time sensor data, order tracking information, and temperature threshold management capabilities.
1. **Step 9**: Users access the web dashboard through Amazon CloudFront to create orders with temperature thresholds and monitor cold chain shipments. They authenticate via Amazon Cognito and can view near real-time sensor data, manage orders, and verify audit trails.
1. **Step 10**: Amazon API Gateway provides REST endpoints for all order management operations, connecting the web dashboard and mobile applications to the AWS Lambda-based business logic with Amazon Cognito-based authentication.
1. **Step 11**: The entire system is secured through AWS IoT Core policies controlling device permissions, Amazon CloudFront Origin Access Identity protecting Amazon S3 content, and Amazon Cognito managing user authentication across both mobile and web interfaces.
[Read usage guidelines](/solutions/guidance-disclaimers/)
