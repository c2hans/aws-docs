---
source_url: https://docs.aws.amazon.com/solutions/tracking-assets-and-locating-devices-using-aws-iot/index.html
---

---
title: 'Guidance for Tracking Assets & Locating Devices Using AWS IoT'
canonical_url: https://docs.aws.amazon.com/solutions/tracking-assets-and-locating-devices-using-aws-iot/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Tracking Assets & Locating Devices Using AWS IoT

## Overview

This Guidance demonstrates how to stream location data from your assets and devices with Internet of Things (IoT) sensors, helping you record and monitor the movement of your assets through a centralized management system. IoT-enabled devices, such as a smart bicycle, a delivery truck, or a shipping container, can be configured with AWS IoT Core, a fully managed service that lets you connect billions of IoT devices and route trillions of message topics to AWS. These message topics can then interface with a host of other AWS services, such as Amazon Location Service, which helps you add location data to your message topics. Other AWS services can be configured with this Guidance to alert you for geofencing events, allow you to receive location updates, and help you visualize asset positions from an interactive web application.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/tracking-assets-and-locating-devices-using-aws-iot.pdf)

![Architecture diagram](/images/solutions/tracking-assets-and-locating-devices-using-aws-iot/images/tracking-assets-and-locating-devices-using-aws-iot-1.png)

1. **Step 1**: A fleet of sensors is deployed in the field that provides location data and sends the data over the Message Queuing Telemetry Transport (MQTT) protocol to AWS IoT Core.
1. **Step 2**: Each sensor is represented by a 'thing' in AWS IoT Core. The messages from each sensor are sent to a topic. Optionally, if the sensor does not use GPS, AWS IoT Core Device Location can be used to resolve location based on Wi-Fi, cellular, global navigation satellite system (GNSS), or IP information. Rules are invoked on the messages and sent to actions, which invoke downstream AWS services.
1. **Step 3a**: Using the Location Action in AWS IoT Core, latitude and longitude updates are sent to Amazon Location Service tracker resources.
1. **Step 3b**: If metadata and accuracy are required in your application, an AWS Lambda function is required to send that data to Location Service. This Lambda function is invoked by an AWS IoT Core Lambda action.
1. **Step 4**: Geofence enter or exit events and location update events are sent to Amazon EventBridge.
1. **Step 5**: EventBridge sends location update events to Amazon Kinesis, and the events are stored in Amazon Simple Storage Service (Amazon S3). The events can be analyzed by Amazon Athena and visualized by Amazon QuickSight.
1. **Step 6**: EventBridge sends geofence enter or exit events to Amazon Simple Notification Service (Amazon SNS) for notifications.
1. **Step 7**: A frontend application utilizing Amazon Location Service Maps visualizes the asset positions and allows for viewing of geofences and events.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-asset-tracking-using-aws-iot-core-and-amazon-location-services)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Location Service, Lambda, and AWS IoT Core were used for this Guidance to automate your workloads and help you respond to events appropriately. Location Service does this by sending metrics to Amazon CloudWatch, giving you the visibility into how many geofences you are evaluating, and how many position updates you are ingesting. Lambda provides detailed metrics about function performance and optimization. AWS IoT Core sends metrics to CloudWatch to monitor incoming messages and alert you when ingestion stops or slows, indicating possible network or other issues. Understanding the metrics for each service allows you to identify ways of optimizing the event workflow, as well as ensure the workflow can scale in the event of a large influx of new events. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Location Service, AWS Identity and Access Management (IAM), and AWS IoT Core were selected for this Guidance to help you protect your data, systems, and assets in a way that improves your security posture. First, IAM policies are scoped to allow for only the minimum level of permissions. Next, Location Service allows for the scoping of permissions to only update permitted trackers and devices. Finally, AWS IoT Core policies create a layer of permissions controlling which devices can send data to MQTT topics, and how those devices can interact with the cloud. Limiting unauthorized access to these services prevents additional charges from being accrued, as well as prevents a device from being tampered with and sending malicious operations, or commands, to the cloud. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Your data is ingested into AWS IoT Core, processed by Lambda and Location Service, and then stored in Amazon S3. Lambda is designed to spread invocations across AZs, while AWS IoT Core is built with a multi-AZ architecture. Amazon S3 replicates data across AZs, and offers high levels of availability. Finally, Amplify uses Amazon S3 to host the web front-end, making it highly available. By using services built with serverless technology, such as these, and designed across multiple Availability Zones (AZ), your workloads can be resilient against failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS IoT Core and Lambda help you maintain efficiency as your business needs evolve. For example, AWS IoT Core scales as messages are ingested, and offers very low latency. And Lambda allows you to set concurrency reservations to reduce cold start times and improve performance. By using services that scale as data is ingested, you can ensure your application will remain up and performant even under heavy load. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Location Service offers filtering to save costs on location updates that may be jitter or if a device has not moved in a time period. By filtering location updates, you reduce costs when retrieving location events or evaluating geofences. Also, Amazon S3 offers multiple storage tiers for long-term location storage, and by setting a colder storage tier for long term storage in Amazon S3, you reduce storage and retrieval costs. Moreover, AWS IoT Core provides a very low-cost ingestion environment with multiple pricing tiers, depending on the number of messages sent. AWS IoT Core pricing scales with the application, and a higher throughput of messages does not mean significantly higher costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Most services in this Guidance are built using serverless technologies, reducing the compute footprint required. Lambda, for instance, will not run unless invoked by AWS IoT Core. Athena is a serverless application that will only consume compute resources when invoked. And Amazon S3 can use slower, more energy-efficient storage volumes for longer-term storage of location events. By building on top of serverless services, you can reduce your overall compute usage, and build a completely event-driven architecture that can scale up and down as the traffic scales, using less energy during slower periods of ingestion. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Tracking Assets using AWS IoT Core and Amazon Location Service**: This blog post explores the recently launched “location action” feature that connects AWS IoT Core with Amazon Location Service trackers, creating a scalable, simple, and cost effective way to track and store IoT device location updates.

[Visit Blog](https://aws.amazon.com/blogs/iot/tracking-assets-using-aws-iot-core-and-amazon-location-service/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
