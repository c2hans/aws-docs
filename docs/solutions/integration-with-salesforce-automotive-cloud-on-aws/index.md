---
source_url: https://docs.aws.amazon.com/solutions/integration-with-salesforce-automotive-cloud-on-aws/index.html
---

---
title: 'Guidance for Integration with Salesforce Automotive Cloud on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/integration-with-salesforce-automotive-cloud-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Integration with Salesforce Automotive Cloud on AWS

## Overview

This Guidance shows how to gather, collect, and distribute data from your connected vehicles using AWS IoT FleetWise to Salesforce Automotive Cloud. To build lasting customer relationships through informed interactions, customer service agents must be empowered with timely, relevant vehicle information. With AWS IoT FleetWise and Salesforce Automotive Cloud, you can take action on vehicle events in near real-time to provide impactful customer experiences that drive brand loyalty and differentiate your business.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/integration-with-salesforce-automotive-cloud-on-aws.pdf)

![Architecture diagram](/images/solutions/integration-with-salesforce-automotive-cloud-on-aws/images/integration-with-salesforce-automotive-cloud-on-aws-1.png)

1. **Step 1**: A connected vehicle has numerous sensors monitoring various data points, such as tire pressure, which need to be collected, analyzed, and acted upon. AWS IoT Core can serve as a communication mechanism to facilitate the transfer of data from the edge to the cloud, supporting protocols like a controller area network (CAN), CAN-FD, an extension of the CAN protocol that allows for faster data rates, and on-board diagnostics (OBDII). Data from various electronic control units (ECUs) can also be collected and analyzed using AWS IoT Core.
1. **Step 2**: The AWS IoT FleetWise Edge Agent communicates with the vehicle's network, decodes signals and sends data payloads through AWS IoT Core. AWS IoT FleetWise campaigns define how the data is selected, collected, and transferred.
1. **Step 3**: AWS IoT Core functions as a secure communication mechanism, facilitating the transfer of data from the edge devices to the cloud infrastructure. AWS IoT Core collaborates with AWS IoT FleetWise to transmit vehicle signal data, such as low tire pressure indications, directly from the vehicle to an Amazon Simple Storage Service (Amazon S3) event bucket.
1. **Step 4**: When an event, originating from either the AWS IoT Core rules engine or an AWS IoT FleetWise campaign, is detected in the specified event bucket, it is automatically ingested into an Amazon Simple Queue Service (Amazon SQS) queue.
1. **Step 5**: Implement an Amazon EventBridge Pipe to source events from the Amazon SQS queue, transform, and potentially enrich the event payload. Next, forward it to a custom event bus target.
1. **Step 6**: The custom event bus is configured with rules to dispatch each incoming event to multiple targets, including a designated application endpoint within the Salesforce Automotive Cloud, which initiates the downstream processing of the event for service technicians.
1. **Step 7**: Select Amazon DynamoDB as a secondary target from the custom event bus, and record all events to display in the fleet management platform.
1. **Step 8**: Salesforce Automotive Cloud then uses internal routing mechanisms to send the event notification to one or more downstream personas.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The low-code, no code services, including AWS IoT Core, Amazon DynamoDB, EventBridge, and Amazon SQS collectively address key challenges in connected vehicle, Internet of Things (IoT) systems, and downstream interactions with your partners. These managed services handle your data transfer, processing, and storage needs while helping ensure security and proactive payload health monitoring. The shared responsibility model lets you concentrate on product development while AWS manages the underlying infrastructure. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS IoT Core provides secure communication and authentication for IoT devices, preventing unauthorized access. EventBridge provides both encryption at rest and encryption in transit to protect your data. EventBridge encrypts data that passes between EventBridge and other services by using Transport Layer Security (TLS). By using these services, you can mitigate security risks, protect sensitive data, and maintain the integrity and confidentiality of information, crucial for building trust and helping ensure compliance in vehicle-to-Salesforce Auto Cloud deployments. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The services in this Guidance help you reduce the risk of system failures, downtime, and data loss in your IoT deployments. Specifically, AWS IoT Core helps ensure reliable and secure data transfer between devices and the cloud, reducing the risk of data loss or communication failures. In addition, all of the cloud resources in this Guidance are serverless and scale with demand, helping prevent system downtime even if demand increases. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses serverless systems to allow for scalability as well as minimum configuration and maintenance for you. For example, AWS IoT Core is purpose-built to manage a large fleet of devices, such as vehicles, through dynamic policies and device configuration for near real-time updates from the edge to the cloud. Additionally, Amazon S3 provides the capability of querying, scaling, and storing the workload data requirements. Lastly, AWS IoT Core offers features such as shared subscriptions, topic aliasing, and payload size reduction, which optimize data transfer and reduce latency, enhancing the overall performance of this architecture and contributing to faster data processing. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS IoT FleetWise can help minimize data transfer charges by limiting the data transferred in and out of the AWS Region to only the necessary information, as determined by the configured campaigns. Additionally, AWS IoT Core optimizes data transfer and communication, reducing data transmission costs and improving overall efficiency, which directly contributes to cost savings. Moreover, the usage-based pricing model of AWS IoT Core helps ensure that you only pay for the resources you consume. These services can assist in striking a balance between maintaining high-quality services and controlling costs, leading to more efficient and cost-effective IoT operations. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The services described in this Guidance reduce the need for on-premises infrastructure and its associated energy consumption. AWS IoT Core enables efficient data processing and transmission, leading to energy savings. AWS IoT Core also supports over-the-air (OTA) updates, reducing the need for physical recalls or manual updates, and incorporate monitoring and analytics tools to identify inefficiencies and anomalies. This helps optimize resource utilization and reduce the environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
