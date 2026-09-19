---
source_url: https://docs.aws.amazon.com/solutions/target-marketing-on-aws/index.html
---

---
title: 'Guidance for Target Marketing on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/target-marketing-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Target Marketing on AWS

## Overview

This Guidance helps you implement geofence target marketing, offering one-to-one personalized recommendations and promotions. It can identify retail customers within the geofenced areas of their physical stores and engage them by push notifications, SMS, and email channels. Retail customer locations can be detected either through GPS or by pre-installed beacon devices within the stores. By extending existing marketing strategies, this Guidance not only enhances customer engagement but also drives foot traffic and potential sales based on retail customers' proximity to physical stores.

## How it works

This architecture diagram shows an approach to implementing geofence target marketing, enabling personalized recommendations and promotions through push notifications, SMS, and email for retail customers detected through GPS or in-store Bluetooth beacons.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/target-marketing-on-aws.pdf)

![Architecture diagram](/images/solutions/target-marketing-on-aws/images/target-marketing-on-aws-1.png)

1. **Step 1**: Users grant either GPS or Bluetooth tracking permissions to the retailer's native app. For GPS, the Amazon Location Service SDK detects the user's current location. For Bluetooth, the retailer's app detects Bluetooth Low Energy (BLE) beacon signals inside the store and publishes user and beacon data to AWS IoT Core using message queuing telemetry transport (MQTT).
1. **Step 2**: Amazon Cognito grants permissions to AWS services for users authenticated in the retailer's app.
1. **Step 3a**: For GPS, Location Service detects if the user's location is within a geofence from the pre-defined geofence collection to generate geofence events that are sent to Amazon EventBridge.
1. **Step 3b**: For Bluetooth, AWS IoT Core invokes an AWS Lambda function with the data from the retailer's app and generates beacon detection events that are sent to EventBridge.
1. **Step 4**: An EventBridge rule responds to geofence and beacon detection events and invokes an AWS Step Functions workflow as a target.
1. **Step 5**: The Step Functions workflow processes the events and validates information such as customer marketing consents and store locations with the help of data persisted in Amazon DynamoDB.
1. **Step 6**: The Step Functions workflow invokes Amazon Personalize APIs with user data to retrieve recommendations.
1. **Step 7**: The Step Functions workflow invokes Amazon Pinpoint APIs with user and recommendations data.
1. **Step 8**: The Amazon Pinpoint SDK is integrated with the retailer's app, enabling Amazon Pinpoint to send recommendations and promotions to users through push notifications, SMS, and emails.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses fully managed and serverless services, minimizing operational overhead. It seamlessly integrates Step Functions, a serverless orchestration service, which eliminates the need for manual coordination and management of the application components. This approach streamlines the deployment and maintenance processes, allowing for efficient resource allocation and scalability while reducing your operational burden. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance implements a robust authentication mechanism using your identity provider and Amazon Cognito, granting temporary security credentials to access backend resources. It enforces least privilege access through AWS Identity and Access Management (IAM) service roles, helping ensure each component operates with minimal permissions. Data in transit is secured through TLS encryption between the mobile client and services like AWS IoT Core and Location Service. Further, data at rest stored in DynamoDB is encrypted using AWS Key Management Service (AWS KMS), providing an additional layer of protection for sensitive information. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

EventBridge controls the event flow between various components in this Guidance, adopting a publish-subscribe (Pub/Sub) model that decouples the beacons data component (which includes AWS IoT Core and Lambda) from the orchestration component (which includes Step Functions). This decoupling allows AWS IoT Core to transmit events as soon as they are received from the client, while Step Functions processes these events, independently of event generation. All components are configured to send events to EventBridge, enabling the creation of specific logging rules and forwarding event logs to a centralized logging service such as Amazon CloudWatch. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses purpose-built AWS services such as Location Service for tracking client locations, AWS IoT Core for real-time communications, and Amazon Cognito for mobile client authentication. It also uses DynamoDB, a highly performant database service, and allows customers to choose the required memory allocation for Lambda functions. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The fully managed and serverless services in this Guidance, such as Amazon Personalize, Step Functions, Lambda, and DynamoDB, operate on a pay-as-you-go pricing model, meaning you pay only for what you consume. This approach provides the necessary elasticity without the need for capacity planning, as the services seamlessly scale to precisely match the required resources, eliminating over-provisioning or under-provisioning concerns. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The serverless services (including Lambda, Step Functions, EventBridge, and DynamoDB) and fully managed services (including Amazon Cognito, Location Service, Amazon Personalize, and Amazon Pinpoint) eliminate the need for you to manage underlying hardware, as AWS runs these services with the minimum required infrastructure. Designed using an event-driven architecture and asynchronous APIs, this Guidance eliminates idle waiting times between components and avoids consuming compute resources unnecessarily. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
