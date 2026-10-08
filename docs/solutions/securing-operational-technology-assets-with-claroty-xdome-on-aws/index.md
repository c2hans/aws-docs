---
source_url: https://docs.aws.amazon.com/solutions/securing-operational-technology-assets-with-claroty-xdome-on-aws/index.html
---

---
title: 'Guidance for Securing Operational Technology (OT) Assets with Claroty xDome on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/securing-operational-technology-assets-with-claroty-xdome-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Securing Operational Technology (OT) Assets with Claroty xDome on AWS

Implement a cybersecurity approach to secure OT, Internet of Things (IoT), and Industrial Internet of Things (IIoT) assets

## Overview

This Guidance helps protect OT infrastructure using cybersecurity services. As digital applications for OT have increased, so has the convergence of OT and IoT technology. However, a more complex OT network may open the way for security vulnerabilities. With this Guidance, you can implement a cybersecurity approach to defend against malicious attacks, support passive monitoring 24/7, and plan for pre-defined actions to avoid security breaches that may lead to plant shutdowns.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/securing-operational-technology-assets-with-claroty-xdome-on-aws.pdf)

![Architecture diagram](/images/solutions/securing-operational-technology-assets-with-claroty-xdome-on-aws/images/securing-operational-technology-assets-with-claroty-xdome-on-aws-1.png)

1. **Step 1**: In the Purdue Model, Level 0 refers to the physical process: sensors and actuators, field devices, solenoid valves, and motors. Level 1 consists of Programmable Logic Controllers (PLC), Distributed Control Systems (DCS) Controllers, and Safety Instrumented System (SIS) that interface with the electromechanical devices in Level 0 to provide basic control.
1. **Step 2**: At Level 2, DCS Supervisory Control and Data Acquisition (SCADA) and human-machine interfaces (HMIs) provide control and monitoring of the manufacturing process. One or more Claroty xDome Collection servers can be installed to collect data from the control system network through a mirror port on an existing network switch that is on a network traffic access point (TAP). Claroty Edge can be deployed in order to actively discover devices.
1. **Step 3**: Level 3 consists of historians, engineering workstations, and other systems that manage manufacturing operations. One Claroty xDome collection server collects data from the supervisory network through a mirror port on the core network. Level 3.5 denotes the demilitarized zone (DMZ) that separates the corporate network from the industrial control systems (ICS) environment. One or more IoT gateways that collect wireless sensor data from Level 0 resides behind the firewall.
1. **Step 4**: The xDome collection server converts network traffic into lightweight metadata, which is then forwarded to Claroty xDome software as a service (SaaS) for correlation and processing through an encrypted connection that supports TLS and IP Security (IPsec) protocols.
1. **Step 5**: The Claroty xDome analysis engine sits on the AWS Cloud, providing native, SaaS-delivered security with the latest protections and low total cost ownership (TCO) due to scalability and continuous updates. Each Amazon Virtual Private Cloud (Amazon VPC) can sit in a corresponding AWS Region to enable multi-site access. Claroty xDome uses Amazon Elastic Kubernetes Service (Amazon EKS) for performance efficiency, Amazon Relational Database Service (Amazon RDS) for disaster recovery, and Amazon Simple Storage Service (Amazon S3) to store backups. Amazon ElastiCache caches frequently accessed data and absorbs spikes in traffic.
1. **Step 6**: Claroty xDome sends events and vulnerabilities to AWS Security Hub and natively sends events to Amazon Security Lake using the Open Cybersecurity Schema Framework (OCSF). These services can be a part of a comprehensive Security Operations Center and Security Information and Event Management workflow that consolidates OT and IIoT security event data and actions.
1. **Step 7**: Security Lake can work with AWS Partner solutions in addition to automation and analytics services, such as Amazon Athena, Amazon OpenSearch Service, and Amazon SageMaker to gain additional insights on security events.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

ElastiCache simplifies deploying, operating, and scaling an in-memory cache in the cloud. ElastiCache is a managed service, so AWS takes care of the operational aspects of running Redis, including hardware provisioning, software patching, horizontal and vertical scaling, upgrading engine versions, automatic backup, and monitoring. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Security Hub provides you with a centralized location to view and manage security alerts, findings, and recommendations across multiple AWS accounts and services. Security Hub in this Guidance provides managed threat intelligence based on analysis from AWS and third-party sources to identify known bad actors. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon RDS automatically performs backups of the database to Amazon S3. This includes daily snapshots and transaction logs captured every 5 minutes, which aids in disaster recovery. This Guidance also uses multi-Availability Zone (AZ) Amazon RDS database instances to provide automated failover to a standby replica in another AZ. This minimizes downtime if there are AZ failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon EKS provides Amazon CloudWatch metrics for monitoring overall cluster health, resource utilization, application performance, and bottlenecks. Amazon EKS integrates tightly with Amazon S3 and Amazon RDS in addition to caching, networking, security, and monitoring services. This integration can help you meet workload requirements around scaling, traffic management, and data access patterns. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

A data lake powered by Amazon S3 provides a highly durable and inexpensive way to store large amounts of log, packet capture, and forensic data from the Guidance over long periods of time at lower costs. Additionally, analyzing storage metrics and access patterns can help you better understand your resource usage so you can make informed decisions about optimizing frequently accessed "hot" data versus using less expensive “cold” data archives. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon RDS makes it easy to right size database instance types and storage based on actual utilization data—this helps you prevent overprovisioning. Additionally, Amazon S3 provides highly durable storage, reducing how often the Guidance must replicate data for redundancy. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
