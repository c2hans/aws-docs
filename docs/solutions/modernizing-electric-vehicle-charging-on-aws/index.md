---
source_url: https://docs.aws.amazon.com/solutions/modernizing-electric-vehicle-charging-on-aws/index.html
---

---
title: 'Guidance for Modernizing Electric Vehicle (EV) Charging on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/modernizing-electric-vehicle-charging-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Modernizing Electric Vehicle (EV) Charging on AWS

## Overview

This Guidance demonstrates how to build and modernize your electric vehicle (EV) charging station using AWS IoT Core. It highlights a modern Charging Station Management System (CSMS) built with serverless technologies, offering improved performance, lower costs, enhanced security, and compliance with the Open Charge Point Protocol (OCPP) for charger-to-cloud interoperability. The Guidance helps establish a reliable, secure, highly available EV charging platform with 99.9% uptime, as required by law in certain countries. Designed for reduced operating expenses and supporting OCPP, the serverless CSMS helps ensure a seamless charging experience while meeting regulatory requirements.

## How it works

This architecture diagram shows how to build and modernize your EV charging system using AWS IoT Core.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/modernizing-electric-vehicle-charging-on-aws.pdf?target=_blank)

![Architecture diagram](/images/solutions/modernizing-electric-vehicle-charging-on-aws/images/modernizing-electric-vehicle-charging-on-aws-1.png)

1. **Step 1**: The EV arrives and connects to the charge point. The customer authenticates to initiate charging.
1. **Step 2**: The charge point performs a DNS lookup and connects to the resolved OCPP endpoint through a Network Load Balancer (NLB), which redirects the connection to a containerized OCPP Handler instance running on AWS Fargate. The OCPP Handler authenticates the charge point and establishes a bi-directional WebSocket connection.
1. **Step 3**: The OCPP Handler application establishes a bidirectional Message Queuing Telemetry Transport (MQTT) connection with AWS IoT Core using the charge point's Thing ID as its identifier. OCPP messages received from the charge point are published to an MQTT topic identified by the charge point ID and the topic path "/in".
1. **Step 4**: An IoT rule subscribes to specific MQTT messages (for example, Heartbeat) that are passed to and handled by an AWS Lambda function for auto-responses. Another IoT rule subscribes to all MQTT messages that include the topic path "/in" and places the message payload to an Amazon Simple Queue Service (Amazon SQS) queue.
1. **Step 5**: AWS Step Functions is invoked by the Amazon SQS queue, which orchestrates the interpretation of the message payload and execution of the appropriate business logic in the CSMS based on the OCPP message payload.
1. **Step 6**: OCPP messages from the CSMS are published as MQTT messages to the charge point's "/out" topic. The OCPP Handler subscribes to the "/out" topic and forwards the OCPP responses over the WebSocket. The charge point receives and acts on the OCPP response, initiating power delivery.
1. **Step 7**: Telemetry and metrics from the charge point are added to the appropriate data stores. Analytics and visualizations can be performed against this data. Charge Point Operator administrators can access a web-based user interface portal to monitor system health, view data, or initiate configuration and firmware changes.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-as or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-modernizing-electric-vehicle-charging-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The architecture leverages NLB to efficiently distribute incoming connections from charge points to OCPP Handler instances running on Fargate. This offloads load balancing and high availability responsibilities, allowing you to focus on the core charging application. Fargate hosts the containerized OCPP Handler, enabling automatic scaling based on traffic and simplifying deployment and management. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS IoT Core establishes secure, encrypted communication channels between charge points and backend systems to handle authentication, authorization, and message encryption. AWS Identity and Access Management (IAM) enforces fine-grained access controls, restricting access to authorized users and services only. Security groups and network ACLs act as virtual firewalls, controlling inbound and outbound traffic, protecting the system from potential network-based attacks. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The stateless architecture allows the NLB to route traffic to any available OCPP Handler instance on Fargate. AWS Auto Scaling groups help ensure system scalability to handle increased load without downtime. AWS IoT Core provides reliable message handling, automatically rerouting traffic during failover or scaling events. Amazon SQS buffers and stores payloads, enhancing overall system resilience. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS IoT Core, Amazon SQS, and Lambda leverage scalability and high-throughput capabilities to efficiently handle potentially large volumes of OCPP messages from charging stations. Their serverless nature supports automatic scaling based on demand, adapting infrastructure to workload fluctuations. Managed services reduce operational overhead, re-directing focus to application-level concerns. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Serverless and pay-as-you-go pricing models (meaning you pay only for what you use) of AWS IoT Core, Amazon SQS, Lambda, and Step Functions allow you to scale the charging network up and down as needed, without incurring fixed costs. The event-driven architecture, facilitated by these services, consumes resources only when specific events or messages invoke actions, improving resource utilization and reducing waste. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The event-driven architecture and serverless services like AWS IoT Core, Amazon SQS, Lambda, and Step Functions minimize the environmental impact by consuming resources only when invoked, reducing the overall operational footprint and the need for always-on computing power. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
