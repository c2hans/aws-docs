---
source_url: https://docs.aws.amazon.com/solutions/aveva-system-platform-on-aws/index.html
---

---
title: 'Guidance for AVEVA System Platform on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/aveva-system-platform-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for AVEVA System Platform on AWS

## Overview

This Guidance demonstrates how to deploy a unified industrial operations platform on AWS that connects distributed facilities through secure networking while providing enterprise-wide near real-time visualization for operational decision-making. You gain a scalable, standards-driven architecture that unifies people, processes, and assets across all locations with built-in redundancy and high availability. The solution enables continuous operational improvement through centralized configuration management, near real-time data processing, and historical data storage, while maintaining data integrity and system resiliency across multiple availability zones for enhanced business continuity.

## Benefits

### Ensure continuous industrial operations

Deploy redundant systems across multiple availability zones with automatic failover capabilities. Maintain near real-time data access and operational continuity even during infrastructure disruptions.

### Secure your operational technology

Protect field operations with encrypted connectivity options and private network isolation. Control administrative access while maintaining data integrity and confidentiality across your industrial infrastructure.

### Scale industrial data management

Centralize historical process data and system configurations with flexible storage solutions. Enable comprehensive trending, reporting, and analysis capabilities that grow with your operational needs.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/aveva-system-platform-on-aws.pdf)

![Architecture diagram](/images/solutions/aveva-system-platform-on-aws/images/aveva-system-platform-on-aws-1.png)

1. **Step 1**: Connect field operations to AVEVA System Platform on AWS using AWS Direct Connect for dedicated protected network links. Use VPN or encrypted MQTT connections as alternative secure options.
1. **Step 2**: Deploy MQTT broker in a private subnet with secure connection requirements to enable protected communication between field devices and AVEVA System Platform. Maintain data integrity and confidentiality.
1. **Step 3**: Deploy AVEVA Application Object Server (AOS) to Amazon Elastic Compute Cloud (Amazon EC2) to host AppEngines and physical equipment object instances. Configure AOS to provide near real-time data and manage communication drivers, System Management servers, and web services.
1. **Step 4**: Configure Instance Connect Endpoint to enable secure administrative access to AVEVA nodes.
1. **Step 5**: Configure Application Load Balancer to provide secure access to Operations Management Interface (OMI) web clients.
1. **Step 6**: Deploy Galaxy Repository Node with Microsoft SQL Server to store object definitions and project configurations in the Galaxy database. Install Integrated Development Environment (IDE) on this node.
1. **Step 7**: Deploy Historian Node with Microsoft SQL Server and AVEVA Historian software to store historical process and alarm data. Configure data access for trending, reporting, and analysis applications.
1. **Step 8**: Configure redundant AOS pairs to distribute primary AppEngines across two platforms with opposite node backups. Balance workload and implement first-level redundancy for continuous operation and high availability.
1. **Step 9**: Deploy System Platform in secondary availability zone with failover configuration to enhance system resiliency.
[Read usage guidelines](/solutions/guidance-disclaimers/)
