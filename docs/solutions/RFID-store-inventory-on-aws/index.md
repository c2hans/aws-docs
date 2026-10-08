---
source_url: https://docs.aws.amazon.com/solutions/RFID-store-inventory-on-aws/index.html
---

---
title: 'Guidance for RFID Store Inventory on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/RFID-store-inventory-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for RFID Store Inventory on AWS

## Overview

This Guidance helps retail companies implement smart inventory management with Radio-Frequency Identification (RFID) using AWS services. Retailers can place RFID tags on items that emit signals to RFID readers, which are then processed to generate near real-time data related to stock, transactions, inventory levels, or purchase order history for individual customers. Implementing RFID can improve the customer experience, reduce operational cost, and enable retailers to make informed decisions while planning. This Guidance includes four separate architectures showing how to use RFID for managing, counting, and identifying store inventory and for detecting inventory loss.

## How it works

### Managing Inventory

This is a logical architecture showing RFID integration of retail store inventory systems using AWS services. It shows the foundational components and flows needed to monitor, maintain, and act on product inventory data.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/RFID-store-inventory-on-aws.pdf)Step 1Inventory items scanned in the store are sent to AWS IoT Core in the Inventory Ingestion Hub using the MQTT protocol. In-store RFID scanners can also link to in-store Point of Sale and inventory management systems (IMS).Step 2The Inventory Ingestion Hub handles ingestion of inventory scan events. AWS IoT Core uses AWS Lambda for data transformation tasks before being published to Amazon EventBridge.Step 3The Inventory Analytics layer reads all events from EventBridge. Amazon Kinesis Data Firehose loads data to Amazon Simple Storage Service (Amazon S3) for analytics and machine learning (ML) use cases, such as store replenishments.Step 4The Global IMS subscribes to EventBridge to maintain near real-time inventory updates in Amazon DynamoDB. This occurs by triggering the AWS Lambda function to update the DynamoDB table and perform transformation, if applicable. As updates take place, AWS AppSync shares them back to the In-Store IMS for reconciliation.Step 5EventBridge posts events to other enterprise systems registered as event targets based on defined rules.Step 6The Inventory Event Proxy accepts mobile scans, such as a quick response (QR) code and near field communications (NFC) through an Amazon API Gateway with Lambda as the backend. The event is matched to an RFID tag stored in DynamoDB and passed to the Inventory Ingestion Hub for processing.### Counting Inventory

This is a logical end-to-end architecture for RFID integration in a retail store that uses AWS services to perform inventory reconciliation.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/RFID-store-inventory-on-aws.pdf#page=2)Step 1You can quickly audit inventory by scanning inventory both stocked on shelves and hung on racks. Scanned tags are sent to AWS IoT Greengrass for pre-processing and deduplication through Lambda. The event is published to EventBridge.Step 2AWS IoT Greengrass notifies the In-Store IMS of the inventory scans. The In-Store IMS runs on Amazon Elastic Container Service (Amazon ECS) Anywhere to allow for centralized management and deployment of updates. It comprises of a data layer and API layer. The In-Store IMS will also house a local inventory storage to have inventory data locally.Step 3AWS IoT Greengrass sends the scanned inventory IDs and the store location to the Inventory Ingestion Hub. The Inventory Ingestion Hub uses AWS IoT Core to receive data from the edge, have the event-driven backend of Lambda perform data transformation if applicable, and publish to EventBridge. EventBridge then publishes this event to subscribers or downstream applications.Step 4The Global IMS subscribes to the inventory scan events in the Inventory Ingestion Hub. This allows it to reconcile any inventory discrepancies into the product inventory database hosted on DynamoDB.Step 5Once the inventory audit is complete, the Global IMS returns any updates or notifications back to the In-Store IMS, which completes the asynchronous update loop.Step 6Inventory discrepancies are reconciled in the In-Store IMS, which then updates the Global IMS to help ensure that both systems are synced.### Identifying Inventory

