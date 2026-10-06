---
source_url: https://docs.aws.amazon.com/solutions/deploying-cygnet-scada-on-aws/index.html
---

---
title: 'Guidance for Deploying CygNet SCADA on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-cygnet-scada-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Deploying CygNet SCADA on AWS

## Overview

This Guidance demonstrates how to implement a highly-available CygNet SCADA system on AWS while maintaining strict operational technology (OT) and information technology (IT) network separation. It shows you how to architect a secure, fault-tolerant SCADA environment using Amazon EC2 instances, with Purdue model network segmentation enforced through AWS Transit Gateway and AWS Network Firewall. Organizations can learn how to properly ingest and manage OT data while maintaining security best practices and ensuring system reliability.

## Benefits

### Secure operational technology with industrial-grade segmentation

Implement true Purdue model security separation between industrial control systems and corporate networks. Protect critical SCADA infrastructure while enabling controlled data flow between operational and business systems.

### Reduce infrastructure costs while maintaining reliability

Deploy highly-available SCADA systems with up to 75% cost savings through reserved EC2 instances. Eliminate redundant on-premises hardware while ensuring continuous operations across multiple Availability Zones.

### Simplify SCADA management with centralized operations

Consolidate disparate control systems into a unified cloud environment with integrated monitoring. Focus on operational insights while AWS manages the underlying infrastructure, security updates, and scaling requirements.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/deploying-cygnet-scada-on-aws.pdf)

![Architecture diagram](/images/solutions/deploying-cygnet-scada-on-aws/images/deploying-cygnet-scada-on-aws-1.png)

1. **Step 1**: Private field networks of various types, including remote terminal unit (RTU), fiber, wireless, router/antenna, Federal Communications Commission (FCC) licensed radio links, private 5G long term evolution (LTE), or multiprotocol label switching (MPLS) networks, aggregate to centralized locations using OT aggregation (OT aggreg.) routers.
1. **Step 2**: AWS Direct Connect is installed at these aggregation locations, providing consistent, private fiber connectivity to AWS. These links carry any IP-based protocols as a dedicated wide area network (WAN) circuit in a hosted connection that supports redundancy in paths, Regions, and devices. Connections are available from 50Mbps to 10 Gbps.
1. **Step 3**: A Direct Connect gateway will be the logical demarcation for these physical connections in AWS. A private autonomous system number (ASN) connects to an AWS Transit Gateway, using transit virtual interface (VIF). Transit VIF is a fully redundant border gateway protocol (BGP)-enabled cloud router. Unlike typical hardware routers, it can have multiple conditional routing tables based on any given network flow direction. This will force traffic through the Inspection virtual private cloud (VPC).
1. **Step 4**: The Inspection VPC contains an AWS Network Firewall to separate Level-2 from Level-3. This is a fully managed appliance that supports deep packet inspection using AWS threat signature managed rules. No updating or patching is needed to stay up to date. Stateful and stateless rules are supported. East/West routing within Level-2 can be inspected through the firewall.
1. **Step 5**: Purdue Level-2 VPC (for OT) CygNet servers, failover, and database (Amazon Relational Database Service [Amazon RDS] for SQL Server) are deployed in a VPC. These are CygNet backend servers for processing. Scale and redundancy options are available for the database and compute nodes. The CygNet deployment will be broken into multiple Amazon Elastic Compute Cloud (Amazon EC2) instances based on disk, I/O, CPU, and memory consumption. Amazon Simple Notification Service (Amazon SNS) uses endpoints to send alarm notifications.
1. **Step 6**: A separate VPC exists at Purdue Level-3, serving as an intermediate network, also known as an OT-IT Demilitarized Zone (DMZ). This VPC contains multiple components: a Citrix Delivery Controller (which delivers the CygNet application), a Citrix Virtual Delivery Agent (VDA) for connection management, Microsoft Internet Information Services (IIS) for hosting CygNet's Thin Web Client, and additional Level-3 functions, including a data lake that uses Amazon Simple Storage Service (Amazon S3) through endpoints. This traffic is strictly separated by the Level 2/3 Inspection VPC. Scale and redundancy options are available for the database and compute nodes.
1. **Step 7**: Supporting services include AWS Managed Microsoft AD, a fully managed cloud Active Directory Service. This service does not expose authentication traffic to VPCs. Additionally, Amazon CloudWatch gives you visibility into your infrastructure. Amazon Workspaces is a fully managed virtual desktop infrastructure (VDI) option that connects to servers and virtual apps.
1. **Step 8**: Purdue Level-3 Transit Gateway is a second AWS Transit Gateway that forces separation between Level-3 and Level-4 VPCs. Inspection VPC contains an AWS Network Firewall to separate Level-3 from Level-4.
1. **Step 9**: VPNs can be used to extend the network to users outside of AWS while still enforcing the use of firewalls.
1. **Step 10**: The L4 VPC can host remote desktops for administrators and IT teams to access the private networks.
[Read usage guidelines](/solutions/guidance-disclaimers/)