This is a logical end-to-end architecture for RFID integration in a retail store that uses AWS services when product details and recommendations need to be returned to a customer.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/RFID-store-inventory-on-aws.pdf#page=3)Step 1A store user scans products of interest using the Store App on their device.Step 2The Store App makes HTTPS requests to Amazon Route 53 to provide domain name service (DNS) translation.Step 3The request is routed to the nearest Amazon CloudFront edge location. AWS WAF [Web Application Firewall] rules are applied to traffic to protect against exploits.Step 4The static website and assets (such as HTML, image, and video) stored in Amazon S3 are returned.Step 5AWS AppSync handles queries by routing to resolvers, such as Lambda.Step 6Lambda uses ProductID to return detailed product information, such as size, color, options, characteristics, and current inventory stored in DynamoDB.Step 7Lambda uses ProductID to return recommendations from Amazon Personalize for items frequently purchased together.Step 8AWS Glue crawls the Product Catalog and Interaction History and creates a data catalog stored in Amazon S3, where ETL jobs can transform data to support Amazon Personalize training jobs.Step 9Datasets are added to an S3 bucket, and the training cycle is initiated in Amazon Personalize.### Detecting Shrink

This is a logical end-to-end architecture for RFID integration in a retail store that uses AWS services to prevent and detect asset loss.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/RFID-store-inventory-on-aws.pdf#page=4)Step 1Completed purchases at the Point of Sale sends an update to the In-Store IMS to update inventory status.Step 2The In-Store IMS updates the Global IMS asynchronously to keep the global inventory status current. This uses the RFID tag to associate the purchase to a specific item.Step 3As an RFID tag passes through an RFID reader at the store exit, event data is sent to AWS IoT Core.Step 4A Lambda function packaged within AWS IoT Greengrass is initiated when an asset is passed by the RFID reader. The function validates if the tag is part of a purchase event. The logic will check the RFID tag and compare it to the In-Store IMS.Step 5If the item has not yet been purchased, AWS IoT Greengrass triggers the device alarm in the physical store and then sends the event to the Inventory Ingestion Hub for further processing.Step 6The Inventory Ingestion Hub handles ingestion of inventory scan events. AWS IoT Core and Lambda publish the events to EventBridge.Step 7The Store Loss Prevention System picks up the event from the Inventory Ingestion Hub and sends SMS messages through Amazon Simple Notification Service (Amazon SNS) to notify proper personnel.Step 8The Global IMS is updated with the events. Proper teams can review using Amazon QuickSight, which generates reports and visualizations from data that has been queried in Amazon Athena. Athena has a direct connection to the inventory in DynamoDB through a Lambda function that runs federated queries against the inventory.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

You can set a workload baseline by using business events collected by RFID scanners or readers, log and metrics from Amazon CloudWatch, and any ancillary or supporting data from other business applications. You can then perform continuous monitoring of these metrics for anomalies or drift (through automation) and set up notifications that alert the right personnel of drift. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

You can enable least-privilege access through AWS Identity and Access Management (IAM) roles during interactions between AWS services. All services in this Guidance are patched to help ensure minimal security vulnerabilities. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

To maintain reliable connection to the internet for this Guidance, you should implement best practices in your infrastructure, particularly for services such as AWS IoT Greengrass, AWS IoT Core, and API Gateway. These services are highly available and use underlying protocols to ensure delivery and security. AWS IoT Core can provide reliable message delivery using MQTT quality of service. Retail stores can be configured to use AWS IoT Greengrass, allowing for offline IoT processing until connectivity is restored. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses an event-driven architecture based on a publish-subscribe model. This model enables you to incorporate additional services without impacting the architecture’s core functionality. To achieve low latency, you should consider your geographical proximity to users and systems that will interact with this Guidance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The Guidance uses serverless services, which allows you to pay only for the resources you use. For additional cost savings, you can use provisioned capacity for DynamoDB and S3 Intelligent-Tiering for automatic cost savings. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By processing as much as possible in the cloud, this Guidance keeps hardware requirements to a minimum. In the event that connectivity to AWS is lost, some on-premises hardware is necessary to support operations. Hardware is also required on-premises to interact with the RFID, in-store inventory, and security devices. Services that will require hardware are AWS IoT Greengrass and Amazon ECS Anywhere. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
